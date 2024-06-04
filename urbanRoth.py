import re
import influxdb_client
import pandas as pd
from typing import List

# influx_db constants
INF_URL = "http://0.0.0.0:8086"  # <- Use this if Influx on another machine
INF_TOKEN = "default-token"  # <- Use this if Influx on another machine # noqa
INF_ORG = "nrel"


org = INF_ORG
token = INF_TOKEN
url = INF_URL


client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)

import pandas as pd
from typing import List


def generate_flux_script(
    csv_file: str,
    bucket_name: str,
    measurement_prefix: str,
    fields: List[str],
    filter_type: str,
    window_period: str,
) -> str:
    """
    Generates an InfluxDB Flux script for aggregating energy data for specific days based on a CSV file.

    Parameters:
    csv_file (str): Path to the CSV file containing dates and inclusion status.
    bucket_name (str): Name of the InfluxDB bucket.
    measurement_prefix (str): The prefix of the measurement to filter on.
    fields (List[str]): List of fields to filter on.
    filter_type (str): Type of the measurement.
    window_period (str): The window period for aggregation.

    Returns:
    str: The generated Flux script.
    """
    try:
        # Read the CSV file
        df = pd.read_csv(csv_file)

        # Validate CSV columns
        required_columns = ["date", "included"]
        if not all(column in df.columns for column in required_columns):
            raise ValueError(
                f"CSV file must contain the following columns: {required_columns}"
            )

        # Filter dates where included is True
        included_dates: List[str] = df[df["included"] == True]["date"].tolist()

        if not included_dates:
            raise ValueError(
                "No dates with 'included' set to True found in the CSV file."
            )

        # Generate Flux scripts for each date
        scripts = []
        for date in included_dates:
            start = f"{date}T00:00:00Z"
            stop = f"{date}T23:59:59Z"

            for field in fields:
                script = f"""
from(bucket: "{bucket_name}")
  |> range(start: {start}, stop: {stop})
  |> filter(fn: (r) => r["type"] == "{filter_type}" and r["_field"] == "{field}" and r["_measurement"] =~ /{measurement_prefix} -.*/)
  |> aggregateWindow(every: {window_period}, fn: sum, createEmpty: false)
  |> yield(name: "sum_{field}_{date}")
"""
                scripts.append(script.strip())

        # Combine scripts into a single script
        combined_script = "\n\n".join(scripts)

        return combined_script

    except FileNotFoundError:
        raise FileNotFoundError(f"The file {csv_file} does not exist.")
    except pd.errors.EmptyDataError:
        raise ValueError(f"The file {csv_file} is empty or not a valid CSV.")
    except Exception as e:
        raise RuntimeError(f"An error occurred while generating the Flux script: {e}")


def list_buckets(query_api):
    # Define the Flux query to list buckets
    query = "buckets()"

    # Query the data
    result = query_api.query(query=query)

    # Extract bucket names
    bucket_names = [record["name"] for table in result for record in table.records]

    return bucket_names


def list_measurements_for_bucket(query_api, bucket, filter_type):
    # Define the Flux query to list measurements for a bucket
    query = (
        f'import "influxdata/influxdb/schema"\nschema.measurements(bucket: "{bucket}")'
    )

    # Query the data
    result = query_api.query(query=query)

    # Extract measurement names and apply filter
    measurement_names = [
        record["_value"] for table in result for record in table.records
    ]  # if filter_type in record['_value']]

    return measurement_names


def list_all_measurements(query_api, filter_type):
    # Get the list of buckets
    buckets = list_buckets(query_api)

    # Dictionary to store measurements for each bucket
    all_measurements = {}

    # List measurements for each bucket
    for bucket in buckets:
        measurements = list_measurements_for_bucket(query_api, bucket, filter_type)
        all_measurements[bucket] = [
            m for m in measurements if buildings_only_pattern.match(m)
        ]

    return all_measurements


# Regular expression to filter out measurements that start with two English alphabets
buildings_only_pattern = re.compile(r"^[A-Za-z]{2}")
query_api = client.query_api()


heating_values = {}
cooling_values = {}
heating_baseline = {}
cooling_baseline = {}

bucket = "urbanRoth_HeatingOnly_setback"
for measurement in list_measurements_for_bucket(query_api, bucket, "timeseries"):
    if buildings_only_pattern.match(measurement):
        try:
            csv_file = f"outputs/core_days/heating/{measurement.split(' - ')[2]}.csv"
            measurement_prefix = " - ".join(measurement.split(" - ")[:-1])
            flux_script = generate_flux_script(
                csv_file,
                bucket_name=bucket,
                measurement_prefix=measurement_prefix,
                fields=["read_FurnaceHeat_y", "read_FanPower_y", "read_ACPower_y"],
                filter_type="timeseries",
                window_period="1d",
            )
            result = query_api.query(org=org, query=flux_script)
            sum_read_FurnaceHeat_y = 0
            sum_read_ACPower_y = 0
            sum_read_FanPower_y = 0
            for table in result:
                for record in table.records:
                    if record.get_field() == "read_FurnaceHeat_y":
                        sum_read_FurnaceHeat_y = (
                            sum_read_FurnaceHeat_y + record.get_value()
                        )
                    if record.get_field() == "read_ACPower_y":
                        sum_read_ACPower_y = sum_read_ACPower_y + record.get_value()
                    if record.get_field() == "read_FanPower_y":
                        sum_read_FanPower_y = sum_read_FanPower_y + record.get_value()

            heating_values[measurement_prefix] = (
                sum_read_FurnaceHeat_y + sum_read_FanPower_y
            )
        except RuntimeError as e:
            print(f"Error: {e} for {measurement}")


bucket = "urbanRoth_CoolingOnly_setback"
for measurement in list_measurements_for_bucket(query_api, bucket, "timeseries"):
    if buildings_only_pattern.match(measurement):
        try:
            csv_file = f"outputs/core_days/cooling/{measurement.split(' - ')[2]}.csv"
            measurement_prefix = " - ".join(measurement.split(" - ")[:-1])
            flux_script = generate_flux_script(
                csv_file,
                bucket_name=bucket,
                measurement_prefix=measurement_prefix,
                fields=["read_FurnaceHeat_y", "read_FanPower_y", "read_ACPower_y"],
                filter_type="timeseries",
                window_period="1d",
            )
            result = query_api.query(org=org, query=flux_script)
            sum_read_FurnaceHeat_y = 0
            sum_read_ACPower_y = 0
            sum_read_FanPower_y = 0
            for table in result:
                for record in table.records:
                    if record.get_field() == "read_FurnaceHeat_y":
                        sum_read_FurnaceHeat_y = (
                            sum_read_FurnaceHeat_y + record.get_value()
                        )
                    if record.get_field() == "read_ACPower_y":
                        sum_read_ACPower_y = sum_read_ACPower_y + record.get_value()
                    if record.get_field() == "read_FanPower_y":
                        sum_read_FanPower_y = sum_read_FanPower_y + record.get_value()

            cooling_values[measurement_prefix] = (
                sum_read_FurnaceHeat_y + sum_read_FanPower_y
            )
        except RuntimeError as e:
            print(f"Error: {e} for {measurement}")
print(cooling_values)

# Get baseline heating values
bucket = "urbanRoth_baseline_setback"
for measurement in list_measurements_for_bucket(query_api, bucket, "timeseries"):
    if buildings_only_pattern.match(measurement):
        try:
            csv_file = f"outputs/core_days/heating/{measurement.split(' - ')[2]}.csv"
            measurement_prefix = " - ".join(measurement.split(" - ")[:-1])
            flux_script = generate_flux_script(
                csv_file,
                bucket_name=bucket,
                measurement_prefix=measurement_prefix,
                fields=["read_FurnaceHeat_y", "read_FanPower_y", "read_ACPower_y"],
                filter_type="timeseries",
                window_period="1d",
            )
            result = query_api.query(org=org, query=flux_script)
            sum_read_FurnaceHeat_y = 0
            sum_read_ACPower_y = 0
            sum_read_FanPower_y = 0
            for table in result:
                for record in table.records:
                    if record.get_field() == "read_FurnaceHeat_y":
                        sum_read_FurnaceHeat_y = (
                            sum_read_FurnaceHeat_y + record.get_value()
                        )
                    if record.get_field() == "read_ACPower_y":
                        sum_read_ACPower_y = sum_read_ACPower_y + record.get_value()
                        if sum_read_ACPower_y != 0:
                            raise Exception(f"Cooling found in heating only bucket for {measurement}")
                    if record.get_field() == "read_FanPower_y":
                        sum_read_FanPower_y = sum_read_FanPower_y + record.get_value()

            heating_baseline[measurement_prefix] = (
                sum_read_FurnaceHeat_y + sum_read_FanPower_y
            )
        except RuntimeError as e:
            print(f"Error: {e} for {measurement}")
print(heating_baseline)

bucket = "urbanRoth_baseline_setback"
for measurement in list_measurements_for_bucket(query_api, bucket, "timeseries"):
    if buildings_only_pattern.match(measurement):
        try:
            csv_file = f"outputs/core_days/cooling/{measurement.split(' - ')[2]}.csv"
            measurement_prefix = " - ".join(measurement.split(" - ")[:-1])
            flux_script = generate_flux_script(
                csv_file,
                bucket_name=bucket,
                measurement_prefix=measurement_prefix,
                fields=["read_FurnaceHeat_y", "read_FanPower_y", "read_ACPower_y"],
                filter_type="timeseries",
                window_period="1d",
            )
            result = query_api.query(org=org, query=flux_script)
            sum_read_FurnaceHeat_y = 0
            sum_read_ACPower_y = 0
            sum_read_FanPower_y = 0
            for table in result:
                for record in table.records:
                    if record.get_field() == "read_FurnaceHeat_y":
                        sum_read_FurnaceHeat_y = (
                            sum_read_FurnaceHeat_y + record.get_value()
                        )
                        if sum_read_FurnaceHeat_y != 0:
                            raise Exception(f"Heating found in cooling only bucket for {measurement}")
                    if record.get_field() == "read_ACPower_y":
                        sum_read_ACPower_y = sum_read_ACPower_y + record.get_value()
                    if record.get_field() == "read_FanPower_y":
                        sum_read_FanPower_y = sum_read_FanPower_y + record.get_value()

            cooling_baseline[measurement_prefix] = (
                sum_read_FurnaceHeat_y + sum_read_FanPower_y
            )
        except RuntimeError as e:
            print(f"Error: {e} for {measurement}")


import csv

# heating_baseline = heating_baseline
# heating_values = heating_values

# cooling_baseline = cooling_baseline
# cooling_values = cooling_values

# Function to calculate percentage difference
def calculate_percentage_difference(baseline_dict, change_dict):
    percentage_diff = {}
    for key in baseline_dict:
        if key in change_dict:
            base_value = baseline_dict[key]
            change_value = change_dict[key]
            if base_value != 0:
                percentage_diff[key] = ((change_value - base_value) / base_value) * 100
            else:
                percentage_diff[key] = None  # Handle division by zero case
    return percentage_diff


# Calculate percentage differences
percentage_diff_heating = calculate_percentage_difference(
    heating_baseline, heating_values
)
percentage_diff_cooling = calculate_percentage_difference(
    cooling_baseline, cooling_values
)

# Write to CSV file
with open("percentage_difference_cases.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(
        [
            "ct_identifier",
            # "Baseline Heating",
            # "Change Heating",
            "Percentage Difference Heating",
            # "Baseline Cooling",
            # "Change Cooling",
            "Percentage Difference Cooling",
        ]
    )

    all_keys = set(heating_baseline.keys()).union(
        heating_values.keys(), cooling_baseline.keys(), cooling_values.keys()
    )

    for key in all_keys:
        if (
            key in heating_baseline
            and key in heating_values
            and key in cooling_baseline
            and key in cooling_values
        ):
            writer.writerow(
                [
                    key.split(" - ")[2],
                    # heating_baseline[key],
                    # heating_values[key],
                    percentage_diff_heating.get(key),
                    # cooling_baseline[key],
                    # cooling_values[key],
                    percentage_diff_cooling.get(key),
                ]
            )

print("CSV file created successfully.")

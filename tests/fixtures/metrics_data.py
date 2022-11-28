import pytest
from numpy import nan

@pytest.fixture(scope="session")
def metrics_type_1_data():
    data = \
[{'_daily_mean_core_day_demand_baseline_baseline_percentile': 9.976082159783457,
  '_daily_mean_core_day_demand_baseline_baseline_regional': 7.12880601688671,
  'alpha': 44.06852749755634,
  'avoided_daily_mean_core_day_runtime_baseline_percentile': 192.715710435758,
  'avoided_daily_mean_core_day_runtime_baseline_regional': 67.2404434393765,
  'avoided_total_core_day_runtime_baseline_percentile': 57043.85028898437,
  'avoided_total_core_day_runtime_baseline_regional': 19903.171258055445,
  'baseline_daily_mean_core_day_runtime_baseline_percentile': 439.6312509762986,
  'baseline_daily_mean_core_day_runtime_baseline_regional': 314.155983979917,
  'baseline_percentile_core_cooling_comfort_temperature': 69.5,
  'baseline_total_core_day_runtime_baseline_percentile': 130130.85028898438,
  'baseline_total_core_day_runtime_baseline_regional': 92990.17125805543,
  'climate_zone': 'Mixed-Humid',
  'cool_stage': '',
  'cool_type': 'heat_pump',
  'core_cooling_days_mean_indoor_temperature': 73.95971753003002,
  'core_cooling_days_mean_outdoor_temperature': 79.8426321875,
  'core_mean_indoor_temperature': 73.95971753003002,
  'core_mean_outdoor_temperature': 79.8426321875,
  'ct_identifier': '8465829e-df0d-449e-97bf-96317c24dec3',
  'cv_root_mean_sq_err': 0.07887381236030344,
  'daily_mean_core_cooling_runtime': 246.91554054054055,
  'end_date': '2014-12-31T00:00:00',
  'heat_stage': 'single_stage',
  'heat_type': 'heat_pump_electric_backup',
  'heating_or_cooling': 'cooling_ALL',
  'mean_abs_err': 12.444656615631587,
  'mean_abs_pct_err': 0.050400459154527476,
  'mean_demand': 5.602990491439324,
  'mean_sq_err': 379.28224705229485,
  'n_core_cooling_days': 296,
  'n_days_both_heating_and_cooling': 212,
  'n_days_in_inputfile_date_range': 1460,
  'n_days_insufficient_data': 13,
  'percent_savings_baseline_percentile': 43.83576235942965,
  'percent_savings_baseline_regional': 21.40352145693172,
  'regional_average_baseline_cooling_comfort_temperature': 73.0,
  'root_mean_sq_err': 19.47517001343749,
  'start_date': '2011-01-01T00:00:00',
  'station': '725314',
  'sw_version': '2.0.0a6',
  'tau': -0.8165326408614967,
  'total_core_cooling_runtime': 73087.0},
 {'_daily_mean_core_day_demand_baseline_baseline_percentile': 27.33218137187926,
  '_daily_mean_core_day_demand_baseline_baseline_regional': 26.799580026817768,
  'alpha': 31.694594789454573,
  'avoided_daily_mean_core_day_runtime_baseline_percentile': 93.45842226220161,
  'avoided_daily_mean_core_day_runtime_baseline_regional': 76.57783844615918,
  'avoided_total_core_day_runtime_baseline_percentile': 83364.91265788383,
  'avoided_total_core_day_runtime_baseline_regional': 68307.43189397399,
  'baseline_daily_mean_core_day_runtime_baseline_percentile': 866.2824132935917,
  'baseline_daily_mean_core_day_runtime_baseline_regional': 849.4018294775493,
  'baseline_percentile_core_heating_comfort_temperature': 69.54999999999988,
  'baseline_total_core_day_runtime_baseline_percentile': 772723.9126578838,
  'baseline_total_core_day_runtime_baseline_regional': 757666.431893974,
  'climate_zone': 'Mixed-Humid',
  'cool_stage': '',
  'cool_type': 'heat_pump',
  'core_heating_days_mean_indoor_temperature': 66.69791666666667,
  'core_heating_days_mean_outdoor_temperature': 44.69122160033633,
  'core_mean_indoor_temperature': 66.69791666666667,
  'core_mean_outdoor_temperature': 44.69122160033633,
  'ct_identifier': '8465829e-df0d-449e-97bf-96317c24dec3',
  'cv_root_mean_sq_err': 0.10753222979305962,
  'daily_mean_core_heating_runtime': 772.8239910313902,
  'end_date': '2014-12-31T00:00:00',
  'heat_stage': 'single_stage',
  'heat_type': 'heat_pump_electric_backup',
  'heating_or_cooling': 'heating_ALL',
  'mean_abs_err': 55.66503659236822,
  'mean_abs_pct_err': 0.07202809079215974,
  'mean_demand': 24.383463368603284,
  'mean_sq_err': 6906.189550425122,
  'n_core_heating_days': 892,
  'n_days_both_heating_and_cooling': 212,
  'n_days_in_inputfile_date_range': 1460,
  'n_days_insufficient_data': 13,
  'percent_savings_baseline_percentile': 10.788447373284908,
  'percent_savings_baseline_regional': 9.015501943674966,
  'regional_average_baseline_heating_comfort_temperature': 69.0,
  'rhu1_00F_to_05F': nan,
  'rhu1_05F_to_10F': 0.35810185185185184,
  'rhu1_10F_to_15F': 0.36336805555555557,
  'rhu1_15F_to_20F': 0.37900691389063484,
  'rhu1_20F_to_25F': 0.375673443706005,
  'rhu1_25F_to_30F': 0.3318400322150354,
  'rhu1_30F_to_35F': 0.28432496802364043,
  'rhu1_30F_to_45F': 0.22154695797667256,
  'rhu1_35F_to_40F': 0.1974189826660588,
  'rhu1_40F_to_45F': 0.15271363589013506,
  'rhu1_45F_to_50F': 0.09249776186213071,
  'rhu1_50F_to_55F': 0.052322643343051506,
  'rhu1_55F_to_60F': 0.028319891645631964,
  'rhu2_00F_to_05F': nan,
  'rhu2_05F_to_10F': 0.35810185185185184,
  'rhu2_10F_to_15F': 0.36336805555555557,
  'rhu2_15F_to_20F': 0.37900691389063484,
  'rhu2_20F_to_25F': 0.375673443706005,
  'rhu2_25F_to_30F': 0.3318400322150354,
  'rhu2_30F_to_35F': 0.28432496802364043,
  'rhu2_30F_to_45F': 0.22154695797667256,
  'rhu2_35F_to_40F': 0.1974189826660588,
  'rhu2_40F_to_45F': 0.15271363589013506,
  'rhu2_45F_to_50F': 0.09249776186213071,
  'rhu2_50F_to_55F': 0.052322643343051506,
  'rhu2_55F_to_60F': 0.028319891645631964,
  'root_mean_sq_err': 83.1034869931769,
  'start_date': '2011-01-01T00:00:00',
  'station': '725314',
  'sw_version': '2.0.0a6',
  'tau': -2.351080209428112,
  'total_auxiliary_heating_core_day_runtime': 144238.0,
  'total_core_heating_runtime': 689359.0,
  'total_emergency_heating_core_day_runtime': 2104.0}]

    return data


@pytest.fixture(scope="session")
def metrics_hpeb_2_hp_2_data():
    data = \
[{'_daily_mean_core_day_demand_baseline_baseline_percentile': 12.606760008550685,
  '_daily_mean_core_day_demand_baseline_baseline_regional': 10.562788562873564,
  'alpha': 28.48315881979677,
  'avoided_daily_mean_core_day_runtime_baseline_percentile': 30.53061871305234,
  'avoided_daily_mean_core_day_runtime_baseline_regional': -27.68814459729872,
  'avoided_total_core_day_runtime_baseline_percentile': 5403.919512210265,
  'avoided_total_core_day_runtime_baseline_regional': -4900.801593721873,
  'baseline_daily_mean_core_day_runtime_baseline_percentile': 359.08034752661166,
  'baseline_daily_mean_core_day_runtime_baseline_regional': 300.86158421626055,
  'baseline_percentile_core_cooling_comfort_temperature': 70.8,
  'baseline_total_core_day_runtime_baseline_percentile': 63557.221512210264,
  'baseline_total_core_day_runtime_baseline_regional': 53252.50040627812,
  'climate_zone': 'Mixed-Humid',
  'cool_stage': 'two_stage',
  'cool_type': 'heat_pump',
  'core_cooling_days_mean_indoor_temperature': 71.87485875706216,
  'core_cooling_days_mean_outdoor_temperature': 74.53503144067797,
  'core_mean_indoor_temperature': 71.87485875706216,
  'core_mean_outdoor_temperature': 74.53503144067797,
  'ct_identifier': 'c61badb0e0c0a7e06932de804af43111',
  'cv_root_mean_sq_err': 0.16357602780022015,
  'daily_mean_core_cooling_runtime': 328.5497288135593,
  'end_date': '2018-12-31T00:00:00',
  'heat_stage': 'two_stage',
  'heat_type': 'heat_pump_electric_backup',
  'heating_or_cooling': 'cooling_ALL',
  'mean_abs_err': 40.78334959625454,
  'mean_abs_pct_err': 0.12413143588195652,
  'mean_demand': 11.534876833436256,
  'mean_sq_err': 2888.294955208049,
  'n_core_cooling_days': 177,
  'n_days_both_heating_and_cooling': 19,
  'n_days_in_inputfile_date_range': 364,
  'n_days_insufficient_data': 14,
  'percent_savings_baseline_percentile': 8.50244768986966,
  'percent_savings_baseline_regional': -9.202951140946054,
  'regional_average_baseline_cooling_comfort_temperature': 73.0,
  'root_mean_sq_err': 53.742859574161564,
  'start_date': '2018-01-01T00:00:00',
  'station': '723170',
  'sw_version': '2.0.0a6',
  'tau': 8.628075151655493,
  'total_core_cooling_runtime': 58153.301999999996},
 {'_daily_mean_core_day_demand_baseline_baseline_percentile': 14.695315526664897,
  '_daily_mean_core_day_demand_baseline_baseline_regional': 13.87197893888318,
  'alpha': 24.12888815088287,
  'avoided_daily_mean_core_day_runtime_baseline_percentile': 30.20112844422813,
  'avoided_daily_mean_core_day_runtime_baseline_regional': 10.334932007113602,
  'avoided_total_core_day_runtime_baseline_percentile': 4016.750083082341,
  'avoided_total_core_day_runtime_baseline_regional': 1374.545956946109,
  'baseline_daily_mean_core_day_runtime_baseline_percentile': 354.58162468482965,
  'baseline_daily_mean_core_day_runtime_baseline_regional': 334.7154282477151,
  'baseline_percentile_core_heating_comfort_temperature': 69.9,
  'baseline_total_core_day_runtime_baseline_percentile': 47159.35608308234,
  'baseline_total_core_day_runtime_baseline_regional': 44517.15195694611,
  'climate_zone': 'Mixed-Humid',
  'cool_stage': 'two_stage',
  'cool_type': 'heat_pump',
  'core_heating_days_mean_indoor_temperature': 68.62462406015037,
  'core_heating_days_mean_outdoor_temperature': 43.35078979323308,
  'core_mean_indoor_temperature': 68.62462406015037,
  'core_mean_outdoor_temperature': 43.35078979323308,
  'ct_identifier': 'c61badb0e0c0a7e06932de804af43111',
  'cv_root_mean_sq_err': 0.2499173059502313,
  'daily_mean_core_heating_runtime': 324.3804962406015,
  'end_date': '2018-12-31T00:00:00',
  'heat_stage': 'two_stage',
  'heat_type': 'heat_pump_electric_backup',
  'heating_or_cooling': 'heating_ALL',
  'mean_abs_err': 62.13151151808365,
  'mean_abs_pct_err': 0.19153898658567647,
  'mean_demand': 13.443657006165555,
  'mean_sq_err': 6572.069220018736,
  'n_core_heating_days': 133,
  'n_days_both_heating_and_cooling': 19,
  'n_days_in_inputfile_date_range': 364,
  'n_days_insufficient_data': 14,
  'percent_savings_baseline_percentile': 8.517398066262583,
  'percent_savings_baseline_regional': 3.0876772132131776,
  'regional_average_baseline_heating_comfort_temperature': 69.0,
  'rhu1_00F_to_05F': nan,
  'rhu1_05F_to_10F': nan,
  'rhu1_10F_to_15F': nan,
  'rhu1_15F_to_20F': 0.8938117141436386,
  'rhu1_20F_to_25F': 0.5963729624072203,
  'rhu1_25F_to_30F': 0.11484128153249978,
  'rhu1_30F_to_35F': 0.06079135092511376,
  'rhu1_30F_to_45F': 0.04260111560494782,
  'rhu1_35F_to_40F': 0.037086580256967316,
  'rhu1_40F_to_45F': 0.03371910830246602,
  'rhu1_45F_to_50F': 0.009995474641406795,
  'rhu1_50F_to_55F': 0.0,
  'rhu1_55F_to_60F': 0.012756025498260699,
  'rhu2_00F_to_05F': nan,
  'rhu2_05F_to_10F': nan,
  'rhu2_10F_to_15F': nan,
  'rhu2_15F_to_20F': 0.8938117141436386,
  'rhu2_20F_to_25F': 0.5963729624072203,
  'rhu2_25F_to_30F': nan,
  'rhu2_30F_to_35F': 0.06079135092511376,
  'rhu2_30F_to_45F': 0.04260111560494782,
  'rhu2_35F_to_40F': 0.037086580256967316,
  'rhu2_40F_to_45F': 0.03371910830246602,
  'rhu2_45F_to_50F': 0.009995474641406795,
  'rhu2_50F_to_55F': 0.0,
  'rhu2_55F_to_60F': nan,
  'root_mean_sq_err': 81.06829972325025,
  'start_date': '2018-01-01T00:00:00',
  'station': '723170',
  'sw_version': '2.0.0a6',
  'tau': 12.16945589758016,
  'total_auxiliary_heating_core_day_runtime': 1921.2,
  'total_core_heating_runtime': 43142.606,
  'total_emergency_heating_core_day_runtime': 110.0}]

    return data


@pytest.fixture(scope="session")
def metrics_ert_hpeb_2_hp_2_data():
    data = \
[{'_daily_mean_core_day_demand_baseline_baseline_percentile': 12.25281033824587,
  '_daily_mean_core_day_demand_baseline_baseline_regional': 10.312943007859884,
  'alpha': 27.60856756116322,
  'avoided_daily_mean_core_day_runtime_baseline_percentile': 27.102996583034777,
  'avoided_daily_mean_core_day_runtime_baseline_regional': -26.45396166762003,
  'avoided_total_core_day_runtime_baseline_percentile': 4770.1273986141205,
  'avoided_total_core_day_runtime_baseline_regional': -4655.897253501125,
  'baseline_daily_mean_core_day_runtime_baseline_percentile': 338.28254203758024,
  'baseline_daily_mean_core_day_runtime_baseline_regional': 284.7255837869254,
  'baseline_percentile_core_cooling_comfort_temperature': 70.9,
  'baseline_total_core_day_runtime_baseline_percentile': 59537.72739861412,
  'baseline_total_core_day_runtime_baseline_regional': 50111.70274649888,
  'climate_zone': 'Mixed-Humid',
  'cool_stage': 'two_stage',
  'cool_type': 'heat_pump',
  'core_cooling_days_mean_indoor_temperature': 71.88806818181817,
  'core_cooling_days_mean_outdoor_temperature': 74.60005241477273,
  'core_mean_indoor_temperature': 71.88806818181817,
  'core_mean_outdoor_temperature': 74.60005241477273,
  'ct_identifier': 'c61badb0e0c0a7e06932de804af43111',
  'cv_root_mean_sq_err': 0.16788677782925684,
  'daily_mean_core_cooling_runtime': 311.17954545454546,
  'end_date': '2018-12-31T00:00:00',
  'heat_stage': 'two_stage',
  'heat_type': 'heat_pump_electric_backup',
  'heating_or_cooling': 'cooling_ALL',
  'mean_abs_err': 39.55504086253661,
  'mean_abs_pct_err': 0.12711324198625543,
  'mean_demand': 11.27112244288543,
  'mean_sq_err': 2729.323861698708,
  'n_core_cooling_days': 176,
  'n_days_both_heating_and_cooling': 19,
  'n_days_in_inputfile_date_range': 364,
  'n_days_insufficient_data': 14,
  'percent_savings_baseline_percentile': 8.011940675325738,
  'percent_savings_baseline_regional': -9.291037818159984,
  'regional_average_baseline_cooling_comfort_temperature': 73.0,
  'root_mean_sq_err': 52.24293121273641,
  'start_date': '2018-01-01T00:00:00',
  'station': '723170',
  'sw_version': '2.0.0a6',
  'tau': 8.310141458385782,
  'total_core_cooling_runtime': 54767.6},
 {'_daily_mean_core_day_demand_baseline_baseline_percentile': 14.0775234005962,
  '_daily_mean_core_day_demand_baseline_baseline_regional': 13.262372650813058,
  'alpha': 23.730080239253436,
  'avoided_daily_mean_core_day_runtime_baseline_percentile': 29.61940648265708,
  'avoided_daily_mean_core_day_runtime_baseline_regional': 10.275813783215527,
  'avoided_total_core_day_runtime_baseline_percentile': 3939.3810621933917,
  'avoided_total_core_day_runtime_baseline_regional': 1366.683233167665,
  'baseline_daily_mean_core_day_runtime_baseline_percentile': 334.06075986611575,
  'baseline_daily_mean_core_day_runtime_baseline_regional': 314.7171671666742,
  'baseline_percentile_core_heating_comfort_temperature': 69.9,
  'baseline_total_core_day_runtime_baseline_percentile': 44430.08106219339,
  'baseline_total_core_day_runtime_baseline_regional': 41857.38323316767,
  'climate_zone': 'Mixed-Humid',
  'cool_stage': 'two_stage',
  'cool_type': 'heat_pump',
  'core_heating_days_mean_indoor_temperature': 68.62462406015037,
  'core_heating_days_mean_outdoor_temperature': 43.35078979323308,
  'core_mean_indoor_temperature': 68.62462406015037,
  'core_mean_outdoor_temperature': 43.35078979323308,
  'ct_identifier': 'c61badb0e0c0a7e06932de804af43111',
  'cv_root_mean_sq_err': 0.258345382172041,
  'daily_mean_core_heating_runtime': 304.44135338345876,
  'end_date': '2018-12-31T00:00:00',
  'heat_stage': 'two_stage',
  'heat_type': 'heat_pump_electric_backup',
  'heating_or_cooling': 'heating_ALL',
  'mean_abs_err': 60.50847476858618,
  'mean_abs_pct_err': 0.1987524825261593,
  'mean_demand': 12.829343614264856,
  'mean_sq_err': 6185.982599217759,
  'n_core_heating_days': 133,
  'n_days_both_heating_and_cooling': 19,
  'n_days_in_inputfile_date_range': 364,
  'n_days_insufficient_data': 14,
  'percent_savings_baseline_percentile': 8.866472822048268,
  'percent_savings_baseline_regional': 3.265094775644526,
  'regional_average_baseline_heating_comfort_temperature': 69.0,
  'rhu1_00F_to_05F': nan,
  'rhu1_05F_to_10F': nan,
  'rhu1_10F_to_15F': nan,
  'rhu1_15F_to_20F': 0.8979559976359601,
  'rhu1_20F_to_25F': 0.6045587903407809,
  'rhu1_25F_to_30F': 0.12034338820193748,
  'rhu1_30F_to_35F': 0.06371785003148996,
  'rhu1_30F_to_45F': 0.04516069332278556,
  'rhu1_35F_to_40F': 0.03934310540012056,
  'rhu1_40F_to_45F': 0.03605074276325836,
  'rhu1_45F_to_50F': 0.010863180256371055,
  'rhu1_50F_to_55F': 0.0,
  'rhu1_55F_to_60F': 0.013987335790568002,
  'rhu2_00F_to_05F': nan,
  'rhu2_05F_to_10F': nan,
  'rhu2_10F_to_15F': nan,
  'rhu2_15F_to_20F': 0.8979559976359601,
  'rhu2_20F_to_25F': 0.6045587903407809,
  'rhu2_25F_to_30F': nan,
  'rhu2_30F_to_35F': 0.06371785003148996,
  'rhu2_30F_to_45F': 0.04516069332278556,
  'rhu2_35F_to_40F': 0.03934310540012056,
  'rhu2_40F_to_45F': 0.03605074276325836,
  'rhu2_45F_to_50F': 0.010863180256371055,
  'rhu2_50F_to_55F': 0.0,
  'rhu2_55F_to_60F': nan,
  'root_mean_sq_err': 78.65101778882304,
  'start_date': '2018-01-01T00:00:00',
  'station': '723170',
  'sw_version': '2.0.0a6',
  'tau': 12.84342248121461,
  'total_auxiliary_heating_core_day_runtime': 1921.2,
  'total_core_heating_runtime': 40490.70000000001,
  'total_emergency_heating_core_day_runtime': 110.0}]

    return data


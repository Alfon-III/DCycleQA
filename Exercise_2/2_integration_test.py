from CarbonFootprintCalculator import get_user_carbon_footprint, get_comparison_with_average
import pytest



# Excel to test the results
# https://docs.google.com/spreadsheets/d/1uDtg-gmnTwtIeVu7pdKuRatCRWwqIjlosS34Xr1C99U/edit?usp=sharing

# Run integration Tests:
# Run tests:
# pytest .\Exercise_2\2_integration_test.py



def test_get_user_carbon_footprint():
    user_data = {
        'energy_consumption': 100,
        'transportation': 50,
        'waste': 30
    }
    expected_output = {
        'energy_footprint': 100 * 0.233,
        'transportation_footprint': 50 * 0.21,
        'waste_footprint': 30 * 0.05,
        'total_footprint': (100 * 0.233) + (50 * 0.21) + (30 * 0.05)
    }

    result = get_user_carbon_footprint(user_data)

    assert result == pytest.approx(expected_output, rel=1e-9)
    

def test_comparison_with_avg_fp():
    
    user_data = {
        'energy_consumption': 200,
        'transportation': 100,
        'waste': 60
    }

    avg_fp = {
        'energy_consumption': 100,
        'transportation': 50,
        'waste': 30
    }
    
    expected_res = {
        'energy_difference': 23.3, 
        'transportation_difference': 10.5, 
        'waste_difference': 1.5, 
        'total_difference': 35.3
    }

    user_footprint = get_user_carbon_footprint(user_data)
    average_footprint = get_user_carbon_footprint(avg_fp)

    assert expected_res == get_comparison_with_average(user_footprint, average_footprint)


def test_comparison_with_avg_fp_2():
    
    user_data = {
        'energy_consumption': 80,
        'transportation': 20.5,
        'waste': -50
    }

    avg_fp = {
        'energy_consumption': 60,
        'transportation': 20,
        'waste': 10
    }
    
    expected_res = {
        'energy_difference': 4.66,
         'transportation_difference': 0.105,
         'waste_difference': -3.000,
         'total_difference': 1.765
    }

    user_footprint = get_user_carbon_footprint(user_data)
    average_footprint = get_user_carbon_footprint(avg_fp)

    result = get_comparison_with_average(user_footprint, average_footprint)

    assert result == pytest.approx(expected_res, rel=1e-9)

def test_comparison_with_avg_fp_decimals():
    
    user_data = {
        'energy_consumption': 123.456,
        'transportation': 8.88888,
        'waste': .000555
    }

    avg_fp = {
        'energy_consumption': 985.25489,
        'transportation': 0.5298,
        'waste': 0.0321654
    }
    
    expected_res = {
        'energy_difference': -200.79914137,
         'transportation_difference': 1.7554067999999998,
         'waste_difference': -0.00158052,
         'total_difference': -199.04531509
    }

    user_footprint = get_user_carbon_footprint(user_data)
    average_footprint = get_user_carbon_footprint(avg_fp)

    assert expected_res == get_comparison_with_average(user_footprint, average_footprint)



def test_comparison_with_avg_fp_case_equal():
    user_data = {
        'energy_consumption': 100,
        'transportation': 50,
        'waste': 30
    }

    avg_fp = {
        'energy_consumption': 100,
        'transportation': 50,
        'waste': 30
    }

    expected_res = {
        'energy_difference': 0,
        'transportation_difference': 0,
        'waste_difference': 0,
        'total_difference': 0
    }

    user_footprint = get_user_carbon_footprint(user_data)
    average_footprint = get_user_carbon_footprint(avg_fp)

    result = get_comparison_with_average(user_footprint, average_footprint)

    assert result == pytest.approx(expected_res, rel=1e-9)
       
     


from CarbonFootprintCalculator import get_user_carbon_footprint, get_comparison_with_average
import pytest

# python3 -m pytest -v ./Exercise\ 2/2_integration_test.py

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
       
     
    

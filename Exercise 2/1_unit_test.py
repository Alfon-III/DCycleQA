
from CarbonFootprintCalculator import CarbonFootprintCalculator
import pytest

# python3 -m pytest -v ./Exercise\ 2/1_unit_test.py

def test_calculation():

    assert CarbonFootprintCalculator(
        energy_consumption=100,
        transportation=20,
        waste=20
    ).total_carbon_footprint() == 28.5


    assert CarbonFootprintCalculator(
        energy_consumption=30,
        transportation=23,
        waste=27
    ).total_carbon_footprint() == 13.17

    
    assert CarbonFootprintCalculator(
        energy_consumption=50,
        transportation=40,
        waste=10
    ).total_carbon_footprint() == 20.55

def test_large_values():
    
    assert CarbonFootprintCalculator(
        energy_consumption=99999999999999999999,
        transportation=99999999999999999999,
        waste=99999999999999999999
    ).total_carbon_footprint() == 49300000000000000000



def test_negatives():

    assert CarbonFootprintCalculator(
        energy_consumption=30,
        transportation=-20,
        waste=20
    ).total_carbon_footprint() == 3.79


    assert CarbonFootprintCalculator(
        energy_consumption=-100,
        transportation=-50,
        waste=40
    ).total_carbon_footprint() == pytest.approx(-31.8, rel=1e-9)

def test_empty_values():
    
    with pytest.raises(TypeError):
        assert CarbonFootprintCalculator(
            energy_consumption=100,
            transportation=20,
        )

    with pytest.raises(TypeError):
        assert CarbonFootprintCalculator(
            energy_consumption=100,
            waste=30,
        )
    
    assert CarbonFootprintCalculator(
            energy_consumption=0,
            transportation=0,
            waste=0,
    ).total_carbon_footprint() == 0
    


def test_invalid_types():
    with pytest.raises(TypeError):
        assert CarbonFootprintCalculator(
            energy_consumption="100",
            transportation=20,
            waste=30
        ).total_carbon_footprint() == 29

    with pytest.raises(TypeError):
        CarbonFootprintCalculator(
            energy_consumption=100,
            transportation="20",
            waste=30
        )

    with pytest.raises(TypeError):
        CarbonFootprintCalculator(
            energy_consumption=100,
            transportation=20,
            waste="30"
        )

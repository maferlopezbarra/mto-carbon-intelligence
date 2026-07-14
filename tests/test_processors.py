from src.processors import total_carbon
from src.processors import carbon_calculator
from src.processors import carbon_factor
import pytest

def test_invalid_material():
    with pytest.raises(ValueError):
        total_carbon([{
            "material": "INVALID_MATERIAL",
            "od_mm": 100,
            "thickness_mm": 5.5,
            "length_mm": 1000,
            "density_kg_m3": 7850            
            }])
        
def test_total_carbon():
    result = total_carbon([{
            "material": "A106-B",
            "od_mm": 100,
            "thickness_mm": 5.5,
            "length_mm": 1000,
            "density_kg_m3": 7850            
            }])
    assert result["total_co2_kg"] == 24.35

def test_carbon_calculator():
    row = {
        "od_mm": 100,
        "thickness_mm": 5,
        "length_mm": 1000,
        "density_kg_m3": 7850
        }
    result = carbon_calculator(2.0, row)
    assert result == 23.43


def test_carbon_factor():
    factors = carbon_factor()
    assert factors["A106-B"] == 1.9
    assert factors["A312-TP304"] == 6.2
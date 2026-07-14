from src.processors import total_carbon
from src.processors import carbon_calculator
import pytest

def test_material_error():
    with pytest.raises(ValueError):
        assert total_carbon([{
            "material": "INVALID_MATERIAL",
            "od_mm": 100,
            "thickness_mm": 5.5,
            "length_mm": 1000,
            "density_kg_m3": 7850            
            }])

def test_carbon_calculator():
    row = {
        "od_mm": 100,
        "thickness_mm": 5,
        "length_mm": 1000,
        "density_kg_m3": 7850
        }
    result = carbon_calculator(2.0, row)
    assert result == 23.43
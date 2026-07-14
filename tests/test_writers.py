from src.writers import export_excel


def test_export_excel(tmp_path):

    output = tmp_path / "result.xlsx"

    result = {
        "total_co2_kg": 25670.53,
        "items": [
            {
                "nominal": 150,
                "od_mm": 165.2,
                "material": "A106-B",
                "length_mm": 8125,
                "density_kg": 7833.028,
                "co2_kg": 426.43
            }
        ]
    }

    export_excel(result, output)

    assert output.exists()
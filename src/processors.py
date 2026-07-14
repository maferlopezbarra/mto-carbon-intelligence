import pandas as pd
import math
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def carbon_factor() -> dict:
    materials = pd.read_csv(BASE_DIR / "src/materials.csv")

    try:
        return {
        row["material"]: row["factor"] 
        for _, row in materials.iterrows()
        }
    except FileNotFoundError:
        raise FileNotFoundError("File src/materials.csv has been deleted or moved.")
    except KeyError:
        raise ValueError("File format not accepted: 'material' and/or 'factor' columns not found")
    

def carbon_calculator(factor: float, row: dict)-> float:
    d_inside = float(row["od_mm"]) - 2*float(row["thickness_mm"])
    volume = ((math.pi/4) * (float(row["od_mm"]) **2 - d_inside**2) * float(row["length_mm"])) * 1e-9
    mass = volume * float(row["density_kg_m3"])
    return round(mass * factor, 2)


def total_carbon(data: list[dict]):
    material_factor = carbon_factor()

    total = 0

    for row in data:
        try:
            co2 = carbon_calculator(
                float(material_factor[row["material"]]), 
                row
                )
            row["co2_kg"] = co2
            total += co2
        except KeyError:
            raise ValueError(f"{row['material']} is not listed in src/materials.csv file")
    return {
        "total_co2_kg": round(total, 2),
        "items": data
    }

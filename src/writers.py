from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_FILE = BASE_DIR / "data/output/mto-carbon-values.xlsx"

def export_excel(result: dict, filename: Path = OUTPUT_FILE):
    
    filename.parent.mkdir(exist_ok=True)

    summary = pd.DataFrame([
        {"Total CO2 (kg)": result["total_co2_kg"]}
    ])
    details = pd.DataFrame(result["items"])

    with pd.ExcelWriter(filename) as writer:
        summary.to_excel(writer, sheet_name="Summary", index=False)
        details.to_excel(writer,sheet_name="Details", index=False)
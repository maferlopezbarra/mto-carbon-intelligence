# MTO Carbon Intelligence

A Python application that estimates the embodied carbon footprint of piping systems from an AutoPIPE SQLite database.

The application extracts pipe information, calculates the CO₂ emissions of each piping item based on material-specific emission factors, and generates an Excel report with both a summary and detailed results.

---

## Features

- Extracts piping data from an AutoPIPE SQLite database.
- Calculates pipe mass from geometry and material density.
- Computes CO₂ emissions using configurable emission factors.
- Exports results to a structured Excel report.
- Validates input files and handles common database errors.
- Includes unit tests for the core business logic.

---

## Tech Stack

- Python
- SQLite
- Pandas
- Pytest
- argparse

---

## Project Structure

```
src/
├── cli.py          # Command-line interface
├── extractors.py   # SQLite data extraction
├── processors.py   # Carbon calculations
├── writers.py      # Excel export
└── main.py         # Application entry point
```

The project follows a modular architecture where extraction, processing and output generation are separated into independent components.

---

## Workflow

```
SQLite Database
        │
        ▼
Data Extraction
        │
        ▼
Carbon Calculation
        │
        ▼
Excel Report
```

---

## Running the project

```bash
python -m src.main --db input.db
```

The database must be placed in:

```
data/input/
```

The generated report is written to:

```
data/output/mto-carbon-values.xlsx
```

---

## Testing

Run the test suite with:

```bash
pytest
```

The tests cover:

- invalid input files
- database validation
- carbon calculations
- emission factor loading
- Excel export

---

## Example Output

The generated Excel workbook contains:

**Summary**

| Total CO₂ (kg) |
|---------------:|
| 25670.53 |

**Details**

| Nominal | Material | Length (mm) | CO₂ (kg) |
|---------|----------|------------:|----------:|
| 150 | A106-B | 8125 | 426.43 |

---

## Skills Demonstrated

- Python application design
- Data extraction from SQLite
- ETL-style data processing
- Modular architecture
- Exception handling
- Unit testing with pytest
- Excel report generation

import sqlite3
from pathlib import Path


def get_values(file: Path) -> list[dict]:
    if not Path(file).exists():
        raise FileNotFoundError("Database not found")
    elif file.suffix.lower() != ".db":
        raise ValueError("Only .db diles are allowed")
    try:
        conn = sqlite3.connect(file)
        conn.row_factory = sqlite3.Row

        query = """
        SELECT
            REPLACE(p.[Nominal (mm)], '.0', '') as nominal,
            prop.[Actual O D (mm)] AS od_mm,
            ROUND(prop.[Wall Thick (mm)], 2) AS thickness_mm,
            id.[Material] AS material,
            ROUND(SUM(p.[Length (mm)]), 2) AS length_mm,
            prop.[Density (kg/m3)] AS density_kg_m3
        FROM Point p
        JOIN [Pres/Temp/PipeID] id
            ON p.[To] = REPLACE(id.[To],' N', '')
        JOIN [Pipe Properties] prop
            ON id.[Pipe ID] = prop.[PipeID]
        WHERE id.[Material] <> 'None' AND p.[Length (mm)] > 0
        GROUP BY 
            prop.[Nominal (mm)],
            id.[Material],
            prop.[Wall Thick (mm)]
        """
        rows: list = [
            dict(row) for row in 
            conn.execute(query).fetchall()
            ]

    except (sqlite3.DatabaseError, sqlite3.OperationalError):
        raise ValueError("Database format not allowed")
    finally:
        if conn is not None:
            conn.close()
    return rows


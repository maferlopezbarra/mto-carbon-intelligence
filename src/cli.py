import argparse
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def path_db(name: str):
    return BASE_DIR / "data/input" / name


def get_path_db() -> Path:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--db", 
        default="input.db", 
        help="database file name in mto-carbon-intelligence/data/input/")
    
    args = parser.parse_args()

    return path_db(args.db)
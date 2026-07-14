import argparse
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def get_database(name: str):
    return BASE_DIR / "data/input" / name


def data() -> Path:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--db", 
        default="input.db", 
        help="database file name in mto-carbon-intelligence/data/input/")
    
    args = parser.parse_args()

    return get_database(args.db)
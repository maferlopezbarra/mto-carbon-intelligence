
from src.cli import get_path_db
from src.extractors import get_values
from src.processors import total_carbon
from src.writers import export_excel


def main():
    values = total_carbon(get_values(get_path_db()))
    export_excel(values)


if __name__ == "__main__":
    main()
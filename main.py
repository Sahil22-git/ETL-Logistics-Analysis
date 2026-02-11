from scripts.extract import extract_data
from scripts.transform import transform_data
from scripts.load import load_data

def main():
    raw_data = extract_data()
    clean_data = transform_data(raw_data)
    load_data(clean_data)

    print("\n ETL Pipeline completed!")

if __name__ == "__main__":
    main()

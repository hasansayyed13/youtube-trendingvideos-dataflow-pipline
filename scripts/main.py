from extract import extract_data
from transform import transform_data
from load import connect_to_mongo

def main():
    region = input("Enter the country code (eg: IN,US ):").upper()
    print("PROCESSING STARTED")
    print(f"Data extracted for {region} region:")
    extract_data(region=region)
    connect_to_mongo()
    transform_data()
    print("PROCESS COMPLETE")




if __name__ == "__main__":
    main()

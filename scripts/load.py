from sqlalchemy import create_engine

def load_data(clean_data):

    print("\n Connecting to MySQL...")

    engine = create_engine(
         "mysql+pymysql://root:5147@localhost/etl_project"
    )

    print(" Loading data into MySQL...")
    
    clean_data["merged"].to_sql(
        name ="orders_customers",
        con=engine,
        if_exists="replace",
        index=False
    )

    print(" Data loaded into MySQL successfully")
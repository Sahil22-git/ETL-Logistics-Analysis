import pandas as pd

def extract_data():
    
    base_path = "Data/Raw/"

    orders = pd.read_csv(base_path + "olist_orders_dataset.csv")
    order_items = pd.read_csv(base_path + "olist_order_items_dataset.csv")
    customers = pd.read_csv(base_path + "olist_customers_dataset.csv")
    sellers = pd.read_csv(base_path + "olist_sellers_dataset.csv")

    print("All datasets extracted succesfully")

    return {
        "orders": orders,
        "order_items": order_items,
        "customers": customers,
        "sellers": sellers
    }

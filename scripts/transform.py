import pandas as pd

def transform_data(data):

    orders = data["orders"]
    order_items = data["order_items"]
    customers = data["customers"]
    sellers = data["sellers"]

    print("\n checking missing values...")

    print("Orders missing values:\n",orders.isnull().sum())
    print("\nOrder Items missing values:\n",order_items.isnull().sum())

    print("\n Removing duplicates...")

    orders = orders.drop_duplicates()
    order_items = order_items.drop_duplicates()

    print("Duplicates Removed")

    print("\n Converting date columns...")

    orders["order_purchase_timestamp"] = pd.to_datetime(orders["order_purchase_timestamp"])

    print("Date conversion complete")

    print("\n Merging datasets...")

    merged_data = orders.merge(customers,
                               on="customer_id",
                               how="left")
    
    print("Merge complete")

    return {"orders":orders,
            "order_items":order_items,
            "customers":customers,
            "sellers":sellers,
            "merged":merged_data
            }

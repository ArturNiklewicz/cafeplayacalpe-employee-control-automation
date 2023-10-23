import pandas as pd
from models.product import Product

class ReadCSV:
    def read_csv(file_path):
        try: 
            df = pd.read_csv(file_path, encoding = 'latin-1')

            if not df.empty:
                product_sales = []

                for index, row in df.iterrows():
                    group = row['FAMILIA VENTA']
                    name = row['ARTíCULO']
                    qtySales = row['UNIDADES']
                    valSales = row['TOTAL']

                    # Create a product instance for each row
                    prod = Product(group, name, qtySales, valSales)

                    product_sales.append(prod)

                return product_sales
            else: 
                print("CSV file is empty.")
                return None
        except Exception as e:
            print(f"ERROR: {str(e)}")
            return None

   


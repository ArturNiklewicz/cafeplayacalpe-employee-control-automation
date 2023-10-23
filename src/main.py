from csv_handling.read_csv import ReadCSV


if __name__ == "__main__":
    file_path = '/Users/arturniklewicz/Desktop/Glop/csv/Total de venta por Artículo y Grupo resumido.csv'
    sales = ReadCSV.read_csv(file_path)

    if sales:
        for product in sales:
            print(f"Group: {product.group}, Name: {product.name}, Qty Sales: {product.qtySales}, Value Sales: {product.valSales}")
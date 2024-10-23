import csv
import psycopg2


with psycopg2.connect(host='localhost', port=5432, user='postgres', password='12345', database='north') as conn:
    with conn.cursor() as cur:
        with open('north_data/customers_data.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            next(csv_reader)
            for row in csv_reader:
                cur.execute("INSERT INTO customers VALUES (%s, %s, %s)", row)
        with open('north_data/employees_data.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            next(csv_reader)
            for row in csv_reader:
                cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)", row)
        with open('north_data/orders_data.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            next(csv_reader)
            for row in csv_reader:
                cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", row)
        conn.commit()

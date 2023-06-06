"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import os
import psycopg2


emp_file = os.path.join('..', 'homework-1', 'north_data', 'employees_data.csv')
cust_file = os.path.join('..', 'homework-1', 'north_data', 'customers_data.csv')
orders_file = os.path.join('..', 'homework-1', 'north_data', 'orders_data.csv')

conn = psycopg2.connect(
    host='localhost',
    database='north',
    user='postgres',
    password = '131091'

)
try:
    with conn:
        with conn.cursor() as cur:

            # запись в таблицу employees
            with open(emp_file,'r', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for item in reader:
                    cur.execute('insert into employees values (%s, %s, %s, %s, %s,%s)', (
                        item['employee_id'],
                        item['first_name'],
                        item['last_name'],
                        item['title'],
                        item['birth_date'],
                        item['notes']
                    ))

            # запись в таблицу customers
            with open(cust_file, 'r', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for item in reader:
                    cur.execute('insert into customers values (%s, %s, %s)', (
                        item['customer_id'], item['company_name'], item['contact_name']))

            # запись в таблицу orders
            with open(orders_file, 'r', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for item in reader:
                    cur.execute('insert into orders values (%s, %s, %s, %s, %s)', (
                        item['order_id'],
                        item['customer_id'],
                        item['employee_id'],
                        item['order_date'],
                        item['ship_city']
                    ))
finally:
    conn.close()





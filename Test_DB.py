import psycopg2

conn = psycopg2.connect("dbname=Test_BD user=postgres password=postgres host=localhost port=5432")
print("Database opened successfully")

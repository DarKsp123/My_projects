#import psycopg2

#conn = psycopg2.connect("dbname=Test_BD user=postgres password=postgres host=localhost port=5432")
#print("Database opened successfully")



M = [[1, 2, 3],  # Матрица в виде вложенных списков
     [4, 5, 6],
     [7, 8, 9]]

print(list(sum(M)))

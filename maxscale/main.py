#Jarre' Owens
#CNE370 Real World Project: Database Shard Github
#6/10/23
#This script will allow a user to connect to and query a sharded database.

import mysql.connector
from tabulate import tabulate

con = mysql.connector.connect(
    host="172.20.0.4",
    user="maxuser",
    password="maxpwd",
    port="4000"
)

cursor = con.cursor()

#Query 1: Finds and prints the largest zipcode in zipcodes_one
query1 = "SELECT MAX(zipcode) FROM zipcodes_one.zipcodes_one WHERE zipcode IS NOT NULL;"
cursor.execute(query1)
largest_zipcode = cursor.fetchone()[0]
print("\033[91mLargest Zipcode:\033[0m", largest_zipcode)

#Query 2: Finds and prints all zipcodes where state=KY (Kentucky)
query2_1 = "SELECT zipcode FROM zipcodes_one.zipcodes_one WHERE state='KY';"
cursor.execute(query2_1)
zipcodes_ky_1 = cursor.fetchall()

query2_2 = "SELECT zipcode FROM zipcodes_two.zipcodes_two WHERE state='KY';"
cursor.execute(query2_2)
zipcodes_ky_2 = cursor.fetchall()

print("\033[91mZipcodes in Kentucky:\033[0m")  # Red label
zipcodes_ky = [row[0] for row in zipcodes_ky_1 + zipcodes_ky_2]
num_columns = 10
num_rows = (len(zipcodes_ky) + num_columns - 1) // num_columns
for i in range(num_rows):
    start_index = i * num_columns
    end_index = (i + 1) * num_columns
    row_values = zipcodes_ky[start_index:end_index]
    row_output = "|" + "|".join(str(code) for code in row_values) + "|"
    print(row_output)

#Query 3: Finds and prints all zipcodes between 40000 and 41000
query3_1 = "SELECT zipcode FROM zipcodes_one.zipcodes_one WHERE zipcode BETWEEN 40000 AND 41000;"
cursor.execute(query3_1)
zipcodes_range_1 = cursor.fetchall()

query3_2 = "SELECT zipcode FROM zipcodes_two.zipcodes_two WHERE zipcode BETWEEN 40000 AND 41000;"
cursor.execute(query3_2)
zipcodes_range_2 = cursor.fetchall()

print("\033[91mZipcodes between 40000 and 41000:\033[0m")  # Red label
zipcodes_range = [row[0] for row in zipcodes_range_1 + zipcodes_range_2]
num_columns = 10
num_rows = (len(zipcodes_range) + num_columns - 1) // num_columns
for i in range(num_rows):
    start_index = i * num_columns
    end_index = (i + 1) * num_columns
    row_values = zipcodes_range[start_index:end_index]
    row_output = "|" + "|".join(str(code) for code in row_values) + "|"
    print(row_output)

#Query 4: Fetch the TotalWages column where state=PA (Pennsylvania)
#Thanks to Celine for the formatting help on this last query
print("\033[91mThe TotalWages column where state = PA:\033[0m")
cursor.execute("SELECT TotalWages FROM zipcodes_one.zipcodes_one WHERE state = 'PA';")
results = cursor.fetchall()
list3 = [result[0] for result in results if result[0] != ""]
cursor.execute("SELECT ALL TotalWages FROM zipcodes_two.zipcodes_two WHERE state = 'PA';")
results = cursor.fetchall()
list3 += [result[0] for result in results if result[0] != ""]
list3split = [list3[i:i+10] for i in range(0, len(list3), 10)]
print(tabulate(list3split, tablefmt='grid'))

# Closes the database connection
cursor.close()
con.close()

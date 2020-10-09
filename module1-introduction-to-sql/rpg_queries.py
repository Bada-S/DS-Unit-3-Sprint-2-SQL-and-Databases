
import pandas as pd
import sqlite3

connection = sqlite3.connect(r'C:\Users\james\Documents\Github\sql\DS-Unit-3-Sprint-2-SQL-and-Databases\module1-introduction-to-sql\rpg_db.sqlite3')

cursor = connection.cursor()


query = """
    SELECT
	count(character_id)
    FROM charactercreator_character;
"""

def execute_query(query):
    records = cursor.execute(query).fetchall()
    return f'{records} \n'

print(execute_query(query))
cursor.close()
connection.close()

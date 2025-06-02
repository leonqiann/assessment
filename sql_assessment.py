# Import the libraries to connect to the database and present the information in tables
import sqlite3
from tabulate import tabulate

# This is the filename of the database to be used
DB_NAME = 'sql_assessment.db'
# This is the SQL to connect to all the tables in the database
TABLES = (" chicago_bulls "
           "LEFT JOIN country ON chicago_bulls.country_id = country.country_id "
           "LEFT JOIN position ON chicago_bulls.position_id = position.position_id ")

def print_query(view_name:str):
    ''' Prints the specified view from the database in a table '''
    # Set up the connection to the database
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    # Get the results from the view
    sql = "SELECT * FROM '" + view_name + "'"
    cursor.execute(sql)
    results = cursor.fetchall()
    # Get the field names to use as headings
    field_names = "SELECT name from pragma_table_info('" + view_name + "') AS tblInfo"
    cursor.execute(field_names)
    headings = list(sum(cursor.fetchall(),()))
    # Print the results in a table with the headings
    print(tabulate(results,headings))
    db.close()

def print_parameter_query(fields:str, where:str, parameter):
    """ Prints the results for a parameter query in tabular form. """
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    sql = ("SELECT " + fields + " FROM " + TABLES + " WHERE " + where)
    cursor.execute(sql,(parameter,))
    results = cursor.fetchall()
    print(tabulate(results,fields.split(",")))
    db.close()


menu_choice = ''
while menu_choice != 'Z':
    menu_choice = input('Welcome to the cars database\n\n'
                        'Type the letter for the information you want\n'
                        "A: \n"
                        "B: \n"
                        'C: \n'
                        'D: \n'
                        'E: \n'
                        'F: \n'
                        'G: \n'
                        'H: \n'
                        'Z: Exit\n\n'
                        'Type option here: ')
    menu_choice = menu_choice.upper()
    if menu_choice == 'A':
        print_query('top 3 ppg')
    elif menu_choice == 'B':
        print_query('top 3 rpg')
    elif menu_choice == 'C':
        print_query('top 3 apg')
    elif menu_choice == 'D':
        print_query('not usa players')
    elif menu_choice == 'H':
        position = input('Which position do you want to see: ')
        print_parameter_query("first_name, last_name, position, age, height, weight, ppg, rpg, apg, jersey_num, country", "position = ? ORDER BY ppg DESC",position)

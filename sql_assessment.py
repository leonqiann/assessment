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
    menu_choice = input('Welcome to the Chicago Bulls database\n\n'
                        'Type the letter for the information you want\n'
                        "A: Top 3 scorers\n"
                        "B: Top 3 rebounders\n"
                        'C: Top 3 assisters\n'
                        "D: Info for player who aren't from the USA \n"
                        'E: Info about a player with a specific jersey number\n'
                        'F: Shortest player\n'
                        'G: Tallest player\n'
                        'H: Info about a player with a specific position\n'
                        'I: All info about a specific player\n'
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
    elif menu_choice == 'E':
        jersey_num = int(input('Enter a jersey number from 0 - 44 to see which player has that specific jersey number (If nothing shows up, that means no player has that jersey number.) : '))
        print_parameter_query("first_name, last_name, position, age, height, weight, ppg, rpg, apg, jersey_num, country", "jersey_num = ? ORDER BY ppg DESC",jersey_num)
    elif menu_choice == 'F':
        print_query('shortest')
    elif menu_choice == 'G':
        print_query('tallest')
    elif menu_choice == 'H':
        position = input('Which position do you want to see (Guard, Forward Center, Center, Guard Forward, Forward): ')
        position_title = position.title()
        print_parameter_query("first_name, last_name, position, age, height, weight, ppg, rpg, apg, jersey_num, country", "position = ? ORDER BY ppg DESC",position_title)
    elif menu_choice == 'I':
        first_name = input('Which player do you want to see: ')
        #makes the parameter query accept uncapitalized inputs 
        first_name_title = first_name.title()
        print_parameter_query("first_name, last_name, position, age, height, weight, ppg, rpg, apg, jersey_num, country", "first_name = ? ORDER BY ppg DESC",first_name_title)

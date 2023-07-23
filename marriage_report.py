"""
Description:
 Generates a CSV reports containing all married couples in
 the Social Network database.

Usage:
 python marriage_report.py
"""
import os
import sqlite3
from create_relationships import db_path, script_dir
import pandas as pd

def main():
    # Query DB for list of married couples
    married_couples = get_married_couples()

    # Save all married couples to CSV file
    csv_path = os.path.join(script_dir, 'married_couples.csv')
    save_married_couples_csv(married_couples, csv_path)

def get_married_couples():
    """Queries the Social Network database for all married couples.

    Returns:
        list: (name1, name2, start_date) of married couples 
    """
    # TODO: Function body
    # Hint: See example code in lab instructions entitled "Get a List of Relationships"
    connection = sqlite3.connect(db_path)
    cur = connection.cursor()

    all_relationships_query = """
 SELECT person1_id, person2_id, type, start_date FROM relationships
 JOIN people person1 ON person1_id = person1.id
 JOIN people person2 ON person2_id = person2.id;
"""
    cur.execute(all_relationships_query)
    all_relationships = cur.fetchall()
    connection.close()

    #Printing a sentence about the relationship.
    for person1_id, person2_id, start_date, type in all_relationships:
        print(f'{person1_id} has been a {type} of {person2_id} since {start_date}.')

def save_married_couples_csv(married_couples, csv_path):
    """Saves list of married couples to a CSV file, including both people's 
    names and their wedding anniversary date  

    Args:
        married_couples (list): (name1, name2, start_date) of married couples
        csv_path (str): Path of CSV file
    """
    # TODO: Function body
    # Hint: We did this in Lab 7.
    csv_path = r'D:\Semester 2\Scripting Applications\Lab_8\married_couples.csv'
    connection = sqlite3.connect('social_network.db')
    married_couple_query = """
    SELECT person1_id, person2_id, start_date FROM relationships 
    WHERE type = "spouse" OR type = "partner"
    """
    cur = connection.cursor()
    cur.execute(married_couple_query)
    married_couples = cur.fetchall()
    df = pd.DataFrame(married_couples, columns=['Pesron1', 'Person2', 'Anniversary'])
    df.to_csv(csv_path, index=True)

if __name__ == '__main__':
   main()
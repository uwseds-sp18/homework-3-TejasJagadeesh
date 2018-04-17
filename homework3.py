import sqlite3
import pandas as pd
import os

def create_dataframe(dbpath):
    """
    Function that takes the sqlite3 database path as an argument and creates a dataframe by reading all the tables.
    Returns the created dataframe.
    """
    #Check if file exists and raise exception if not
    if not os.path.exists(dbpath):
        raise ValueError("'{0}' doest not exist".format(dbpath))
    
    #Create the connection to the sqlite db using the dbpath argument
    conn = sqlite3.connect(dbpath)
    
    #Build the SQL query to read all the tables in the database
    sql_query = "SELECT video_id,category_id,'us' as language from USvideos"
    sql_query += " UNION SELECT video_id,category_id,'gb' as language from GBvideos"
    sql_query += " UNION SELECT video_id,category_id,'fr' as language from FRvideos"
    sql_query += " UNION SELECT video_id,category_id,'de' as language from DEvideos"
    sql_query += " UNION SELECT video_id,category_id,'ca' as language from CAvideos;"
    
    #use pandas to fetch the data from the database using the sql query and the connection
    df = pd.read_sql(sql_query,conn)
    
    #return the dataframe
    return df


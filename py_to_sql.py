# Send instructions to MySQL database server

import mysql.connector
import words_frequencies
import datetime
import os

# Main words list
most_pop_100 = ['the', 'i', 'a', 'of', 'and', 'to', 'it', 'that', 'in', 'was', 's', 'as', 'he', 'you', 'my', 'his', 'is', 'for', 'what', 'up', 'manuel', 'lin', 'just', 'think', 'musical', 'me', 'like', 'writing', 'with', 'who', 'this', 'so', 'school', 're', 'from', 'time', 'm', 'hamilton', 'best', 'because', 'at', 'about', 'when', 'were', 'we', 'under', 'kid', 'island', 'hop', 'hip', 'him', 'do', 'all', 'writer', 'very', 'there', 'them', 'start', 'she', 'remember', 'pseudonym', 'parents', 'out', 'one', 'on', 'miranda', 'life', 'if', 'get', 'be', 'an', '11', 'would', 've', 'thought', 'things', 'they', 'than', 'starts', 'show', 'scared', 'people', 'part', 'old', 'not', 'myself', 'musicals', 'most', 'more', 'into', 'home', 'have', 'got', 'going', 'ever', 'early', 'discs', 'desert', 'could', 'but']
most_pop_20 = most_pop_100[0:20]



# create a MySQL table with list 
def create_mysql_table():
    table_name = 'news_'+str(datetime.date.today())
    
    column_names = []

    for item in most_pop_20:
        column_names.append(item+'_'+' VARCHAR(100)') # using underscore to
                                          # avoid the words reserved for MySQL

    # create a string to be interpreted by the MySQL server
    list_to_mysql_str = """CREATE TABLE %s(
                       id INT AUTO_INCREMENT PRIMARY KEY,
                       %s);""" % (table_name, column_names)

    # remove some symbols which don't fit the SQL expression
    list_to_mysql_str_2 = list_to_mysql_str.replace('[', '')
    list_to_mysql_str_3 = list_to_mysql_str_2.replace(']', '')
    list_to_mysql_str_4 = list_to_mysql_str_3.replace('-', '')
    list_to_mysql = list_to_mysql_str_4.replace('\'', '')
    
    print(list_to_mysql) # check how the string looks

    conn = mysql.connector.connect(user = 'root', password = 'dance',
                                   host = 'localhost')
    cursor = conn.cursor()
    cursor.execute('USE info_3;')
    cursor.execute(list_to_mysql)    

    conn.commit()
    conn.close()

# Populate mysql table function
def populate_mysql_table(text_file_name):
    table_name = 'news_'+str(datetime.date.today())

    most_pop_100 = words_frequencies.word_usage(text_file_name)
    most_pop_20 = most_pop_100[0:20]

    column_names = []
    column_values = []

    for item in most_pop_20:
        column_names.append(item[1]+'_') # using underscore to avoid the words
        column_values.append(item[0]) # reserved for MySQL

    list_to_mysql_str = """INSERT INTO %s(id, %s)
                       VALUES(NULL, %s);""" % (table_name, column_names,
                                               column_values)

    list_to_mysql_str_2 = list_to_mysql_str.replace('[', '')
    list_to_mysql_str_3 = list_to_mysql_str_2.replace(']', '')
    list_to_mysql_str_4 = list_to_mysql_str_3.replace('-', '')
    list_to_mysql = list_to_mysql_str_4.replace('\'', '')
    
    print(list_to_mysql)

    conn = mysql.connector.connect(user = 'root', password = 'dance',
                                   host = 'localhost')
    cursor = conn.cursor()
    cursor.execute('USE info_3;')
    cursor.execute(list_to_mysql)    

    conn.commit()
    conn.close()

def multiple_files():
    os.chdir('today\'s_articles')
    folder_files = os.listdir()

    for text_file_name in folder_files:
        if text_file_name[-3:] == 'txt':
            populate_mysql_table(text_file_name)





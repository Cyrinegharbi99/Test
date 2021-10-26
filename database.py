# -*- coding: utf-8 -*-
"""
Created on Dim Oct 24 09:52:47 2021

@author: lenovo
"""
#Launching the facebook page scraper
import mysql.connector
from facebook_scraper import get_posts
listposts = []
for post in get_posts("wikiHow", pages=2):
    print(post['text'][:50])
    listposts.append(post)
#establishing the connection
conn = mysql.connector.connect(user='root', password='password', host='127.0.0.1')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Doping database MYDATABASE if already exists.
cursor.execute("DROP database IF EXISTS Facebook")

#Preparing query to create a database
sql = "CREATE database Facebook"
cursor.execute(sql)
#Creating table as per requirement
sql ='''CREATE TABLE POSTS(
   POST(20) CHAR
)'''
cursor.execute(sql)
# Preparing SQL query to INSERT a record into the database.
mySql_insert_query = """INSERT INTO WIKI2 (Post) 
VALUES (%s) """
records_to_insert = listposts
cursor.executemany(mySql_insert_query, records_to_insert)
conn.commit()
print(cursor.rowcount, "Record inserted successfully into Facebook table")

# disconnect from server
conn.close()
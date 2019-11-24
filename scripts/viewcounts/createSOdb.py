# this script creates or accesses a database containting viewcounts from 
# each StackOverflow posts dump and imports each postid,questiontype,viewcount,tag 
# into newly created tables relative to each dump

import sqlite3
import subprocess

dirnames = ("2016-09-12","2016-12-15","2017-03-14","2017-06-12","2017-12-01","2018-03-13","2018-06-05","2018-09-05","2018-12-02","2019-03-04","2019-06-03","2019-09-04")
pathtodb = "./SOviews.db"
pathtodirs = "./"

def checkTableExists(connection, tablename):
    cursor = connection.cursor()
    cursor.execute("""
        SELECT COUNT(name)
        FROM sqlite_master
        WHERE type='table'
        AND name='""" + tablename + """'""")
    if cursor.fetchone()[0] == 1:
        cursor.close()
        return True

    cursor.close()
    return False


if __name__ == "__main__":
    # connect to or create SOviews database
    connection = sqlite3.connect(pathtodb)
    cursor = connection.cursor()

    # loop through Post dump csv's by date
    for dir in dirnames:
        infile = pathtodirs + dir + "/postviews.csv"
        tablename = "views_" + dir.replace("-","_")

        # stops if table/data already exists
        if(checkTableExists(connection,tablename)): 
            continue

        # create table in SOviews db
        createtablequery = '''CREATE TABLE IF NOT EXISTS ''' + tablename + '''(
            postid integer, 
            viewcount integer, 
            tag text);'''

        # import each dump's csv
        importcall = ".import " + infile + " " + tablename
        
        cursor.execute(createtablequery)
        subprocess.call(["sqlite3", pathtodb, importcall])

    cursor.close()
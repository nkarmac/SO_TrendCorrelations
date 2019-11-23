# this script queries the SOviews database to extracts viewcounts
# of each considered language from each dump into an output dir

import sqlite3
import csv
import os

dirnames = ("2016-09-12","2016-12-15","2017-03-14","2017-06-12","2017-12-01","2018-03-13","2018-06-05","2018-09-05","2018-12-02","2019-03-04","2019-06-03","2019-09-04")
languages = (   'java','c','c++','python','.net', 'c#','javascript', 'sql','php',
                'assembly', 'objective-c', 'delphi', 'perl','matlab', 'ruby','vba',
                'groovy','swift','go','r','sas' ,'abap','fortran', 'dart','scala', 
                'prolog', 'lisp', 'lua', 'rust', 'ada','f#', 'apex', 'kotlin', 
                'scheme', 'labview', 'typescript', 'julia', 'awk', 'haskell','clojure', 
                'erlang', 'bash', 'elixir', 'html', 'vhdl', 'verilog', 'vb.net', 'd', 'plsql', 
                'netlogo', 'cobol', 'actionscript-3', 'vbscript', 'powershell', 'coffeescript',  'common-lisp', 'erlang')

outputdir = "./langviews/"
pathtodb = "./SOviews.db"

if __name__ == "__main__":
    # connect to SOviews database
    connection = sqlite3.connect(pathtodb)
    cursor = connection.cursor()
    
    # creates output (langviews) directory
    if not os.path.exists(outputdir):
        os.makedirs(outputdir)

    # loops through tables relative to each dump
    for dir in dirnames:

        # creates directory in langviews for each dump
        if not os.path.exists(outputdir + dir + "/"):
            os.makedirs(outputdir + dir + "/")

        # loops through each language
        tablename = "views_" + dir.replace("-","_")
        for lang in languages:
            # query's all SO question type posts tagged with the given language
            query = ''' SELECT postid, viewcount
                        FROM ''' + tablename + ''' 
                        WHERE tag = \'''' + lang + '''\'
                        AND posttype = 1; '''
            cursor.execute(query)

            # create output csv for each language in each dump's directory within langviews
            outfile = outputdir + dir + "/" + lang + ".csv"
            with open(outfile,'w') as out_csv_file:
                csv_out = csv.writer(out_csv_file)
                # write header
                csv_out.writerow(["postid", "viewcount"])
                # write data
                for result in cursor:
                    csv_out.writerow(result)

    cursor.close()
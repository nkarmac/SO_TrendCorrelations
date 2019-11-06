# return 0 padded month number as a string
def stringmonth(month):
    if month < 10:
        return '0' + str(month)
    else:
        return str(month)

# progress to the next month
def next(month, year):
    month += 1
    if (month == 13):
        year += 1
        month = 1
    return month, year

import sqlite3
import csv

year = 2008
month = 8

nextyear = 2008
nextmonth = 9


connection = sqlite3.connect ("stackoverflow.db")
cursor = connection.cursor()

# loop monthly until June 2019
# query all posts per month for each language and sum viewcounts
while (year == 2019 and month <= 6) or year < 2019:

    query = "select tag, sum(postmeta.viewcount) from posttags inner join postmeta on postmeta.postid = posttags.postid where postmeta.creationdate < '" + str(nextyear) + "-"+stringmonth(nextmonth)+"-01' and postmeta.creationdate > '" + str(year)+"-"+stringmonth(month)+"-01' and postmeta.posttypeid = 1 and posttags.tag in ('java','c','c++','python','.net', 'c#','javascript', 'sql','php','assembly', 'objective-c', 'delphi', 'perl','matlab', 'ruby','vba','groovy','swift','go','r','sas' ,'abap','fortran', 'dart','scala', 'prolog', 'lisp', 'lua', 'rust', 'ada','f#', 'apex', 'kotlin', 'scheme', 'labview', 'typescript', 'julia', 'awk', 'haskell','clojure', 'erlang', 'bash', 'elixir', 'html', 'vhdl', 'verilog', 'vb.net', 'd', 'plsql', 'netlogo', 'cobol', 'actionscript-3', 'vbscript', 'powershell', 'coffeescript',  'common-lisp', 'erlang') group by tag;"
    cursor.execute(query)

    # output each languages total viewcount to the respective month file
    filename = './viewcount/' + str(year) + "-" + stringmonth(month) + ".csv"
    
    with open(filename,'w') as out_csv_file:
        csv_out = csv.writer(out_csv_file)
        # write header
        csv_out.writerow([d[0] for d in cursor.description])
        # write data
        for result in cursor:
            csv_out.writerow(result)

    month, year = next(month, year)
    nextmonth, nextyear = next(nextmonth, nextyear)


cursor.close()
connection.close()



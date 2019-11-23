# Viewcount Scripts

### Pre-reqs:
* scala 2.11.8+
* jdk/jre 8+
* p7zip-full
* sqlite3

## Usage

Place all files in base directory containing all dump directories, then run
* dump2csv.sh
* createSOdb.py
* viewcounts.py

## Extract Dumps to csv

Place [dump2csv.sh](./dump2csv.sh) in the dir containing all the dump dirs, and run to extract all dumps at once into csv's containing postid,posttype,viewcount,tag
```
chmod +x dump2csv.sh
./dump2csv.sh
```

Alternatively, extract one at a time using [post-views.scala](./post-views.scala)
```
gzip -c -d ./2016-09-12/Posts.xml.gz | tail -c +4| scala post-views.scala > ./2016-09-12/postviews.csv
```
or
```
p7zip -c -d ./2019-09-04/Posts.7z | tail -c +4| scala post-views.scala > ./2019-09-04/postviews.csv
```


## Import to database

After extracting each csv into each dumps directory, run [createSOdb.py](createSOdb.py) to import all csv's into a new sqlite3 database named SOviews.db, with each dump's viewcounts as a table:
```
python createSOdb.py
```

Alternatively, import one at a time:
```
CREATE TABLE IF NOT EXISTS views_2016_09_12(
    postid integer, 
    posttype integer, 
    viewcount integer, 
    tag text
);
.import ./2016-09-12/postviews.csv views_2016_09_12
```


## Extract Language Viewcounts

To extract viewcounts for each considered language into new dirs relative to each dump, run:
```
python viewcounts.py
```
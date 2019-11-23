#!/bin/bash

declare -a gzip_dirs=("2016-09-12" "2016-12-15" "2017-03-14")
declare -a p7zip_dirs=("2017-06-12" "2017-12-01" "2018-03-13" "2018-06-05" "2018-09-05" "2018-12-02" "2019-03-04" "2019-06-03" "2019-09-04")
pathtodirs="./"

for dir in ${gzip_dirs[@]}; do
    dirname="$pathtodirs$dir"
    gzip -c -d $dirname/Posts.xml.gz | tail -c +4 | scala post-views.scala > $dirname/postviews.csv
done

for dir in ${p7zip_dirs[@]}; do
    dirname="$pathtodirs$dir"
    p7zip -c -d $dirname/Posts.7z | tail -c +4 | scala post-views.scala > $dirname/postviews.csv

done
#/bin/bash
clear
d=`echo $1 | tr '\' '/' 2> /dev/null`
python.exe $d
read

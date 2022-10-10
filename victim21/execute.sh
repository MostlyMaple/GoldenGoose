#!/bin/sh
END=5
for ((i=1;i<=END;i++));
do
   python3 goldengoose.py $i
done

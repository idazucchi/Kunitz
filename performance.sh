# evaluate the best threshold

for i in `cat threshold.txt`
do
python3 confusionM.py labeled_data.txt $i 2
done > prot_roc.txt
echo 'done'

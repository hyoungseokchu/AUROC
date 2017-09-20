#!/usr/bin/python
'''
	File name : main.py
	Author : Hyoungseok Chu (hyoungseok.chu@gmail.com)
	Date created : 18/09/2017
	Date last modified : 20/09/2017
	Python version : 2.7.5
'''

from auroc import compute_auroc

inputfile = open("test_data.txt","r")

lines = inputfile.readlines()

predict = []
target  = []

for line in lines : 
	predict.append(    line.split()[0] )
	target.append (int(line.split()[1]))

[auc, roc] = compute_auroc(predict,target)
print(auc)

inputfile.close()

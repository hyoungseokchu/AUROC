#!/usr/bin/python
'''
	File name : main.py
	Author : Hyoungseok Chu (hyoungseok.chu@gmail.com)
	Date created : 18/09/2017
	Date last modified : 29/09/2017
	Python version : 2.7.5
'''

from auroc import compute_auroc, read_file

predict_file = 'prediction_file.txt'
label_file   = 'label_file.txt'

[predict, target] = read_file(predict_file, label_file

[auc, roc] = compute_auroc(predict,target)
print(auc)

inputfile.close()

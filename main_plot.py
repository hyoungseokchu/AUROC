#!/usr/bin/python
'''
	File name : main_plot.py
	Author : Hyoungseok Chu (hyoungseok.chu@gmail.com)
	Date created : 20/09/2017
	Date last modified : 29/09/2017
	Python version : 2.7.5
'''

from auroc import compute_auroc, read_file
import matplotlib.pyplot as plt

predict_file = 'prediction_file.txt'
label_file   = 'label_file.txt'

[predict, target] = read_file(predict_file, label_file)

[auc, roc] = compute_auroc(predict,target)
print(auc)

n = len(predict)

plt.plot(*zip(*roc), label='ROC curve')
plt.plot([0,1],      label='Random guess', linestyle='--', color='red')
plt.legend(loc=4)
plt.ylabel('TPR (True Positive Rate)')
plt.xlabel('FPR (False Positive Rate)')
plt.title('ROC Curve (AUROC : %7.3f)' % (auc))
plt.axis([0,1,0,1])
plt.grid()
plt.show()


#!/usr/bin/python
'''
	File name : main_plot.py
	Author : Hyoungseok Chu (hyoungseok.chu@gmail.com)
	Date created : 20/09/2017
	Date last modified : 15/09/2017
	Python version : 2.7.5
'''

import sys
import argparse
import matplotlib.pyplot as plt
from auroc import compute_auroc, read_file, read_merged_file

"""
Arguments rule
-p : prediction file name
-l : label file name
-i : merged (problem number, prediction, label order) file name

ex) $ python ./main.py -p prediction_file.txt -l label_file.txt
    $ python ./main.py -i merged_pl.txt
"""

argparser = argparse.ArgumentParser(description='compute AUROC to evaluate binary classification performance.')
argparser.add_argument('-p', '--pred', default='prediction_file.txt', help='prediction result file.')
argparser.add_argument('-l', '--label', default='label_file.txt', help='label file.')
argparser.add_argument('-i', '--integrated', default='', help='prediction+label merged file. The input file must consist of triples of ID,pred_prob,and label. DO NOT USE WITH -p(--pred) OR -l(--label) OPTIONS. if -i option is assigned, -p and -l options will be ignored.')

args = argparser.parse_args()

if len(args.integrated) > 0:
    sys.stderr.write('Read a merged file with -i option: ' + args.integrated + '\n')

    [predict, target] = read_merged_file(args.integrated)
else:
    predict_file = args.pred 
    label_file   = args.label
    sys.stderr.write('Read two files with -p, -l options: ' + predict_file + ', ' + label_file + '\n')

    [predict, target] = read_file(predict_file, label_file)

[auc, roc] = compute_auroc(predict,target)

print('%0.7f' % (auc))

n = len(predict)

# This is for plotting
plt.plot(*zip(*roc), label='ROC curve')
plt.plot([0,1],      label='Random guess', linestyle='--', color='red')
plt.legend(loc=4)
plt.ylabel('TPR (True Positive Rate)')
plt.xlabel('FPR (False Positive Rate)')
plt.title('ROC Curve (AUROC : %7.3f)' % (auc))
plt.axis([0,1,0,1])
plt.grid()
plt.show()


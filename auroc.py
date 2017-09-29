'''
	File name : auroc.py
	Author : Hyoungseok Chu (hyoungseok.chu@gmail.com)
	Date created : 18/09/2017
	Date last modified : 29/09/2017
	Python version : 2.7.5
'''


def compute_auroc(predict, target):

	n = len(predict)

	# Cutoffs are of prediction values
	cutoff = predict

	TPR = [0 for x in range(n)]
	FPR = [0 for x in range(n)]

	for k in range(n):

		predict_bin = 0

		TP = 0	# True  Positive
		FP = 0	# False Positive
		FN = 0	# False Negative
		TN = 0	# True  Negative

		for j in range(n):
			if (predict[j] >= cutoff[k]):
				predict_bin = 1
			else :
				predict_bin = 0

			TP = TP + (      predict_bin  &      target[j]  ) 
			FP = FP + (      predict_bin  & (not target[j]) )
			FN = FN + ( (not predict_bin) &      target[j]  )
			TN = TN + ( (not predict_bin) & (not target[j]) )

		# True  Positive Rate
		TPR[k] = float(TP) / float(TP + FN)
		# False Positive Rate
		FPR[k] = float(FP) / float(FP + TN)

	# Positions of ROC curve (FPR, TPR)
	ROC = sorted(zip(FPR, TPR), reverse=True)

	AUROC = 0

	# Compute AUROC Using Trapezoidal Rule
	for j in range(n-1):
		h =   ROC[j][0] - ROC[j+1][0]
		w =  (ROC[j][1] + ROC[j+1][1]) / 2.0

		AUROC = AUROC + h*w
	
	return AUROC, ROC

def read_file(predict_file, label_file):
	# ASSUMPTION #
	# 1. The dimension of two input file should have same dimension.
	# 2. Both files must be sorted in increasing order by problem index.

	# ex) predict_file
	#     1_00001,0.239
	#     1_00002,0.931
	#     1_00003,...

	# ex) label_file
	#     1_00001,0
	#     1_00002,1
	#     1_00003,...

	p_fid = open(predict_file, "r")
	l_fid = open(label_file, "r")

	plines = p_fid.readlines()
	llines = l_fid.readlines()

	predict = []
	target  = []

	for pline in plines : 
		predict.append(    pline.split(',')[1] )

	for lline in llines : 
		target.append (int(lline.split(',')[1]))
	
	p_fid.close()
	l_fid.close()
	
	return predict, target

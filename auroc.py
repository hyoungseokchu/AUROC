'''
	File name : auroc.py
	Author : Hyoungseok Chu (hyoungseok.chu@gmail.com)
	Date created : 18/09/2017
	Date last modified : 22/11/2017
	Python version : 2.7.5 
'''

# import regular expression to parse input files 
import re

def compute_auroc(predict, target):
	"""
	This function is to compute AUROC. 
	The dimension of two input parameters should be same.
	
	Parameters
	----------
	predict : Prediction vector between 0 to 1 (single precision)
	target  : Label vector weather 0 or 1      (single precision or boolean)
	
	Returns
	-------
	ROC   : Positions of ROC curve (FPR, TPR)
	        This is for plotting or validation purposes
	AUROC : The value of area under ROC curve
	"""
	n = len(predict)

	# Cutoffs are of prediction values
	cutoff = predict

	TPR = [0 for x in range(n+2)]
	FPR = [0 for x in range(n+2)]

	for k in range(n):
		predict_bin = 0

		TP = 0	# True	Positive
		FP = 0	# False Positive
		FN = 0	# False Negative
		TN = 0	# True	Negative

		for j in range(n):
			if (predict[j] >= cutoff[k]):
				predict_bin = 1
			else :
				predict_bin = 0

			TP = TP + (	 predict_bin  &      target[j]	) 
			FP = FP + (	 predict_bin  & (not target[j]) )
			FN = FN + ( (not predict_bin) &	 target[j]	)
			TN = TN + ( (not predict_bin) & (not target[j]) )

		# True	Positive Rate
		TPR[k] = float(TP) / float(TP + FN)
		# False Positive Rate
		FPR[k] = float(FP) / float(FP + TN)

	TPR[n] = 0.0
	FPR[n] = 0.0
	TPR[n+1] = 1.0
	FPR[n+1] = 1.0
	
	# Positions of ROC curve (FPR, TPR)
	ROC = sorted(zip(FPR, TPR), reverse=True)

	AUROC = 0

	# Compute AUROC Using Trapezoidal Rule
	for j in range(n+1):
		h =   ROC[j][0] - ROC[j+1][0]
		w =  (ROC[j][1] + ROC[j+1][1]) / 2.0

		AUROC = AUROC + h*w

	return AUROC, ROC

def read_merged_file(given_file):
	"""
	This function is to read prediction and label values from one file.
	
	Assumptions
	-----------
	1. The dimension of each vectro should have same dimension.
	2. 'given_file' must be sorted in increasing order by problem index.
	  ex) given_file
	      1_00001,0.239,0
	      1_00002,0.931,1
	      1_00003,...
	
	Parameters
	----------
	given_file : merged (prediction and label) file name (string)
		
	Returns
	-------
	pred    : Prediction vector (single precision)
	target  : Label vector      (single precision or boolean)
	
	Raises
	------
	Exception : The dimension of two files should be same
	"""

	splitre = re.compile('[,\s]')
	pred = []
	target = []

	with open(given_file, "r") as pl_fid:
		for plline in pl_fid:
			triples = splitre.split(plline.strip())
			if len(triples) != 3:
				continue
			pred.append(float(triples[1]))
			target.append(int(triples[2]))
		pl_fid.close()

	if len(pred) != len(target) or len(pred) == 0 or len(target) == 0:
		raise Exception("ERROR: the number of lines in the prediction file and label file is not the same: len(pred) - "\
                        + str(len(pred)) + ", len(target) - " + str(len(target)))

	return pred, target

def read_file(predict_file, label_file):
	"""
	This function is to read prediction and label values from file.
	 * If there are two different files of prediction and label, use this function.
	
	Assumptions
	-----------
	1. The dimension of two input file should have same dimension.
	2. Both files must be sorted in increasing order by problem index.
	  ex) predict_file
	      1_00001,0.239
	      1_00002,0.931
	      1_00003,...
	  ex) label_file
	      1_00001,0
	      1_00002,1
	      1_00003,...
	
	Parameters
	----------
	predict_file : prediction file name (string)
	label_file   : label file name      (string)
	
	Returns
	-------
	predict : Prediction vector (single precision)
	target  : Label vector      (single precision or boolean)
	
	Raises
	------
	Exception : The dimension of two files should be same
	"""

	splitre = re.compile("[,\s]")

	p_fid = open(predict_file, "r")
	l_fid = open(label_file, "r")

	predict = []
	target	= []

	for pline in p_fid: 
		sval = splitre.split(pline.strip())
		if len(sval) != 2:
			print (sval)
			continue
		predict.append(float(sval[1]))

	for lline in l_fid: 
		sval = splitre.split(lline.strip())
		if len(sval) != 2:
			continue
		target.append(int(sval[1]))

	if len(predict) != len(target) or len(predict) == 0 or len(target) == 0:
		raise Exception("ERROR: the number of lines in the prediction file and label file is not the same: len(pred) - "\
                        + str(len(predict)) + ", len(target) - " + str(len(target)))

	p_fid.close()
	l_fid.close()

	return predict, target

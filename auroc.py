'''
	File name : auroc.py
	Author : Hyoungseok Chu (hyoungseok.chu@gmail.com)
	Date created : 18/09/2017
	Date last modified : 20/09/2017
	Python version : 2.7.5
'''


def compute_auroc(predict, target):

	n = len(predict)

	cutoff = predict

	TPR = [0 for x in range(n)]
	FPR = [0 for x in range(n)]

	for k in range(n):

		predict_bin = 0

		TP = 0
		FP = 0
		FN = 0
		TN = 0

		for j in range(n):
			if (predict[j] >= cutoff[k]):
				predict_bin = 1
			else :
				predict_bin = 0

			TP = TP + (      predict_bin  &      target[j]  ) 
			FP = FP + (      predict_bin  & (not target[j]) )
			FN = FN + ( (not predict_bin) &      target[j]  )
			TN = TN + ( (not predict_bin) & (not target[j]) )

		TPR[k] = float(TP) / float(TP + FN)
		FPR[k] = float(FP) / float(FP + TN)

	ROC = sorted(zip(FPR, TPR), reverse=True)

	AUROC = 0

	for j in range(n-1):
		h =   ROC[j][0] - ROC[j+1][0]
		w =  (ROC[j][1] + ROC[j+1][1]) / 2.0

		AUROC = AUROC + h*w
	
	return AUROC, ROC

# AUROC
AUROC (Area Under the Receiver Operating Characteristic)

This offers a function to evaluate AUROC. I assume that the input file should be consist of two vectors. The first vector is a predicted one ranging from 0 to 1 of real variable. The second vector is the target variable which contains labels wether 0 or 1. Cut-off values of ROC curve are of predicted elements. I applied trapezoidal rule to calculate the area under ROC curve. By default, the position (0,0) and (1,1) will be added to prevent some loss of area.

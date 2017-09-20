# AUROC
AUROC (Area Under the Receiver Operating Characteristic)

This offers a function to compute AUROC. Basic assumption of an input file should be consist of two vectors. The first vector is a predicted one ranging from 0 to 1 of real variable. The second vector is the target variable which contains labels wether 0 or 1. Cut-off values of ROC curve are of predicted elements. Trapezoidal rule is applied to calculate the area under ROC curve.

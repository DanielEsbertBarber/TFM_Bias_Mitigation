import numpy as np
from sklearn.metrics import confusion_matrix

def compute_metrics(df, target, model, threshold):


    y_pred = (model.predict_proba(df)[:, 1] > threshold)

    TN, FP, FN, TP = confusion_matrix(target, y_pred).ravel()

    # Positive = Loan granted
    # Negative = Loan denied

    total_loans    = TN + FP + FN + TP
    loans_granted  = FP + TP
    loans_rejected = FN + TN

    bad_loans  = TN + FP
    good_loans = FN + TP

    # What % of the granted loans will default

    if loans_granted > 0:
        tmo = FP / loans_granted
    else:
        tmo = 0

    # What % of loans that won't default we accept

    if good_loans > 0:
        recall = TP / good_loans
    else:
        recall = 0

    # When we accept a loan, what is the % that won't default
    if loans_granted > 0:
        precision = TP / loans_granted
    else:
        precision

    # Given that a loan will default, what is the chance it will be accepted?

    if bad_loans > 0:
        FPR = FP / bad_loans
    else:
        FPR = 0

    # Given that a loan won't default, what is the chance it won't be accepted?

    if good_loans > 0:
        FNR = FN / good_loans
    else:
        FNR = 0

    if total_loans > 0:
        approval_rate = loans_granted / total_loans
    else:
        approval_rate = 0

    return [threshold, tmo, approval_rate, recall, precision, FPR, FNR]

def fpr(y_true, y_pred):
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
    return fp / (fp + tn)

def fnr(y_true, y_pred):
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
    return fn / (fn + tp)

    

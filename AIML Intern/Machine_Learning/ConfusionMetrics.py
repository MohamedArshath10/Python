from sklearn.metrics import confusion_matrix

# True values
y_true = [1, 0, 1, 1, 0, 1, 0]

# Predicted values
y_pred = [1, 0, 1, 0, 0, 1, 1]

# Generate confusion matrix
cm = confusion_matrix(y_true, y_pred)
# tp,fp,tn,fn = cm
# print("True Positives:", tp)
# print("False Positives:", fp)
# print("True Negatives:", tn)
# print("False Negatives:", fn)
print(cm)


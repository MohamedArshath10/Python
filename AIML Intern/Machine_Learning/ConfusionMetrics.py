from sklearn.metrics import confusion_matrix

# True values
y_true = [1, 0, 1, 1, 0, 1, 0]

# Predicted values
y_pred = [1, 0, 1, 0, 0, 1, 1]

# Generate confusion matrix
cm = confusion_matrix(y_true, y_pred)

print("Confusion Matrix:")
print(cm)

# TP = 3
#
# TN = 2
#
# FP = 1
#
# FN = 1
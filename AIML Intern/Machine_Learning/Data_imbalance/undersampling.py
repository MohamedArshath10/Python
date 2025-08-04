from imblearn.under_sampling import RandomUnderSampler

rus = RandomUnderSampler()
X_under, y_under = rus.fit_resample(X_train, y_train)
print("After Undersampling:", Counter(y_under))

model = LogisticRegression()
model.fit(X_under, y_under)
y_pred = model.predict(X_test)

print(classification_report(y_test, y_pred))
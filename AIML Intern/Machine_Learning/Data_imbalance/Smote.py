from collections import Counter
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from imblearn.over_sampling import RandomOverSampler, SMOTE
from imblearn.under_sampling import RandomUnderSampler

# 1. Create Imbalanced Dataset
X, y = make_classification(n_classes=2, class_sep=2,
                           weights=[0.90, 0.10],  # 90% vs 10%
                           n_informative=3, n_redundant=1,
                           flip_y=0, n_features=5,
                           n_clusters_per_class=1,
                           n_samples=1000, random_state=10)

print("Original class distribution:", Counter(y))

# 2. Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.3, random_state=42)

# Utility function to train and evaluate
def train_evaluate(X_train, y_train, model_name="Original"):
    model = LogisticRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print(f"\n--- {model_name} ---")
    print(classification_report(y_test, y_pred))

# 3. Original Model (No Balancing)
train_evaluate(X_train, y_train, "Original Imbalanced")

# 4. Random Oversampling
ros = RandomOverSampler()
X_ros, y_ros = ros.fit_resample(X_train, y_train)
print("After Random Oversampling:", Counter(y_ros))
train_evaluate(X_ros, y_ros, "Random Oversampling")

# 5. SMOTE
sm = SMOTE()
X_smote, y_smote = sm.fit_resample(X_train, y_train)
print("After SMOTE:", Counter(y_smote))
train_evaluate(X_smote, y_smote, "SMOTE Oversampling")

# 6. Random Undersampling
rus = RandomUnderSampler()
X_rus, y_rus = rus.fit_resample(X_train, y_train)
print("After Random Undersampling:", Counter(y_rus))
train_evaluate(X_rus, y_rus, "Random Undersampling")

# 7. Class Weights
model_weighted = LogisticRegression(class_weight='balanced')
model_weighted.fit(X_train, y_train)
y_pred_weighted = model_weighted.predict(X_test)
print("\n--- Class Weight Balanced ---")
print(classification_report(y_test, y_pred_weighted))
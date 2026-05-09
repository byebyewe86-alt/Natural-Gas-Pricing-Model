import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

df = pd.read_csv('Task 3 and 4_Loan_Data.csv')

print(df.head(10))
print(df.info())
print(df.describe())

df.drop('customer_id', axis=1, inplace=True)

X = df.drop('default', axis=1)
y = df['default']

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LogisticRegression()
model.fit(X_train_scaled, y_train)

y_pred = model.predict(X_test_scaled)

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\nAccuracy Score:", accuracy_score(y_test, y_pred))

# Probability of default for test data
y_prob = model.predict_proba(X_test_scaled)

print("\nProbability of Default (First 10 Customers):")
print(y_prob[:10])


# Function to calculate expected loss
def calculate_expected_loss(
    credit_lines_outstanding,
    loan_amt_outstanding,
    total_debt_outstanding,
    income,
    years_employed,
    fico_score
):

    customer_data = [[
        credit_lines_outstanding,
        loan_amt_outstanding,
        total_debt_outstanding,
        income,
        years_employed,
        fico_score
    ]]

    pd_probability = model.predict_proba(
        scaler.transform(customer_data)
    )[0][1]

    expected_loss = (
        pd_probability
        * loan_amt_outstanding
        * 0.9
    )

    return pd_probability, expected_loss


# Example customer
pd_value, loss = calculate_expected_loss(
    2, 5000, 10000, 50000, 4, 620
)

print("\nProbability of Default:", pd_value)
print("Expected Loss:", loss)
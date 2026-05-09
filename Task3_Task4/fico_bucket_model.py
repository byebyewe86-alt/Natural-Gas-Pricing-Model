import pandas as pd


df = pd.read_csv('Task 3 and 4_Loan_Data.csv')

# Create 5 FICO buckets (5 = worst, 1 = best)
df['rating'] = pd.qcut(
    df['fico_score'],
    q=5,
    labels=[5, 4, 3, 2, 1]
)

# Probability of default for each rating
pd_table = df.groupby('rating')['default'].mean()

print("Probability of Default by Rating:")
print(pd_table)



def get_rating(fico_score):

    for rating in pd_table.index:
        bucket = df[df['rating'] == rating]['fico_score']

        if fico_score >= bucket.min() and fico_score <= bucket.max():
            return rating, pd_table[rating]


# Example
rating, pd_probability = get_rating(669)

print("\nRating:", rating)
print("Probability of Default:", pd_probability)
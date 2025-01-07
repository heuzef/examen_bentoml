import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load Data
df = pd.read_csv("data/raw/admission.csv")

# Remove the "Serial No."
df = df.drop(columns=["Serial No."])

# Renaming
df = df.rename(columns={
    "GRE Score": "GRE_Score",
    "TOEFL Score": "TOEFL_Score",
    "University Rating": "University_Rating",
    "SOP": "SOP",
    "LOR ": "LOR",
    "CGPA": "CGPA",
    "Research": "Research",
    "Chance of Admit ": "Chance_of_Admit"
})

# Set features and target
X, y = df.drop(["Chance_of_Admit"], axis = 1), df["Chance_of_Admit"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Export processed data
X_train.to_csv("data/processed/X_train.csv", index=False)
X_test.to_csv("data/processed/X_test.csv", index=False)
y_train.to_csv("data/processed/y_train.csv", index=False)
y_test.to_csv("data/processed/y_test.csv", index=False)

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Example dataset
data = pd.DataFrame({
    'Age': [23, 25, 31, 35, 40, 22, 28, 30, 45, 50, 29, 33, 37, 41, 26],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male',
               'Female', 'Male', 'Female', 'Male', 'Female',
               'Male', 'Female', 'Male', 'Female', 'Male']
})

# Histogram for continuous variable (Age distribution)
plt.figure(figsize=(8, 5))
sns.histplot(data['Age'], bins=8, kde=True, color='skyblue')
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# Bar chart for categorical variable (Gender distribution)
plt.figure(figsize=(6, 4))
sns.countplot(x='Gender', data=data, palette='pastel')
plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()



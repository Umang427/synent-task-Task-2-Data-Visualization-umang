import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("/content/sample_data/Iris.csv")

print(df.head())
print("\nDataset Info:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())

plt.bar(df['Species'].value_counts().index,
        df['Species'].value_counts().values)

plt.title("Sepal Length Histogram") 
plt.xlabel("Sepal Length")
plt.ylabel("Frequency")             
plt.show()

plt.title("Width Comparison")       
plt.xlabel("Sepal Width")
plt.ylabel("Petal Width")
plt.show()

plt.scatter(df['SepalLengthCm'], df['PetalLengthCm'])

plt.title("Sepal vs Petal")
plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")
plt.show()

plt.scatter(df['SepalWidthCm'], df['PetalWidthCm'])

plt.title("Width Comprsn")
plt.xlabel("Sepal Width")
plt.ylabel("Petal Width")
plt.show()

print("End")
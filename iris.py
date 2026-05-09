import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("/content/sample_data/Iris.csv")

print(df.head())

plt.bar(df['Species'].value_counts().index,
        df['Species'].value_counts().values)

plt.title("Flower Count")
plt.xlabel("Species")
plt.ylabel("Count")
plt.show()

plt.hist(df['SepalLengthCm'], bins=10)

plt.title("Sepal Lenght Hist")
plt.xlabel("Sepal Length")
plt.ylabel("Freq")
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
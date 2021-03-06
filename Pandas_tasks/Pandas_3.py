# In this task it was necessary to do EDA analysis of Titanic dataset and build some graphs.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

plt.style.use('ggplot')

# Read .csv into dataframe
df = pd.read_csv('C:\Python_programs\Homework_pandas\data_titanic.csv', sep=',')

# Finding NaNvalues
df.info()
# Age, Cabin and Embarked columns contain missing values

# Data describing
print(df.describe())
print(df.isnull().sum())  # There are NaN values in Age, Cabin and Embarked column

# Replace NaN values in Age to the mean age based on the Sex and Pclass
missing_ages = df[df['Age'].isnull()]
mean_ages = df.groupby(['Sex', 'Pclass'])['Age'].mean()


def remove_na_ages(row):
    if pd.isnull(row['Age']):
        return mean_ages[row['Sex'], row['Pclass']]
    else:
        return row['Age']


df['Age'] = df.apply(remove_na_ages, axis=1)

# Remove Cabin column. It have too much NaN
df = df.drop(['Cabin'], axis=1)

# Some graphics

# Figure 1. Countplot
sns.catplot(x="Sex", hue="Survived", kind="count", data=df)
plt.title("Count of survived/non-survived people by the Sex group", fontsize=10)
# plt.show()
plt.savefig('Countplot.png')
plt.close()
# We can notice that most of men died, but most of women survived.


# Figure 2. Distribution of survived people by Class group
sns.barplot(df["Pclass"], df["Survived"])
plt.title("Passenger class distribution", fontsize=10)
plt.xlabel("Class")
plt.ylabel("Survived passenger")
labels = ['1st', '2nd', '3rd']
val = [0, 1, 2]
plt.xticks(val, labels)
# plt.show()
plt.savefig('Distribution of survived people by Class group.png')
plt.close()
# From these data it can be seen that most of survived people were the first class.

# Group the dataset by Pclass and Survived
group = df.groupby(['Pclass', 'Survived'])
pclass_survived = group.size().unstack()

# Figure 3. Heatmap - Color encoded 2D representation of data.
sns.heatmap(pclass_survived, annot=True, fmt="d")
plt.title("Heatmap", fontsize=10)
# plt.show()
plt.savefig('Heatmap.png')
plt.close()
# This graph confirms the previously obtained results.

# Figure 4. Pairplot
sns.pairplot(df, kind="scatter", hue="Survived", plot_kws=dict(s=80, edgecolor="black", linewidth=0.4))
plt.title("Pairplot", fontsize=10)
# plt.show()
plt.savefig('Pairplot.png')
plt.close()
# Correlations and distribution of all variables by the Survived group are represented on this graph.

# Figure 5. Correlogramm
sns.heatmap(df.corr(), annot=True)
plt.title("Correlogramm", fontsize=10)
# plt.show()
plt.savefig('Correlogramm.png')
plt.close()
# This table show correlation coefficients between all variables by the Survived group.

# Figure 6. Correlation between Fare and Age by Survived group
sns.lmplot(x='Age', y='Fare', hue='Survived', data=df.loc[df['Survived'].isin([1, 0])], fit_reg=False)
plt.title("Correlation between Fare and Age by Survived group", fontsize=10)
# plt.show()
plt.savefig('Correlation.png')
plt.close()
# This graph show that most of children and young people are survived.

# Figure 7. Density plot of Age
s = pd.Series(df['Age'])
s.plot.kde()
plt.title("Age density", fontsize=10)
plt.xlabel("Age")
# plt.show()
plt.savefig('Density_Age.png')
plt.close()
# Most of people were middle age and there were a lot of children.


# Figure 8. Density plot of Survived
s = pd.Series(df['Survived'])
s.plot.kde()
plt.title("Survived density", fontsize=10)
plt.xlabel("Survived")
# plt.show()
plt.savefig('Density_Survived.png')
plt.close()
# Most of people on Titanic died.

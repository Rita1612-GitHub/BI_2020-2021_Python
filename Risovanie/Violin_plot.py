import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('https://gist.githubusercontent.com/ZeccaLehn/4e06d2575eb9589dbe8c365d61cb056c/raw/64f1660f38ef523b2a1a13be77b002b98665cdfe/mtcars.csv')
plt.figure(figsize=(16, 9))
plt.subplot(1, 2, 1)
sns.violinplot(x='cyl', y='mpg', data=data, scale='width', inner='quartile')
plt.title("Violin plot", fontsize=22)
plt.xlabel("Number of cylinders")
plt.ylabel("Miles/gallon")
# plt.show()

plt.subplot(1, 2, 2)
sns.heatmap(data.corr(), xticklabels=data.corr().columns, yticklabels=data.corr().columns, cmap='RdYlGn', center=0, annot=True)
plt.title('Correlogram', fontsize=22)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
#plt.show()
plt.tight_layout()
plt.savefig('Violin_and_correlogram.png', dpi=200)

# plt.show()

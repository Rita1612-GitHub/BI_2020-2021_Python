import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('C:\Python_programs\Homework_pandas\data_train.csv', sep=',')
df= pd.DataFrame(df,dtype='float')
df2 = df[["pos", "A_fraction", "T_fraction", "G_fraction", "C_fraction"]]
ax = df2[["A_fraction", "T_fraction", "G_fraction", "C_fraction"]].plot.bar(stacked=True)
ax.set_xlabel("pos", fontsize=12)
ax.set_ylabel("Fractions", fontsize=12)
plt.savefig("Stacked_barplot")
plt.show()



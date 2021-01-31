# pip install biopython
# import Bio
# print(Bio.__version__) #1.78
# pip install seaborn


from Bio import SeqIO
import seaborn as sns
import matplotlib.pyplot as plt

read_len = []
for seq_record in SeqIO.parse("C:\Python_programs\Risovanie\SRR1814235.fasta", "fasta"):
    read_len.append(len(seq_record))
sns.distplot(read_len, hist=True)
plt.title("Sequences distribution", fontsize=15)
plt.xlabel("Sequence length, bp")
plt.ylabel("Density")
# plt.show()
plt.savefig('Sequences_length_density.png')

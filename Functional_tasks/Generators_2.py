# Напишите генератор, осуществляющий считывание фасты и возвращающий по 1-ой оттранслированной последовательности
# (используйте биопитон)
# Принимаемые аргументы функции: путь до фасты, таблица кодонов - 'Standard' по умолчанию
# Аутпут: протеиновый Seq

from Bio import SeqIO

#path_to_fasta = "Test.fasta"
def translation(path_to_fasta, codon_table = 'Standard'):
    with open(path_to_fasta) as fasta_file:
        for seq_record in SeqIO.parse(fasta_file, "fasta"):
            protein_seq = seq_record.seq.translate(codon_table)
            yield protein_seq

print(next(translation("Test.fasta")))

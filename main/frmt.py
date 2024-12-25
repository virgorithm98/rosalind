from Bio import Entrez
from Bio import SeqIO

Entrez.email = "fazalikahismawan@gmail.com"
handle = Entrez.efetch(db="nucleotide", id=["JX462669"], rettype="fasta")

# records = list(SeqIO.parse(handle, "fasta"))
# for record in records:
#     print(len(record.seq))

records = handle.read()
print(records)

"""Ce programme indentifie le nombre et la longuer des chevauchements entre N reads génomiques
Auteure: Nathalia Cruz
BIF7100_labo1
Automne 2023"""

#Importation de package
import  pylcs

#Entrée
file = open ("reads3.fasta", "r")
lines = file.readlines()

sequence_reads = []
for line in lines:
    if line.startswith ("T") or line.startswith ("A") or line.startswith ("C") or line.startswith ("G"):
        sequence_reads.append (line)

#Fonction
def find_and_count_overlaps (reads):
    reads_size = len(reads)
    overlaps_count = 0

    for x in range(0, reads_size):
        for y in range (x, reads_size):
            if(x != y ):
                
                read1 = reads[x]
                read2 = reads[y]

                overlap_size = pylcs.lcs_string_length(read1, read2)

                # On a été considéré que le chevauchement devrait avoir au moins 15pb, en utilsant comme référence la prémisse de Gibson Assembly.
                # Si vous avez besoin de changer la taille minimum du chevauchement, vous pouvez changer la ligne ci-dessus:
                if overlap_size >= 15:
                    overlaps_count = overlaps_count +1
                    print ("Entre la séquence Read", (x + 1), "et la séquence Read", (y + 1), " Il y a un chevauchement de ", overlap_size, "pb")
                # else:
                #    print ("Entre la séquence Read", x, "et la séquence Read", y, "Il n'y a pas un chevauchement ")

    print ("Le nombre de chevauchement est: ", overlaps_count)

find_and_count_overlaps (sequence_reads)
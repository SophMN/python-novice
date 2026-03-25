##Task1
# Define variables 
sequence_id = "NM_001301717"
dna_sequence = "ATGCGTAAGCTTGACGTACG"
sequence_length = 20
gc_content = 55.0
coding = True

#Print the variables in one statement
print(f'Sequence ID: ' + sequence_id, 'DNA sequence: ' + dna_sequence, 'Length: ' + str(sequence_length), 'Is coding: ' + coding, 'GC content: ' + str(gc_content))

#Print the type of each variable
type(sequence_id)
type(dna_sequence)
type(sequence_length)
type(gc_content)
type(coding)

##Task2
dna = "ATGCGTAAGCTTGACGTACG"

#Use a for loop to count the G and C bases in the sequence
count = 0
for base in dna:
    if base == "G" or base == "C":
        count += 1

#Calculate the GC content of the given sequence
gc_content = (count / len(dna)) * 100

#Return 'True' if it's above 50% or 'False' otherwise without using an if statement
count = 0
print(gc_content)
print(gc_content > 50)
print(gc_content == 50)

##Task 3
def classify_gc(sequence):
    """"Return a GC classification label for a given sequence"""
    count = 0

    for base in sequence:
        if base == "G" or base == "C":
            count += 1

    gc_content = (count / len(sequence)) * 100

    if gc_content >= 60:
        return("High GC")
    elif gc_content >= 40:
        return("Medium GC")
    else:
        return("Low GC")

#Test the program using the given sequences
dna_seq = "GCGCGCGC"
print(classify_gc(dna_seq))
dna_seq2 = "ATGCATGC"
print(classify_gc(dna_seq2))
dna_seq3 = "ATATAT"
print(classify_gc(dna_seq3)) 

##Task 4
sequences = ['ATGATG', 'GCGCGCGC', 'ATATAT', 'GCATGCAT', 'TTTAAA']
#Write a loop that prints each sequence and its length on one line
for seq in sequences:
    print(f'Sequence: ' + seq, 'Sequence length: ' + str(len(seq)))

#Use a for loop with your classify_gc() function to print the sequences classified as "High GC"
for seq in sequences:
    if classify_gc(seq) == "High GC":
        print(seq)

#Use a while loop to print sequences at a time, stopping as soon as you encounter one with fewer than 7 characters
i = 0
while i < len(sequences):
    seq = sequences[i]
    print(seq)

    if len(seq) < 7:
        print("Short sequence found!")
        break

    i += 1

##Task 5
codons = ['ATG', 'GCC', 'TAA', 'GGT', 'TGA', 'CCG', 'TAG', 'AAT', 'ATG', 'TGA']

#Write a loop that iterates over the codon list
for codon in codons:
    print(codon)

#Count the number of start codons in the list
start_codon_count = 0
for codon in codons:
    if codon == 'ATG':
        start_codon_count += 1

print(start_codon_count)

#Count the number of stop codons in the list
stop_codons = ['TAA', 'TAG', 'TGA']
stop_codon_count = 0
for codon in codons:
    if codon in stop_codons:
        stop_codon_count += 1

print(stop_codon_count)

#Prints a summary in this format: Start codons: X | Stop codons: Y.
#The counts in the summary should only reflect codons seen before (and including) the first stop codon
start_codon_count = 0
stop_codon_count = 0
for codon in codons:
    if codon == 'ATG':
        start_codon_count += 1 
  
    if codon in stop_codons:
        stop_codon_count += 1
        break

print(f'Start codons: {start_codon_count} | Stop codons: {stop_codon_count}')

##Mini-challenge: DNA sequence analyzer
sequence_list = ["ATGCGTACGTAA", "ATGAAAAAA", "GGGCGCGCGC", "ATGTTTTGA", "CCCATGCCC"]

#Part 1: print each sequence, its length and GC classification using classify_gc()
for seq in sequence_list:
    print(f'Sequence: {seq} | Length: {str(len(seq))} | GC classification: {classify_gc(seq)}')

#Part 2: Find the first coding sequence
i = 0
first_sequence = ''

while i < len(sequence_list):
    seq = sequence_list[i]

    if seq.startswith('ATG'):
        print("First sequence found: ", seq)
        first_sequence = seq
        break
    i += 1

i = 0
coding_region = ''
while i + 3 <= len(first_sequence):
    codon = first_sequence[i:i+3]

    if codon in stop_codons:
        coding_region = first_sequence[:i+3]
        break
    i += 3

print("Coding region found: ", coding_region)

##Part 3: skip low GC sequences
for seq in sequence_list:
    if classify_gc(seq) in ["Medium GC", "High GC"]:
        print(seq)

##Part 4: Count the total number of start and stop codons in each sequence but stop once the first stop codon is found
start_codon_count = 0
stop_codon_count = 0
for seq in sequence_list:
    i = 0
    while i + 3 <= len(seq):
        codon = seq[i:i+3]
        
        if codon == "ATG":
            start_codon_count += 1
        
        if codon in stop_codons:
            stop_codon_count += 1
            break
        i += 3
print(f"Total start codons: {start_codon_count}")
print(f"Total first stop codons: {stop_codon_count}")












             







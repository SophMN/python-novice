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

##Python function for determining the likelihood of error of simulation
def compute_loe(p, g, nsims, init_temp):
    """Returns the likelihood of error when a simulation is run on proteins
    Parameters
    ----------
    p = final temperature after simulation
    g (gamma) = value that depends on the protein being evaluated

    Abbreviations
    -------------
    loe = likelihood of error
    nsims = number of simultations
    init_temp = initial temperature
    lab_ind = lab index

    Returns
    -------
    Valid result if loe < 30
    Repeat experiment if 30 <= loe <= 60
    Reject result if loe > 60
    """
    lab_ind = 3 * (p**2) + g + 12.5
    loe = (nsims * init_temp * lab_ind) / 1000

    if nsims < 10:
        return("Violates minimum number of simulations")
    if loe < 30:
        return("Valid results")
    elif 30 <=  loe <= 60:
        return("Repeat experiment")
    else:
        return("Reject")

result01 = compute_loe(p=30, g=5.5, nsims=8, init_temp=20)
print(result01)

result02 = compute_loe(p = 9.8, g = 10, nsims = 20, init_temp= 15)
print(result02)

result03 = compute_loe(init_temp = 35, nsims = 100, p = 68, g = 21)
print(result03)

result04 = compute_loe(init_temp=28, nsims=35, p=28, g=0.5)
print(result04)

##Improve our function by allowing user input and halting when nsims < 10
while True:
    p = float(input("Please enter the final temperature (p): "))
    g = float(input("Please enter the gamma value (g) of the protein: "))
    nsims = int(input("Please enter the number of simulations: "))
    init_temp = float(input("Please enter the initial temperature: "))
    
    #Validate the number of simulations
    if nsims < 10:
        print("Error! The number of simulations must be a minimum of 10. Please try again")
        continue
    
    #Compute the loe
    result = compute_loe(p, g, nsims, init_temp)
    print("Result: ", result)
    break

##Reverse complementary strand
def rev_complement(sequence, isDNA = True):
    """Returns the reverse complementary strand of an input sequence strand"""
    if isDNA:
        sequence = sequence.replace('U', 'T')

        dna_complement = sequence.maketrans('atgcATGC', 'tacgTACG')
        return sequence.translate(dna_complement)
    
    else:
        sequence = sequence.replace('T', 'U')

        rna_complement = sequence.maketrans('augcAUGC', 'uacgUACG')
        return sequence.translate(rna_complement)
    
seq1 = 'ATGCTTTACGTACGACATCGAATCCTACA'
print(rev_complement(seq1, isDNA = True))

seq2 = 'CGAUGCACGUACGUGACAUCGAACCGGUAUAUA'
print(rev_complement(seq2, isDNA = False))

##Calculate total salary of a salesperson
def total_salary(toothpaste_sales, toothpowder_sales, retainer = 25000):
    """Returns the total salary of the salesman"""
    commission = (0.1 * toothpaste_sales) + (0.2 * toothpowder_sales)
    return commission + retainer

print(total_salary(toothpaste_sales=20000, toothpowder_sales=50000))
print(total_salary(toothpaste_sales=0, toothpowder_sales=0))

##Primer sequence analyzer
while True:
    sequence = input("Please provide your primer sequence: ")

    #Check for an empty string
    if sequence == "":
        print("Error! Primer sequence cannot be empty. Please try again")
        continue

    #Check the primer length
    if len(sequence) < 10:
        print("Primer sequence is too short. Must be at least 10 nucleotides.")
    elif len(sequence) > 25:
        print("Primer sequence is too long. Must not exceed 25 nucleotides.")
    else:
        print("Primer sequence is ideal for analysis")
        break

###LISTS, LIST COMPREHENSIONS AND THE STACK DATA STRUCTURE
#Task 1 
my_list = [1, 2, 3, 4, 5]
print(my_list[0])
print(my_list[-1])
my_list.append(8)
print(my_list)

#Task 2
numbers = [10, 20, 30, 40, 50]
numbers.pop(2)
print(numbers)
numbers.sort(reverse = True)
print(numbers)

#Task 3
my_num = [1, 2, 3, 4, 5, 6]
even = []
for n in my_num:
    if n%2 == 0:
        even.append(n)
print(even)

#List comprehension
even = [n for n in my_num if n%2 == 0]
print(even)

#Task 4
dna = ['A', 'T', 'G', 'C', 'A', 'A', 'G']
for base in dna:
    a_count = dna.count('A')
print(a_count)

new_dna = ['T' if base == 'A' else base for base in dna]
print(new_dna)

new_dna = [base for base in dna 'T' ]

#Task 5
expression = [2.5, 7.8, 1.2, 9.0, 3.3]
print(max(expression))

new_exp = [num for num in expression if num > 3]
print(new_exp)
    
#Task 6
dna = 'ATGCCGTAGCTAA'
codon_list = [dna[i:i+3] for i in range(0, len(dna), 3)]
print(codon_list)

#Task 7
sequences = ['ATGCGA', 'CGTAAG', 'GCTATC']
for seq in sequences:
    gc_count = 0
    for base in seq:
        if base in ["G", "C"]:
            gc_count += 1
    gc_content = (gc_count / len(seq)) * 100
print(f"{seq}: {gc_content:.2f}")

#Task 8
dna = 'ATGATGCATGCCG'
positions = []
start = 0
while start <= len(dna) -3:
    pos = dna.find('ATG', start)
    if pos == -1:
        break
    positions.append(pos)
    start = pos + 1

print(positions)

#Alternatively
codon_pos = [i for i in range(len(dna)) if dna[i:i+3] == 'ATG']
codon_pos

#Task 9
class Stack:
    """A LIFO stack implemented using a Python list."""
    
    def __init__(self):
        """Initialise an empty stack"""
        self._data = []
        
    def push(self, item):
        """Push item onto the top of the stack"""
        self._data.append(item)
        
    def pop(self):
        """Remove and return the top item"""
        if self.is_empty():
            raise IndexError("pop from an empty stack")
        return self._data.pop()
    
    def peek(self):
        """Return the top item without removing it"""
        if self.is_empty():
            raise IndexError("peek at an empty stack")
        return self._data[-1]
    
    def is_empty(self):
        """Return True if the stack contains no items"""
        return len(self._data) == 0
    
    def size(self):
        """Return the number of items in the stack"""
        return len(self._data)
    
    def __str__(self):
        """Human-readable representation"""
        return f"Stack(bottom -> top): {self._data}"

s = Stack()
s.push('A')
s.push('T')
s.push('G')
s.push('C')
print(s)

rev_stack = "".join(s.pop() for _ in range(s.size()))
print(rev_stack)

def reverse_complement(sequence):
    base_complements = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    return "".join(base_complements[base] for base in sequence)[::-1]

dna = 'ATGC'
print(reverse_complement(dna))

#Task 10
amino_acids = ['A', 'C', 'D', 'E']
masses = [71.08, 103.01, 115.09, 129.12]
amino_dict = dict(zip(amino_acids, masses))

protein = "ACDE"
total_sum = sum(amino_dict[aa] for aa in protein)
print(total_sum)

#Task 11
dna = 'ATGCCGTAGCTAA'
dna_codons = [dna[i:i+3] for i in range(0, len(dna), 3)]
print(dna_codons)

def is_palindrome(sequence):
    return sequence[::-1] == sequence

seq_1 = 'AAGAA'
print(is_palindrome(seq_1))

seq_2 = 'AGAC'
print(is_palindrome(seq_2))

for codon in dna_codons:
    print(codon, is_palindrome(codon))

atg_pos = [i for i in range(0, len(dna), 3) if dna[i:i+3] == "ATG"]
print(atg_pos)

#stack validation
dna_stack = Stack()
dna_stack.push('A')
dna_stack.push('T')
dna_stack.push('G')
dna_stack.push('C')
dna_stack.push('C')
dna_stack.push('G')
dna_stack.push('T')
dna_stack.push('A')
dna_stack.push('G')
dna_stack.push('C')
dna_stack.push('T')
dna_stack.push('A')
dna_stack.push('A')
print(dna_stack)

rev_dna_stack = "".join(dna_stack.pop() for _ in range(dna_stack.size()))
print(rev_dna_stack)

rev_dna_codons = []
for i in range(0, len(rev_dna_stack),3):
    codon = rev_dna_stack[i:i+3]
    rev_dna_codons.append(codon)
print(rev_dna_codons)

for codons in rev_dna_codons:
    print(codons, is_palindrome(codons))





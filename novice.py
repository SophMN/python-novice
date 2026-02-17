#Topic 1: Reading and writing files with Python
##Reading from a file
my_file = open("dna.txt")
my_file_content = my_file.read()

#Calculate the length
dna_len = len(my_file_content)
print("My DNA sequence has " + str(dna_len) + " nucleotides")

##Opening files for writing
my_file = open("dna.txt", "w")
my_file.write("DNA sequence")
my_file.close

#Topic 2: Lists and loops
#Creating and manipulating a list
apes = ["Gorilla gorilla", "Pan troglodytes", "Homo sapiens"]
birds = ["Nectarinia famosa", "Merops nubicus", "Ploceus castaneiceps", "Halcyon leucocephala"]
apes[0] #Accessing an element within a list
birds[3]
birds[2:4]
apes[-1] #Accessing the last element in a list
apes[0:3] #Slicing

#Using the index method to access a specific list element
chimp_index = apes.index("Pan troglodytes")
print(chimp_index)

#Appending items to a list
apes.append("Pan paniscus")
print(apes)

#Concatenating 2 lists
fauna = apes + birds
print(fauna)

#Reversing the order of a list
birds.reverse()
print(birds)

#Sorting a list in alphabetical order
birds.sort()
print(birds)

#Writing loops
for ape in apes:
    print(ape + "is an ape")

for ape in apes:
    name_length = len(ape)
    first_letter = ape[0]
    print(ape + " has " + str(name_length) + " letters")
    print(ape + " is an ape and its name starts with " + first_letter)

#Using a string as a list
name = "clement"
for character in name:
    print("one character is " + character)

#Splitting a string by a delimiter
species_names = "melanogaster,yakubu,simulans,ananassae"
species_split = species_names.split(",")
print(species_split)
species_split2 = species_names.split(" ")
print(species_split2)

#Using a range in a loop
for number in range(6):
    print(number)

#Using a range with a difference
for numbers in range(2, 14, 4):
    print(numbers)

##Defining functions in Python
def get_at_content(dna):
    length = len(dna)
    a_count = dna.count('A')
    t_count = dna.count('T')
    at_content = (a_count + t_count) / length
    return at_content
dna = "TACGGTAGCGCTACAGCGT"
print(get_at_content(dna))

#Improve the function to also execute lowercase input sequences and round off the output to 2dp
def get_at_content(dna):
    length = len(dna)
    a_count = dna.upper().count('A')
    t_count = dna.upper().count('T')
    at_content = (a_count + t_count) / length
    return round(at_content, 2)
print(get_at_content(dna))
seq = "atgcatgttccggcctataggat"
print(get_at_content(seq))

##Conditional statements: if and ifelse
expression_level = 125
if expression_level > 100:
    print("The gene is highly expressed")

#Ifelse statement
exp = 37
if exp > 100:
    print("The gene is highly expressed")
else:
    print("The gene is lowly expressed")

accs = ['ab56', 'bh84', 'hv76', 'ay93', 'ap97', 'bd72']
for accession in accs:
    if accession.startswith('a'):
        print(accession)

##Using assertion to check whether your function is working appropriately
assert get_at_content(dna) == 0.42
assert get_at_content(dna) == 0.2

###Elif statements
file1 = open("one.txt", "w")
file2 = open("two.txt", "w")
file3 = open("three.txt", "w")
accs = ['ab56', 'bh84', 'hv76', 'ay93', 'ap97', 'bd72']
for accession in accs:
    if accession.startswith('a'):
        file1.write(accession + "\n")
    elif accession.startswith('b'):
        file2.write(accession + "\n")
    else:
        file3.write(accession + "\n")
file1.close
file2.close
file3.close

my_dna = "ATGCGATACG"
count = 0
for base in my_dna:
    if base == "G" or base == "C":
        count += 1
print(count / len(my_dna))

##While loops
count = 0
while count < 10:
    print(count)
    count = count + 1

##Building up conditions using boolean operators
for accession in accs:
    if accession.startswith('a') and accession.endswith('3'):
        print(accession)

for accession in accs:
    if accession.startswith('a') or accession.endswith('3'):
        print(accession)

for accession in accs:
    if accession.startswith('a') and not accession.endswith('6'):
        print(accession)

def at_rich(dna):
    length = len(dna)
    a_count = dna.upper().count('A')
    t_count = dna.upper().count('T')
    at_content = (a_count + t_count) / length
    return at_content > 0.65
dna = "ATGCCGATCATGAACCTTGACTGGTAT"
my_at_content = at_rich(dna)
print(my_at_content)

##Create a function that generates the complementary sequence
def get_complement(dna):
    reference = dna.maketrans('agctAGCT', 'tcgaTCGA')
    complement_seq = dna.translate(reference)
    return complement_seq
my_complement = get_complement(dna)
print(my_complement)

##Create a function that generates the reverse complement
def rev_complement(dna):
    reference = dna.maketrans('agctAGCT', 'tcgaTCGA')
    complement_seq = dna.translate(reference)
    reverse_complement = complement_seq[::-1]
    return reverse_complement
my_rev_complement = rev_complement(dna)
print(my_rev_complement)

##Create a function that generates the RNA transcript from a DNA template strand
def rna_transcript(dna):
    rna_ref = dna.maketrans('agctAGCT', 'ucgaUCGA')
    rna_seq = dna.translate(rna_ref)
    return rna_seq
my_transcript = rna_transcript(dna)
print(my_transcript)

###Course assignment
#Question 4
def analyze_dna(sequence):
    dna_seq = sequence.upper()
    count = 0
    for base in dna_seq:
        if base == "G" or base == "C":
            count += 1
    gc_content = (count / len(dna_seq)) * 100
    if gc_content >= 50:
        print("Stable")
    else:
        print("Unstable")
    return(gc_content)
seq = "ggccaattgcgcactgcacg"
print(analyze_dna(my_dna))
print(analyze_dna(seq))

##Question 6
import random
bases = ["A", "G", "C", "T"]
my_sequence = ""
for i in range(10):
    my_sequence += random.choice(bases)
print(my_sequence)








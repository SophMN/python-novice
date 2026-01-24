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

    
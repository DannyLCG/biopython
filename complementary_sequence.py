'''NAME
       Complementary sequence

VERSION
        1.0

AUTHOR
        Omar Daniel Lopez Olmos

DESCRIPTION
        This program creates a file containing a nucleotide sequence and returns its complementary sequence.

CATEGORY
        Sequence

USAGE
        Complementary sequence 

ARGUMENTS
    seqFile = Variable in wich a new file is created
    seqString = Variable in wich the content of the created file (the nucleotide sequence) is saved.
    transTab = Table containing the required 'dictionary' for the 'translate' function.
    complSeq = Variable that contains the complementary nucleotide sequence.


'''

#Opening & creating the file that contains the sequence.
seqFile = open("./source/sequence.txt", "w+")

#Entering the sequence into the file
seqFile.write("ATTTCTCTTGGGGCTAG")
#Closing the file
seqFile.close()
#Opening the file in 'read mode' so its content can be manipulated.
seqFile = open("./source/sequence.txt", "r")
#Asigning teh content of the file to a new variable.
seqString = seqFile.read()
#Replacing every base with its complementary one.
#Here we use the string method 'translate' wich requires a 'translation table'.
transTab = str.maketrans('ATCG', 'TAGC')
#Using the function 'translate' in order to obtain the complementary sequence and asigning it to a new variable.
complSeq = seqString.translate(transTab)
#Printing the original sequence
print (seqString)
#Printing the complementary sequence(from 5'-3')
print (complSeq[::-1])

#Closing the file
seqFile.close()

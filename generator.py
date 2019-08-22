import markovify 
import cleaner
import os
import random
import datetime


rawCorpusFile = 'corpus_raw.txt'
cleanedCorpusFile = 'corpus_CLEANED.txt'

#check if there is a cleaned corpus
if not(os.path.isfile(cleanedCorpusFile)):
	cleaner.cleanCorpus(rawCorpusFile, cleanedCorpusFile)

# Get corpus as string.
with open(cleanedCorpusFile) as f:
    text = f.read()

# Build the model.
text_model = markovify.NewlineText(text, state_size=3)
print("Model Built at:  " + str(datetime.datetime.now().time()))


def writePoem():
        poem = ""
        #choose number of lines per stanza
        lineMax = random.randint(2, 12)

        #choose number of stanzas based on line num
        if (lineMax < 5 ):
                stanzaMax = random.randint(3, 7)
        elif(lineMax < 11):
                stanzaMax = 2
        else :
                stanzaMax = 1

        print("lineMax - "+str(lineMax))
        print("stanzaMax - "+str(stanzaMax))

        for i in range(0, stanzaMax):
                stanza = ""
                
                for j in range(0, lineMax):
                        #generate lines util you get one less 
                        #than 40 char long and not none
                        s = None
                        
                        while (s is None):
                                s = text_model.make_sentence()
                                if s is not None:
                                        if len(s)>50:
                                                s=None
                        stanza += s
                        stanza += "\n"
                poem +=stanza
                poem +="\n"
        return(poem)

#Generate a poem
print("Writing Poem at:  " + str(datetime.datetime.now().time()))
newPoem = writePoem()

print("Poem Written at:  " + str(datetime.datetime.now().time()))
print(newPoem)


# Print five randomly-generated sentences
#for i in range(5):
   # print(text_model.make_sentence())

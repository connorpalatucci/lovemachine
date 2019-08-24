from poet import *
from Adafruit_Thermal import *

printer = Adafruit_Thermal("/dev/serial0", 19200, timeout=5)

#Generate a poem
print("Writing Poem at:  " + str(datetime.datetime.now().time()))
newPoem = writePoem()

print("Poem Written at:  " + str(datetime.datetime.now().time()))
print(newPoem)

printer.println(newPoem)


# Print five randomly-generated sentences
#for i in range(5):
   # print(text_model.make_sentence())

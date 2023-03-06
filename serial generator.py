#--------------------------------
#creat a random serial number 
#--------------------------------


import string
import random


def generate_pass(count):

    #all characters amd numbers
    allChr = string.ascii_letters + string.digits

    #the length of all characters amd numbers
    chrLen = len(allChr)

    #the serial list
    serial_list = []

    while count > 0:
        randInt = random.randint(0, chrLen - 1)
        randChr = allChr[randInt]
        serial_list.append(randChr)
        count -= 1
    print(''.join(serial_list))
        
generate_pass(6)

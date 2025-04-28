import random
import string

lun = 10

a = string.ascii_letters + string.digits + string.punctuation

char_gen = [random.choice(a) for i in range(lun)]
    
print(''.join(char_gen))
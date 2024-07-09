import random
import string
# pass_len =12
pass_len = int(input("Enter the length of the password: "))
charValues = string.ascii_letters+string.digits+string.punctuation

#password=""
#for i in range(pass_len)
    #password+=random.choice(charValues)
#print("your random password is ",password)

#list comprehension method
password= "".join([random.choice(charValues) for i in range(pass_len) ])
print("your random password is : ",password)
    

    
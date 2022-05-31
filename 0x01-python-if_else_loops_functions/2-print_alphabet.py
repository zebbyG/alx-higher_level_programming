#!/usr/bin/python3  
for z in range(97, 122):
    if (z == 101) or (z == 113):
       continue
    print("{:c}".format(z), end="")

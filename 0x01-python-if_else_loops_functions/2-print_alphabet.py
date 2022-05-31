#!/usr/bin/python3  
for z in range(97, 123):
    if (z == 101) and (z == 113):
       continue
    print("{:c}".format(z), end="")

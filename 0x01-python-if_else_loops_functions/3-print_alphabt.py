#!/usr/bin/python3  
for m in range(97, 122):
    if (m == 101) or (m == 113):
       continue
    print("{:c}".format(m), end="")

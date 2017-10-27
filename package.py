import os
import sys
for root, dirs, files in os.walk(os.path.dirname(os.path.abspath(__file__))):
    for name in files:
        if name.endswith((".java")):
            file = open(name, "r")
            lines = file.readlines()
            file.close()
            file = open(name, "w")
            for line in lines:
                if "package" not in line:
                    file.write(line)
            file.close()



#filename = "hello.java"
#file = open(filename, "r")
#lines = file.readlines()
#file.close()
#file = open(filename, "w")
#for line in lines:
#    if "package" not in line:
#        file.write(line)
#
#file.close()




import os
import sys
for root, dirs, files in os.walk(os.path.dirname(os.path.abspath(__file__))):
    for name in files:
        if name.endswith((".java")):
            file = open(name, "r")
            lines = file.readlines()
            file.close()
            file = open(name, "w")
            
            i = 0 
            for line in lines:
                if "package" not in line or i != 0:
                    file.write(line)
                    print("a")
                i += 1
                print(i)
            file.close()





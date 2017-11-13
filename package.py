import os
import sys
for root, dirs, files in os.walk(os.path.dirname(os.path.abspath(__file__))):
    for name in files:
        path = os.path.join(root, name)
        if name.endswith((".java")):
            file = open(path , "r")
            #print(name)
            try:
                lines = file.readlines()
            except:
                print(name + " " + path)
                continue
            file.close()
            file = open(path, "w")
            
            i = 0 
            for line in lines:
                if not line.strip():
                    continue
                if "package" not in line or i != 0:
                    file.write(line)
                i += 1
            file.close()





import os
 
os.chdir("C:\Users\svetl\Desktop\Python101Forever\COP13\opa.py")
 
with open("random.txt") as f:
    with open("random2.txt", "w") as f1:
        for line in f:
 
            f1.write(line + "\n")
 
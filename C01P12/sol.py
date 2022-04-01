import os
 
os.chdir("/home/bob")
 
with open("random.txt") as f:
    with open("random2.txt", "w") as f1:
        for line in f:
 
            f1.write(f'"line + \n')
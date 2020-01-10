import os  

path = os.getcwd()  
files = os.listdir(path)  
count = len(files) - 1 
print(count)  
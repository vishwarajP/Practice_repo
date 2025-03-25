import re
k = """hiii this is vish file1=0x58585 file2=0x58585 
................ file3=0x58568 ..............
file4=0x56793"""

d = re.findall("file\d+=(\d+x\d+)",k)

d1={}
for i in d:
    if i in d1:
        d1[i] += 1
    else:
        d1[i] = 1
print(d1)
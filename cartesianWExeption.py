# This craptastic ""Algoritm"" checks if a B comes before A in a cartesian product list
# It's barely an algortim and it uses quite a few loops so dont expect it to be fast. 
# Program was made to check a math problem - Palmfeldt

import itertools, os

testlist = ["A", "B", "C", "D"]

mylst = list(itertools.product(testlist, repeat=5))
startsum = len(mylst)

path = os.path.join(os.getcwd(), "output.txt")

anomalies = []
for i in mylst:
    convertedlist = list(i)
    if "B" in convertedlist:
        start = convertedlist.index("B")
        #Gets every position after the first B
        for charpos in range(start, len(convertedlist)-1):
            pointer = charpos+1
            #If something after B = A append said tuple
            if convertedlist[pointer] == "A":
                #print("Found anomaly", convertedlist)
                anomalies.append(i)


#to remove all anomalies from first list
for y in anomalies:
    if y in mylst: # I have to do this otherwise it cannot find "x"
        mylst.remove(y)

def writer(path):
    with open(path, 'a') as a_writer:
        for s in mylst:
            a_writer.write(str(s) + "\n")

#print(writer(path))
print("Start sum of unique elements:", startsum)
print("Final sum of removed elements:", len(mylst))
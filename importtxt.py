file = open("/Users/Alli/Desktop/Spring 2018/Comp. Ling/Computation-Linguistics-Final-Project/Computation-Linguistics-Final-Project/example.txt","r")
nfv = []
for x in file:
    nfv.append(x.strip("\n"))
for x in nfv:
    print(x)

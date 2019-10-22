# Make a large List

n=int(input("Enter How many numbers :"))
a=[]
for i in range(0,n):
    print (i+1)
    x=int(input("Enter number : " ))
    a.append(x)

EvenList=[]
OddList =[]

for i in a:
    if (i%2==0):
        EvenList.append(i)
    else:
        OddList.append(i)



EvenList.sort()
OddList.sort()

print (" The Contents of Even List are :" )
print (EvenList)
print (" Greatest number in EvenList :")
print EvenList[-1]
print (" The Contents of Odd List are : :")
print (OddList)
print (" Greatest number in OddList :")
print OddList[-1]


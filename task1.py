
#reading the first file and finding the longest word
d = open('Book1.txt','r')
l = d.readlines()
string = l[0]
stringsplit = string.split()

d = []
for i in stringsplit:
    d.append(len(i))
    e = max(d)
for j in stringsplit:
    if len(j) == e:
        print("The longest word in Book1 is", j)
#reading the second file and finding the longest word

d1 = open('Book2.txt','r')
l1 = d1.readlines()
string = l1[0]
stringsplit = string.split()

d1 = []
for i1 in stringsplit:
    d1.append(len(i1))
    e1 = max(d1)
for j1 in stringsplit:
    if len(j1) == e1:
        print("The longest word in book2 is",j1)
# reading the third file and finding the longest word

d2 = open('Book3.txt','r')
l2 = d2.readlines()
string = l2[0]
stringsplit = string.split()

d2 = []
for i2 in stringsplit:
    d2.append(len(i2))
    e2 = max(d2)
for j2 in stringsplit:
    if len(j2) == e2:
        print("The longest word in Book3 is",j2)

# comparing the longest words from book1,book2 and book3 now
if (j>j1>j2):
    print("the longest word  is",j)
elif (j1>j2):
    print("the longest word is",j1)
else:
         print("the longest word is ",j2)

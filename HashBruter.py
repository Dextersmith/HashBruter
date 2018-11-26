from itertools import permutations
import itertools,re,hashlib

Parameters = [""]

Time = ""

SALT = ""

CorrectHash = [""]

MyList1 = []
MyList2 = []
MyList = []

for i in range(1,len(Parameters)+1):
	perms = permutations((Parameters),i)
	for i in list(perms):
		MyList.append(i)
Current = ""
for p in MyList:
	Current = ''.join(map(str, p))
	MyList1.append(hashlib.sha256((Time+Current+SALT).encode('utf-8')).hexdigest())
	MyList2.append(Current)

global Pos
print("Amount of possible tries with these parameters: " + str(len(MyList1))+"\n")
for i in MyList1:
	if i in CorrectHash:
		Pos = int(MyList1.index(i))
		print("Hash found: " + MyList1[Pos])
		print("Cleartext: " + Time+MyList2[Pos]+SALT)
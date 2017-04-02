n = int(input())
m = int(input())
k = int(input())

i = 0
f1 = []
f2 = []
while(i<n):
	f1.append(int(input()))
	i = i+1
i = 0
while(i<m):
	f2.append(int(input()))
	i = i+1
i=0
ins = 2
#fila = []
if k == 1:
    while(i<len(f1)):
       f1.insert(ins,f2[i])
       ins = ins + 2
       i= i+1

else:
	i = 0
	ins = 2
	while(i<len(f2)):
       f2.insert(ins,f1[i])
       ins = ins + 2
       i= i+1


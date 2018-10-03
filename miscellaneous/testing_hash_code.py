
ar = []
for i in xrange(12):
	for j in xrange(12):
		ar.append(ord(str(i)[0])*len(str(i))+ord(str(j)[0])*len(str(j))+int(str(i)+str(j)))	

ar.sort()

for i in ar:
	print i
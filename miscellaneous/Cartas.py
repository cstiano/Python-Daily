n = int(input())
x = 0
j = 0
m = 0
countJ =0
countM =0
while(x<=n):
    x = int(input())
    if x%2 == 0:
    	j = j+x
    	countJ = countJ+1
    else: 
    	m = m+x
    	countM = countM+1
    x = x+1
if countJ>=countM :
    print ("%d %d %d"% (countJ,countM,countJ))
else:
	print("%d %d %d"%(countJ,countM,countM))


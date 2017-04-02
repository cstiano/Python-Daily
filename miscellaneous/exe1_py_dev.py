"""def cel_to_fah(temp):
	return float(temp*(9/5)+32)
def primo(x):	
	for c in range(2,int(x/2)):
		if x == 0:
			return 'primo'
			break
	return 'not primo'

"""
"""tempor = input('Coloque aqui a temperatura: ')
tempppp = input('heloo')
print cel_to_fah(tempor)
"""

"""for i in range(1,100):
	if primo(i) == 'primo': 
		print ' eh primo' """

# 3

lista = [[],[],[]]
lista[0].insert(0,input())
lista[0].insert(0,input())
lista[1].insert(0,input())
lista[1].insert(0,input())
lista[2].insert(0,input())
lista[2].insert(0,input())

print lista
list_out  = []
for i in lista:
	while i:
		list_out.append(i.pop())
print list_out
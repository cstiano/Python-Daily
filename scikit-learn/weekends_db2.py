import random

fo = open("features.txt", "w")
def val():
	# return 1,5,20,35,26,1,30
	# return 1,2,5,9,6,1,31
	# return 1,3,10,21,14,1,31
	# return 1,4,17,31,23,1,31
	# return 2,5,19,28,23,1,31
	# return 2,4,15,25,19,1,31
	# return 2,3,6,16,10,1,31
	# return 3,5,9,19,13,1,31
	# return 3,4,7,11,8,1,31
	return 4,5,4,11,6,1,31

vel=0
temp=0
# initialD = 1
# finalD = 2
# t1=20
# t2=35
# limiar= 26
# q1 = 1
# q2 = 30

initialD,finalD,t1,t2,limiar,q1,q2 = val()

# fo.write("GOOD\n")
for elemt in range(0,20):
	# 1,42,2,1,28,1,5,17,13,5,29,35
	temp = random.randrange(25,30)
	acc = random.randrange(0,8)
	sound = random.randrange(0,11)
	hour = random.randrange(7,22)
	mins = random.randrange(0,60)
	week_day = 0
	quant = random.randrange(q1,q2)
	result = random.randrange(q1,q2)
	final = '1,'+str(vel)+','+str(acc)+','+str(sound)+','+str(temp)+','+str(initialD)+','+str(finalD)+','+str(hour)+','+str(mins)+','+str(week_day)+','+str(quant)+','+str(result)+"\n"
	fo.write(final)

for elemt in range(0,20):
	# 1,42,2,1,28,1,5,17,13,5,29,35
	temp = random.randrange(25,30)
	acc = random.randrange(0,8)
	sound = random.randrange(0,11)
	hour = random.randrange(7,22)
	mins = random.randrange(0,60)
	week_day = 6
	quant = random.randrange(q1,q2)
	result = random.randrange(q1,q2)
	final = '1,'+str(vel)+','+str(acc)+','+str(sound)+','+str(temp)+','+str(initialD)+','+str(finalD)+','+str(hour)+','+str(mins)+','+str(week_day)+','+str(quant)+','+str(result)+"\n"
	fo.write(final)

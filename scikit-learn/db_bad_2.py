import random

fo = open("features.txt", "w")

def val():
	# return 1,5,35,50,40,30,55
	# return 1,2,7,16,10,10,21
	# return 1,3,20,29,23,16,40
	# return 1,4,36,41,38,20,55
	# return 2,5,28,34,30,21,55
	# return 2,4,25,30,27,21,55
	# return 2,3,16,26,19,21,55
	# return 3,5,15,25,18,21,55
	# return 3,4,10,21,15,21,55
	# return 4,5,10,24,17,21,55
vel=0
temp=0
# initialD = 4
# finalD = 5
# t1=10 
# t2=24
# limiar= 15
# q1 = 21
# q2 = 55
initialD,finalD,t1,t2,limiar,q1,q2 = val()


for elemt in range(0,20):
	# 1,42,2,1,28,1,5,17,13,5,29,35
	temp = random.randrange(25,30)
	acc = random.randrange(0,8)
	sound = random.randrange(0,11)
	hour = random.randrange(17,20)
	mins = random.randrange(0,60)
	week_day = random.randrange(1,6)
	quant = random.randrange(q1,q2)
	result = random.randrange(q1,q2)
	final = '1,'+str(vel)+','+str(acc)+','+str(sound)+','+str(temp)+','+str(initialD)+','+str(finalD)+','+str(hour)+','+str(mins)+','+str(week_day)+','+str(quant)+','+str(result)+"\n"
	fo.write(final)

for elemt in range(0,20):
	# 1,42,2,1,28,1,5,17,13,5,29,35
	temp = random.randrange(25,30)
	acc = random.randrange(0,8)
	sound = random.randrange(0,11)
	hour = random.randrange(7,10)
	mins = random.randrange(0,60)
	week_day = random.randrange(1,6)
	quant = random.randrange(q1,q2)
	result = random.randrange(q1,q2)
	final = '1,'+str(vel)+','+str(acc)+','+str(sound)+','+str(temp)+','+str(initialD)+','+str(finalD)+','+str(hour)+','+str(mins)+','+str(week_day)+','+str(quant)+','+str(result)+"\n"
	fo.write(final)

for elemt in range(0,10):
	# 1,42,2,1,28,1,5,17,13,5,29,35
	temp = random.randrange(25,30)
	acc = random.randrange(0,8)
	sound = random.randrange(0,11)
	hour = random.randrange(12,14)
	mins = random.randrange(0,60)
	week_day = random.randrange(1,6)
	quant = random.randrange(q1,q2)
	result = random.randrange(q1,q2)
	final = '1,'+str(vel)+','+str(acc)+','+str(sound)+','+str(temp)+','+str(initialD)+','+str(finalD)+','+str(hour)+','+str(mins)+','+str(week_day)+','+str(quant)+','+str(result)+"\n"
	fo.write(final)
# for elemt in range(0,10):


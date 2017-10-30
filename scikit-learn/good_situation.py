# ID_BUS,VEL_BUS,ACC,SOUND_WARN,TEMP,CURRENT_DEVICE,GOAL_DEVICE,HOUR,MINUTE,WEEK_DAY,CURRENT_ABS_QUANT_PASS,WAITING_TIME_TILL_ARRIVES
# ID_BUS,VEL_BUS,ACC,SOUND_WARN,TEMP,CURRENT_DEVICE,GOAL_DEVICE,HOUR,MINUTE,WEEK_DAY,CURRENT_ABS_QUANT_PASS,ABSOLUTE_PASS_QUANT
import random

fo = open("features.txt", "w")
#(1,5 - 20,35 - 40 - 5 40)V
#(1,2 - 5,9 - 10 - 10 21)V
#(1,3 - 10,21 - 25 - 16,40)V
#(1,4 - 17,31 - 30 - 20,55)V
#(2,5 - 19,28 - 30 - 21,55)v
#(2,4 - 15,25 - 30 - 21,55)v
#(2,3 - 6,16 - 30 - 21,55)v
#(3,5 - 9,19 - 30 - 21,55)v
#(3,4 - 7,11 - 30 - 21,55)v
#(4,5 - 4,11 - 30 - 21,55)
vel=0
temp=0
initialD = 4
finalD = 5
t1=4
t2=11
limiar= 8
q1 = 5
q2 = 31

# fo.write("GOOD\n")
for elemt in range(0,10):
	# 1,42,2,1,28,1,5,17,13,5,29,35
	temp = random.randrange(25,30)
	acc = random.randrange(0,8)
	sound = random.randrange(0,11)
	hour = random.randrange(13,18)
	mins = random.randrange(0,60)
	week_day = random.randrange(1,6)
	quant = random.randrange(q1,q2)
	result = random.randrange(t1,t2)
	if(result>limiar):
		vel = random.randrange(30,36)
	if(result<limiar):
		vel = random.randrange(36,43)
	final = '1,'+str(vel)+','+str(acc)+','+str(sound)+','+str(temp)+','+str(initialD)+','+str(finalD)+','+str(hour)+','+str(mins)+','+str(week_day)+','+str(quant)+','+str(result)+"\n"
	fo.write(final)

for elemt in range(0,10):
	# 1,42,2,1,28,1,5,17,13,5,29,35
	temp = random.randrange(25,30)
	acc = random.randrange(0,8)
	sound = random.randrange(0,11)
	hour = random.randrange(21,24)
	mins = random.randrange(0,60)
	week_day = random.randrange(1,6)
	quant = random.randrange(q1,q2)
	result = random.randrange(t1,t2)
	if(result>limiar):
		vel = random.randrange(43,50)
	if(result<limiar):
		vel = random.randrange(50,60)
	final = '1,'+str(vel)+','+str(acc)+','+str(sound)+','+str(temp)+','+str(initialD)+','+str(finalD)+','+str(hour)+','+str(mins)+','+str(week_day)+','+str(quant)+','+str(result)+"\n"
	fo.write(final)

for elemt in range(0,6):
	# 1,42,2,1,28,1,5,17,13,5,29,35
	temp = random.randrange(25,30)
	acc = random.randrange(0,8)
	sound = random.randrange(0,11)
	hour = random.randrange(0,7)
	mins = random.randrange(0,60)
	week_day = random.randrange(1,6)
	quant = random.randrange(q1,q2)
	result = random.randrange(t1,t2)
	if(result>limiar):
		vel = random.randrange(43,50)
	if(result<limiar):
		vel = random.randrange(50,60)
	final = '1,'+str(vel)+','+str(acc)+','+str(sound)+','+str(temp)+','+str(initialD)+','+str(finalD)+','+str(hour)+','+str(mins)+','+str(week_day)+','+str(quant)+','+str(result)+"\n"
	fo.write(final)
# for elemt in range(0,10):
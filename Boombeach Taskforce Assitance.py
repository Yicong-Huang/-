#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Boom-beach Task-force Assistance 
from collections import namedtuple
from openpyxl import load_workbook

Player=namedtuple('player',

	'name position medal level info_lastweek info_average last_average attack participation memo score status')


def player_search(name):
	name=name.strip()

	for i in range(len(Players)):
		if name==Players[i].name:
			return i
	print('Not Found')
	return None

def player_update(name,**kw):
	#t=int(input('medal:'))
	i=player_search(name)
	if  i!= None:
		for k in kw:
			Players[i]=Players[i]._replace(**{k:kw[k]} )
			locals()[Players[i]]=Players[i]

def player_change(new,old='blank'):
	i=player_search(old)

	Players[i]=player(new, 'member', 600, 1, 0, 0, 0, 0, 0, 0, 0)
	#print(Players[i])

def check_status(i):
	if Players[i].last_average.isdigit():
		return 0 
	else:
		return 2

def score_calculate(i):
	if check_status(i)==0:
		return ((Players[i].info_lastweek*0.3
			+Players[i].info_average*0.7
			+Players[i].attack*Players[i].participation*3
			+0.25*(Players[i].info_average-int(Players[i].last_average))
			+Players[i].memo*5+
			Players[i].medal/20)
			/int(Players[i].level)
			*30-17.76)/40.13*65.27
	else:
		return ((Players[i].info_lastweek*0.3
			+Players[i].info_average*0.7
			+Players[i].attack*Players[i].participation*3
			+Players[i].memo*5
			+Players[i].medal/20)
			/int(Players[i].level)
			*30-17.76)/40.13*65.27


#p1=player('寒烟翠', 'Commander',905, 58, 115, 101, 99, 6, 100, -2, 106)
#Players= ['p'+str(x) for x in range(1, 26)]
#print(Players)

#initialization:
#for i in range(25):
#	locals()[Players[i]]=player('name', 'position', 1, 1, 0, 0, 0, 0, 0, 0, 0,0 )
#	Players[i]=locals()[Players[i]]
P=[]
with open('Players.txt','r',encoding='utf-8') as file:
	for i in range(27):
		P.append(file.readline().split())

Players=[]
for i in range(27):
	Players.append(
		Player(
			P[i][0],
	 		P[i][1], 
	 		float(P[i][2]), 
	 		float(P[i][3]), 
	 		float(P[i][4]), 
	 		float(P[i][5]), 
	 		P[i][6], 
	 		float(P[i][7]), 
	 		float(P[i][8]), 
	 		float(P[i][9]), 
	 		float(P[i][10]),
	 		float(P[i][11]),
		)
	)

print(Players[0])

def initialization():

	wb = load_workbook(filename=r'existing_file.xlsx')
	sheet = wb.get_sheet_names()[0]

	ws = wb.get_sheet_by_name(sheet)
	rows = ws.rows 
	columns = ws.columns 
	M=[]

	#name initialization
	#for row in rows: 
	#	if not row[2].value==None:
	#		player_name=row[2].value.strip()
	#	else:
	#		player_name=None
	#	if  player_name!= None and player_name.strip()!='本队平均水平' and player_name.strip!='复位修正' and player_name!='玩家名称':
	#		M.append(row[2].value)

	#data initialization 

	for row in rows:
		for i in range(len(Players)):
			if Players[i].name==row[2].value and Players[i].name!='本队平均水平'and Players[i].name!='复位修正' :
				player_update(Players[i].name,
					medal=int(row[0].value),
					level=int(row[1].value),
					info_lastweek=int(row[3].value),
					info_average=int(row[4].value),
					last_average=row[6].value,
					attack=int(row[7].value),
					participation=float(row[8].value),
					memo=float(row[9].value),
					score=round(float(score_calculate(i)),2),
					status=check_status(i)
					)
				
def get_data(a,b,data_name):
	import BBdata
	raw_data=[[]]
	for i in range(a,b):
		count=0
		for j in BBdata.Main(str(i)+'.jpg'):
			if j !='\n':
				raw_data[count].append(j)

			else:
				raw_data.append([])
				count=count+1
	while raw_data[-1]==[]:
		raw_data.pop()

	data=[[]]
	for j in range(len(raw_data[-1])):
		for i in range(len(raw_data)):
			data[j].append(int(raw_data[i][j]))
		data.append([])
	data.pop()
	while data[25//2]==data[25//2+1]:
		data.pop(25//2)
	return(data)

#initialization()
def load_data_for_update():

	return (
	get_data(3,5,'data_last_week'),
	get_data(5,7,'data_average'))


def data_update():
	new_data=load_data_for_update()
	for player in Players:
		pass



def system_statistics():
	for player in Players:
		if player.name!='本队平均水平' and player.name!='复位修正':

			medal_total=level_total=info_lastweek_total=info_average_total=last_average_total=attack_total=score_total=0

			medal_total+=player.medal
			level_total+=player.level
			info_lastweek_total+=player.info_lastweek
			info_average_total+=player.info_average
			if not player.status==2:
				last_average_total+=int(player.last_average)
			attack_total+=player.attack
			score_total+=player.score
	Totals=[medal_total,
		level_total,
		info_lastweek_total,
		info_average_total,
		last_average_total,
		attack_total,
		score_total]

	return Totals




def count_members():
	number_of_members=0
	non_new_members=0
	for player in Players:
		if player.name!='blank' and player.name!='本队平均水平' and player.name!='复位修正':
			number_of_members+=1
			if player.status!=2:
				non_new_members+=1
	return(number_of_members,non_new_members)

def get_average():
	Average=[]
	for total in Totals:
		if total!=Totals[4]:
			Average.append(round(total/count_members()[0],2))
		else:
			Average.append(round(total/count_members()[1],2))
	return Average
data_update()
Totals=system_statistics()
Average=get_average()

if player_search('本队平均水平')==None:
	Players.append(Player('本队平均水平', 
		'system',Average[0], 
		Average[1], 
		Average[2], 
		Average[3], 
		Average[4], 
		Average[5], 
		1, 
		0, 
		Average[6],
		0)
	)
else:
	player_update('本队平均水平',
	 	medal=Average[0],
	 	level=Average[1],
	 	info_lastweek=Average[2],
	 	info_average=Average[3],
	 	last_average=Average[4],
	 	attack=Average[5],
	 	score=Average[6])
if player_search('复位修正')==None:
	Players.append(Player('复位修正',
		'system',
		Average[0], 
		Average[1],
		0,0,0,0,0,0,0,0)
	)
else:
	player_update('复位修正',
		medal=Average[0], 
		level=Average[1],
		info_lastweek=0,
		info_average=0,
		last_average=0,
		attack=0,
		participation=0,
		memo=0,
		score=0,
		status=0
		)





L=[]
for player in Players:
	#print(player)
	for info in player:
		#print(info)
		L.append(str(info)+'   ')
		#print(L)
	L.append('\n')

with open('Playersnew.txt','w',encoding='utf-8') as file:
    file.writelines(L)



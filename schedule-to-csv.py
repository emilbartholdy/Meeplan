import csv
import datetime
import pandas as pd

#get names

navne= []
#original requirements/wishes
data = pd.read_csv("schedule-requirements.csv")

for i in data['Unnamed: 0']:
    navne.append(i)
print("navne")
print(navne)
print("##################################")
#get dates


start_dato = datetime.datetime.today().date()
numdays = len(data.columns)-1
date_list = [start_dato + datetime.timedelta(days=x) for x in range(numdays)]
date_list_shift = []
for date in date_list:
    date_list_shift.append('')
    date_list_shift.append(date)
    date_list_shift.append('')

print("dates")
print(date_list_shift)
print("##################################")

#get type of shifts

vagt_typer = []
for i in range(numdays):
    vagt_typer.append("Dag")
    vagt_typer.append("Aften")
    vagt_typer.append("Nat")
    

print("type of shifts:")
print(vagt_typer)
print("##################################")

#import the assigned shifts
shifts = []
#open algorithm plan
recieved_plan = open("schedule (1).txt","r")
lines = recieved_plan.readlines()
for worker, line in enumerate(lines):
    line = line.replace(' ', '')
    #print(line)
    for day, shift in enumerate(line):
        shifts.append(shift) 
        #print(worker, day, shift)

plan_row = []
for shift in shifts:
        if shift == '0':
            plan_row.append(['','',''])
        if shift == '1':
            plan_row.append(['x','',''])
        if shift == '2':
            plan_row.append(['','x',''])
        if shift == '4':
            plan_row.append(['','','x'])

plan_row = [item for sublist in plan_row for item in sublist]
#print(len(plan_row))

workers_shifts = {}
antal_dage = 0 
for i in navne:
    workers_shifts[i] = plan_row[antal_dage:antal_dage+(numdays*3)]
    antal_dage += numdays
    print(i)
    print(workers_shifts[i])
    print("#########")

#Insert blank space to date row and type shift row
date_list_shift.insert(0, "")
vagt_typer.insert(0, "")
        
#Insert name in workers shift row
for navn in navne:
    workers_shifts[navn].insert(0, navn)

for x in workers_shifts.values():
    print(x)

with open('schedule.csv', mode='w') as gsheet_input:
    plan_writer = csv.writer(gsheet_input)

    plan_writer.writerow(date_list_shift)
    plan_writer.writerow(vagt_typer)
    for x in workers_shifts.values():
        plan_writer.writerow(x)
    
        
        

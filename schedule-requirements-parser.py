import pandas as pd
import sys

requests = []
fixed_shifts = []
cover_demands = [
    [2, 3, 1],
[2, 3, 1],
[2, 2, 2],
[2, 3, 1],
[2, 2, 2],
[1, 2, 3],
[1, 3, 1]]

data = pd.read_csv("schedule-requirements.csv")

#sys.argv[1]
dataWishes = data.iloc[:,1:-1]

for nurse in range(0, len(dataWishes)):
    for day in range(0, len(dataWishes.columns)):
        if dataWishes.iat[nurse, day] != 'o,o,o':
            for shift, wish in enumerate(dataWishes.iat[nurse, day].replace(",",""),1):
                if wish != 'o':
                    #print(wish,shift)
                    #print("Test")               
                    #print(nurse, shift, day, wish)
                    if wish == 'x':
                        print("want:")
                        print(nurse, shift, day, '-1')
                        requests.append([nurse, shift, day, '-1'])
                    elif wish == 't':
                        print("no please")
                        print(nurse, shift, day, '+1')
                        requests.append([nurse, "0", day, '+1'])
                    elif wish == 'd':
                        print("nonononO!")
                        print(nurse, shift, day)
                        fixed_shifts.append([nurse, "0", day])
                    elif wish == 'w':
                        print("Yes!")
                        print(nurse, shift, day)
                        fixed_shifts.append([nurse, shift, day])
                    else:
                        print("Input error!")


file1 = open("schedule-requirements.txt","w")
file1.write('%s\n' % str(len(dataWishes)))
file1.write('%s\n' % str(int((len(dataWishes.columns)+1)/7)))
file1.write('---\n')
for fix in fixed_shifts:
    file1.write('%s\n' % ' '.join(map(str, fix)))
file1.write('---\n')
for req in requests:
    file1.write('%s\n' % ' '.join(map(str, req)))
file1.write('---\n')
for dem in cover_demands:
    file1.write('%s\n' % ' '.join(map(str, dem)))
file1.close() #to change file access modes
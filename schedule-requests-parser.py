import pandas as pd
import sys

requests = []
fixed_shifts = []

# This is hardcoded for now, put should
# be read from a "cover-demands.txt".
cover_demands = [
    [2, 3, 1],
    [2, 3, 1],
    [2, 3, 2],
    [2, 3, 1],
    [2, 3, 1],
    [2, 3, 1],
    [2, 3, 1]
]


schedule_requirements_csv_file_name = sys.argv[1]

data = pd.read_csv(schedule_requirements_csv_file_name)

dataWishes = data.iloc[:,1:-1]

for nurse in range(0, len(dataWishes)):
    for day in range(0, len(dataWishes.columns)):
        if dataWishes.iat[nurse, day] != 'o,o,o':
            for shift, wish in enumerate(dataWishes.iat[nurse, day].replace(",",""), 1):
                if wish != 'o':
                    #print(wish,shift)
                    #print("Test")               
                    #print(nurse, shift, day, wish)
                    if wish == 'v':
                        # print("want:")
                        # print(nurse, shift, day, '-1')
                        requests.append([nurse, shift, day, '-2'])
                    elif wish == 'f':
                        # print("no please")
                        # print(nurse, shift, day, '+1')
                        requests.append([nurse, shift, day, '4'])
                    elif wish == 'F':
                        # print("nonononO!")
                        # print(nurse, shift, day)
                        fixed_shifts.append([nurse, shift, day])
                    elif wish == 'V':
                        # print("Yes!")
                        # print(nurse, shift, day)
                        fixed_shifts.append([nurse, shift, day])
                    else:
                        print("Input error!")

file1 = open("schedule-requests.txt", "w")
file1.write('%s\n' % str(len(dataWishes))) # Number of employees.
file1.write('%s\n' % str(int((len(dataWishes.columns)+1)/7))) # Number of weeks
file1.write('---\n')
for fix in fixed_shifts:
    file1.write('%s\n' % ' '.join(map(str, fix)))
file1.write('---\n')
for req in requests:
    file1.write('%s\n' % ' '.join(map(str, req)))
file1.write('---\n')
for dem in cover_demands:
    file1.write('%s\n' % ' '.join(map(str, dem)))
file1.close() # to change file access modes
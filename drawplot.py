#import matplotlib.pyplot as plt
import csv,datetime

result_file='results.csv'

with open(result_file) as f:
    reader = csv.reader(f)
    for row in reader:
        download_speed = row[0]
        upload_speed = row[1]
        latency = row[2]
        start_time = datetime.datetime.strptime(row[3], '%d-%m-%Y %H:%M:%S')
        stop_time = datetime.datetime.strptime(row[4], '%d-%m-%Y %H:%M:%S')
        print(download_speed, upload_speed, latency, start_time, stop_time)

#plot not implemented yet :) 
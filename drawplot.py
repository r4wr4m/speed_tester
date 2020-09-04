import matplotlib.pyplot as plt
import csv,datetime

result_file='results.csv'

download=[]
upload=[]
latency=[]
start_time=[]
start_time_str=[]
stop_time=[]
test_duration=[]

with open(result_file) as f:
    reader = csv.reader(f)
    for row in reader:
        download.append(row[0])
        upload.append(row[1])
        latency.append(row[2])
        start_time.append(datetime.datetime.strptime(row[3], '%d-%m-%Y %H:%M:%S'))
        start_time_str.append(datetime.datetime.strptime(row[3], '%d-%m-%Y %H:%M:%S').strftime('%Y%m%d_%H:%M:%S'))

        stop_time.append(datetime.datetime.strptime(row[4], '%d-%m-%Y %H:%M:%S'))
        test_duration.append((stop_time[-1] - start_time[-1]).total_seconds())


plt.plot(start_time_str, download, label="Download")
plt.plot(start_time_str, upload, label="Upload")
plt.plot(start_time_str, latency, label="Latency")


plt.xlabel('Time')
plt.ylabel('Value')
plt.title('SpeedTest!')
plt.legend()
plt.show()

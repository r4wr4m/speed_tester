import matplotlib.pyplot as plt
import csv,datetime

result_file='results.csv'

expected_download_speed = 90.0 #[Mbps]
expected_upload_speed = 90.0 #[Mbps]

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
        download.append(float(row[0]))
        upload.append(float(row[1]))
        latency.append(float(row[2]))
        start_time.append(datetime.datetime.strptime(row[3], '%d-%m-%Y %H:%M:%S'))
        start_time_str.append(datetime.datetime.strptime(row[3], '%d-%m-%Y %H:%M:%S').strftime('%Y%m%d_%H:%M:%S'))

        stop_time.append(datetime.datetime.strptime(row[4], '%d-%m-%Y %H:%M:%S'))
        test_duration.append((stop_time[-1] - start_time[-1]).total_seconds())

plt.plot(start_time_str, download, label="Download [Mbps]")
plt.plot(start_time_str, upload, label="Upload [Mbps]")
plt.plot(start_time_str, [expected_download_speed]*len(download), label="Expected download speed [Mbps]",linestyle='dashed')
plt.plot(start_time_str, [expected_upload_speed]*len(download), label="Expected upload speed [Mbps]",linestyle='dashed')
plt.bar(start_time_str, test_duration, label="Test duration [s]")
plt.bar(start_time_str, latency, label="Latency [ms]")

plt.xlabel('Time')
plt.xticks(rotation=45)
plt.ylabel('Value')
plt.title('SpeedTest!')
plt.legend()
plt.show()

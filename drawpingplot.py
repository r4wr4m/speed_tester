import matplotlib.pyplot as plt
import csv,datetime

result_file='pingresults.csv'

ping=[]
start_time=[]
start_time_str=[]
stop_time=[]
test_duration=[]

with open(result_file) as f:
    reader = csv.reader(f)
    for row in reader:
        if row[0][:3]!='---':
            ping.append(float(row[0]))
            start_time.append(datetime.datetime.strptime(row[1], '%d-%m-%Y %H:%M:%S'))
            start_time_str.append(datetime.datetime.strptime(row[1], '%d-%m-%Y %H:%M:%S').strftime('%Y%m%d_%H:%M:%S'))
            stop_time.append(datetime.datetime.strptime(row[2], '%d-%m-%Y %H:%M:%S'))
            test_duration.append((stop_time[-1] - start_time[-1]).total_seconds())
        else:
            #Drawing vertical separators (---comment in results file)
            x=len(ping)
            plt.axvline(x,linestyle='dotted',color="red")
            
plt.bar(start_time_str, ping, label="Ping")

plt.xlabel('Time')
plt.xticks(rotation=45)
plt.ylabel('Value')
plt.title('PingTest!')
plt.legend()
plt.show()

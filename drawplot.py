import matplotlib.pyplot as plt
import csv,datetime

result_file='results.csv'

expected_speeds= [ #[Mbps]
    [50,"Expected download speed [Mbps]"],
    [30,"Expected download speed [Mbps]"],
    [1,"Expected upload speed [Mbps]"]
    ] 

download=[]
upload=[]
latency=[]
start_time=[]
start_time_str=[]
stop_time=[]
test_duration=[]
average_down=[]
average_up=[]

def calculate_avg(values,average):
    if len(values)-len(average)!=0:
        avg=sum(values[len(average):len(values)])/(len(values)-len(average))
        for i in range(len(average),len(values)):
            average.append(avg)
    return average
    
with open(result_file) as f:
    reader = csv.reader(f)
    for row in reader:
        if row[0][:3]!='---':
            download.append(float(row[0]))
            upload.append(float(row[1]))
            latency.append(float(row[2]))
            start_time.append(datetime.datetime.strptime(row[3], '%d-%m-%Y %H:%M:%S'))
            start_time_str.append(datetime.datetime.strptime(row[3], '%d-%m-%Y %H:%M:%S').strftime('%Y%m%d_%H:%M:%S'))

            stop_time.append(datetime.datetime.strptime(row[4], '%d-%m-%Y %H:%M:%S'))
            test_duration.append((stop_time[-1] - start_time[-1]).total_seconds())
        else:
            #Drawing vertical separators (---comment in results file)
            x=len(download)
            plt.axvline(x,linestyle='dotted',color="red")
            plt.text(x+1,expected_speeds[0][0]/4*3,row[0][3:],color="red",rotation=90)
            
            #Calculating average
            if len(download)>0:
                average_down = calculate_avg(download,average_down)
                average_up = calculate_avg(upload,average_up)
average_down = calculate_avg(download,average_down)
average_up = calculate_avg(upload,average_up)

plt.plot(start_time_str, download, label="Download [Mbps]")
plt.plot(start_time_str, upload, label="Upload [Mbps]")

for expected_speed in expected_speeds: #Drawing expected speeds
    plt.plot(start_time_str, [expected_speed[0]]*len(download), label=expected_speed[1],linestyle='dashed')

plt.plot(start_time_str, average_down, label='Average download speed',linestyle='dashed')#,color='yellow')
plt.plot(start_time_str, average_up, label='Average upload speed',linestyle='dashed')#,color='yellow')


#Latency, test duration
#plt.bar(start_time_str, test_duration, label="Test duration [s]")
#plt.bar(start_time_str, latency, label="Latency [ms]")

plt.xlabel('Time')
plt.xticks(rotation=45)
plt.ylabel('Value')
plt.title('SpeedTest!')
plt.legend()
plt.show()

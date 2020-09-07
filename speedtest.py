import subprocess,re,time, os, sys, csv, datetime

interval=1
count=0
result_file='results.csv'

executable = ''
if os.name == 'nt':
    executable = 'speedtest.exe'
else:
    executable = './speedtest'


def test():
    start_time = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    cmd = executable + ' --accept-license --accept-gdpr -p no'
    raw=str(subprocess.check_output(cmd.split()))
    download_speed=float(re.findall("Download:(.*?)Mbps",raw)[0].strip())
    upload_speed=float(re.findall("Upload:(.*?)Mbps",raw)[0].strip())
    latency=float(re.findall("Latency:(.*?)ms",raw)[0].strip())
    return [download_speed, upload_speed, latency, start_time, datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')]


def write_result(result):
    with open(result_file, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(result)

while True:
    t = time.localtime()
    minute = int(time.strftime('%M',t))
    second = int(time.strftime('%S',t))
    if minute%interval == 0:
        if second == 0:
            try:
                print("Tests: ",count)
                write_result(test())
                count+=1
                time.sleep(1)
            except Exception as e : #error
                print(e)
                t = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
                write_result([0,0,0,t,t,str(e)])

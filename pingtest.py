import subprocess,re,time, os, sys, csv, datetime

interval=1 # in minutes
count=0
result_file='pingresults.csv'

def ping():
    s,r=subprocess.getstatusoutput("ping -n 1 8.8.8.8")
    if 'TTL=' in r:
        #print("Success")
        return 1
    else:
        #print("Failed with {}".format(r))
        return 0
        
def test():
    start_time = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    return [ping(), start_time, datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')]


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
            count+=1
            try:
                print("Ping tests: ",count)
                write_result(test())
                time.sleep(1)
            except Exception as e : #error
                print('Exception: ' + str(e))
                t = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
                write_result([0,t,t,str(e)])
    time.sleep(1)


import urllib3
import boto3
sns= boto3.client('sns')
http = urllib3.PoolManager()

urls = ['http://150.136.83.3'
]
topic_arn='arn:aws:sns:xxxxxxx'

def lambda_handler(event, context):
    do_health_check()

def do_health_check():
    failures = list()
    for url in urls:
        try:
            response = http.request('GET', url)
            if response.status != 200:
                error = dict()
                temp=url.split('://')
                error['url'] = '('+temp[0]+') '+temp[1]
                error['status'] = response.status
                error['response'] = response.data
                failures.append(error)
            else:
                print('reached url successfully'+url)
        except e:
            error = dict()
            temp=url.split('://')
            error['url'] = '('+temp[0]+') '+temp[1]
            error['status'] = 'xxx'
            error['response'] = e
            failures.append(error)
            message = "Error occurred for url: " + error['url']+ ". Error: " + e
            print(message)
            
    if len(failures) > 0:
        message = "Health check failures in following. \n\n"
        for failure in failures:
            message += repr(failure) + '\n'
        print('Sending message:'+ message)

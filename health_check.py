import concurrent.futures
import urllib.request
import ssl
## context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

import os
import time
import sys
import configparser

configParser = configparser.RawConfigParser()
configParser.read('application.ini')
#server1 = configParser.get('dev', 'server1')
#server2 = configParser.get('dev', 'server2')
#server3 = configParser.get('dev', 'server3')
#server4 = configParser.get('dev', 'server4')
#server5 = configParser.get('dev', 'server5')

#URLS_FROM_INI = [server1, server2, server3, server4, server5]

print("loading urls to check health")
URLS = list(map(lambda url: url.strip(), os.environ['SERVERS'].split(",")))

def check_health(url, timeout):
    with urllib.request.urlopen(url, context=ctx, timeout=timeout) as conn:
        return conn.getcode()

def check_healths():
    print("checking health for servers")
    # We can use a with statement to ensure threads are cleaned up promptly
    with concurrent.futures.ThreadPoolExecutor(max_workers = len(URLS)) as executor:
        # Start the healthcheck operations and mark each future with its URL
        sys.stdout.write("starting health check for " + str(len(URLS)) + " services.\n")
        tasks = {executor.submit(check_health, url, 60): url for url in URLS}
        for task in concurrent.futures.as_completed(tasks):
            url = tasks[task]
            try:
                data = task.result()
            except Exception as exc:
                print('%r : %s' % (url, exc))
            else:
                print('%r : %s' % (url, data))

while True:
    check_healths()
    time.sleep(60)

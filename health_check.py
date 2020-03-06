import concurrent.futures
import urllib.request
import ssl
## context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

import time

URLS = ['https://api.github.com',
        'https://twitter.com',
        'https://api.facebook.com',
        'https://expedia.com',
        'http://some-made-up-domain.com']

def check_health(url, timeout):
    with urllib.request.urlopen(url, context=ctx, timeout=timeout) as conn:
        return conn.getcode()

def check_healths():
    # We can use a with statement to ensure threads are cleaned up promptly
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        # Start the load operations and mark each future with its URL
        tasks = {executor.submit(check_health, url, 60): url for url in URLS}
        for task in concurrent.futures.as_completed(tasks):
            url = tasks[task]
            try:
                data = task.result()
            except Exception as exc:
                print('%r : %s' % (url, exc))
            else:
                print('%r : %s' % (url, data))

check_healths()

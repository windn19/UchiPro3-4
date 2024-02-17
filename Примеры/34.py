import datetime
import time

import schedule


def print_time():
    now = datetime.datetime.now()
    print(now.strftime('%H:%M'))


schedule.every().minutes.do(print_time)

while True:
    schedule.run_pending()
    time.sleep(1)

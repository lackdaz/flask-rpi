import os
import time
from flaskr.db import get_db

import random
import decimal

def measure_temp():
    # temp = os.popen("vcgencmd measure_temp").readline()
    # return (temp.replace("temp=",""))
    return float(decimal.Decimal(random.randrange(0, 1000) / 10))


def temp_daemon():
    db = get_db()
    while True:
            time.sleep(1)
            current_temp = measure_temp()
            db.execute(
                'INSERT INTO reading (temp) VALUES (?)',
                (current_temp, )
            )
            # print("inserted ", current_temp)
            db.commit()

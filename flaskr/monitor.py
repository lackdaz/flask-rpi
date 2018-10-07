import os
import time
import sqlite3

import random
import decimal


def measure_temp():
    try:
        temp = os.popen("vcgencmd measure_temp").readline()
        temp = temp.replace("temp=","")
        temp = temp.replace("'C\n", "")

    except Exception as e:
        temp = float(decimal.Decimal(random.randrange(0, 1000) / 10))
    return float(temp)


def log_temp(temp):
    conn = sqlite3.connect('./instance/flaskr.sqlite')
    cursor = conn.cursor()

    cursor.execute(
        'INSERT INTO reading (temp) VALUES (?)',
        (temp, )
    )
    print("logged")
    conn.commit()
    conn.close()

def init():
    while True:
        time.sleep(5)
        current_temp = measure_temp()
        print("measured ", current_temp)
        log_temp(current_temp)

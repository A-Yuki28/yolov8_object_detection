import schedule
from time import sleep
from Myscreenshot import get_screenshot

def task():
    print("タスク実行中")
    get_screenshot()
    
schedule.every(10).seconds.do(task)

try:
    while True:
        schedule.run_pending() # 指定時間が来てたら実行、まだなら何もしない 
        sleep(1) # 待ち
except KeyboardInterrupt:
    print("end")
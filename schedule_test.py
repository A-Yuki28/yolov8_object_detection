import schedule
from time import sleep

def task():
    print("タスク実行中")
    
schedule.every(10).seconds.do(task)

while True:
    schedule.run_pending() # 指定時間が来てたら実行、まだなら何もしない 
    sleep(1) # 待ち

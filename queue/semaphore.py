import time
import threading

semaphore = threading.Semaphore(2)
 
def func():
    if semaphore.acquire():
        for i in range(3):
          print (threading.currentThread().getName() + ' get semaphore')
        time.sleep(2)
        semaphore.release()
        print (threading.currentThread().getName() + ' release semaphore')
        
        
for i in range(5):
  t1 = threading.Thread(target=func)
  t1.start()

import threading
global x #declaration
x = 10
def increment():
    global x #used to refer
    x+=1

def thread_task(lock): #task for thread
    for _ in range(100000): #call increment function
        lock.acquire()
        increment()
        lock.release()

def main_task():
    global x #setting global var as 0
    x = 0
    lock = threading.Lock() #creating lock
    t1 = threading.Thread(target = thread_task, args = (lock,))
    t2 = threading.Thread(target = thread_task, args = (lock,))
    t1.start() #start thread
    t2.start() 
    t1.join() #wait until threads finish their job
    t2.join()

if __name__ == "__main__": #main thread
    for i in range (10):
        main_task()
        print("Iteration {0}: x = {1}".format(i,x))
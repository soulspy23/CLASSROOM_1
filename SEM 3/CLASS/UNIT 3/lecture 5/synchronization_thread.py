import threading
lock = threading.Lock()
class MyClass(threading.Thread):
    def __init__(self,thread_name,thread_ID):
        threading.Thread.__init__(self)
        self.thread_name = thread_name
        self.thread_ID = thread_ID

    def run(self):
        lock.acquire()
        if(self.thread_ID == 1000):
            #lock.acquire()
            print("Enter 5 numbers :")
            list1 = []
            for i in range(0,5):
                num = int(input())
                list1.append(num)
            print("Maximum :",max(list1))
            #lock.release()
        else:
            for i in range(1,51):
                print(i)
        lock.release()

thread1 = MyClass("STUDY",1000)
thread2 = MyClass("STUDY",2000)
thread1.start()
thread2.start()
print("Exit !")
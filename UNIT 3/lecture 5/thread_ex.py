# to create 2 threads thread 1 & 2. Thread 1 is going to generate the max no from the accepted list whereas 
# thread 2 is going to display a counter from 1 to 15 | 50

import threading
class myclass(threading.Thread):
    def __init__(self,thread_name,thread_id):
        threading.Thread.__init__(self)
        self.thread_name = thread_name
        self.thread_id = thread_id
    
    def run(self):
        if(self.thread_id==1000):
            print("Enter 5 numbers :")
            list1 = []
            for i in range(0,5):
                num = int(input())
                list1.append(num)
            print("Maximum = ",max(list1))
        else:
            for i in range(1,51):
                print(i)

t1 = myclass("STUDY",1000)
t2 = myclass("STUDY",2000)

t1.start()
t2.start()
print("Exit !")
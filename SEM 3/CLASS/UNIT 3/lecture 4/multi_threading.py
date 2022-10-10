#create thread using class
import threading
class thread(threading.Thread):
    def __init__(self,thread_name,thread_ID):
        threading.Thread.__init__(self)
        self.thread_name = thread_name
        self.thread_ID = thread_ID
    def run(self): #indicates to run the program
        print(str(self.thread_name)+" "+str(self.thread_ID))

thread1 = thread("STUDY", 1000) #user-defined
thread2 = thread("STUDY", 2000)
thread1.start()
thread2.start()
print("Exit !")
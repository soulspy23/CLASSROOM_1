#creating thread using function
from threading import Thread
from time import sleep
def threaded_fun(arg):
    for i in range(arg):
        print("Running !")
        sleep(1) #wait 1 second between threads

if __name__ == "__main__": #name of process
    thread = Thread(target=threaded_fun,args=(10,))
    thread.start()
    thread.join()
    print("Thread finished...exiting!")
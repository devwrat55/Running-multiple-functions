from threading import Thread
import time
global stop_threads

def function1():
    while True: 
        print('thread running')
        time.sleep(1) 
        global stop_threads 
        print("Executing tasks for 1 seconds")
        time.sleep(1)
        if stop_threads: 
            break
        
def function2():
    global stop_threads
    stop_threads = False
    time.sleep(10) 
    stop_threads = True
    print('thread kill initiated') 
    
if __name__ == '__main__':
    Thread(target = function1).start()
    Thread(target = function2).start()
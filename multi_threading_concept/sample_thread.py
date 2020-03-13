from threading import Thread
import time


def timer(name,delay,repeat):
    print ("Timer is {} started:".format(name))
    while repeat > 0:
        time.sleep(delay)
        print(str(time.ctime(time.time())))
        print("Thread {}".format(name))
        repeat -= 1
    print ("Timer is {}completed".format(name))

def Main():
    t1 = Thread(target=timer,args=("Timer1",3,5))
    t2 = Thread(target=timer,args=("Timer2",2,5))
    t1.start()
    t2.start()

if __name__ == "__main__":
    Main()

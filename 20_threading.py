import time, random, threading

def worker1():
    print("Worker1 started...")
    time.sleep(random.randint(1, 10))
    print("Worker1 stopped.")

def worker2():
    print("Worker2 started...")
    time.sleep(random.randint(1, 10))
    print("Worker2 stopped.")

def worker3():
    print("Worker3 started...")
    time.sleep(random.randint(1, 10))
    print("Worker3 stopped.")


t1 = threading.Thread(target=worker1)
t2 = threading.Thread(target=worker2)
t3 = threading.Thread(target=worker3)

t1.start()
t2.start()
t3.start()
import time, random

def my_timer(func):
    def wrapper():
        start = time.time()
        func()
        stop = time.time()
        print(f"process time: {stop-start}")

    return wrapper


@my_timer
def worker1():
    print("Worker1 started...")
    time.sleep(random.randint(1, 10))
    print("Worker1 stopped.")

@my_timer
def worker2():
    print("Worker2 started...")
    time.sleep(random.randint(1, 10))
    print("Worker2 stopped.")

@my_timer
def worker3():
    print("Worker3 started...")
    time.sleep(random.randint(1, 10))
    print("Worker3 stopped.")

worker1()
worker2()
worker3()
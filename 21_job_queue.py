import time, random, queue, threading

file_list = [
    "image_0001.exr",
    "image_0002.exr",
    "image_0003.exr",
    "image_0004.exr",
    "image_0005.exr",
    "image_0006.exr",
    "image_0007.exr",
    "image_0008.exr",
    "image_0009.exr",
    "image_0010.exr",
    "image_0011.exr",
]

# convert our list to a queue
job_queue = queue.Queue()
for i in file_list:
    job_queue.put(i)


def converter():
    while not job_queue.empty():
        file = job_queue.get()
        print(f"Conerting {file}...")
        time.sleep(random.randint(6, 30))
        print("Convert finished")
        job_queue.task_done()

for _ in range(10):
    t = threading.Thread(target=converter)
    t.start()
import time, random


def temp_warning(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result > 80:
            print(f"WARNING: Temperature is high ({result})")

        return result
    return wrapper


@temp_warning
def get_sensor_data(min, max):
    print("get sensor data...")
    time.sleep(2)
    return random.uniform(min, max)


for i in range(10):
    result = get_sensor_data()
    print(f"Temperature: {result}")
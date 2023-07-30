import random
import time
import sys
# from memory_profiler import profile


# import matplotlib
# pip install matplotlib memory_profiler
# mprof run --include-children python __generator_vs_brutfors.py
# mprof plot --output memory-profile.png

# @profile
def start():
    car_names = ["Toyota", "Honda", "Audi", "Nissan"]
    car_colors = ["Black", "Blue", "Red", "Yellow", "White"]

    def create_cars_bad(car_count: int) -> list[dict]:
        # size: 8448728
        # Elapsed time: 6.5499268

        cars = []
        for i in range(0, car_count):
            car = {"id": i, "name": random.choice(car_names), "color": random.choice(car_colors)}
            cars.append(car)
        return cars

    def create_cars_good(car_count: int) -> list[dict]:
        # size: 104
        # Elapsed time: 7.2534857

        for i in range(0, car_count):
            car = {"id": i, "name": random.choice(car_names), "color": random.choice(car_colors)}
            yield car

    cars_objs = create_cars_bad(10000000)
    # cars_objs = create_cars_good(10000000)
    for i in cars_objs:
        # print(i["name"])
        pass

    print("size: ", sys.getsizeof(cars_objs))


t_start = time.perf_counter()
start()
t_stop = time.perf_counter()
print("Elapsed time: ", round(t_stop - t_start, 7))

# size:  104
# Elapsed time:  2.4491786

# size:  8448728
# Elapsed time:  7.7333951

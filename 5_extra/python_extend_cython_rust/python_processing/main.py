import time
from src import check_python

def time_measure(func):
    def wrap(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        stop_time = time.perf_counter()
        print(f"TIme elapsed: {round(stop_time-start_time, 5)}")
        return result
    return wrap

@time_measure
def test_clear(data):
    time.sleep(1.666)

@time_measure
def test_python(data):
    check_python.get_borders_double_loop(data)

if __name__ == "__main__":
    data1 = list(range(1, 1000))
    data2 = list(range(1, 10000))
    # test_clear()
    test_python(data1)
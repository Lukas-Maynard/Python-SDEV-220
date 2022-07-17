import multiprocessing
import time
import random

def waiting():
    t = random.random()
    time.sleep(t)
    print(f'Slept for {t} seconds')
    
p1 = multiprocessing.Process(target=waiting)
p2 = multiprocessing.Process(target=waiting)
p3 = multiprocessing.Process(target=waiting)


if __name__ == "__main__":
    start = time.time()
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
    end = time.time()

    print(f'Total time: {end - start}')
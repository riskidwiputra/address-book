import time
import sys
import random
from abstract.observer import Observer


class LoadingObserver(Observer):
    def __call__(self):
        loading_text = "Loading"
        duration = random.uniform(0.5, 2.0) 
        end_time = time.time() + duration
        while time.time() < end_time:
            for i in range(4):
                sys.stdout.write(f"\r{loading_text}{'.' * i}")
                sys.stdout.flush()
                time.sleep(0.2)
        sys.stdout.write("\r" + " " * (len(loading_text) + 3) + "\r")
        sys.stdout.flush()
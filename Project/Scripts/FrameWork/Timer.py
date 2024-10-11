import time

class Timer:

    def __init__(self):
        self.__startTime = 0
        pass

    def __del__(self):
        pass

    def Start(self):
        self.__startTime = time.time()
        pass

    def Time(self):
        return time.time() - self.__startTime

    pass
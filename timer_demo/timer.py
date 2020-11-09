from time import time


class Timer:
    def __init__(self):
        self.clear()

    def start(self):
        self.start_time = time()

    def end(self):
        if not self.started:
            return

        curr_time = time()

        if self.paused:
            self.resume(timestamp=curr_time)

        self.end_time = time()

    def pause(self):
        if self.paused or not self.started:
            return

        self.ballast_start = time()

    def resume(self, timestamp=None):
        if not self.paused or not self.started:
            return

        curr_time = timestamp or time()

        self.ballast += curr_time - self.ballast_start
        self.ballast_start = None

    @property
    def paused(self):
        return self.ballast_start is not None

    @property
    def started(self):
        return self.start_time is not None

    @property
    def ended(self):
        return self.start_time is not None and self.end_time is not None

    @property
    def current_time(self):
        if not self.started:
            return 0

        if self.ended:
            return self.end_time - self.start_time - self.ballast

        if self.paused:
            return self.ballast_start - self.start_time - self.ballast

        return time() - self.start_time - self.ballast

    def clear(self):
        self.ballast = 0
        self.start_time = None
        self.end_time = None
        self.ballast_start = None

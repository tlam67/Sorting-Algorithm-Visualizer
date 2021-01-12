import random

class Algorithm:
    def __init__(self, name):
        self.array = random.sample(range(512), 512)
        self.name = name

    def update_display(self, swap1=None, swap2=None):
        import visualizer
        visualizer.update(self, swap1, swap2)

    def run(self):
        self.start_time = time.time()
        self.algorithm()
        time_elapsed = time.time() - self.start_time
        return self.array, time_elapsed
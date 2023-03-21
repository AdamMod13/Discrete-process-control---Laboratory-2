from dataclasses import dataclass

@dataclass
class Task:
    def __init__(self, release_t, processing_t, delivery_t):
        self.release_t = release_t
        self.processing_t = processing_t
        self.delivery_t = delivery_t

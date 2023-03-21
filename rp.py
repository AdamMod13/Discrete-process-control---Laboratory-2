from RandomNumberGenerator import *
from dataclasses import dataclass

rng = RandomNumberGenerator(1)
p = []
for _ in range(1,11):
    p.append(rng.nextInt(1,29))
    
A = sum(p)

r = []
for _ in range(1,11):
    r.append(rng.nextInt(1,A))

q = []
for _ in range(1,11):
    q.append(rng.nextInt(1,29))

r_copy = r
p_copy = p
q_copy = q

@dataclass
class Task:
    def __init__(self, release_t, processing_t, delivery_t):
        self.release_t = release_t
        self.processing_t = processing_t
        self.delivery_t = delivery_t

tasks = []

print(r)
print(p)
print(q)

def Schrage(tasks):
    tasks_copy = tasks.copy()
    tasks_copy.sort(key=lambda x: x.release_t)
    pi = [] # Kolejność zadań
    G = [] # Gotowe zadania

    c_time = tasks_copy[0].release_t 
    Cmax = 0

    while G or tasks_copy:
        while tasks_copy and tasks_copy[0].release_t <= c_time:
            j = tasks_copy.pop(0)
            G.append(j)

        if not G:
            c_time = tasks_copy[0].release_t
            continue
        j = max(G, key=lambda x: x.delivery_t)
        G.remove(j)
        pi.append(j)
        c_time += j.processing_t
        Cmax = max(Cmax, c_time + j.delivery_t)

    return Cmax, pi

tasks = []

for i in range(0,10):
    tasks.append(Task(r[i], p[i], q[i]))

Cmax, pi = Schrage(tasks)
print("Cmax:", Cmax)
print("Kolejnośc zadań:")
for p in pi:
    print(p.release_t, p.processing_t, p.delivery_t)


import math
from Classes import Task
from RandomNumberGenerator import RandomNumberGenerator

rng = RandomNumberGenerator(7523)
p = []
for _ in range(0,10):
    p.append(rng.nextInt(1,29))

A = sum(p)

r = []
for _ in range(0,10):
    r.append(rng.nextInt(1,A))

X = A

q = []
for _ in range(0,10):
    q.append(rng.nextInt(1,X))

tasks = []
for i in range(0,10):
    tasks.append(Task(r[i], p[i], q[i]))

print(r)
print(p)
print(q)

def SchragePmtn(tasks):
    tasks_copy = tasks.copy()
    pi = [] # Kolejność zadań
    G = [] # Gotowe zadania
    NG = [task for task in tasks_copy]

    # c_time = tasks_copy[0].r 
    c_time = 0
    Cmax = 0
    breaking_task = Task(0,0, math.inf) # Zadanie przerywające

    while G or NG:
        while NG and min(NG, key=lambda task: task.r).r <= c_time:
            j = min(NG, key=lambda task: task.r)
            NG.remove(j)
            G.append(j)

            if j.q > breaking_task.q:
                breaking_task.p = c_time - j.r
                c_time = j.r
                if breaking_task.p > 0:
                    G.append(breaking_task)
        if not G:
            c_time = min(NG, key=lambda task: task.r).r
            continue
        else:
            j = max(G, key=lambda x: x.q)
            G.remove(j)
            breaking_task = j
            pi.append(j)
            c_time += j.p
            Cmax = max(Cmax, c_time + j.q)

    return Cmax, pi

tasks = []
for i in range(len(r)):
    tasks.append(Task(r[i], p[i], q[i]))

Cmax, pi = SchragePmtn(tasks)
print("Cmax:", Cmax)
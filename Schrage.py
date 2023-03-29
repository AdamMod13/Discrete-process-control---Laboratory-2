from Classes import Task
from RandomNumberGenerator import RandomNumberGenerator

rng = RandomNumberGenerator(1)
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

print(r)
print(p)
print(q)

def Schrage(tasks):
    tasks_copy = tasks.copy()
    sorted_tasks = sorted(tasks, key=lambda x: x.r)
    pi = [] # Kolejność zadań
    G = [] # Gotowe zadania
    C = []
    Cq = []
    S = []

    # c_time = tasks_copy[0].r 
    c_time = 0
    Cmax = 0
    j = 0

    while G or sorted_tasks:
        while sorted_tasks and sorted_tasks[0].r <= c_time:
            j = sorted_tasks.pop(0)
            G.append(j)

        if not G:
            c_time = sorted_tasks[0].r
        else:
            j = max(G, key=lambda x: x.q)
            G.remove(j)
            S.append(max(j.r, c_time))
            pi.append(j)
            c_time += j.p
            C.append(S[-1] + j.p)
            Cmax = max(Cmax, c_time + j.q)
            Cq.append(C[-1] + j.q)

    return S, C, Cq, Cmax, pi

# Init Task array
tasks = []
for i in range(0,10):
    tasks.append(Task(r[i], p[i], q[i]))

# Schrage algorithm
print("Schrage Algorithm")

S, C, Cq, Cmax, pi = Schrage(tasks)
print("Cmax:", Cmax)
print("Kolejnośc zadań:")
# for p in (pi):
#     print(p.r, p.p, p.q)

print("S: ", S)
print("C: ", C)
print("Cq: ", Cq)
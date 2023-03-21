from RandomNumberGenerator import *
from Classes import Task
from Schrage import Schrage

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

print(r)
print(p)
print(q)

# Init Task array
tasks = []
for i in range(0,10):
    tasks.append(Task(r[i], p[i], q[i]))

# Schrage algorithm
print("Schrage Algorithm")

Cmax, pi = Schrage(tasks)
print("Cmax:", Cmax)
print("Kolejnośc zadań:")
for index, p in enumerate(pi):
    print(index,": ", p.release_t, p.processing_t, p.delivery_t)


#
print("\n")
#

# Schrage PMTN algorith 
print("SchragePmtn Algorithm")

Cmax_pmtn, pi_pmtn = Schrage(tasks)
print("Cmax:", Cmax_pmtn)
print("Kolejnośc zadań:")
for index_pmtn, p in enumerate(pi_pmtn):
    print(index_pmtn,": ", p.release_t, p.processing_t, p.delivery_t)
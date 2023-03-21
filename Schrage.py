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
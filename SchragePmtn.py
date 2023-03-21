def Schrage(tasks):
    tasks_copy = tasks.copy()
    tasks_copy.sort(key=lambda x: x.release_t)
    pi = [] # Kolejność zadań
    G = [] # Gotowe zadania

    c_time = tasks_copy[0].release_t 
    Cmax = 0
    breaking_task = (0, float("inf")) # Zadanie przerywające

    while G or tasks_copy:
        while tasks_copy and tasks_copy[0].release_t <= c_time:
            j = tasks_copy.pop(0)
            G.append(j)

            if j.delivery_t > breaking_task.delivery_t:
                breaking_task.processing_t = c_time - j.release_t
                if breaking_task.processing_t > 0:
                    G.append((breaking_task.release_t, breaking_task.processing_t, float("inf")))
        if not G:
            c_time = tasks_copy[0].release_t
            continue
        j = max(G, key=lambda x: x.delivery_t)
        G.remove(j)
        breaking_task = j
        pi.append(j)
        c_time += j.processing_t
        Cmax = max(Cmax, c_time + j.delivery_t)

    return Cmax, pi
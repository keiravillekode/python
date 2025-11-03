def moves(poles, discs):
    if discs == 0:
        return 0

    # all on the first pole
    start = tuple([2 ** discs - 1] + [0] * (poles - 1))

    # all on the last pole
    destination = tuple([0] * (poles - 1) + [2 ** discs - 1])

    count = 0
    next_generation = [start]
    seen = {start}

    while True:
        current_generation = next_generation
        next_generation = []
        count += 1
        while len(current_generation) > 0:
            current = current_generation.pop()
            for source in range(poles):
                # source pole empty?
                if current[source] == 0:
                    continue

                disk = current[source] & (-current[source])
                for sink in range(poles):
                    # sink pole already contains a smaller disk?
                    if sink == source or (current[sink] & (disk - 1)) != 0:
                        continue

                    values = list(current)
                    values[source] -= disk
                    values[sink] += disk
                    state = tuple(values)
                    if state in seen:
                        continue

                    if state == destination:
                        return count

                    seen.add(state)
                    next_generation.append(state)

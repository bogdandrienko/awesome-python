def get_borders_double_loop(deposits: list[float], min_length: int=10) -> list[tuple]:
    borders = []
    for i in range(len(deposits)):
        for j in range(len(deposits)):
            temp = 0
        if deposits[i] > 0:
            if len(borders) == 0:
                borders.append([i])
            else:
                if i - borders[-1][0] >= min_length:
                    borders[-1].extend([i])
                    borders.append([i])
    return borders
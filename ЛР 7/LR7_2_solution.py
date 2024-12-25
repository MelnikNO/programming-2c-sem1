def two_sum(lst: list[int], target: int) -> tuple[int, int] | None:
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] + lst[j] == target:
                return (i, j)
    return None
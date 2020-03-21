from functools import reduce

print(
    reduce(
        min,
        filter(
            lambda x: x % 2 == 1,
            map(
                int,
                input().split()
            )
        )
    )
)

import sys

print(
    len(
        set(
            sys.stdin.read().split()
            )
    )
)

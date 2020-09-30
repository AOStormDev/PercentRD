import random
def Random(percent: int):
    r = random.randint(0, 100)
    if r <= percent:
        return "a"
    else:
        return "b"
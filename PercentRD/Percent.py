from random import randint
def random(percent: int):
    r = randint(0, 100)
    if r <= percent:
        return True
    else:
        return False

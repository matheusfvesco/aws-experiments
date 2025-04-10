from fastapi import FastAPI
from pydantic import BaseModel
from mangum import Mangum
import hashlib
import numpy as np

app = FastAPI()
handler = Mangum(app)


class Target(BaseModel):
    string: str


@app.get("/")
def root():
    return {"api_name": "hash api", "author": "matheusfvesco"}


@app.post("/hash/md5")
def hash_md5(target: Target):
    hash_hex = hashlib.md5(target.string.encode()).hexdigest()
    return {"hash": hash_hex}


@app.post("/hash/sha256")
def hash_sha256(target: Target):
    hash_hex = hashlib.sha256(target.string.encode()).hexdigest()
    return {"hash": hash_hex}

@app.post("/hash/art")
def hash_drunken_bishop(target: Target):
    art = drunken_bishop(target.string)
    return {"art": art}


def drunken_bishop(input_string):
    hash_bytes = hashlib.sha256(input_string.encode()).digest()

    width, height = 17, 9
    grid = np.zeros((height, width), dtype=int)

    x, y = width // 2, height // 2
    path = [(y, x)]

    # Walk: Each byte gives 4 2-bit steps (00, 01, 10, 11)
    for byte in hash_bytes:
        for shift in [6, 4, 2, 0]:
            step = (byte >> shift) & 0b11
            dx = 1 if step & 1 else -1
            dy = 1 if step & 2 else -1

            x = max(0, min(width - 1, x + dx))
            y = max(0, min(height - 1, y + dy))
            path.append((y, x))

    for y, x in path:
        grid[y, x] += 1

    symbols = ' .o+=*BOX@%&#/^SE'
    max_val = len(symbols) - 2

    result = ['+----[SHA256]-----+']
    for y in range(height):
        row = '|'
        for x in range(width):
            if (y, x) == path[0]:
                row += 'S'
            elif (y, x) == path[-1]:
                row += 'E'
            else:
                val = grid[y, x]
                row += symbols[min(val, max_val)]
        row += '|'
        result.append(row)
    result.append('+----[SHA256]-----+')

    return '\n'.join(result)
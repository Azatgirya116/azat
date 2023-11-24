# TODO решите задачу
import json

def task() -> float:
    with open('input.json', 'r') as f:
        xx = json.load(f)

    product_sum = sum(item["score"] * item["weight"] for item in xx)
    res = round(product_sum, 3)
    return res

print(task())
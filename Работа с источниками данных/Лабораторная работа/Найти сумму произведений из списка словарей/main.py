import json
import sys

def task() -> float:
    with open('input.json', encoding='utf-8') as f:
        data = json.load(f)
    total = sum(item['score'] * item['weight'] for item in data)
    return round(total, 3)

if __name__ == '__main__':
    print(task())

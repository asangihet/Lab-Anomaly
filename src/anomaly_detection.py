import random
from statistics import mean, stdev

def flag_anomalies(amounts: list[int], student_id: str) -> list[int]:
    random.seed(int(student_id[-3:]))
    sample = random.sample(amounts, k=max(1, len(amounts) // 10))
    μ = mean(sample)
    σ = stdev(sample) if len(sample) > 1 else 0
    return [a for a in amounts if abs(a - μ) > 1.5 * σ]

transactions = [102, 98, 97, 99, 101, 100, 250,
                97, 95, 420, 101, 99]

result = flag_anomalies(transactions, student_id="7461502")
print(result)
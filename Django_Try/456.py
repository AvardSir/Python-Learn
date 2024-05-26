def resource_allocation(resource_table):
    num_participants = len(resource_table)

    num_resources = len(resource_table[0])

    dp = [[0] * (num_resources + 1) for _ in range(num_participants + 1)]

    for i in range(1, num_participants + 1):
        for j in range(1, num_resources + 1):
            max_val = 0
            for k in range(j):
                max_val = max(max_val, dp[i-1][j-k-1] + sum(resource_table[i-1][:k]))

            dp[i][j] = max_val

    return dp[num_participants][num_resources],dp

# Пример данных

import numpy as np


resource_table =(
[[0.50,0.3,0.80,1.20],
[0.60,0.5,0.90,1.30],
[0.70,0.7,1.00,1.40],
[0.80,0.9,1.10,1.50],
[0.80,1.10,1.20,1.50],
[0.90,1.20,1.30,1.60],
[0.90,1.30,1.40,1.60],
[1.00,1.40,1.50,1.70],
[1.00,1.50,1.60,1.70]]
)
max_profit,dp = resource_allocation(resource_table)
dp=np.array(dp)
for i in range(len(dp)):
    print(f'sum {i} {sum(dp[i])}')
print(f"Максимальная прибыль: {round(max_profit,2)}")
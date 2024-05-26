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
[
[0.5,0.9,0.3],
[0.8,1,0.6],
[0.9,1.1,0.9],
[1,1.2,1.1],
[1.2,1.3,1.3],
[1.3,1.4,1.4],
[1.4,1.4,1.5]]
)
print(resource_table)
max_profit,dp = resource_allocation(resource_table)
dp=np.array(dp)
print(dp)

print(f"Максимальная прибыль: {round(max_profit,2)}")
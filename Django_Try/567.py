
for _ in range(1000):
    dfg_1.append(dfg.generate_next())

dfg_1=np.array(dfg_1)
dfg_1 = dfg_1.astype(np.float64)

dfg_5=[]
for _ in range(5000):
    dfg_5.append(dfg)

dfg_10 = []
for _ in range(10000):
    dfg_10.append(dfg)
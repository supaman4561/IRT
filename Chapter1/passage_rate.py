import numpy as np

data = []

filename = input("filename:")
with open(filename, 'r') as f:
    for row in f:
        data.append([int(v) for v in list(row.strip('\n'))])

data = np.array(data)

passage_rate = []

for item in data.transpose():
    passage_rate.extend(item.sum() / item.shape)

passage_rate = np.array(passage_rate)

print(passage_rate)

dict = {}

for i, p in enumerate(passage_rate):
    dict.update({str(i+1):p})

# 通過率を基に項目を降順に表示
for k, v in sorted(dict.items(), key=lambda x:-x[1]):
    print(k, v)

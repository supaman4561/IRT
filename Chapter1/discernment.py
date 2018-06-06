import numpy as np

def get_scores(data, allotment):
    score = []
    for subject in data:
        score.append(np.dot(subject, allotment))
    score = np.array(score)
    return score

def get_corrcoef(res, scores):
    ave_res = np.sum(res)/res.size
    ave_scores = np.sum(scores)/scores.size
    s_xy = sum([(x-ave_res)*(y-ave_scores) for x, y in zip(res, scores)])
    s_x = np.sqrt(sum([(x-ave_res)**2 for x in res]))
    s_y = np.sqrt(sum([(y-ave_scores)**2 for y in scores]))
    corrcoef = s_xy / (s_x * s_y)
    return corrcoef

if __name__ == '__main__':
    data = []
    filename = input("filename:")
    with open(filename, 'r') as f:
        for row in f:
            data.append([int(v) for v in list(row.strip('\n'))])
    data = np.array(data)
    allotment = np.array([1 for i in range(data.shape[1])])
    scores = get_scores(data, allotment)
    discernment = np.array([get_corrcoef(res, scores) for res in data.T])
    print(discernment)

import numpy as np

def get_scores(data, allotment):
    score = []
    for subject in data:
        score.append(np.dot(subject, allotment))
    score = np.array(score)
    return score

if __name__ == '__main__':
    data = []
    filename = input("filename:")
    with open(filename, 'r') as f:
        for line in f:
            data.append([int(v) for v in list(line.strip('\n'))])
    data = np.array(data)
    allotment = np.array([1 for i in range(data.shape[1])])
    scores = get_scores(data, allotment)
    dict_score = {i: score for (i, score) in enumerate(scores)}
    dict_score = sorted(dict_score.items(), key=lambda x: -x[1])

    H = dict_score[0 : int(len(dict_score)/5)]
    MH = dict_score[int(len(dict_score)/5) : int(len(dict_score)*2/5)]
    M = dict_score[int(len(dict_score)*2/5) : int(len(dict_score)*3/5)]
    LM = dict_score[int(len(dict_score)*3/5) : int(len(dict_score)*4/5)]
    L = dict_score[int(len(dict_score)*4/5) : ]

    pass_H = []
    pass_MH = []
    pass_M = []
    pass_LM = []
    pass_L = []
    for res in data.T:
        pass_H.append(sum([res[sub[0]] for sub in H]) / len(H))
        pass_MH.append(sum([res[sub[0]] for sub in MH]) / len(MH))
        pass_M.append(sum([res[sub[0]] for sub in M]) / len(M))
        pass_LM.append(sum([res[sub[0]] for sub in LM]) / len(LM))
        pass_L.append(sum([res[sub[0]] for sub in L]) / len(L))

    print(pass_H)
    print(pass_MH)
    print(pass_M)
    print(pass_LM)
    print(pass_L)

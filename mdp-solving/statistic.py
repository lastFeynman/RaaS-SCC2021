import matplotlib.pyplot as plt
import numpy as np

sample_number_per_episode = 100
N_episode = 200

def average(data):
    return sum(data) / len(data)


def bootstrap(data, B, c, func):
    """
    计算bootstrap置信区间
    :param data: array 保存样本数据
    :param B: 抽样次数 通常B>=1000
    :param c: 置信水平
    :param func: 样本估计量
    :return: bootstrap置信区间上下限
    """
    array = np.array(data)
    n = len(array)
    sample_result_arr = []
    for i in range(B):
        index_arr = np.random.randint(0, n, size=n)
        data_sample = array[index_arr]
        sample_result = func(data_sample)
        sample_result_arr.append(sample_result)

    a = 1 - c
    k1 = int(B * a / 2)
    k2 = int(B * (1 - a / 2))
    auc_sample_arr_sorted = sorted(sample_result_arr)
    lower = auc_sample_arr_sorted[k1]
    higher = auc_sample_arr_sorted[k2]

    return lower, higher

if __name__ == '__main__':
    revenues_data = np.zeros((N_episode, sample_number_per_episode))
    violation_data = np.zeros((N_episode, sample_number_per_episode))

    for i in range(sample_number_per_episode):
        with open("results/sample-" + str(i), "r") as f:
            for j in range(N_episode):
                line = f.readline()
                line = line.split(" ")
                revenues_data[j][i] = float(line[2])
                violation_data[j][i] = float(line[1])
            f.close()

    with open("result", "w") as f:
        for i in range(N_episode):
            revenues = revenues_data[i]
            violations = violation_data[i]

            print(min(revenues), max(revenues))
            print(min(violations), max(violations))

            mean_revenue = np.average(revenues)
            mean_violation = np.average(violations)
            confidence_low_revenue, confidence_high_revenue = bootstrap(revenues, 1000, 0.95, average)
            f.write(str(confidence_low_revenue)+" ")
            f.write(str(mean_revenue)+" ")
            f.write(str(confidence_high_revenue)+" ")
            f.write(str(mean_violation)+"\n")
        f.close()

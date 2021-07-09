import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import rcParams

N_episode = 200

if __name__ == '__main__':
    x = []
    for i in range(N_episode):
        x.append(i)
    revenue_high = []
    revenue_mean = []
    revenue_low = []
    violation_mean = []
    with open("result", "r") as f:
        for i in range(N_episode):
            revenues = []
            revenues_str = f.readline()
            revenues_str = revenues_str.split(" ")
            for revenue in revenues_str:
                revenues.append(float(revenue))
            revenue_low.append(revenues[0])
            revenue_mean.append(revenues[1])
            revenue_high.append(revenues[2])
            violation_mean.append(revenues[3])
        f.close()

    print(revenue_low)
    print(revenue_mean)
    print(revenue_high)
    print(violation_mean)

    fig, ax1 = plt.subplots(figsize=(5.5, 4))
    fig1 = ax1.get_figure()

    ax2 = ax1.twinx()
    ax1.set_xlabel("Episodes")
    ax1.set_ylabel("incomes($)")
    ax2.set_ylabel("fatigue driving ratio(%)")
    ax2.set_yticks([0.67, 1, 2, 3, 4, 5], [0.67, 1, 2, 3, 4, 5])
    ax2.set_ylim((0, 5.2))
    ax1.plot(x, revenue_mean, color="purple", label="average income")
    ax1.fill_between(x, revenue_low, revenue_high, alpha=0.4, color="purple", label="95% CI of income")
    ax2.plot(x, np.array(violation_mean)*100, color="orange", label="fatigue driving ratio")
    fig.legend(bbox_to_anchor=(0.47, 0.1, 0.4, 0.6))
    #plt.text(210, 5.3, "(%)")
    plt.text(214, 0.6, "0.67")
    plt.tight_layout()
    plt.savefig("result.pdf")
    plt.show()


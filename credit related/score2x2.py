import matplotlib.pyplot as plt
import numpy
import random


def increase_diff_init():
    s_max = 100
    k = 0.01
    c = 6
    xs = [[0], [10], [20], [30], [40], [50], [60], [70], [80]]
    ys = [[0], [0], [0], [0], [0], [0], [0], [0], [0]]
    for j in range(9):
        x = xs[j]
        y = ys[j]
        for i in range(500):
            x.append(x[len(x) - 1] + k * c * numpy.log(s_max - x[len(x) - 1]))
            y.append(i + 1)
            print(x, y)

    plt.xlabel("Transaction Counts\n(a)")
    plt.ylabel("Driver Credits")

    plt.plot(ys[0], xs[0], color="red", label="init=0")
    plt.plot(ys[1], xs[1], color="blue", label="init=10")
    plt.plot(ys[2], xs[2], color="green", label="init=20")
    plt.plot(ys[3], xs[3], color="grey", label="init=30")
    plt.plot(ys[4], xs[4], color="orange", label="init=40")
    plt.plot(ys[5], xs[5], color="yellow", label="init=50")
    plt.plot(ys[6], xs[6], color="black", label="init=60")
    plt.plot(ys[7], xs[7], color="aqua", label="init=70")
    plt.plot(ys[8], xs[8], color="brown", label="init=80")

    plt.legend()


def decrease_diff_init():
    s_max = 100
    k = 0.5
    c = 6

    xs = [[0], [10], [20], [30], [40], [50], [60], [70], [80]]
    ys = [[0], [0], [0], [0], [0], [0], [0], [0], [0]]

    for j in range(9):
        x = xs[j]
        y = ys[j]
        for i in range(15):
            x.append(x[len(x) - 1] - k * c * numpy.log(s_max - x[len(x) - 1]))
            if x[len(x) - 1] < 0:
                x[len(x) - 1] = 0

            y.append(i + 1)
            print(x, y)

    plt.xlabel("Transaction Counts\n(b)")
    plt.ylabel("Driver Credits")

    plt.plot(ys[0], xs[0], color="red", label="init=0")
    plt.plot(ys[1], xs[1], color="blue", label="init=10")
    plt.plot(ys[2], xs[2], color="green", label="init=20")
    plt.plot(ys[3], xs[3], color="grey", label="init=30")
    plt.plot(ys[4], xs[4], color="orange", label="init=40")
    plt.plot(ys[5], xs[5], color="yellow", label="init=50")
    plt.plot(ys[6], xs[6], color="black", label="init=60")
    plt.plot(ys[7], xs[7], color="aqua", label="init=70")
    plt.plot(ys[8], xs[8], color="brown", label="init=80")

    plt.legend()

def rand_rate():
    s_max = 100
    k_in = 0.01
    k_de = 0.5

    xs = [[60], [60], [60], [60], [60], [60]]
    ys = [[0], [0], [0], [0], [0], [0]]
    for j in range(6):
        x = xs[j]
        y = ys[j]
        for i in range(10000):
            c = numpy.random.normal(6, 1.5, 1)[0]

            if numpy.random.choice(2, 1, p = [0.1, 0.9]) == 0:
                if random.randrange(0, 5) >= j:
                    x.append(x[len(x) - 1] + k_in * c * numpy.log(s_max - x[len(x) - 1]))
                else:
                    x.append(x[len(x) - 1] - k_de * c * numpy.log(s_max - x[len(x) - 1]))
                if x[len(x) - 1] < 0:
                    x[len(x) - 1] = 0
            else:
                x.append(x[len(x) - 1] + k_in * c * numpy.log(s_max - x[len(x) - 1]))

            y.append(i + 1)
            print(c, x[len(x) - 1])

    plt.xlabel("Transaction Counts\n(c)")
    plt.ylabel("Driver Credits")

    plt.plot(ys[0], xs[0], color="red", label="rate=0.0")
    plt.plot(ys[1], xs[1], color="blue", label="rate=0.2")
    plt.plot(ys[2], xs[2], color="green", label="rate=0.4")
    plt.plot(ys[3], xs[3], color="grey", label="rate=0.6")
    plt.plot(ys[4], xs[4], color="orange", label="rate=0.8")
    plt.plot(ys[5], xs[5], color="black", label="rate=1.0")

    plt.legend()

def unit_price():
    s_max = 100
    s_high = 70
    s_low = 60
    ks = [0.001, 0.002, 0.003, 0.004, 0.005]
    c = 6
    xs = [[], [], [], [], []]
    ys = [[], [], [], [], []]
    for j in range(5):
        k = ks[j]
        x = xs[j]
        y = ys[j]
        for i in range(100):
            if i < s_low:
                x.append(1 - k * (s_low - i))
                y.append(i)
            elif i > s_high:
                x.append(1 + k * (i - s_high))
                y.append(i)
            else:
                x.append(1)
                y.append(i)
            print(x, y)

    plt.xlabel("Driver Credits\n(d)")
    plt.ylabel("discount(penalty)")

    plt.plot(ys[0], xs[0], color="red", label="k=0.001")
    plt.plot(ys[1], xs[1], color="blue", label="k=0.002")
    plt.plot(ys[2], xs[2], color="green", label="k=0.003")
    plt.plot(ys[3], xs[3], color="grey", label="k=0.004")
    plt.plot(ys[4], xs[4], color="orange", label="k=0.005")

    plt.legend()


if __name__ == "__main__":
    plt.figure(figsize=(8, 6))

    plt.subplot(2, 2, 1)
    increase_diff_init()

    plt.subplot(2, 2, 2)
    decrease_diff_init()

    plt.subplot(2, 2, 3)
    rand_rate()

    plt.subplot(2, 2, 4)
    unit_price()

    plt.tight_layout()

    plt.savefig("images/score2x2.pdf")
    plt.show()

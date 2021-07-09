import numpy as np

if __name__ == '__main__':
    C = 60
    C_max = 100
    C_high = 70
    C_low = 60

    k_in = 0.01
    k_de = 0.5

    k_re = 0.002
    k_pu = 0.004

    p = 0.84
    mileage = 6

    i = 1

    result = [[], [], [], [], []]

    while True:
        C_pre = C
        result[0].append(i)
        result[1].append(C)
        m = p
        if C <= C_low:
            m = (1 - k_pu * (C_low - C)) * p
        result[2].append(m)
        revenue = m * mileage
        result[3].append(revenue)

        C_change = k_de * revenue * np.log(C_max - C)
        C = max(C - C_change, 0)
        C_change = C_pre - C

        result[4].append(-C_change)

        i += 1
        if C_pre == 0:
            break

    print(result)
    with open("result-fatigue", "w") as f:
        for i in range(len(result[0])):
            f.write(str(result[0][i]) + ", " +
                    str(round(result[1][i],2)) + ", " +
                    str(round(result[2][i],2)) + ", " +
                    str(round(result[3][i],2)) + ", " +
                    str(round(result[4][i],2)) + "\n")



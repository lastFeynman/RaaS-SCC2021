import numpy as np


distance = 6
p_sleepy = 0.1

m = price = 1
c = 60
c_high = 70
c_low = 60
c_max = 100

k_in = 0.01

k_re = 0.005
k_pu = 0.004

cost_per_mile = 0.3
total_revenue = []

if __name__ == "__main__":
    with open("./honest_kre_005", 'w') as f:
        for j in range(1000):
            total_revenue.append(0)
            c = 60
            for i in range(10000):
                sleepy = np.random.choice(2, 1, p=[1 - p_sleepy, p_sleepy])
                if sleepy == 0:
                    revenue = distance * (m - cost_per_mile)
                    total_revenue[j] += revenue
                    c += k_in * revenue * np.log(c_max - c)
                else:
                    continue

                if c >= c_high:
                    m = (1 + k_re * (c - c_high)) * price
                if c <= c_low:
                    m = (1 - k_pu * (c_low - c)) * price

            f.write(str(total_revenue[j]) + "\n")
            f.flush()
            print(total_revenue[j])

        average_revenue = np.average(total_revenue)
        f.write("average revenue:" + str(average_revenue))
        f.flush()
        f.close()
        print("average revenue:" + str(average_revenue))

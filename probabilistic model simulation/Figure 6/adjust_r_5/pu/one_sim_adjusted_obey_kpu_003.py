import numpy as np


distance = 6
p_sleepy = 0.1
p_obey = 0.7
p_detect = 0.888

m = price = 1
c = 60
c_high = 70
c_low = 60
c_max = 100

k_in = 0.01
k_de = 0.5

k_re = 0.002
k_pu = 0.003

cost_per_mile = 0.3
total_revenue = []
above_count = 0
def get_honest_average():
    with open("../../honest/pu/honest_kpu_003", "r") as f:
        for i in range(1000):
            f.readline()
        number = float(f.readline()[16:])
    return number


honest_average = get_honest_average()

epoch = 1000

r = 0.7

if __name__ == "__main__":
    with open("adjusted_obey_r_5_kpu_003", 'w') as f:
        for j in range(epoch):
            total_revenue.append(0)
            c = 60
            for i in range(10000):
                adjusted_p_obey = p_obey
                if price > m:
                    adjusted_p_obey = np.minimum(1, p_obey + np.float_power((price - m) / price, r))
                sleepy = np.random.choice(2, 1, p=[1 - p_sleepy, p_sleepy])
                if sleepy == 0:
                    revenue = distance * (m - cost_per_mile)
                    total_revenue[j] += revenue
                    c += k_in * revenue * np.log(c_max - c)
                else:
                    obey = np.random.choice(2, 1, p=[1 - adjusted_p_obey, adjusted_p_obey])
                    if obey == 1:
                        continue
                    else:
                        revenue = distance * (m - cost_per_mile)
                        total_revenue[j] += revenue
                        detect = np.random.choice(2, 1, p=[1 - p_detect, p_detect])
                        if detect == 0:
                            c += k_in * revenue * np.log(c_max - c)
                        else:
                            c -= k_de * revenue * np.log(c_max - c)
                            if c < 0:
                                c = 0

                if c >= c_high:
                    m = (1 + k_re * (c - c_high)) * price
                if c <= c_low:
                    m = (1 - k_pu * (c_low - c)) * price

            f.write(str(total_revenue[j]) + "\n")
            f.flush()
            print(total_revenue[j])
            if total_revenue[j] > honest_average:
                above_count += 1

        average_revenue = np.average(total_revenue)
        f.write("average revenue:" + str(average_revenue) + "\n")
        f.write("possibility:" + str(above_count/epoch))
        f.flush()
        f.close()
        print("average revenue:" + str(average_revenue))



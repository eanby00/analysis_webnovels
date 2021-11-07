def cal_avg(data_1, data_2, data_3, data_4, data_5):
    temp = []
    if data_2 != 0:
        temp.append((data_1 - data_2) / data_2)
    if data_3 != 0:
        temp.append((data_2 - data_3) / data_3)
    if data_4 != 0:
        temp.append((data_3 - data_4) / data_4)
    if data_5 != 0:
        temp.append((data_4 - data_5) / data_5)
    if len(temp) == 0:
        return 0
    else:
        return sum(temp) / len(temp)


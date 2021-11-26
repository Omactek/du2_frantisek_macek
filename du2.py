flow_average = []
sedm = 0
def average(): #funkce pocitajici aritmeticky prumer
    prumer = sum(flow_average)/len(flow_average)
    return prumer
flow = [1,2,3,4,5,6,7,8]
for i in range(2):
    flow_average = []
    try:
        for z in range (7):
            o = sum([flow[7*i+z]])
            flow_average.append(o)
            print(flow_average)
    except IndexError:
        pass
    y = average()
    print(y)

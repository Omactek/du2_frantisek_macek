import csv
list_average_flow = [] #přednastavení listu pro uchování průměrných průtoků
def average(flow_average): #funkce pocitajici aritmeticky prumer
    prumer = sum(flow_average)/len(flow_average)
    return prumer
flow_not_stripped = []
flow = []
def calc_average_flow(): #funkce vypočítá průměrný průtok za sedmidenní období
    for i in range(2):
        flow_average = []
        try:
            for z in range (7):
                o = sum([flow[7*i+z]])
                flow_average.append(o)
                print(flow_average)
        except IndexError:
            pass
        y = average(flow_average)
        list_average_flow.append(y)
    return list_average_flow
def get_list(load_list,col_num):
    for col in reader:
        load_list.append(col[col_num])
    return load_list


with open("test_data.csv", encoding = "UTF-8") as csvinfile:
    reader = csv.reader(csvinfile, delimiter = ",")
    for col in reader:
        flow.append(col[5]) #uloží do seznamu prutoky
    flow = list(map(str.strip,flow)) #prepise na hodnoty bez mezer !NENI MOZNA POTREBA!
    flow = list(map(float, flow)) #prevede na float
print(flow)
calc_average_flow()

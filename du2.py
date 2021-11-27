import csv

database_num = []
data_type = []
year = []
month = []
day = []
flow = []
list_average_flow = [] #přednastavení listu pro uchování průměrných průtoků

def average(flow_average): #funkce pocitajici aritmeticky prumer
    prumer = sum(flow_average)/len(flow_average)
    return prumer
def calc_average_flow(): #funkce vypočítá průměrný průtok za sedmidenní období
    for i in range(2):
        flow_average = []
        try:
            for z in range (7):
                o = sum([flow[7*i+z]])
                flow_average.append(o)
        except IndexError:
            pass
        y = average(flow_average)
        list_average_flow.append(y)
    return list_average_flow
def get_list(load_list,col_num): #funkce uklada do listu
    for col in reader:
        load_list.append(col[col_num])
    return load_list
def get_max():
    max_value = max(flow)
    min_value = min(flow)
    max_index = flow.index(max_value)
    min_index = flow.index(min_value)
    print("f{}")

with open("test_data.csv", encoding = "UTF-8") as csvinfile:
    reader = csv.reader(csvinfile, delimiter = ",")
    get_list(database_num,0)
    get_list(data_type,1)
    get_list(year,2)
    get_list(month,3)
    get_list(day,4)
    get_list(flow,5)
    flow = list(map(str.strip,flow)) #prepise na hodnoty bez mezer !NENI MOZNA POTREBA!
    flow = list(map(float, flow)) #prevede na float
print(database_num)
print(data_type)
print(year)
print(month)
print(day)
print(flow)


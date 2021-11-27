import csv

database_num = []
data_type = []
year = []
month = []
day = []
flow = []
list_average_flow = [] #přednastavení listu pro uchování průměrných průtoků
eve_list = []
unique_year = []
year_flow = []
pocet_radku = 0
temp_year = []

def average(flow_average): #funkce pocitajici aritmeticky prumer
    prumer = sum(flow_average)/len(flow_average)
    return prumer
#def calc_average_flow_year():
 #   while
def calc_average_flow_seven(): #funkce vypočítá průměrný průtok za sedmidenní období
    if len(flow) % 7 == 0:
        for i in range(len(flow)/7):
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
    else:
        for i in range((len(flow)//7)+1):
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
def get_list(load_list,col_num): #rozřadí všechna data do příslušných seznamů
    for i in range(pocet_radku):
        load_list.append(eve_list[i][col_num])
    return load_list
def print_max(): #zjistí a vypíše minimální a maximální průtok
    max_value = max(flow)
    min_value = min(flow)
    max_index = flow.index(max_value)
    min_index = flow.index(min_value)
    print(f"Největší průtok byl {max_value} dne {day[max_index]}. {month[max_index]}. {year[max_index]}")
    print(f"Nejmenší průtok byl {min_value} dne {day[min_index]}. {month[min_index]}. {year[min_index]}")

with open("test_data.csv", encoding = "UTF-8") as csvinfile:
    reader = csv.reader(csvinfile, delimiter = ",")
    for row in reader: #vytvoří seznam seznamů všech dat
        eve_list.append(row)
        pocet_radku += 1

#rozžazení dat do seznamů
flow = get_list(flow,5)
database_num = get_list(database_num,0)
data_type = get_list(data_type,1)
year = get_list(year,2)
month = get_list(month,3)
day = get_list(day,4)

flow = list(map(str.strip,flow)) #prepise na hodnoty bez mezer !NENI MOZNA POTREBA!
try:
    flow = list(map(float, flow)) #prevede na float
except ValueError:
    print("V průtocích chybí hodnota")
    quit()

calc_average_flow_seven()
print_max()

for i in year:
    if i not in unique_year:
        unique_year.append(i)
last = 0
for i in range(len(unique_year)):
    for z in range(last,len(year)):
        if year[z] == unique_year[i]:
            temp_year.append(flow[z])
        else:
            last = z
            break
    year_flow.append(average(temp_year))
print(year_flow)

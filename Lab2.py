def display_main_menu():
    print("Enter some numbers seperated by commas: ")

def calc_average():
    print("calc_average")

def get_user_input():
    x = input()
    list = x.split(",")
    for i in list:
        i = float(i)
    return list

def calc_average_temperature(temp_list):
    temp = 0
    for x in temp_list:
        temp += float(x)/len(temp_list)
    print("Average Temperature: "+ str(temp))
    return temp

def calc_min_max_temperature(temp_list):
    min_max = [float(temp_list[0]), float(temp_list[0])]
    for x in temp_list:
        y = float(x)
        if y<min_max[0]:
            min_max.insert(0,y)
        if y>min_max[1]:
            min_max.insert(1, y)
    print("Min temp: " + str(min_max[0]))
    print("Max temp: " + str(min_max[1]))
    return min_max

def calc_median_temperature(temp_list):
    temp_list.sort(key=float)
    print(temp_list)
    length = len(temp_list)
    if length % 2 == 0:
        x = int(length / 2)
        median = (float(temp_list[x - 1]) + float(temp_list[x])) / 2
    else:
        median = temp_list[int((length - 1) / 2)]
    print("Median: " + str(median))
    return median

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    calc_median_temperature(num_list)
    calc_average_temperature(num_list)
    calc_min_max_temperature(num_list)

if __name__ == "__main__":
    main()
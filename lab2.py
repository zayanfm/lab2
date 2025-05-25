def main(): 
    print("ET0735 (DEVOps for AIoT) - Lab 2 Introduction to Python Programming")
    display_main_menu()
    temp = get_user_input()
    print ("average is " + str(calc_average_temp(temp)))
    calc_min_max_temperature(temp)
    sort_temperature_list(temp)
    print ("median is " + str(calc_median_temp(temp)))

def display_main_menu(): 
    print("Enter some numbers separated by commas: ") 
    return 

def get_user_input(): 
    temp = input()
    temp = temp.split(",") 
    temp_list = list(map(float, temp)) 
    return temp_list

def calc_average_temp(templist): 
    avg_temp = sum(templist)/len(templist) 
    return avg_temp

def calc_min_max_temperature(templist):
    min_max_temp= [min(templist), max(templist)] 
    print("this is the [min,max]: ", min_max_temp)
    return min_max_temp

def sort_temperature_list(templist): 
    ascending_sorted=sorted(templist) 
    print("temperatures in ascending order: ", ascending_sorted)
    return ascending_sorted

def calc_median_temp(templist): 
    sorted_temps=sorted(templist) 
    n = len(sorted_temps) 
    mid = n//2

    if n%2==1: 
        return sorted_temps[mid] 
    else: 
        return (sorted_temps[mid - 1] + sorted_temps[mid]) / 2


if __name__ == "__main__":
    main()
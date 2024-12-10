def task_1():
    num_resistors = int(input("pls put number: "))
    total_resistance = 0 
    
    for i in range(num_resistors):
        resistance = float(input(f"enter rsistance {i + 1}: "))
        total_resistance += resistance

    print(f"Total resistance: {total_resistance}")
    return total_resistance

def task_2(cost):
    vat = cost * 0.2
    
    tip_percentage = -1
    while tip_percentage < 0:
	    tip_percentage = float(input("enter tip percentage (BIGGER THAN 0 PRETTY PLEASE ^_^): "))
    
    tip = (tip_percentage / 100) * cost
    total_cost = cost + tip + vat

    return total_cost

def task_3():
    result = []

    return result

def task_4():
    result = []

    return result

def task_5():
    height = None

    return 

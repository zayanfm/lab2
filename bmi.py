def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi= weight/(height**2)
    print("BMI = " + str(bmi))
    
    if (bmi < 18.5): 
        print("underweight") 
        return -1
    elif (bmi >= 18.5 and bmi <= 25.0): 
        print("normal weight") 
        return 0
    else: 
        print("overweight")
        return -1 

calculate_bmi(1.73, 57)



def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi= weight/(height**2)
    print("BMI = " + str(bmi))
    return bmi

def bmi_classification(bmi): 
    if (bmi < 18.5): 
        print("underweight") 
    elif (bmi >= 18.5 and bmi <= 25.0): 
        print("normal weight") 
    else: 
        print("overweight")

def check_bmi(): 
    height= 1.73
    weight= 57 
    bmi = calculate_bmi(height, weight) 
    bmi_classification(bmi) 

check_bmi()



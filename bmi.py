


def calculate_bmi(weight,height):
    print("Height = "+ str(height))
    print("Weight = "+ str(weight))
    bmi = weight/(height*height)
    print("Your BMI is " + str(bmi))

    if(bmi<18.5):
        print("You are underweight")
    elif(bmi>25.0):
        print("You are overweight")
    else:
        print("You are normal weight")

calculate_bmi(weight=79,height=1.78)
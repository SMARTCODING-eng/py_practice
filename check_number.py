def check_if_even():
    results = []
    for number in range(1, user_number+1):
        if number % 2 == 0:
            results.append(f"{number} Is and Even Number.")
        else:
            results.append(f"{number} Is an Odd Number.")
    return results

    

user_number = int(input("Enter your number range (5 upwards): "))
for result in check_if_even():
    print(result)
    
    

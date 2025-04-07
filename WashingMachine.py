import time
def get_clothes_list():
    clothes_input = input("Enter the clothes to Wash(seperated by commas)=")
    clothes_list = [c.strip() for c in clothes_input.split(",")]
    return clothes_list

def get_detergent_amount():
    detergent = float(input("Enter the detergent amount(in ml)="))
    return detergent

def get_washing_mode():
    print("-" * 30)
    print("select washing mode = ")
    print("1. Quick Wash")
    print("2. Normal Wash")
    print("3. Deep Wash ")

    mode = input("Enter mode number = ")
    print("-" * 30)

    if mode == "1":
        return "Quick Wash"
    elif mode == "2":
        return "Normal Wash"
    elif mode == "3":
        return "Deep Wash"
    else:
        print("Invalid mode selected , defaulting to normal wash.")
        return "Normal Wash" 
    

def simulate_washing(clothes,detergent,mode):
        print("washing process initiated")
        print(f"clothes to be washed:{clothes}")
        print(f"detergent amount:{detergent}ml")
        print(f"washing mode : {mode}")

        if mode == "Quick Wash":
            delay = 1
        elif mode == "Normal Wash":
            delay = 2
        else:
            delay = 3

        time.sleep(2)
        print("*" * 30)
        
        for progress in range(1,6):
            print(f"Washing......{progress * 20}% complete")
            time.sleep(delay)
        
        print("*" * 30)
        print("Washing Completed Successfully !!!  ")

def main ():
    clothes = get_clothes_list()
    detergent = get_detergent_amount()
    mode = get_washing_mode()
    simulate_washing(clothes,detergent,mode)

if __name__ == '__main__':
    main()

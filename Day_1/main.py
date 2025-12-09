def left_turn(number,amount):
    return (number-amount) % 100

def right_turn(number,amount):
    return (number+amount) % 100
"""
Output: 1154
"""
def main():
    test=False
    if test:
        filename="Day_1/test.txt"
    else:
        filename="Day_1/input.txt"
    in_file=open(filename,"r")
    password=0
    counter=50
    for line in in_file:
        direction, amount=line[0],int(line[1:])
        print(direction,amount)
        if direction=="L":
            counter=left_turn(int(counter),int(amount))
        else:
            counter=right_turn(int(counter),int(amount))
        print(f"Current Position: {counter}")
        if counter==0:
            password+=1
                

    print(password)

    
    pass

if __name__ == "__main__":
    main()
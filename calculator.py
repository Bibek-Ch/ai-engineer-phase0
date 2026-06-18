import sys

def main():
    
    if len(sys.argv) == 1:
        print(f"Usage: python calculator.py <operation> <num1> <num2>")
        return
    
    #if first argumen is --help show usage
    if sys.argv[1] == "--help":
        print(f"Usage: python calculator.py <operation> <num1> <num2>")
        print(f"operation: add, subract, multiply, divide")
        return
    
    #we expect 4 argume - script, operation, num1, num2
    if len(sys.argv) != 4:
        print(f"expected 3 argument: operation, num1, num2")


    operation = sys.argv[1]
    num1 = float(sys.argv[2])
    num2 = float(sys.argv[3])


    #calculate on the basis of operator

    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 == 0:
            print(f"dividing by 0 is mathamatically not possible")
            return
        result = num1/num2
    else:
        print(f"Invalid operation: {operation}")
        return
    
    print(result)
    return
    
if __name__ == "__main__":
    main()


# Program to check if a number is prime or not

num = int(input("Enter a number: "))

# To take input from the user
#num = int(input("Enter a number: "))

def Prime(num):
    """
    function will determine 
    if the number is a prime
    """
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                print(num, "is not a prime number")
                print(i,"times",num//i,"is",num)
                break
        else:
            print(num,"is a prime number")

    else:
        print(num,"is not a prime number")


if __name__ == "__main__":
    # only run the code below IF this script is invoked from the command-line
    # not if it is imported from another script
    print("HELLO")
    num = int(input("Enter a number: "))
    print(num, Prime(num))


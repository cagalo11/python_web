import sys

def ejemplo(num):
    if num == 5:
        print("correcto")
    else:
        print("el numero es diferente a 5")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num = int(sys.argv[1])
        ejemplo(num)
    else:
        print("Please provide a number as an argument.")

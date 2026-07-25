def collatzconjecture(num):
    if num == 1:
        return None
    if num % 2 == 0:
        num =num//2
    else:
        num = num*3+1
    print(num)
    return num

def main():
    num = int(input("Enter a number: "))
    print(num)
    i=1
    while num != None:
        num = collatzconjecture(num)
        i+=1
    print(f"Number of steps: {i}")

if __name__ == "__main__":
    main()
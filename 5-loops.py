def power_func0(num):
    for i in range(num):
        print(i*i)

def power_func1(num):
    i=1
    while i<=num:
        print(i*i)
        i=i+1
        
if __name__ == '__main__':
    n = int(input())
    power_func1(n)


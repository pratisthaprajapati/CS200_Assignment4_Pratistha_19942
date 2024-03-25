
def is_even(m,n):
    num= (6*m)+(8*n)
    return num%2==0

def is_odd(m,n):
    num1=(10*m*n) + 7
    return num1%2 !=0



def is_composite(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return True
    return False

def is_m2_minus_n2_composite(m, n):
    result = m**2 - n**2
    return is_composite(result)

m = int(input("Enter the value of m: "))
n = int(input("Enter the value of n: "))

print(f"Is 6m + 8n  even? : {is_even(m,n)}")
print(f"Is (10*m*n) + 7 odd? : {is_odd(m,n)}")    

if m > n > 0:
    if is_m2_minus_n2_composite(m, n):
        print("m^2 - n^2 is composite")
    else:
        print("m^2 - n^2 is not composite")
else:
    print("m should be greater than n and both should be greater than 0 for checking m^2 - n^2")



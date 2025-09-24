def get_gcd(num1: int, num2: int) -> int:

    while True:

        remainder = max(num1,num2) % min(num1,num2)

        if remainder == 0:
            num1 = min(num1,num2)
            break

        else:
            if (num1 > num2):
                num1 = remainder
                
            else:
                num2 = remainder

    return num1
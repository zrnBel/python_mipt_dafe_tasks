#def is_palindrome(num: int) -> bool:
#    num_reversed = 0
#    num_origin = num
# 
#    return num_origin == num_reversed
#
def is_palindrome(num: int) -> bool:
    
    if str(num)[::] == str(num)[::-1]:
        return True
    
    else:
        return False
    
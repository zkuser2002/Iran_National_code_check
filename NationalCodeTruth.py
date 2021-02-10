#insert your National Code
national_code=int(input('plase Enter your National Code: '))
    
# check digit of National Code
if (len(str(national_code))< 8 or len(str(national_code))> 10):
    national_code=int(input('plase Enter your National Code with 10 digit '))
    
# add digit if Code has 8 or 9 digit: some National code starts with '0' or '00'
def check_digit(national_code):
    check_digit=str(national_code)
    if len(check_digit)== 8:
        check_digit= '00'+check_digit
    elif len(check_digit)== 9:
        check_digit= '0'+check_digit
    else:
        check_digit
    return check_digit
# get remain of (reverse nine left index of National Code*National Code[item]) per 11
def remain(num):
    num= check_digit(num)
    summ=0
    index=0
    while index <= len(num)-1:
        for i in [10,9,8,7,6,5,4,3,2]:
            summ +=( i* (int(num[index])))
            index +=1
            i +=1
        remaining=summ%11
        return remaining
# Check the correctness of the national code 
def check_code(national_code):
    num = check_digit(national_code)
    num_remain= remain(national_code)
    numb= (int(num[-1]))
    if (11-num_remain == numb) :
            return 'Your National Code is Right'
    elif (num_remain < 2 and num_remain ==numb):
        return 'Your National Code is Right'
    else:
        return 'Your National Code is False'
        
print(check_code(national_code))


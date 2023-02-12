#This code adds, subtracts, multiply and divide the numbers you enter.
def sign():
    num1=input("Enter your first number?:")
    num2=input("Enter your second number?:")
    numbers=[float(num1), float(num2)]
    print(type(numbers))
    return numbers

def calc(nums):
    print(nums[0])
    print(nums[1])
    addition=float(nums[0])+float(nums[1])
    print(addition)
    print(str(nums[0])+"+"+str(nums[1])+"="+str(addition))
    sub=float(nums[0])-float(nums[1])
    print(sub)
    print(str(nums[0])+"-"+str(nums[1])+"="+str(sub))
    multi=float(nums[0])*float(nums[1])
    print(multi)
    print(str(nums[0])+"*"+str(nums[1])+"="+str(multi))
    div=float(nums[0])/float(nums[1])
    print(div)
    print(str(nums[0])+"/"+str(nums[1])+"="+str(div))
    power=float(nums[0])**float(nums[1])
    print(power)
    print(str(nums[0])+"^"+str(nums[1])+"="+str(power))






try:
    numbers=sign()
    calc(numbers)
except ValueError as i:
    print(i)
    print("You need to enter a number or a decimal number")
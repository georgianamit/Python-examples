# taking a temp variable to store the result from reverseNumber() function
temp = 0
# defining the reverseNumber() recursive function
def reverseNumber(num):
    global temp
    if num == 0:
        return num
    else:
        temp = (temp * 10) + (num%10)
        reverseNumber(num//10)
    return temp

# Taking a number from user
num = int(input("Enter a number: "))
# initializing variable rnum to the return value of reverseNumber() function
rnum = reverseNumber(num)

# printing the reverse of the number
print("The reverse of the number",num,"is",rnum)
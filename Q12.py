

# Write a program, which will find all such numbers between 1000 and 3000 (both included)
# such that each digit of the number is an even number.The numbers obtained should be
# printed in a comma-separated sequence on a single line.

#

all_digits_even=[]
#print(bool(10%2))

def check_if_only_even_digits(number):
    search_values = ('1', '3', '5', '7', '9')
    x=str(number)
  #  print(x)
    for value in search_values:
        if  x.find(value)!= -1:
   #         print(value)
            return False
    return True

print(list(filter(check_if_only_even_digits,range(1000,3000))))


for num in range(1000,3000):


     if check_if_only_even_digits(num):
         # print(num)
         all_digits_even.append(num)

#print(all_digits_even)
""" x = 3
y = float(3)
print(x,y) """

""" 
values = [1,2.23,5,7,2,30,15]
print(values)
for i in values:
    print(i)

print(values[0])
print(values[6])
 """


""" x = "this is a thing"
y= x.split( )
z = y[0]
print(y)
print(z) 
 """






""" x = input("write something: ")

count_word = x.split( )
print(f"The total number of words is {len(count_word)}.") """






""" x = input("Adj")
y = input("Adj")
z = input("Food")

print("it was a")
print(x)
print("cold morning. I woke up to the")
print(y)
print("smell of")
print(z) """


""" day_of_week = input("what day is it? ")

if day_of_week == "Friday":
    print("correct")
else:
    print("incorrect") """




""" x = "test"
print(f"hello {x}") """





""" 
temp = 75
if temp > 68:
    print('warm')
elif temp == 68:
    print('perfect')
else:
    print('cold') """



""" number = int(input('Pick any number : '))
if number % 2==0:
    print ('this number is EVEN')
else:
    print ('This number is ODD') """


""" 
Price = float(input("Price:"))
tip = input("how was the service(bad)(okay)(good)(great):")
if tip == "bad":
    print(Price) 
if tip == "okay":
    Price = round(Price * 1.15)
    print(f"Pay: {Price}")
if tip == "good":
    Price = round(Price * 1.20)
    print(f"Pay: {Price}")
if tip == "great":
    Price = round(Price * 1.25)
    print(f"Pay: {Price}")  """





""" 
number1 = int(input("input a number: "))
def find_Factors(number1):
    Factors = []
    for i in range(1, number1 + 1):
            if number1 % i == 0:
                Factors.append(i)
    return Factors

Factors = find_Factors(number1)
print(Factors) """


""" 

number1 = int(input("Input a number: "))
number2 = int(input("Input another number: "))

def find_Factors(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

factors1 = find_Factors(number1)
factors2 = find_Factors(number2)

common_factors = set(factors1) & set(factors2)

GCF = max(common_factors)

print(f"The GCF of {number1} and {number2} is {GCF}.") """






            

       





    










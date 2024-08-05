"""  def example(a, b, c, d):
	return int(a * b + c / d) if a != b else "ït's not working"
a=int(input(f"paste a: "))		
b=int(input(f"paste b: "))
c=int(input(f"paste c: "))
d=int(input(f"paste d: "))

print(f"your result is : {example(a, b, c, d)}")

def example_2(a:int, b:int, c=True, ) -> int:
    return a*b if c==True else a/b 
a=2
b=3
print(f"your result is : {example_2(a,b)}") 



def my_function(*args):
    if args:
        first, second, *rest = args
        print("First argument:", first, second)
        print("Rest arguments:", rest)
    else:
        print("No arguments were passed")

my_function(1, 2, 3, 4)  
# Выведет:
# First argument: 1
# Rest arguments: [2, 3, 4]

my_function()  
# Выведет:
# No arguments were passed

 
 
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3))  # Выведет: 6
print(sum_all(4, 5, 6, 7))  # Выведет: 22

  """
""" def my_function(a, b, *args):
    print("a:", a)
    print("b:", b)
    print("args:", args)

my_function(1, "cool", "dex", 212, "good")   """

""" 
def new_func(a,b,c,*args):
    print("a:", a)
    print("b:", b)
    print("c:", c)
    print("args:", args)
new_func(3,2,5,4,7,8,9,2) """
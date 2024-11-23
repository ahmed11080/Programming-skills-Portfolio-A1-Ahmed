def OddorEven(number):
    if number % 2 == 0:
        print( "even" )
    else:
        print( "odd" )
     
def main():
    number = int(input("Enter a number: "))
    OddorEven(number)

main()

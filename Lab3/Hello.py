x= int(input("Enter a number of repetitions"))

# Write your decorator here
def announce(f):
    def wrapper():
        for _ in range(x):
            f()
    return wrapper

@announce
def hello():
       print ('Hello')

hello()

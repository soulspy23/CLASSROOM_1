#29th June 2022
#parameter -> passing the value
#arguments -> receiving the value / parameter with no value

def my_function(country = "Norway"):
    print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()

#if you don't give default values it will give error of positional argument
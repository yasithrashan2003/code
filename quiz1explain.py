var1=1 # Globle variable


def function():
    global var2 
    var2=2
    print(f"from func var 1 {var1}")
    print(f"from func var 2 {var2}")

function()

print(var1)
print(var2)
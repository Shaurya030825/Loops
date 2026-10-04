print("====Power Calculaor====")

base= int(input("Please enter the base:"))
exponent= int(input("Please enter the power(exponent):"))

result= 1
for i in range(1, exponent+1):
    result= result * base
    print("Step",i, ":result=", result)

print("\n Answer=",base, "to the power:", exponent, "=", result)
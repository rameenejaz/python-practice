import sys
if len(sys.argv)!=3:
    print("usage: python add.py num1 num2")
else:
    num1,num2=float(sys.argv[1]),float(sys.argv[2])
    print(f"Sum:{num1+num2}")
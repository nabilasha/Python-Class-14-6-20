math=int(input("enter your math marks:\n"))
print(f' you etered {math}')
phy=int(input("enter your phy marks:\n"))
print(f' you entered {phy}')
chem=int(input("enter your chem marks:\n"))
print(f' you enterd{chem}')
average=(math+phy+chem)/3
print(average)
if average>90:
    print("your fee is exempted")
else:
    print("your fee is not exempted")

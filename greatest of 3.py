txt = []
for i in range (3):
    s = int(input("Enter number {i+1}: "))
    txt.append(s)
if txt[0]>txt[1] and txt[0]>txt[2]:
    print("the greater number is ",txt[0])
elif txt[1] > txt[0] and txt[1] > txt[2]:
    print("the greater number is ", txt[1])
elif txt[2]>txt[1] and txt[2]>txt[0]:
    print("the greater number is ",txt[0])
print("The list of numbers is:", txt)

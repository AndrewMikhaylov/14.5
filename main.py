import math
def checker(number, name):
    flag = True
    try:
        int(number)
    except ValueError:
        flag = False
    assert flag == True,  name + "має бути числом"
    if(name =="a"):
        assert int(a) != 0, "а має не дорівнювати нулю"

def solve(a, b, c):
    listWithAnswers = []
    d = b** -4*a*c
    firstX = (-b+math.sqrt(d))/2*a
    listWithAnswers.append(firstX)
    secondX = (-b-math.sqrt(d))/2*a
    listWithAnswers.append(secondX)
    for i in listWithAnswers:
        print(str(i))

print("Введіть а")
a=input()
checker(a, "a")

print("Введіть b")
b=input()
checker(b, "b")

print("Введіть с")
c=input()
checker(c, "c")

solve(int(a), int(b), int(c))
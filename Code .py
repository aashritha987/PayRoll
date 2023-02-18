_list = [0,0,0,0,0,0,0]
total,Sum,extra,hours = 0,0,0,0
print("Enter the number of Hours you have worked on each day (Starting From Sunday):")
for x in range(7):
    _list[x] =int(input())
    if (_list[x]>24):
        print("wrong entry,Pls re-enter the value")
        _list[x] =int(input())
    else :
        pass
print("Your Number of Working Hours on each day in this week is:",end='')
print(_list)
for x in range(1,6):
        Sum += _list[x]
        if (_list[x] > 8 ):
            hours = ((_list[x]) - 8)* 2.0  
            total += hours + 8 
        elif(_list[x] <= 8):
            total += _list[x] * 1.0           
if (Sum > 30):   
    Sum = Sum -30
    extra = Sum * 1.5
for x in range(0,7,6):
    if (_list[x] >= 0 ):
        total += _list[x] * 2.0
total = total + extra
print("The total salary of this week is",total)

#solution goes here
#user input
year = int(input("Enter the 4 digit year: "))
m = int(input("Enter the month as an integer: "))
d = int(input("Enter the day as an integer: "))
y = year
if m== 1 or m==2:
    y-=1
p = str(y)[2:4]
q = str(y)[0:2]
p = int(p)
q = int(q)
r = (((m+9)%12)+1)
s = ((13*r)-1)/5
t = p//4
u = q//4
v = round(d+p+s+t+u+(5*q))
w = v% 7
if w ==  0:
    day = "Sunday"
elif w == 1:
    day = "Monday"
elif w ==2:
    day = "Tuesday"
elif w ==3:
    day = "Wednesday"
elif w ==4:
    day = "Thursday"
elif w ==5:
    day = "Friday"
else:
    day = "Saturday"
if m == 1:
    month = "January"
elif m == 2:
    month = "February"
elif m == 3:
    month = "March"
elif m == 4:
    month = "April"
elif m == 5:
    month = "May"
elif m == 6:
    month = "June"
elif m == 7:
    month = "July"
elif m == 8:
    month = "August"
elif m == 9:
    month = "September"
elif m == 10:
    month = "October"
elif m == 11:
    month = "November"
else:
    month = "December"
print ("{} {}, {} is a {}".format(month, d, year, day))

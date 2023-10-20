salary=int(input("Enter Your Salary:"))
sevenpercent=(7/100)*salary
fivepercent=(5/100)*salary

if salary>=30000:
    print("Total salary is ",salary)
    print("Your Salary deduct 7% ",sevenpercent)
    salaryleft=salary-sevenpercent
    print("Net salary is ",salaryleft)
elif salary>=20000 and salary<30000:
    print("Total salary is ",salary)
    print("Your Salary deduct 5% ",fivepercent)
    salaryleft=salary-fivepercent
    print("Net salary is ",salaryleft)
else:
    print("your Salary is ",salary," no deduciton")
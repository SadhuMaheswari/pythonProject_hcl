from hcl_basic import salary
basic=float(input("Enter the basic salary: "))
hra=float(input("Enter the hr percentage:"))
da=float(input("Enter the da percentage:"))

net_salary = mh.cal_salary(basic,hra,da)
print(net_salary)

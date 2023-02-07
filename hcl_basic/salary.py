'''
basic_salary=float(input("Enter the basic salary: "))
HP=float(input("Enter the HRA percentage:"))
DAP=float(input("Enter the DA percentage:"))

HRA= (basic_salary * HP)/100
DA = (basic_salary * DAP)/100

net_salary = basic_salary + HRA + DA
print(net_salary)
'''

def cal_salary(basic,hra,da):
    net_salary = basic+(basic*hra)/100+(basic*da)/100
    return net_salary

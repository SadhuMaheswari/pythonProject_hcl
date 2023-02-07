def no_of_days(month):
    days= 0
    if month == 2:
        return '28 days'
    elif month in [1,3,5,7,8,10,12]:
        return '31 days'
    else:
        return '30 days'

#print(no_of_days(12))

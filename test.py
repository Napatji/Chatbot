from datetime import datetime
from openModel import thumnaii as th    
def compareDate(day,month,year):
    d = day
    m = month
    y = year
    date_format = "%m/%d/%Y"
    a = datetime.strptime('11/10/2021', date_format)
    b = datetime.strptime(f'{m}/{d}/{y}', date_format)
    delta = b - a
    return delta.days # that's it

index = 80 + compareDate(12,12,2021)
print(index)

print(int(th(108,0,9)))
from datetime import datetime
def compareDate():
    date_format = "%m/%d/%Y"
    a = datetime.strptime('11/10/2008', date_format)
    b = datetime.strptime('11/11/2008', date_format)
    delta = b - a
    print(delta.days) # that's it
    print(type(delta.days))
compareDate()
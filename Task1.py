from datetime import datetime

def get_days_from_today(date):
    date_as_date = datetime.strptime(date, '%Y-%m-%d')
    return  datetime.now().toordinal()-date_as_date.toordinal()


print(get_days_from_today('3001-09-08'))

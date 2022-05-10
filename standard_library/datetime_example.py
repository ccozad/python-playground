from datetime import datetime, timedelta

past_date = datetime(1830,4,6) # April 6, 1830
now = datetime.now()
print('\nA date in the past: {}'.format(past_date))
print('The date for today is {}'.format(now))
difference = now - past_date
print('April 30, 1830 is {} days in the past'.format(difference.days))

four_days = timedelta(days=4)
future_date = now + four_days
print('\nFour days from now is {}'.format(future_date.strftime('%A')))

print('\nThe ISO 8601 formatted time is {}'.format(now.isoformat()))

string_date = '2020-05-04T08:34:22'
parsed_date = datetime.fromisoformat(string_date)
print('\nWe can also parse dates and times')
print('The string {} parses out to'.format(string_date))
print('Year: {}, Month: {}, Day: {}, Hour: {}, Minute: {}, Seconds: {}'.format(
    parsed_date.year, 
    parsed_date.month, 
    parsed_date.day,
    parsed_date.hour,
    parsed_date.minute,
    parsed_date.second))

print('\nWe are not limited to ISO dates, we can also parse arbitrary formats')
custom_format_date = '09/21/2022'
parsed_custom_date = datetime.strptime(custom_format_date, '%m/%d/%Y')
print('The string {} parses out to'.format(custom_format_date))
print('Year: {}, Month: {}, Day: {}'.format(
    parsed_custom_date.year, 
    parsed_custom_date.month, 
    parsed_custom_date.day))
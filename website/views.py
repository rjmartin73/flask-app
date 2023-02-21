from flask import Blueprint, render_template, request
if __name__ != '__main__':
    from ._calendar import get_calendar_data
else:
    from _calendar import get_calendar_data
from datetime import date, datetime
from calendar import monthcalendar, month_name

_year: int = date.today().year
month_names = list(month_name[1:])

views = Blueprint('views', __name__)
# environment = jinja2.Environment()


@views.route('/')
def home():
    return render_template('home.html')


@views.route('/calendar', methods=['GET', 'POST'])
def calendar():
    try:
        year = dict(request.form)['year']
    except KeyError:
        year = _year
    # print(dict(request.form)['year'])
    return render_template('calendar.html',
                           months=get_calendar_data(int(year)),
                           year=year)


@views.route('/aicalendar')
def ai_calendar():
    # Get current date
    now = datetime.now()
    year = now.year
    month = now.month
    current_month = now.month
    current_day = now.day
    months = [monthcalendar(year, m) for m in range(1, 13)]
    # Render template with current year and months
    return render_template('aicalendar.html',
                           year=year,
                           month=month,
                           monthcalendar=months,
                           month_names=month_names,
                           current_month=current_month,
                           current_day=current_day)

from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import date
import requests


def main():
    url = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
    print(url)
    calculate_salary()
    get_employees()
    print(date.today())


if __name__ == '__main__':
    main()

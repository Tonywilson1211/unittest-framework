from datetime import date, timeedelta


class Student:
    """
    A student class as base for method testing
    created a student.py file  with a Student class which will form the  
    base of our tests. It has properties, sets values  automatically on creating 
    an instance of the class and has a method to return a student’s full name.
    """

    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
        self._start_date = date.today()
        self.end_date = date.today() + timedelta(days=365)
        self.naughty_list = False


@property
def full_name(self):
    return f"{self._first_name} {self._last_name}"

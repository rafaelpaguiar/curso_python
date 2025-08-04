class Employee:
    def __init__(self, first_name, last_name, yearly_income):
        self.first_name = first_name
        self.last_name = last_name
        self.yearly_income = yearly_income

    def give_raise(self, salary_raise=5000):
            self.yearly_income += salary_raise
            
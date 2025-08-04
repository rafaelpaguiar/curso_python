import pytest
from employee import Employee

@pytest.fixture
def new_employee():
    new_employee = Employee('Rafael', 'Aguiar', 120000)
    return new_employee

def test_give_default_raise(new_employee):
    new_employee.give_raise()
    assert new_employee.yearly_income == 125000

def test_give_custom_raise(new_employee):
    new_employee.give_raise(10000)
    assert new_employee.yearly_income == 130000
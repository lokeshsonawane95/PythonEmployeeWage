import pytest
from employee_wage import Employee, Company, MultipleCompanies


@pytest.fixture
def employee_object():
    return Employee({"employee_name": "Lokesh", "employee_wage": 20,
                     "maximum_working_hrs": 100, "maximum_working_days": 20})


@pytest.fixture
def company_object():
    return Company("Tata")


@pytest.fixture
def company_object():
    return Company("Tata")


@pytest.fixture
def multiple_companies_object():
    return MultipleCompanies()


# Test methods in Company class
def test_employee_dictionary_length(employee_object, company_object):

    # Testing employee_dictionary length
    assert len(company_object.employee_dict) == 0
    company_object.add_emp(employee_object)
    assert len(company_object.employee_dict) == 1


def test_if_employee_object_is_present_in_company_dictionary_or_not(employee_object, company_object):
    company_object.add_emp(employee_object)
    # Testing if employee object is in company dictionary or not
    assert employee_object == company_object.get_emp("Lokesh")


def test_delete_emp_method(employee_object, company_object):
    # Testing delete_emp method
    company_object.add_emp(employee_object)
    company_object.delete_emp("Lokesh")
    assert not company_object.get_emp("Lokesh")


def test_employee_wage_calculation_method(employee_object):
    employee_object.calc_wage()
    # Testing employee wage calculation variables are integer or not
    assert isinstance(employee_object.total_wage, int)
    assert isinstance(employee_object.total_emp_hrs, int)
    assert isinstance(employee_object.total_emp_days, int)


# Test methods in MultipleCompanies class
def test_length_of_company_dictionary(company_object, multiple_companies_object):
    # Testing company_dict dictionary length
    assert len(multiple_companies_object.company_dict) == 0
    multiple_companies_object.add_company(company_object)
    assert len(multiple_companies_object.company_dict) == 1


def test_whether_company_object_is_present_in_company_dictionary_or_not(company_object, multiple_companies_object):
    multiple_companies_object.add_company(company_object)
    # Testing whether company dictionary contains company object or not
    assert company_object == multiple_companies_object.get_company_object("Tata")


def test_remove_company_method(company_object, multiple_companies_object):
    multiple_companies_object.add_company(company_object)
    # Testing remove_company method
    multiple_companies_object.remove_company("Tata")
    assert not multiple_companies_object.get_company_object("Tata")

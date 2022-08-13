# Program to calculate Employee Wage
import logging
import random

logging.basicConfig(filename='EmployeeWage_logs.log', encoding='utf-8', level=logging.DEBUG)


class Employee:

    def __init__(self, employee_parameters_dict):
        self.total_wage = 0
        self.total_emp_hrs = 0
        self.total_emp_days = 0
        self.emp_name = employee_parameters_dict.get("employee_name")
        self.emp_wage = employee_parameters_dict.get("employee_wage")
        self.max_working_hrs = employee_parameters_dict.get("maximum_working_hrs")
        self.max_working_days = employee_parameters_dict.get("maximum_working_days")

    def calc_wage(self):
        """
        Function calculates wage of month
        :return: Employee Wage for the month
        """
        try:
            is_full_time = 1
            is_part_time = 2

            while self.total_emp_hrs < self.max_working_hrs and self.total_emp_days < self.max_working_days:

                emp_check = random.randrange(0, 3)
                if emp_check == is_full_time:
                    emp_hrs = 8
                    self.total_emp_days += 1
                elif emp_check == is_part_time:
                    emp_hrs = 4
                    self.total_emp_days += 1
                else:
                    emp_hrs = 0

                self.total_emp_hrs += emp_hrs
                self.total_wage += emp_hrs * self.emp_wage

        except Exception as e:
            print(e)
            logging.exception(e)


class Company:

    def __init__(self, company_name):
        self.company_name = company_name
        self.employee_dict = {}

    def add_emp(self, employee_object):
        """
        Function to add employee object to employee_dict dictionary
        :param employee_object:
        :return:
        """
        try:
            self.employee_dict.update({employee_object.emp_name: employee_object})
        except Exception as e:
            print(e)
            logging.exception(e)

    def get_emp(self, emp_name):
        """
        Function to get employee object
        :param emp_name: string
        :return: Employee object
        """
        return self.employee_dict.get(emp_name)

    def update_emp(self, employee_object, data_dict):
        """
        Function to update employee information in employee_dict dictionary
        :return:
        """
        try:
            employee_object.emp_wage = data_dict.get("update_wage")
            employee_object.max_working_hrs = data_dict.get("update_working_hours")
            employee_object.max_working_days = data_dict.get("update_working_days")

        except Exception as e:
            print(e)
            logging.exception(e)

    def delete_emp(self, emp_name):
        """
        Function deletes existing employee from the employee_dict dictionary
        :return:
        """
        try:
            self.employee_dict.pop(emp_name, "Employee not found")
        except Exception as e:
            print(e)
            logging.exception(e)

    def display_employees(self):
        """
        Function to display all employees
        :return: Employee information
        """
        for key, value in self.employee_dict.items():
            print("Employee Name : {}\nEmployee Wage : {}\nTotal Working hours : {}\nTotal working days : {}\n"
                  .format(value.emp_name, value.emp_wage, value.max_working_hrs, value.max_working_days))

    def display_employee_data(self, emp_name):
        """
        Function displays monthly wage, hours and days
        :return:
        """
        try:
            employee_object = self.get_emp(emp_name)
            if not employee_object:
                print("Employee not present")
            else:
                print("Total employee wage for the month : {}".format(employee_object.total_wage))
                print("Total days employee worked for the month : {}".format(employee_object.total_emp_days))
                print("Total hours employee worked for the month : {}".format(employee_object.total_emp_hrs))
        except Exception as e:
            print(e)
            logging.exception(e)


class MultipleCompanies:

    def __init__(self):
        self.company_dict = {}

    def add_company(self, company_object):
        """
        Function add company to company_dict dictionary
        :param company_object:
        """
        try:
            self.company_dict.update({company_object.company_name: company_object})
        except Exception as e:
            print(e)
            logging.exception(e)

    def get_company_object(self, company_name):
        return self.company_dict.get(company_name)

    def display_company(self):
        """
        Function to display company_dict dictionary
        """
        # print(self.company_dict.keys())
        # display values
        for company_name, company_object in self.company_dict.items():
            print(company_name)

    def remove_company(self, company_name):
        """
        Function to remove a company from company_dict dictionary
        :param company_name:
        """
        self.company_dict.pop(company_name, "Company not present")


def add_employee():
    """
    Function to add employee
    """
    # Taking input from user
    company_name = input("Enter company name : ")
    company_object = multiple_companies.get_company_object(company_name)
    if not company_object:
        company_object = Company(company_name)
        multiple_companies.add_company(company_object)

    employee_name = input("Enter employee name : ")
    if employee_name == "":
        print("Please enter employee name")
        return
    employee_wage = int(input("Enter employee wage per hour : "))
    maximum_working_hrs = int(input("Enter employee work hours : "))
    maximum_working_days = int(input("Enter employee working days : "))

    # using dictionary instead of passing multiple parameters
    emp_parameters = {"employee_name": employee_name, "employee_wage": employee_wage,
                      "maximum_working_hrs": maximum_working_hrs, "maximum_working_days": maximum_working_days}
    employee = Employee(emp_parameters)

    # calculating employee wage
    employee.calc_wage()

    # adding employee object in dictionary
    company_object.add_emp(employee)


def update_employee():
    """
    Function to update employee
    """
    comp_name_to_update = input("Enter company to update employee information : ")
    company_obj = multiple_companies.get_company_object(comp_name_to_update)
    employee_name = input("Enter employee name to update : ")
    emp_object = company_obj.get_emp(employee_name)
    if not emp_object:
        print("Employee not present")
    else:
        update_wage = int(input("Enter new wage to update : "))

        update_working_hours = int(input("Enter new working hours to update : "))

        update_working_days = int(input("Enter new working days to update : "))

        company_obj.update_emp(emp_object, {"update_wage": update_wage,
                                            "update_working_hours": update_working_hours,
                                            "update_working_days": update_working_days})


def display_employee():
    """
    Function to display specific employee information
    """
    # Display all employees
    company_name = input("Enter company to view employees : ")
    company_object = multiple_companies.get_company_object(company_name)
    company_object.display_employees()


def display_employee_wage():
    """
    Function to display employee wage information
    """
    # display monthly wage information
    company_name = input("Enter company to view employee wage information : ")
    company_object = multiple_companies.get_company_object(company_name)
    employee_name = input("Enter name of the employee you want the wage information of : ")
    company_object.display_employee_data(employee_name)


def delete_employee():
    """
    Function to delete specific employee from a specific company
    """
    # delete
    company_name = input("Enter company to delete employees : ")
    company_object = multiple_companies.get_company_object(company_name)
    employee_name = input("Enter employee name : ")
    company_object.delete_emp(employee_name)


def display_companies():
    """
    Function to display all companies
    """
    # Display company_dict dictionary
    multiple_companies.display_company()


def delete_company():
    """
    Function to remove a company from dictionary
    """
    # Delete a company
    company_name = input("Enter company name to delete : ")
    multiple_companies.remove_company(company_name)


if __name__ == "__main__":
    try:
        multiple_companies = MultipleCompanies()

        while True:
            choice = int(input("1. Add new employee\n2. Show all employees\n3. Show employee wage data\n"
                               "4. Update employee\n5. Delete employee\n6. Display all companies\n"
                               "7. Delete a company\n0. Exit\nEnter your choice : "))

            choice_dict = {1: add_employee, 2: display_employee, 3: display_employee_wage, 4: update_employee,
                           5: delete_employee, 6: display_companies, 7: delete_company}

            if choice == 0:
                break
            elif choice > 7:
                print("Enter correct choice")
            else:
                choice_dict.get(choice)()

    except Exception as err:
        print(err)
        logging.exception(err)

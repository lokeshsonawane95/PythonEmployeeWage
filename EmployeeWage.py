# Program to calculate Employee Wage
import logging
import random

logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)


class Employee:

    def __init__(self, emp_name, emp_wage=20, max_working_hrs=140, max_working_days=20):
        self.total_wage = 0
        self.total_emp_hrs = 0
        self.total_emp_days = 0
        self.emp_name = emp_name
        self.emp_wage = emp_wage
        self.max_working_hrs = max_working_hrs
        self.max_working_days = max_working_days

    def calc_wage(self):
        """
        Function calculates wage of month
        :return: Employee Wage for the month
        """
        try:
            is_full_time = 1
            is_part_time = 2

            while self.total_emp_hrs < self.max_working_hrs and self.total_emp_days < self.max_working_days:

                self.total_emp_days += 1
                emp_check = random.randrange(0, 3)
                if emp_check == is_full_time:
                    emp_hrs = 8
                elif emp_check == is_part_time:
                    emp_hrs = 4
                else:
                    emp_hrs = 0

                self.total_emp_hrs += emp_hrs
                self.total_wage += emp_hrs * self.emp_wage

        except Exception as e:
            print(e)
            logging.exception(e)


class Company:

    def __init__(self, company_name):
        self.name = company_name
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
        :param emp_name:
        :return: Employee object
        """
        return self.employee_dict.get(emp_name)

    def update_emp(self, emp_name):
        """
        Function to update employee information in employee_dict dictionary
        :return:
        """
        try:
            employee_object = self.get_emp(emp_name)
            if not employee_object:
                print("Employee not present")
            else:
                update_choice = int(input("1. Update Wage\n2. Update working hours\n3. Update working days\n"
                                          "Enter your choice : "))

                if update_choice == 1:
                    update_wage = int(input("Enter new wage to update : "))
                    employee_object.emp_wage = update_wage
                elif update_choice == 2:
                    update_working_hours = int(input("Enter new working hours to update : "))
                    employee_object.max_working_hrs = update_working_hours
                elif update_choice == 3:
                    update_working_days = int(input("Enter new working days to update : "))
                    employee_object.max_working_days = update_working_days

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


if __name__ == "__main__":
    try:
        company = Company("Tata")
        while True:
            choice = int(input("1. Add new employee\n2. Show all employees\n3. Show employee wage data\n"
                               "4. Update employee\n5. Delete employee\n0. Exit\nEnter your choice : "))

            if choice == 1:
                # Taking input from user
                employee_name = input("Enter employee name : ")
                if employee_name == "":
                    print("Please enter employee name")
                    continue
                employee_wage = int(input("Enter employee wage per hour : "))
                maximum_working_hrs = int(input("Enter employee work hours : "))
                maximum_working_days = int(input("Enter employee working days : "))
                employee = Employee(employee_name, employee_wage, maximum_working_hrs, maximum_working_days)

                # calculating employee wage
                employee.calc_wage()

                # adding employee object in dictionary
                company.add_emp(employee)
            elif choice == 2:
                # Display all employees
                company.display_employees()
            elif choice == 3:
                # display monthly wage information
                display_employee = input("Enter name of the employee you want the wage information of : ")
                company.display_employee_data(display_employee)
            elif choice == 4:
                # update
                update_input = input("Enter employee name to update : ")
                company.update_emp(update_input)
            elif choice == 5:
                # delete
                delete_name = input("Enter employee name : ")
                company.delete_emp(delete_name)
            elif choice == 0:
                break
            else:
                print("Please enter correct choice")
                continue

    except Exception as err:
        print(err)
        logging.exception(err)

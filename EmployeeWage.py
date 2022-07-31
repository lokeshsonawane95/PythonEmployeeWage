# Program to calculate Employee Wage
import random


class Employee:

    # class variable
    total_wage = 0

    def __init__(self, name, wage):
        self.name = name
        self.wage = wage

    def wage_for_month(self):
        """
        Function calculates wage of month
        :return: Employee Wage for the month
        """
        is_full_time = 1
        is_part_time = 2
        emp_rate_per_hour = self.wage
        num_of_working_days = 20

        # to calculate wage of the month
        for days in range(num_of_working_days):
            emp_check = random.randrange(0, 3)
            if emp_check == is_full_time:
                emp_hrs = 8
            elif emp_check == is_part_time:
                emp_hrs = 4
            else:
                emp_hrs = 0

            emp_wage = emp_hrs * emp_rate_per_hour
            self.total_wage += emp_wage

        # print("The months wage for {} is : {}".format(self.name, self.total_wage))


class Company:

    def __init__(self, name):
        self.name = name
        self.employee_dict = {}


if __name__ == "__main__":
    company1 = Company("Tata")
    emp1 = Employee("Lokesh", 25)
    emp2 = Employee("Loki", 26)
    emp1.wage_for_month()
    emp2.wage_for_month()

    # adding in dictionary of company1
    company1.employee_dict.update({emp1.name: emp1, emp2.name: emp2})

    # getting keys from dictionary of company1
    employee1 = company1.employee_dict.get("Lokesh")
    employee2 = company1.employee_dict.get("Loki")
    print("Company Name : {}".format(company1.name))
    print("Employee Name : {} , Employee wage for the month : {}".format(employee1.name, employee1.total_wage))
    print("Employee Name : {} , Employee wage for the month : {}".format(employee2.name, employee2.total_wage))
    print()
    company2 = Company("Mahindra")
    emp3 = Employee("Mahesh", 20)
    emp4 = Employee("Mack", 24)
    emp3.wage_for_month()
    emp4.wage_for_month()
    company2.employee_dict.update({emp3.name: emp3, emp4.name: emp4})
    Mahindra_emp1 = company2.employee_dict.get("Mahesh")
    Mahindra_emp2 = company2.employee_dict.get("Mack")
    print("Company Name : {}".format(company2.name))
    print("Employee Name : {} , Employee wage for the month : {}".format(Mahindra_emp1.name, Mahindra_emp1.total_wage))
    print("Employee Name : {} , Employee wage for the month : {}".format(Mahindra_emp2.name, Mahindra_emp2.total_wage))

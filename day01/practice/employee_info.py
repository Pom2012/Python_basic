"""
1. Create a python file named employee_info. declare the following variables:
                1. name
                2. age
                3. gender
                4. company
                5. jobTitle
                6. yearsOfExperience
                7. salary
                8. is_fullTime
                9. is_married
                10. employee_id
"""




class employee_info:

    def __init__(self, name: str = '', age: int = 0, gender: str = '', company: str = '',
                 job_title: str = '', yearsOfExperience: int = 0, salary: int = 0,
                 is_fullTime: bool = False,
                 is_married: bool = False, employee_id: int = 0):
        self.name = name
        self.age = age
        self.gender = gender
        self.company = company
        self.job_title = job_title
        self.yearsOfExperience: int = yearsOfExperience
        self.salary = salary
        self.is_fullTime = is_fullTime
        self.is_married = is_married
        self.employee_id = employee_id

employee1=employee_info('Tom')
print(employee1.name)



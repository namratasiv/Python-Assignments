# Namrata Sivakumar, 1001508168

# The Employee Class holds employee information - name, ID_number, dept, job_title.

class Employee:

    def __init__(self, name, ID_number, dept, job_title):
        self.__name = name
        self.__ID_number = ID_number
        self.__dept = dept
        self.__job_title = job_title
    
    def set_name(self, name):
        self.__name = name
    
    def set_id(self, ID_number):
        self.__ID_number = ID_number
    
    def set_dept(self, dept):
        self.__dept = dept
    
    def set_job_title(self, job_title):
        self.__job_title = job_title
    
    def get_name(self):
        return self.__name
    
    def get_id(self):
        return self.__ID_number
    
    def get_dept(self):
        return self.__dept
    
    def get_jobtitle(self):
        return self.__job_title
    
    def __str__(self):
        return "Name: " + self.__name + \
               "\nID Number: " + str(self.__ID_number) + \
               "\nDepartment: " + self.__dept + \
                "\nJob Title: " + self.__job_title
                    
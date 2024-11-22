class Person:
    def __init__(self, name, age):
        self.name = name  
        self.age = age    
    
    def display_info(self):
        """Kişinin bilgilerini görüntüler"""
        print(f"Ad: {self.name}, Yaş: {self.age}")
    


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  
        self.student_id = student_id  
    
    def display_info(self):
        """Öğrencinin bilgilerini görüntüler"""
        super().display_info()  
        print(f"Öğrenci No: {self.student_id}")


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age) 
        self.subject = subject  
    
    def display_info(self):
        """Öğretmenin bilgilerini görüntüler"""
        super().display_info() 
        print(f"Öğrettiği ders: {self.subject}")


if __name__ == "__main__":
    person = Person("Güney", 50)
    student = Student("Tarık", 20, "S12345")
    teacher = Teacher("Mehmet", 30, "Matematik")
    
    print("Person Bilgisi:")
    person.display_info()
    print("\nStudent Bilgisi:")
    student.display_info()
    print("\nTeacher Bilgisi:")
    teacher.display_info()
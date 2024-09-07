#!/usr/bin/env python
# coding: utf-8

# In[1]:


# CONSTRUCTOR


# In[3]:


#Q1. What is a constructor in Python? Explain its purpose and usage.

A constructor in Python is a special method used for initializing the object’s attributes. It is called 
automatically when a new object of a class is created. The constructor in Python is defined using the 
__init__ method.

Constructor is used for initializing an objects state and assign values to object attributes at the start.


# In[ ]:


#Q2. Differentiate between a parameterless constructor and a parameterized constructor in Python.

Parameterless Constructor: Does not take any arguments except self. It is used when you want to create objects 
without passing any parameters.

Parameterized Constructor: Takes parameters along with self. It is used to pass different values to object 
attributes when creating objects.


# In[4]:


#Q3. How do you define a constructor in a Python class? Provide an example.

class Student:
    def __init__(self, name):  # Constructor
        self.name = name

obj = Student("John")  # Creating an object
print(obj.name)  # Output: John


# In[ ]:


#Q4. Explain the __init__ method in Python and its role in constructors.

The __init__ method is the Python constructor used to initialize the object's attributes. It is automatically 
called when an object is created.

It sets the initial state of object and sends in values to attributes using self keyword.


# In[6]:


#Q5. In a class named Person, create a constructor that initializes the name and age attributes. 
# Provide an example of creating an object of this class.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person1 = Person("Alice", 30)  #An object of Person class is created
print(person1.name)  
print(person1.age)   


# In[7]:


#Q6. How can you call a constructor explicitly in Python? Give an example.

class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        # Explicitly calling the parent class's constructor
        super().__init__(name)
        self.age = age

# Creating an instance of ChildClass
child_instance = Child("Alice", 30)


# In[ ]:


#Q7. What is the significance of the self parameter in Python constructors? Explain with an example.

The self parameter represents the instance of the class. It helps us in creating instance attribute
and instance methods with ease that we can use any number of times. 

class MyClass:
    def __init__(self, name):
        self.name = name  # `self.name` is the instance variable acquiring the values from attributes.

obj = MyClass("John")
print(obj.name) 


# In[ ]:


#Q8. Discuss the concept of default constructors in Python. When are they used?

A default constructor in Python is a constructor that does not take any parameters other than self. It’s used 
when there is no need to pass parameters during object creation.


# In[9]:


#Q9. Create a Python class called Rectangle with a constructor that initializes the width and height attributes. 
# Provide a method to calculate the area of the rectangle.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height


rect = Rectangle(10, 5)  # Rectangle class object
print(rect.area())  


# In[11]:


#10.How can you have multiple constructors in a Python class? Explain with an example.

class Details:
    def __init__(self, name=None, age=None):
        if name and age:
            self.name = name
            self.age = age
        elif name:
            self.name = name
            self.age = "Unknown"
        else:
            self.name = "Anonymous"
            self.age = "Unknown"

# Different ways to create an object
obj1 = Details("John", 30)
obj2 = Details("Alice")
obj3 = Details()

print(obj1.name, obj1.age)  # Output: John 30
print(obj2.name, obj2.age)  # Output: Alice Unknown
print(obj3.name, obj3.age)  # Output: Anonymous Unknown


# In[ ]:


#Q11. What is method overloading, and how is it related to constructors in Python?

Method overloading refers to defining multiple methods with the same name but different parameters. Constructors 
can use this technique to handle different types of initializations.


# In[12]:


#Q12. Explain the use of the super() function in Python constructors. Provide an example.

The super() function is used to call a method from the parent class in a child class. 

class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Calls Parent constructor
        self.age = age

child = Child("John", 18)
print(child.name, child.age)  


# In[13]:


#Q13. Create a class called Book with a constructor that initializes the title, author, and published_year 
# attributes. Provide a method to display book details.

class Book:
    def __init__(self, title, author, published_year):
        self.title = title
        self.author = author
        self.published_year = published_year
    
    def display_details(self):
        print(f"Title: {self.title}, Author: {self.author}, Published Year: {self.published_year}")

book1 = Book("1984", "George Orwell", 1949)
book1.display_details()  # Output: Title: 1984, Author: George Orwell, Published Year: 1949


# In[14]:


#Q14. Discuss the differences between constructors and regular methods in Python classes.

Constructors if present are called automatically during object creation, while methods have to be called manually.
Constructors are used to set the initial state of an object while methods are used to define or modify action
or behavior of objects created from the class. 


# In[ ]:


#Q15. Explain the role of the self parameter in instance variable initialization within a constructor.

The "self" parameter allows the constructor to assign values to the instance variables (attributes) of the object. 
Without self, Python won’t know which instance’s attributes are being referred to.


# In[15]:


#Q16. How do you prevent a class from having multiple instances by using constructors in Python? 
# Provide an example.

We can use the Singleton design pattern to prevent multiple instances from being created. 

class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

# Creating objects
obj1 = Singleton()
obj2 = Singleton()

print(obj1 is obj2)  # Output: True (Both references point to the same object)


# In[21]:


#Q17. Create a Python class called Student with a constructor that takes a list of subjects as a parameter and 
# initializes the subjects attribute.

class Student:
    def __init__(self, subjects):
        self.subjects = subjects
    
    def display_subjects(self):
        print(f"Subjects : {self.subjects}")

student1 = Student(["Math", "Science", "History"])
student1.display_subjects()  


# In[22]:


#Q18. What is the purpose of the __del__ method in Python classes, and how does it relate to constructors?

The __del__ method is called a destructor which cleans up tasks before object destruction. Its the opposite of 
__init__ method which is used to initialize an object. 


# In[ ]:


#Q19. Explain the use of constructor chaining in Python. Provide a practical example.

Constructor chaining is when a child class’s constructor calls the parent class’s constructor, allowing
the parent class attributes and methods to be initialized within the child class. We can do constructor chaining
using the super() function. 


class Parent:
    def __init__(self, name):
        self.name = name
        print(f"Parent constructor: {self.name}")

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Calls Parent's constructor
        self.age = age
        print(f"Child constructor: {self.age}")

child = Child("John", 18)
# Output:
# Parent constructor: John
# Child constructor: 18


# In[23]:


#Q20. Create a Python class called Car with a default constructor that initializes the make and model attributes. 
# Provide a method to display car information.

class Car:
    def __init__(self):
        self.make = "Toyota"
        self.model = "Corolla"
    
    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}")

# Creating a Car object
car1 = Car()
car1.display_info()  # Output: Make: Toyota, Model: Corolla


# In[24]:


## INHERITANCE


# In[ ]:


#Q1. What is inheritance in Python? Explain its significance in object-oriented programming.

Inheritance is when one class (child class) gets properties and methods from another class (parent class). 
It lets us create a hierarchy of classes, where the child class can also have its own additional features. It also
helps in reusing codes and avoid redundancy. 


# In[25]:


#Q2. Differentiate between single inheritance and multiple inheritance in Python. Provide examples for each.

Single inheritance is when a class inherits from one parent class. Multiple inheritance is when a class inherits 
from more than one parent class. 
    
## Single inheritance example: 
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    pass

dog = Dog()
dog.speak()  # Inherits speak() from Animal


##Multiple inheritance example: 
class Parent1:
    def feature1(self):
        print("Feature 1")

class Parent2:
    def feature2(self):
        print("Feature 2")

class Child(Parent1, Parent2):
    pass

child = Child()
child.feature1()  # Inherits feature1 from Parent1
child.feature2()  # Inherits feature2 from Parent2


# In[26]:


#Q3. Create a Python class called Vehicle with attributes color and speed. Then, create a child class 
# called Car that inherits from Vehicle and adds a brand attribute. Provide an example of creating a Car object.

class Vehicle:
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed

class Car(Vehicle):
    def __init__(self, color, speed, brand):
        super().__init__(color, speed)
        self.brand = brand

car = Car("Red", 120, "Toyota")
print(f"Car brand: {car.brand}, Color: {car.color}, Speed: {car.speed}")


# In[27]:


#Q4. Explain the concept of method overriding in inheritance. Provide a practical example.

Method overriding is when a child class has a method with the same name as a method in the parent class, but the 
child class gives it a different behavior. The parent’s version is ignored when the child’s version is called.

class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        print("Bark")

dog = Dog()
dog.speak()  # Output: Bark (overrides Animal's speak method)


# In[ ]:


#Q5. How can we access the methods and attributes of a parent class from a child class in Python? Give an example.

We can access a parent class’s methods or attributes using the super() function or by calling the parent 
class directly.
    
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        super().greet()  # Calls Parent's greet method
        print("Hello from Child")

child = Child()
child.greet()


# In[ ]:


#Q6. Discuss the use of the super() function in Python inheritance. When and why is it used? Provide an example.

The super() function allows us to call methods from a parent class in the child class. We use it when we want to 
extend or modify a parent’s behavior without completely overriding it.

class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Calls Animal's constructor
        self.breed = breed

dog = Dog("Rex", "Labrador")
print(dog.name, dog.breed)


# In[28]:


#Q7. Create a Python class called Animal with a method speak(). Then, create child classes Dog and Cat that inherit
#  from Animal and override the speak() method. Provide an example of using these classes.

class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        print("Bark")

class Cat(Animal):
    def speak(self):
        print("Meow")

dog = Dog()
cat = Cat()

dog.speak()  # Output: Bark
cat.speak()  # Output: Meow


# In[ ]:


#Q8. Explain the role of the isinstance() function in Python and how it relates to inheritance.

The isinstance() function checks if an object is an instance of a particular class or a subclass. 
It’s useful in inheritance when we want to verify the type of object we’re dealing with.


# In[ ]:


#Q9. What is the purpose of the issubclass() function in Python? Provide an example.

The issubclass() function checks if a class is a subclass of another class. It helps confirm relationships
between classes.

class Animal:
    pass

class Dog(Animal):
    pass

print(issubclass(Dog, Animal))  # Output: True


# In[ ]:


#Q10. Discuss the concept of constructor inheritance in Python. How are constructors inherited in child classes?

Constructors in Python are not inherited automatically. If we don’t define a constructor in the child class, 
it will use the parent class’s constructor. But if the child class has its own constructor, we need to 
explicitly call the parent’s constructor using super() if we want to initialize the parent’s attributes.


# In[29]:


#Q11. Create a Python class called Shape with a method area() that calculates the area of a shape. Then, create 
# child classes Circle and Rectangle that inherit from Shape and implement the area() method accordingly. 
# Provide an example.

import math

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius**2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

circle = Circle(5)
rectangle = Rectangle(4, 6)

print(f"Circle area: {circle.area()}")
print(f"Rectangle area: {rectangle.area()}")


# In[ ]:


#Q12. Explain the use of abstract base classes (ABCs) in Python and how they relate to inheritance. 
# Provide an example using the abc module.

Abstract Base Classes (ABCs) in Python are classes that cannot be instantiated directly. They are meant to define 
methods that must be implemented by any child class that inherits from them. We use them when we want to ensure
that certain methods are always implemented in the child classes. 

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2

circle = Circle(5)
print(f"Circle area: {circle.area()}")


In this example, we cannot create an instance of Shape directly because it’s an abstract class. Only child 
classes that implement the area method can be instantiated.


# In[ ]:


#Q13. How can we prevent a child class from modifying certain attributes or methods inherited from a parent 
# class in Python?

To prevent a child class from modifying certain methods or attributes, we can define them as private by using a 
double underscore __ before their name. 


# In[30]:


#Q14. Create a Python class called Employee with attributes name and salary. Then, create a child class Manager 
# that inherits from Employee and adds an attribute department. Provide an example.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

manager = Manager("Alice", 50000, "IT")
print(f"Name: {manager.name}, Salary: {manager.salary}, Department: {manager.department}")


# In[ ]:


#Q15. Discuss the concept of method overloading in Python inheritance. How does it differ from method overriding?

Method overloading isn't supported in Python like in other languages. Instead, we handle it by using default 
arguments or varying the method’s behavior based on the input. 
Method overriding, on the other hand, is when a child class redefines a method inherited from a parent class.


# In[ ]:


#Q16. Explain the purpose of the __init__() method in Python inheritance and how it is utilized in child classes.

In inheritance, we use __init__() in the child class to initialize both the parent and child class attributes. 
We usually call the parent class’s __init__() using super() to ensure that the parent class's initialization
happens too.


# In[31]:


#Q17. Create a Python class called Bird with a method fly(). Then, create child classes Eagle and Sparrow that 
# inherit from Bird and implement the fly() method differently. Provide an example of using these classes.

class Bird:
    def fly(self):
        print("Bird is flying")

class Eagle(Bird):
    def fly(self):
        print("Eagle soars high")

class Sparrow(Bird):
    def fly(self):
        print("Sparrow flaps quickly")

eagle = Eagle()
sparrow = Sparrow()

eagle.fly()  # Output: Eagle soars high
sparrow.fly()  # Output: Sparrow flaps quickly


# In[32]:


#Q18. What is the "diamond problem" in multiple inheritance, and how does Python address it?

The "diamond problem" happens when a class inherits from two classes that both inherit from the same parent class.
This creates confusion about which version of a method or attribute the child class should inherit.

Python addresses it with Method Resolution Order (MRO) , which determines the order in which methods should be 
inherited when using multiple inheritance. 


# In[ ]:


#Q19. Discuss the concept of "is-a" and "has-a" relationships in inheritance, and provide examples of each.

In an "is-a" relationship, a class is a type of another class. For example, a Dog is an Animal. It is modeled 
using inheritance. 

#Example:
class Animal:
    pass

class Dog(Animal):
    pass  # Dog is an Animal


In a "has-a" relationship, one class contains or owns another class as part of its attributes. For example, 
a Car has an Engine. It is modeled using composition.

#Example: 
class Engine:
    pass

class Car:
    def __init__(self):
        self.engine = Engine()  # Car has an Engine


# In[33]:


#Q20. Create a Python class hierarchy for a university system. Start with a base class Person and create child 
# classes Student and Professor, each with their own attributes and methods. 
# Provide an example of using these classes in a university context.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self):
        print(f"{self.name} is studying")

class Professor(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def teach(self):
        print(f"{self.name} is teaching {self.subject}")

student = Student("John", 21, "S123")
professor = Professor("Dr. Smith", 45, "Physics")

student.study()  # Output: John is studying
professor.teach()  # Output: Dr. Smith is teaching Physics


# In[34]:


##ENCAPSULATION


# In[ ]:


#Q1. Explain the concept of encapsulation in Python. What is its role in object-oriented programming?

Encapsulation is about bundling the attributes (data) and methods into a single unit, which is the class. 
It’s crucial in OOP because it promotes data security and integrity.


# In[35]:


#Q2. Describe the key principles of encapsulation, including access control and data hiding.

Key principles of encapsulation are access control and data hiding. 

Access control determines which parts of the code can directly interact with certain attributes or methods. This 
is done through public, protected, and private access levels. 

Whereas, data hiding ensures that sensitive parts of the code are not exposed to the outside world 
and can only be interacted through controlled ways.


# In[ ]:


#Q3. How can we achieve encapsulation in Python classes? Provide an example.

In Python, we achieve encapsulation by using private attributes (with __ prefix) or protected attributes 
(with _ prefix) and providing public methods (getters and setters) to access or modify them.

class Person:
    def __init__(self, name, age):
        self.__name = name  # Private attribute
        self._age = age     # Protected attribute

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name


# In[ ]:


#Q4. Discuss the difference between public, private, and protected access modifiers in Python.

Public attributes/methods: Accessible from anywhere.
Private attributes/methods: Not accessible directly outside the class. 
Protected attributes/methods: Intended to be accessed only within the class and its subclasses. 


# In[36]:


#Q5. Create a Python class called Person with a private attribute __name. Provide methods to get and set the 
# name attribute.

class Person:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

person = Person("John")
print(person.get_name())  # Output: John
person.set_name("Jane")
print(person.get_name())  # Output: Jane


# In[37]:


#Q6. Explain the purpose of getter and setter methods in encapsulation. Provide examples.

Getter methods are used to access private or protected attributes, while setter methods are used to modify them.

class Employee:
    def __init__(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Invalid salary")


# In[ ]:


#Q7. What is name mangling in Python, and how does it affect encapsulation?

Name mangling is Python’s way of making private attributes less accessible outside the class by changing the 
name of the variable internally. If we define a private attribute with a __ prefix, Python alters its name 
to _ClassName__attribute. By doing this it helps in preventing accidental access or modification from outside
the class.


# In[38]:


#Q8. Create a Python class called BankAccount with private attributes for the account balance (__balance) 
# and account number (__account_number). Provide methods for depositing and withdrawing money.

class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid withdrawal amount")

    def get_balance(self):
        return self.__balance

account = BankAccount("123456789", 1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance())  # Output: 1300


# In[ ]:


#Q9. Discuss the advantages of encapsulation in terms of code maintainability and security.

We can modify the internal implementation of a class without affecting external code, as long as the getters 
and setters remain the same. Encapsulation helps in promoting security by hiding sensitive data from being 
accessed or modified directly, thus preventing accidental or malicious interference.


# In[ ]:


#Q10. How can we access private attributes in Python? Provide an example demonstrating the use of name mangling.

We can access using Python's name mangling convention. 

#Example:
class Example:
    def __init__(self):
        self.__private = "Secret"

obj = Example()
print(obj._Example__private)  # Output: Secret


# In[40]:


#Q11. Create a Python class hierarchy for a school system, including classes for students, teachers, and 
# courses, and implement encapsulation principles to protect sensitive information.

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.__student_id = student_id

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.__subject = subject

class Course:
    def __init__(self, course_name, teacher):
        self.course_name = course_name
        self.teacher = teacher


# In[ ]:


#Q12. Explain the concept of property decorators in Python and how they relate to encapsulation.

Property decorators allows us to define getter, setter, and deleter methods in a simple way. They make it easier 
to control access to attributes while using encapsulation principles.

#Example: 
class Circle:
    def __init__(self, radius):
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        if value > 0:
            self.__radius = value
        else:
            print("Invalid radius")


# In[ ]:


#Q13. What is data hiding, and why is it important in encapsulation? Provide examples.

Data hiding is where we restrict access to certain attributes or methods to prevent unintended interference. 
It ensures that critical data is protected and only accessed through a controlled way.

#Example: 
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance


# In[41]:


#Q14. Create a Python class called Employee with private attributes for salary (__salary) and employee ID 
# (__employee_id). Provide a method to calculate yearly bonuses.

class Employee:
    def __init__(self, salary, employee_id):
        self.__salary = salary
        self.__employee_id = employee_id

    def calculate_bonus(self):
        return self.__salary * 0.1

employee = Employee(50000, "E123")
print(employee.calculate_bonus())  # Output: 5000


# In[ ]:


#Q15. Discuss the use of accessors and mutators in encapsulation. How do they help maintain control over 
# attribute access?

Accessors (getters) allow us to retrieve the value of private attributes, while mutators (setters) allow us to 
modify them. They help maintain control by ensuring that only valid data is used to update the attributes, 
preventing errors.


# In[42]:


#Q16. What are the potential drawbacks or disadvantages of using encapsulation in Python?

Encapsulation is more of a convention than strict rules, so that means, attributes are not truly private, 
and they can still be accessed using name mangling. Additionally, using getters and setters can sometimes add 
unnecessary complexity to simple programs.


# In[43]:


#Q17. Create a Python class for a library system that encapsulates book information, including titles, authors, 
# and availability status.

class Book:
    def __init__(self, title, author, available=True):
        self.__title = title
        self.__author = author
        self.__available = available

    def get_info(self):
        return f"{self.__title} by {self.__author}, Available: {self.__available}"

    def check_out(self):
        if self.__available:
            self.__available = False
        else:
            print("Not available")

    def return_book(self):
        self.__available = True


# In[ ]:


#Q18. Explain how encapsulation enhances code reusability and modularity in Python programs.

Encapsulation enhances reusability by allowing us to design classes that bundle related data and methods together.
This makes it easier to maintain and update code since the internal details of a class are hidden and changes 
won’t break the external code that interacts with it.


# In[ ]:


#Q19. Describe the concept of information hiding in encapsulation. Why is it essential in software development?

Information hiding is the practice of restricting access to the internal details of a class. It’s essential
because it prevents unauthorized modifications to data. This leads to more secure and maintainable code.


# In[44]:


#Q20. Create a Python class called Customer with private attributes for customer details like name, address, and 
# contact information. Implement encapsulation to ensure data integrity and security.

class Customer:
    def __init__(self, name, address, contact):
        self.__name = name
        self.__address = address
        self.__contact = contact

    def get_details(self):
        return f"Name: {self.__name}, Address: {self.__address}, Contact: {self.__contact}"

    def update_address(self, new_address):
        self.__address = new_address

    def update_contact(self, new_contact):
        self.__contact = new_contact


# In[45]:


## POLYMORPHISM


# In[ ]:


#Q1. What is polymorphism in Python? Explain how it is related to object-oriented programming.

Polymorphism allows objects of different classes to be treated as objects of a common parent class. 
In OOP, polymorphism provides the ability for different classes to implement the same method in different ways. 
It allows us to write code that works with objects of various types, provided they share a common interface.


# In[ ]:


#Q2. Describe the difference between compile-time polymorphism and runtime polymorphism in Python.

Compile-time polymorphism: Happens when the method or operation is resolved during compilation. 

Runtime polymorphism: It is handled at runtime, allowing us to define methods in the parent class that can 
be overridden by child classes.


# In[46]:


#Q3. Create a Python class hierarchy for shapes (e.g., circle, square, triangle) and demonstrate polymorphism 
# through a common method, such as calculate_area().

import math

class Shape:
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius**2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side**2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

shapes = [Circle(5), Square(4), Triangle(3, 6)]
for shape in shapes:
    print(f"Area: {shape.calculate_area()}")


# In[ ]:


#Q4. Explain the concept of method overriding in polymorphism. Provide an example.

Method overriding occurs when a subclass provides a specific implementation of a method that is already defined in its parent class. 
This allows the subclass to change the behavior of the method.

#Example: 
class Animal:
    def speak(self):
        return "Animal makes a sound"

class Dog(Animal):
    def speak(self):
        return "Dog barks"

class Cat(Animal):
    def speak(self):
        return "Cat meows"

dog = Dog()
cat = Cat()
print(dog.speak())  # Output: Dog barks
print(cat.speak())  # Output: Cat meows


# In[ ]:


#Q5. How is polymorphism different from method overloading in Python? Provide examples for both.

Polymorphism: Different classes can have methods with the same name but different implementations. It's based 
on inheritance and method overriding.

#Example: 
class Bird:
    def fly(self):
        return "Bird is flying"

class Airplane:
    def fly(self):
        return "Airplane is flying"

for obj in [Bird(), Airplane()]:
    print(obj.fly())



Method overloading: Not natively supported in Python. Python uses default arguments or *args and **kwargs to 
handle multiple argument types.

#Example: 
class Math:
    def add(self, a, b=0, c=0):
        return a + b + c

math = Math()
print(math.add(5))      # Output: 5
print(math.add(5, 10))  # Output: 15
print(math.add(5, 10, 20))  # Output: 35


# In[47]:


#Q6. Create a Python class called Animal with a method speak(). Then, create child classes like Dog, Cat, and 
# Bird, each with their own speak() method. Demonstrate polymorphism by calling the speak() method on 
# objects of different subclasses.

class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"

class Bird(Animal):
    def speak(self):
        return "Tweet"

animals = [Dog(), Cat(), Bird()]
for animal in animals:
    print(animal.speak())


# In[48]:


#Q7. Discuss the use of abstract methods and classes in achieving polymorphism in Python. 
# Provide an example using the abc module.

Abstract methods and classes enforce that child classes must implement specific methods. This is achieved by 
using the abc (Abstract Base Classes) module.

#Example: 
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Bark"

class Cat(Animal):
    def speak(self):
        return "Meow"

dog = Dog()
cat = Cat()
print(dog.speak())  # Output: Bark
print(cat.speak())  # Output: Meow


# In[49]:


#Q8. Create a Python class hierarchy for a vehicle system (e.g., car, bicycle, boat) and implement a polymorphic 
# start() method that prints a message specific to each vehicle type.

class Vehicle:
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        return "Car engine starts"

class Bicycle(Vehicle):
    def start(self):
        return "Bicycle pedals start turning"

class Boat(Vehicle):
    def start(self):
        return "Boat engine starts"

vehicles = [Car(), Bicycle(), Boat()]
for vehicle in vehicles:
    print(vehicle.start())


# In[ ]:


#Q9. Explain the significance of the isinstance() and issubclass() functions in Python polymorphism.

isinstance(): Checks if an object is an instance of a specific class or its subclass.
issubclass(): Checks if a class is a subclass of another class.

class Animal:
    pass

class Dog(Animal):
    pass

dog = Dog()
print(isinstance(dog, Animal))  # True
print(issubclass(Dog, Animal))  # True


# In[ ]:


#Q10. What is the role of the @abstractmethod decorator in achieving polymorphism in Python? Provide an example.

The @abstractmethod decorator ensures that any subclass of an abstract class must implement the abstract method, 
enabling polymorphism by enforcing a common interface.

#Example: 
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        return "Car starts"

car = Car()
print(car.start())  # Output: Car starts


# In[50]:


#Q11. Create a Python class called Shape with a polymorphic method area() that calculates the area of 
# different shapes (e.g., circle, rectangle, triangle).

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

shapes = [Circle(5), Rectangle(4, 6)]
for shape in shapes:
    print(f"Area: {shape.area()}")


# In[ ]:


#Q12. Discuss the benefits of polymorphism in terms of code reusability and flexibility in Python programs.

Polymorphism improves code reusability by allowing methods in different classes to share the same interface. 
This makes the code more flexible because we can treat different objects with similar behaviors in the same way. 
It also simplifies maintaining the code, as changes in one class do not affect others.


# In[ ]:


#Q13. Explain the use of the super() function in Python polymorphism. How does it help call methods of 
# parent classes?

The super() function allows us to call methods from the parent class within a child class, ensuring we can 
extend or modify the behavior without completely overriding it.

class Animal:
    def speak(self):
        return "Animal makes a sound"

class Dog(Animal):
    def speak(self):
        parent_speak = super().speak()
        return f"Dog barks. {parent_speak}"

dog = Dog()
print(dog.speak())  # Output: Dog barks. Animal makes a sound


# In[51]:


#Q14. Create a Python class hierarchy for a banking system with various account types (e.g., savings, checking, 
# credit card) and demonstrate polymorphism by implementing a common withdraw() method.

class Account:
    def withdraw(self, amount):
        pass

class SavingsAccount(Account):
    def withdraw(self, amount):
        return f"Withdrawing {amount} from Savings Account"

class CheckingAccount(Account):
    def withdraw(self, amount):
        return f"Withdrawing {amount} from Checking Account"

accounts = [SavingsAccount(), CheckingAccount()]
for account in accounts:
    print(account.withdraw(100))


# In[ ]:


#Q15. Describe the concept of operator overloading in Python and how it relates to polymorphism. 
# Provide examples using operators like + and *.

Operator overloading defines how built-in operators behave for objects of a user-defined class. It is a type of 
polymorphism because operators work differently based on the objects they operate on.


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

point1 = Point(2, 3)
point2 = Point(4, 5)
result = point1 + point2
print(result.x, result.y)  # Output: 6 8


# In[ ]:


#Q16. What is dynamic polymorphism, and how is it achieved in Python?

Dynamic polymorphism is when a method call is resolved at runtime based on the object type. It is achieved 
through method overriding and inheritance in Python.


# In[52]:


#Q17. Create a Python class hierarchy for employees in a company (e.g., manager, developer, designer) and 
# implement polymorphism through a common calculate_salary() method.

class Employee:
    def calculate_salary(self):
        pass

class Manager(Employee):
    def calculate_salary(self):
        return "Manager salary calculated"

class Developer(Employee):
    def calculate_salary(self):
        return "Developer salary calculated"

employees = [Manager(), Developer()]
for employee in employees:
    print(employee.calculate_salary())


# In[ ]:


#Q18. Discuss the concept of function pointers and how they can be used to achieve polymorphism in Python.

In Python, we can treat functions as first-class objects, meaning they can be assigned to variables and passed 
as arguments. This flexibility allows for function-based polymorphism, where we can dynamically assign and 
call different functions.


# In[ ]:


#Q19. Explain the role of interfaces and abstract classes in polymorphism, drawing comparisons between them.

Abstract classes: Can have both concrete and abstract methods. Enforces polymorphism by requiring subclasses to implement abstract methods.
Interfaces: In Python, interfaces are typically defined through abstract classes, which enforce a common structure.


# In[53]:


#Q20. Create a Python class for a zoo simulation, demonstrating polymorphism with different animal types 
# (e.g., mammals, birds, reptiles) and their behavior (e.g., eating, sleeping, making sounds).

class Animal:
    def make_sound(self):
        pass

class Mammal(Animal):
    def make_sound(self):
        return "Mammal makes a sound"

class Bird(Animal):
    def make_sound(self):
        return "Bird chirps"

class Reptile(Animal):
    def make_sound(self):
        return "Reptile hisses"

animals = [Mammal(), Bird(), Reptile()]
for animal in animals:
    print(animal.make_sound())


# In[54]:


##ABSTRACTION


# In[ ]:


#Q1. What is abstraction in Python, and how does it relate to object-oriented programming?

Abstraction in Python is the process of hiding the complex details of an implementation and exposing only the 
necessary functionality. In OOP, abstraction helps in defining methods and attributes in a way that hides 
unnecessary details, allowing users to interact with objects at a higher level without worrying about their 
internal workings.


# In[ ]:


#Q2. Describe the benefits of abstraction in terms of code organization and complexity reduction.

Reducing code complexity.
Making code easier to maintain and extend.
Enhancing code organization by focusing on what needs to be done rather than how it is done.


# In[55]:


#Q3. Create a Python class called Shape with an abstract method calculate_area(). Then, create child classes 
# (e.g., Circle, Rectangle) that implement the calculate_area() method. Provide an example of using these classes.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

# Example usage:
circle = Circle(5)
rectangle = Rectangle(4, 6)
print(f"Circle area: {circle.calculate_area()}")
print(f"Rectangle area: {rectangle.calculate_area()}")


# In[ ]:


#Q4. Explain the concept of abstract classes in Python and how they are defined using the abc module. 
# Provide an example.

Abstract classes in Python serve as templates for other classes. They cannot be instantiated directly and 
contain one or more abstract methods, which must be implemented by subclasses. Abstract classes are defined 
using the abc (Abstract Base Classes) module.

#Example: 
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"


# In[ ]:


#Q5. How do abstract classes differ from regular classes in Python? Discuss their use cases.

Abstract classes: Cannot be instantiated directly and require subclasses to implement abstract methods.
Regular classes: Can be instantiated, and all methods are concrete (fully implemented).

Use case: Abstract classes are used when we want to define a general structure for child classes but leave 
specific implementations to the subclasses.


# In[56]:


#Q6. Create a Python class for a bank account and demonstrate abstraction by hiding the account balance and 
# providing methods to deposit and withdraw funds.

class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance

# Example usage:
account = BankAccount(100)
account.deposit(50)
account.withdraw(30)
print(f"Current balance: {account.get_balance()}")


# In[ ]:


#Q7. Discuss the concept of interface classes in Python and their role in achieving abstraction.

Interface classes define methods that must be implemented by any subclass but do not provide any method body. 
In Python, this can be simulated using abstract classes with all methods marked as abstract. They enforce a 
common structure and help in achieving abstraction by hiding implementation details.


# In[57]:


#Q8. Create a Python class hierarchy for animals and implement abstraction by defining common methods 
# (e.g., eat(), sleep()) in an abstract base class.

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def sleep(self):
        pass

class Lion(Animal):
    def eat(self):
        return "Lion eats meat"

    def sleep(self):
        return "Lion sleeps for 16 hours"

class Elephant(Animal):
    def eat(self):
        return "Elephant eats plants"

    def sleep(self):
        return "Elephant sleeps for 4 hours"

# Example usage:
lion = Lion()
elephant = Elephant()
print(lion.eat())
print(elephant.sleep())


# In[ ]:


#Q9. Explain the significance of encapsulation in achieving abstraction. Provide examples.

Encapsulation ensures that the internal state of an object is hidden from the outside world. It helps achieve 
abstraction by exposing only relevant parts of the object's functionality while hiding the implementation details.

#Example: 

class Car:
    def __init__(self, speed=0):
        self.__speed = speed  # Private attribute

    def accelerate(self, increment):
        self.__speed += increment

    def get_speed(self):
        return self.__speed

# Example usage:
car = Car()
car.accelerate(20)
print(car.get_speed())  # Output: 20


# In[ ]:


#Q10. What is the purpose of abstract methods, and how do they enforce abstraction in Python classes?

Abstract methods in Python are methods declared in an abstract class without any implementation. They enforce 
abstraction by requiring subclasses to provide their own implementations, ensuring a uniform interface across different classes.


# In[58]:


#Q11. Create a Python class for a vehicle system and demonstrate abstraction by defining common methods 
# (e.g., start(), stop()) in an abstract base class.

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        return "Car starts"

    def stop(self):
        return "Car stops"

class Bike(Vehicle):
    def start(self):
        return "Bike starts"

    def stop(self):
        return "Bike stops"

# Example usage:
car = Car()
bike = Bike()
print(car.start())
print(bike.stop())


# In[ ]:


#Q12. Describe the use of abstract properties in Python and how they can be employed in abstract classes.

Abstract properties in Python are declared using the @property decorator along with @abstractmethod. They 
enforce that subclasses must implement the property getter (and optionally the setter).


# In[59]:


#Q13. Create a Python class hierarchy for employees in a company (e.g., manager, developer, designer) and 
# implement abstraction by defining a common get_salary() method.

from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def get_salary(self):
        pass

class Manager(Employee):
    def get_salary(self):
        return 70000

class Developer(Employee):
    def get_salary(self):
        return 50000

# Example usage:
employees = [Manager(), Developer()]
for employee in employees:
    print(employee.get_salary())


# In[ ]:


#Q14. Discuss the differences between abstract classes and concrete classes in Python, including their instantiation.

Abstract classes: Cannot be instantiated directly and may contain abstract methods that must be implemented
by subclasses.
Concrete classes: Can be instantiated directly and contain fully implemented methods.


# In[ ]:


#Q15. Explain the concept of abstract data types (ADTs) and their role in achieving abstraction in Python.
Abstract Data Types (ADTs) define the behavior (operations) of data types without specifying their implementation. 
ADTs are achieved using classes and focus on what operations are possible, not how they are implemented.


# In[60]:


#Q16. Create a Python class for a computer system, demonstrating abstraction by defining common methods 
# (e.g., power_on(), shutdown()) in an abstract base class.

from abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod
    def power_on(self):
        pass

    @abstractmethod
    def shutdown(self):
        pass

class Laptop(Computer):
    def power_on(self):
        return "Laptop is powered on"

    def shutdown(self):
        return "Laptop is shutting down"

# Example usage:
laptop = Laptop()
print(laptop.power_on())


# In[ ]:


#Q17. Discuss the benefits of using abstraction in large-scale software development projects.

Abstraction simplifies complex systems by hiding details, allowing developers to work on smaller, manageable 
components. It improves code reusability, reduces redundancy, and makes collaboration across teams easier by 
focusing on high-level functionality.


# In[ ]:


#Q18. Explain how abstraction enhances code reusability and modularity in Python programs.

By abstracting common functionality, we can reuse the same abstract class or method across different classes. 
This makes the code more modular, as each component can be developed independently based on the abstract interface.


# In[61]:


#Q19. Create a Python class for a library system, implementing abstraction by defining common methods 
# (e.g., add_book(), borrow_book()) in an abstract base class.

from abc import ABC, abstractmethod

class Library(ABC):
    @abstractmethod
    def add_book(self, book):
        pass

    @abstractmethod
    def borrow_book(self, book):
        pass

class CityLibrary(Library):
    def add_book(self, book):
        return f"Book {book} added to the city library"

    def borrow_book(self, book):
        return f"Book {book} borrowed from the city library"

# Example usage:
library = CityLibrary()
print(library.add_book("Python Programming"))


# In[ ]:


#Q20. Describe the concept of method abstraction in Python and how it relates to polymorphism.

Method abstraction involves hiding the method's implementation and focusing on its signature and behavior. 
It relates to polymorphism because different classes can provide their own implementations of the same method 
signature, allowing for flexible and interchangeable object behavior.


# In[62]:


## COMPOSITION


# In[ ]:


#Q1. Explain the concept of composition in Python and how it is used to build complex objects from simpler ones.

Composition in Python is a design principle where one class contains an instance of another class to model a 
"has-a" relationship. This allows us to build complex objects by combining simpler objects as their components.


# In[ ]:


#Q2. Describe the difference between composition and inheritance in object-oriented programming.

Composition models a "has-a" relationship, where one object contains other objects as its components.
Inheritance models an "is-a" relationship, where a class inherits properties and behavior from a parent class. 


# In[63]:


#Q3. Create a Python class called Author with attributes for name and birthdate. Then, create a Book class that 
# contains an instance of Author as a composition. Provide an example of creating a Book object.

class Author:
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author  # Composition: Book "has an" Author

    def get_details(self):
        return f"'{self.title}' by {self.author.name}, born on {self.author.birthdate}"

# Example usage:
author = Author("George Orwell", "1903-06-25")
book = Book("1984", author)
print(book.get_details())


# In[ ]:


#Q4. Discuss the benefits of using composition over inheritance in Python, especially in terms of code 
# flexibility and reusability.

Composition provides more flexibility than inheritance because it allows for the independent replacement or 
modification of components without altering the main class structure. With composition, we can reuse different 
objects in multiple places and change their behaviors at runtime, whereas inheritance creates a tight dependency 
between the child and parent classes, making modifications less flexible.


# In[ ]:


#Q5. How can you implement composition in Python classes? Provide examples of using composition to create 
# complex objects.

We can implement composition by creating instances of one class inside another class.

#Example: 

class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

class Wheels:
    def __init__(self, count):
        self.count = count

class Car:
    def __init__(self, engine, wheels):
        self.engine = engine
        self.wheels = wheels

    def car_details(self):
        return f"Car with {self.engine.horsepower} HP and {self.wheels.count} wheels"

# Example usage:
engine = Engine(250)
wheels = Wheels(4)
car = Car(engine, wheels)
print(car.car_details())


# In[64]:


#Q6. Create a Python class hierarchy for a music player system, using composition to represent playlists and songs.

class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def show_playlist(self):
        return [f"{song.title} by {song.artist}" for song in self.songs]

# Example usage:
playlist = Playlist("Road Trip")
playlist.add_song(Song("Song A", "Artist 1"))
playlist.add_song(Song("Song B", "Artist 2"))
print(playlist.show_playlist())


# In[ ]:


#Q7. Explain the concept of "has-a" relationships in composition and how it helps design software systems.

In composition, a "has-a" relationship means that one class contains or is composed of instances of another class. 
This approach helps design flexible and modular software systems because it allows objects to contain other 
objects as components, which can be reused and swapped independently.


# In[65]:


#Q8. Create a Python class for a computer system, using composition to represent components like CPU, RAM, and 
# storage devices.

class CPU:
    def __init__(self, model):
        self.model = model

class RAM:
    def __init__(self, size):
        self.size = size

class Storage:
    def __init__(self, capacity):
        self.capacity = capacity

class Computer:
    def __init__(self, cpu, ram, storage):
        self.cpu = cpu
        self.ram = ram
        self.storage = storage

    def get_specs(self):
        return f"CPU: {self.cpu.model}, RAM: {self.ram.size}GB, Storage: {self.storage.capacity}GB"

# Example usage:
cpu = CPU("Intel i7")
ram = RAM(16)
storage = Storage(512)
computer = Computer(cpu, ram, storage)
print(computer.get_specs())


# In[ ]:


#Q9. Describe the concept of "delegation" in composition and how it simplifies the design of complex systems.

Delegation in composition means that an object passes tasks or responsibilities to another object. 
This simplifies the design of complex systems by allowing each object to focus on its specific task. 
For example, a Car object can delegate the task of starting to its Engine component.


# In[66]:


#Q10. Create a Python class for a car, using composition to represent components like the engine, wheels, 
# and transmission.

class Engine:
    def start(self):
        return "Engine starts"

class Wheels:
    def roll(self):
        return "Wheels are rolling"

class Transmission:
    def shift(self):
        return "Transmission shifts gears"

class Car:
    def __init__(self):
        self.engine = Engine()
        self.wheels = Wheels()
        self.transmission = Transmission()

    def drive(self):
        return f"{self.engine.start()}, {self.wheels.roll()}, {self.transmission.shift()}"

# Example usage:
car = Car()
print(car.drive())


# In[67]:


#Q11. How can you encapsulate and hide the details of composed objects in Python classes to maintain abstraction?

To encapsulate and hide details, we can mark composed objects as private by prefixing their names with double 
underscores (__). This prevents direct access to the composed objects, exposing only the necessary functionality 
through methods.


# In[68]:


#Q12. Create a Python class for a university course, using composition to represent students, instructors, 
# and course materials.

class Student:
    def __init__(self, name):
        self.name = name

class Instructor:
    def __init__(self, name):
        self.name = name

class CourseMaterial:
    def __init__(self, material):
        self.material = material

class Course:
    def __init__(self, title, instructor, students, materials):
        self.title = title
        self.instructor = instructor
        self.students = students
        self.materials = materials

    def get_course_info(self):
        return f"Course: {self.title}, Instructor: {self.instructor.name}, Students: {[student.name for student in self.students]}"

# Example usage:
instructor = Instructor("Prof. Smith")
students = [Student("Alice"), Student("Bob")]
materials = [CourseMaterial("Chapter 1"), CourseMaterial("Chapter 2")]
course = Course("Python Programming", instructor, students, materials)
print(course.get_course_info())


# In[ ]:


#Q13. Discuss the challenges and drawbacks of composition, such as increased complexity and potential for tight 
# coupling between objects.

Composition can increase complexity as it requires managing multiple objects and their interactions. Additionally,
tight coupling can occur if objects are too dependent on each other, making the system harder to modify and
test independently.


# In[69]:


#Q14. Create a Python class hierarchy for a restaurant system, using composition to represent menus, dishes, 
# and ingredients.

class Ingredient:
    def __init__(self, name):
        self.name = name

class Dish:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

class Menu:
    def __init__(self):
        self.dishes = []

    def add_dish(self, dish):
        self.dishes.append(dish)

    def show_menu(self):
        return [f"{dish.name} ({', '.join([ingredient.name for ingredient in dish.ingredients])})" for dish in self.dishes]

# Example usage:
menu = Menu()
menu.add_dish(Dish("Pasta", [Ingredient("Tomato"), Ingredient("Cheese")]))
print(menu.show_menu())


# In[ ]:


#Q15. Explain how composition enhances code maintainability and modularity in Python programs.

Composition enhances maintainability by separating responsibilities into individual objects. This modularity 
allows each component to be developed, tested, and modified independently without affecting other parts of the 
program, making the code more maintainable.


# In[71]:


#Q16. Create a Python class for a computer game character, using composition to represent attributes like 
# weapons, armor, and inventory.

class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

class Armor:
    def __init__(self, name, defense):
        self.name = name
        self.defense = defense

class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def list_items(self):
        return [item.name for item in self.items]

class Character:
    def __init__(self, name, weapon, armor):
        self.name = name
        self.weapon = weapon
        self.armor = armor
        self.inventory = Inventory()

    def get_character_info(self):
        return (f"Character: {self.name}, Weapon: {self.weapon.name} (Damage: {self.weapon.damage}), "
                f"Armor: {self.armor.name} (Defense: {self.armor.defense}), "
                f"Inventory: {', '.join(self.inventory.list_items())}")

# Example usage:
sword = Weapon("Sword", 50)
shield = Armor("Shield", 20)
character = Character("Knight", sword, shield)
character.inventory.add_item(Weapon("Potion", 0))
print(character.get_character_info())


# In[ ]:


#Q17. Describe the concept of "aggregation" in composition and how it differs from simple composition.

Aggregation is a type of composition where the contained object can exist independently of the container object. 
This means the lifecycle of the contained object is not tightly bound to the container. For example, a Department 
class might aggregate Employee objects, where Employees can exist outside the Department.

In simple composition, the contained object’s lifecycle is tightly coupled with the container. For example, a 
House class with Room objects typically means that if the House is destroyed, its Rooms are too.


# In[72]:


#Q18. Create a Python class for a house, using composition to represent rooms, furniture, and appliances.

class Room:
    def __init__(self, name):
        self.name = name

class Furniture:
    def __init__(self, item):
        self.item = item

class Appliance:
    def __init__(self, appliance):
        self.appliance = appliance

class House:
    def __init__(self):
        self.rooms = []
        self.furniture = []
        self.appliances = []

    def add_room(self, room):
        self.rooms.append(room)

    def add_furniture(self, furniture):
        self.furniture.append(furniture)

    def add_appliance(self, appliance):
        self.appliances.append(appliance)

    def get_house_details(self):
        return (f"Rooms: {', '.join([room.name for room in self.rooms])}, "
                f"Furniture: {', '.join([furniture.item for furniture in self.furniture])}, "
                f"Appliances: {', '.join([appliance.appliance for appliance in self.appliances])}")

# Example usage:
house = House()
house.add_room(Room("Living Room"))
house.add_furniture(Furniture("Sofa"))
house.add_appliance(Appliance("Fridge"))
print(house.get_house_details())


# In[ ]:


#Q19. How can you achieve flexibility in composed objects by allowing them to be replaced or modified 
# dynamically at runtime?

Flexibility can be achieved by allowing composed objects to be swapped out or modified dynamically. This can be 
done by defining components as variables and providing methods to update them.


# In[73]:


#Q20. Create a Python class for a social media application, using composition to represent users, posts, 
# and comments.

class User:
    def __init__(self, username):
        self.username = username

class Comment:
    def __init__(self, user, text):
        self.user = user
        self.text = text

class Post:
    def __init__(self, content):
        self.content = content
        self.comments = []

    def add_comment(self, comment):
        self.comments.append(comment)

    def get_post_details(self):
        return (f"Post: {self.content}, Comments: {', '.join([f'{comment.user.username}: {comment.text}' for comment in self.comments])}")

class SocialMediaApp:
    def __init__(self):
        self.users = []
        self.posts = []

    def add_user(self, user):
        self.users.append(user)

    def create_post(self, post):
        self.posts.append(post)

    def show_posts(self):
        return [post.get_post_details() for post in self.posts]

# Example usage:
app = SocialMediaApp()
user1 = User("alice")
user2 = User("bob")
post = Post("Hello World!")
post.add_comment(Comment(user1, "Nice post!"))
app.create_post(post)
print(app.show_posts())


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





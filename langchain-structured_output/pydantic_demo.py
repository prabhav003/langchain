from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name : str = 'Nitish'
    age : Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0,lt=10, default=5.0, description='A decimal value representing the cgpa of a student')

new_student = {'age':'32', 'email':'abc@gmail.com'}

student = Student(**new_student)

student_dict = dict(student)

print(student)
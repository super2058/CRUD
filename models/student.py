from typing import Optional
from pydantic import BaseModel, EmailStr, Field

class StudentSchema(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    course_of_study: str = Field(...)
    year: int = Field(..., gt=0, lt=9)
    gpa: float = Field(..., le=0.4)
    
    class Config:
        schema_extra = {
            "example" : {
                "fullname": "Ankit Hans",
                "email": "ankithans1947@gmail.com",
                "course_of_study": "Computer Science",
                "year": 2,
                "gpa": "3.0"
            }
        }
        
class UpdateSchema(BaseModel):
    fullname: Optional[str]
    email: Optional[EmailStr]
    course_of_study: Optional[str]
    year: Optional[int]
    gpa: Optional[float]
    
    class Config:
        schema_extra = {
            "example": {
                "fullname": "Ankit Hans",
                "email": "ankithans1947@gmail.com",
                "course_of_study": "Mechanical Engineering",
                "year": 3,
                "gpa": "4.0"
            }
        }

def ResponseModel(data, message):
    return {
        "data" : [data],
        "code" : 200,
        "message" : message
    }
    
def ErrorModel(error, code, message):
    return {
        "error" : error,
        "code" : code,
        "message" : message
    }
    
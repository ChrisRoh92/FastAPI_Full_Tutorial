from pydantic import BaseModel, Field, EmailStr
from typing import List
import datetime

########################################
## User 
########################################
class UserBaseSchema(BaseModel):
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)

class UserLoginSchema(UserBaseSchema):
    class Config: ## TODO(chrohne): check, if this actually works!
        schema_extra = {
            "user" : {
                "email": "max@mustermann.de",
                "password" : "mustermann"
            }
        }

class UserRegisterSchema(UserBaseSchema):
    fullname: str = Field(default=None)
    is_employee: bool = Field(default=None)
    class Config: ## TODO(chrohne): check, if this actually works!
        schema_extra = {
            "user" : {
                "fullname" : "max mustermann",
                "email": "max@mustermann.de",
                "password" : "mustermann",
                "is_employee": True
            }
        }

########################################
## Booking 
########################################
class BookingBaseSchema(BaseModel):
    from_date: datetime.date
    to_date: datetime.date
    isbn: str
    description: str

########################################
## Book
########################################
class BookBaseSchema(BaseModel):
    isbn: str
    title: str
    author: str
    class Config: ## TODO(chrohne): check, if this actually works!
        schema_extra  = {
            "example" : {
                "title" : "Mathematik für Ingenieure und Naturwissenschaftler Band 1: Ein Lehr- und Arbeitsbuch für das Grundstudium",
                "author": "Lothar Papula",
                "isbn" : "9783658217457"
            }
        }

class BookBaseListSchema(BaseModel):
    books: List[BookBaseSchema] = []
    class Config: ## TODO(chrohne): check, if this actually works!
        schema_extra  = {
            "example" : {
                "books" : [
                    {
                    "title" : "Mathematik für Ingenieure und Naturwissenschaftler Band 1: Ein Lehr- und Arbeitsbuch für das Grundstudium",
                    "author": "Lothar Papula",
                    "isbn" : "9783658217457"
                    },
                    {
                    "title" : "Mathematik für Ingenieure und Naturwissenschaftler Band 2: Ein Lehr- und Arbeitsbuch für das Grundstudium",
                    "author": "Lothar Papula",
                    "isbn" : "3658077891"
                    },
                    {
                    "title" : "Mathematische Formelsammlung: Für Ingenieure und Naturwissenschaftler",
                    "author": "Lothar Papula",
                    "isbn" : "3658161949"
                    }
            
            ]
            }
        }

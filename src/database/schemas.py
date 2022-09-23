from pydantic import BaseModel, Field, EmailStr
import datetime

########################################
## User 
########################################
class UserBaseSchema(BaseModel):
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)

class UserLoginSchema(UserBaseSchema):
    class Config: ## TODO(chrohne): check, if this actually works!
        the_schema = {
            "user" : {
                "email": "max@mustermann.de",
                "password" : "mustermann"
            }
        }

class UserRegisterSchema(UserBaseSchema):
    fullname: str = Field(default=None)
    class Config: ## TODO(chrohne): check, if this actually works!
        the_schema = {
            "user" : {
                "fullname" : "max mustermann",
                "email": "max@mustermann.de",
                "password" : "mustermann"
            }
        }

########################################
## User 
########################################
class BookingBaseSchema(BaseModel):
    from_date: datetime.date
    to_date: datetime.date

class BookingSchema(BookingBaseSchema):
    isbn: str
    description: str

########################################
## User 
########################################
class BookBaseSchema(BaseModel):
    isbn: str
    title: str
    author: str

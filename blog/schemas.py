from pydantic import BaseModel


class Blog(BaseModel):
    title: str
    body: str


class ShowBlog(Blog):
    class Config():
        orm_mode = True
"""
class ShowBlog(BaseModel):
    title: str
    body: str"""

class User(BaseModel):
    name:str
    email:str
    password: str
from tortoise.models import Model
from tortoise import Tortoise, fields
from fastapi import FastAPI
from tortoise import Tortoise

class Register_student(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(50,)
    email = fields.CharField(50, unique=True)
    phone = fields.CharField(10)
    password = fields.CharField(200)
    address = fields.CharField(100)
    student_image = fields.TextField()


class Subjects(Model):
    sub_name = fields.CharField(100)

class Questions(Model):
    sno=fields.CharField(500)
    sname =fields.ForeignKeyField( "models.Subjects", related_name="subname", on_delete="CASCADE")
    que = fields.CharField(500)
    opt1 = fields.CharField(500)
    opt2 = fields.CharField(500)
    opt3 = fields.CharField(500)
    opt4 = fields.CharField(500)
    answer = fields.CharField(500)
    url = fields.CharField(500)


class Attempt(Model):
    id = fields.IntField(pk=True)
    sname =fields.ForeignKeyField( "models.Subjects", related_name="subn", on_delete="CASCADE")
    student = fields.ForeignKeyField( "models.Register_student", related_name="Astudent", on_delete="CASCADE")
    queattempt = fields.ForeignKeyField( "models.Questions", related_name="ques", on_delete="CASCADE")
    queno = fields.IntField()
    ans = fields.CharField(100)
    marking = fields.BooleanField()

class Submission(Model):
    id = fields.IntField(pk=True)
    student = fields.ForeignKeyField( "models.Register_student", related_name="stud", on_delete="CASCADE")
    submitstatus = fields.CharField(100)
    currectans = fields.IntField()
    percentage = fields.IntField()
    totq=fields.CharField(100)
    subid =fields.ForeignKeyField( "models.Subjects", related_name="subid", on_delete="CASCADE")
    attempt = fields.CharField(100)
    name = fields.CharField(100)

class Visited(Model):
    quevisited = fields.ForeignKeyField( "models.Questions", related_name="quevv", on_delete="CASCADE")



    Tortoise.init_models(['mytestapp.models'], 'models')

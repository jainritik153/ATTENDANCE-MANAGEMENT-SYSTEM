from django.db import models

# Create your models here.



class Teacherreg(models.Model):
    username = models.CharField(max_length=20,default='NULL')
    email = models.CharField(max_length=20,default='a@b.com')
    password = models.CharField(max_length=20,default='0')
    subject = models.CharField(max_length=20,default='NULL')
    account=models.IntegerField(default=1)
    def __str__(self):
        return "%s %s %s %s" % (self.username, self.email ,self.password,self.subject)


class Studentreg(models.Model):
    username = models.CharField(max_length=20,default='NULL')
    email = models.CharField(max_length=20,default='a@b.com')
    password = models.CharField(max_length=20,default='0')
    roll=models.IntegerField(default=0,primary_key=True)
    account = models.IntegerField(default=2)
    def __str__(self):
        return "%s %s %s %s %s" % (self.username, self.email ,self.password,self.roll,self.account)


class Aoa(models.Model):
    roll=models.IntegerField(primary_key=True)
    _1 =models.CharField(default='Not',max_length=20)
    _2 = models.CharField(default='Not',max_length=20)
    _3 = models.CharField(default='Not',max_length=20)
    _4 =  models.CharField(default='Not',max_length=10)
    _5 = models.CharField(default='Not', max_length=10)
    _6 = models.CharField(default='Not', max_length=10)
    _7 = models.CharField(default='Not', max_length=10)


class Maths(models.Model):
    roll=models.IntegerField(primary_key=True)
    _1 =models.CharField(default='Not',max_length=20)
    _2 = models.CharField(default='Not',max_length=20)
    _3 = models.CharField(default='Not',max_length=20)
    _4 =  models.CharField(default='Not',max_length=10)
    _5 = models.CharField(default='Not', max_length=10)
    _6 = models.CharField(default='Not', max_length=10)
    _7 = models.CharField(default='Not', max_length=10)


class Ostl(models.Model):
    roll=models.IntegerField(primary_key=True)
    _1 =models.CharField(default='Not',max_length=20)
    _2 = models.CharField(default='Not',max_length=20)
    _3 = models.CharField(default='Not',max_length=20)
    _4 =  models.CharField(default='Not',max_length=10)
    _5 = models.CharField(default='Not', max_length=10)
    _6 = models.CharField(default='Not', max_length=10)
    _7 = models.CharField(default='Not', max_length=10)
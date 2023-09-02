from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

# Create your models here.


class UserManager(BaseUserManager):
   
   def create_user(self, username,email,password=None):
      if not username :
         raise ValueError("Username must be provided")
      if not email :
         raise ValueError("Email must be provided")
    
      user=self.model(email=self.normalize_email(email),username=username)
      user.set_password(password)
      user.save(self.db)
      return user



   def create_superuser(self,username,email,password):
      user=self.create_user(email=self.normalize_email(email),username=username,password=password)
      user.is_admin=True
      user.is_superuser=True
      user.is_staff=True
      user.save(self.db)
      return user


class User(AbstractBaseUser):
    email=models.EmailField(verbose_name='email',unique=True,null=True,max_length=60)
    username=models.CharField(max_length=50,unique=True,null=True)
    first_name=models.CharField(max_length=60,null=True)
    last_name=models.CharField(max_length=60,null=True)
    other_names=models.CharField(max_length=60,null=True)
    phone_number=models.CharField(max_length=11,null=True)
    profile_picture=models.ImageField(null=True,blank=True,upload_to='proile_pics/')
    date_joined=models.DateTimeField(null=True, blank=True,auto_now_add=True,verbose_name='date joined')
    last_login=models.DateTimeField(null=True,auto_now=True,)
    is_superuser=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_admin=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)


    objects=UserManager()


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    def has_perm(self,perm,obj=None):
       return self.is_admin
    
    def has_module_perms(self,app_label):
       return True
                       
    


    def _str_(self):
     return self.firstname +self.last_name 

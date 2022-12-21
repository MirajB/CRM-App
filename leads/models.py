# from asyncio.windows_events import NULL
from django.db import models
from Django_crm.mixins import infomixin
from django.contrib.auth.models import AbstractBaseUser, UserManager, BaseUserManager
# from django.contrib.auth.models import UserManager
# Create your models here.


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None, first_name=None, last_name=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name = first_name,
            last_name= last_name
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password, first_name, last_name):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
            first_name = first_name,
            last_name= last_name
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, first_name, last_name):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
            first_name = first_name,
            last_name= last_name
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        null=False
    )
    first_name  =  models.CharField(max_length=50, default=None)
    last_name  =  models.CharField(max_length=50, default=None)
    contact_no = models.CharField(default=None, null=True, blank=True, max_length=20)
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser

    # notice the absence of a "Password field", that is built in.
    objects = MyUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name'] # Email & Password are required by default.

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.get_full_name()

class lead(infomixin):
    SOURCE_CHOICES = (
        ('1', '---'),
        ('FB', 'Facebook'),
        ('GS', 'Google Search'),
        ('SM', 'Social Media'),
        ('Ph', 'Phone'),
        ('Ot', 'Others')
    )
    contacted = models.BooleanField(default= False)
    source = models.CharField(choices=SOURCE_CHOICES, default=None, max_length=100)
    profile_picture = models.ImageField(blank=True, null=True, upload_to='media/')
    files = models.FileField(blank=True, null=True)
    agent = models.ForeignKey(Agent, on_delete=models.SET_DEFAULT,  default=None, null = True, blank=True)
    dt_stamp = models.DateTimeField(auto_created=True, null=True, auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def lead_contact_info(self):
        return f"{self.first_name} {self.last_name} - {self.contact_no}"


 
    
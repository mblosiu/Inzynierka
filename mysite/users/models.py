from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=30, default="")
    surname = models.CharField(max_length=30, default="")
    birthday = models.DateField(default=None)
    location = models.CharField(max_length=30, default="")

    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # physical features:
    sex = models.CharField(max_length=30, null=True, blank=True)
    hair_color = models.CharField(max_length=30, null=True, blank=True)
    growth = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)
    body_type = models.CharField(max_length=30, null=True, blank=True)
    race_orgin = models.CharField(max_length=30, null=True, blank=True)

    # character (scale 1-10)
    Assertiveness = models.FloatField(null=True, blank=True)
    Sincerity = models.FloatField(null=True, blank=True)
    Empathy = models.FloatField(null=True, blank=True)
    Communication = models.FloatField(null=True, blank=True)
    Selflessness = models.FloatField(null=True, blank=True)
    Honesty = models.FloatField(null=True, blank=True)
    Scrupulousness = models.FloatField(null=True, blank=True)
    Diligence = models.FloatField(null=True, blank=True)
    Kindness = models.FloatField(null=True, blank=True)

    # Habits:
    is_smoking = models.CharField(max_length=30, null=True, blank=True)
    is_drinking_alcohol = models.CharField(max_length=30, null=True, blank=True)
    # never, sporadically, occasionally, moderately, often, addictively

    # user partner preferences:
    sex_preference = models.CharField(max_length=30, null=True, blank=True)
    hair_color_blonde_preference = models.CharField(max_length=30, null=True, blank=True)
    hair_color_brunette_preference = models.CharField(max_length=30, null=True, blank=True)
    hair_color_red_preference = models.CharField(max_length=30, null=True, blank=True)
    growth_preference = models.CharField(max_length=30, null=True, blank=True)
    weight_preference = models.CharField(max_length=30, null=True, blank=True)
    body_type_preference = models.CharField(max_length=30, null=True, blank=True)
    race_orgin_preference = models.CharField(max_length=30, null=True, blank=True)

    Assertiveness_preference = models.CharField(max_length=30, null=True, blank=True)
    Sincerity_preference = models.CharField(max_length=30, null=True, blank=True)
    Empathy_preference = models.CharField(max_length=30, null=True, blank=True)
    Communication_preference = models.CharField(max_length=30, null=True, blank=True)
    Selflessness_preference = models.CharField(max_length=30, null=True, blank=True)
    Honesty_preference = models.CharField(max_length=30, null=True, blank=True)
    Scrupulousness_preference = models.CharField(max_length=30, null=True, blank=True)
    Diligence_preference = models.CharField(max_length=30, null=True, blank=True)
    Kindness_preference = models.CharField(max_length=30, null=True, blank=True)

    is_smoking_preference = models.CharField(max_length=30, null=True, blank=True)
    is_drinking_alcohol_preference = models.CharField(max_length=30, null=True, blank=True)


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'location', 'birthday']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True


# user account - uwierzytelnianie, podstawowe informacje
# user profile - wszystkie informacje o użytkowniku
# user settings - ustawienia użytkownika


class UserProfile(models.Model):
    username = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.username
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class Preferences(models.Model):
    sex_preference = models.CharField(max_length=30, null=True, blank=True, default=None)
    hair_color_blonde_preference = models.CharField(max_length=30, null=True, blank=True, default=None)
    hair_color_brunette_preference = models.CharField(max_length=30, null=True, blank=True, default=None)
    hair_color_red_preference = models.CharField(max_length=30, null=True, blank=True, default=None)
    growth_preference = models.CharField(max_length=30, null=True, blank=True, default=None)
    weight_preference = models.CharField(max_length=30, null=True, blank=True, default=None)
    body_type_preference = models.CharField(max_length=30, null=True, blank=True, default=None)
    freckles_preference = models.CharField(max_length=30, null=True, blank=True, default=None)
    glasses_preference = models.CharField(max_length=30, null=True, blank=True, default=None)
    hair_length_preference = models.CharField(max_length=30, null=True, blank=True, default=None)

    is_smoking_preference = models.CharField(max_length=30, null=True, blank=True, default=None)
    is_drinking_alcohol_preference = models.CharField(max_length=30, null=True, blank=True, default=None)

    Assertiveness_preference = models.CharField(max_length=30, null=True, blank=True, default=None)
    Sincerity_preference = models.CharField(max_length=30, null=True, blank=True, default=None)
    Empathy_preference = models.CharField(max_length=30, null=True, blank=True, default=None)
    Communication_preference = models.CharField(max_length=30, null=True, blank=True, default=None)
    Selflessness_preference = models.CharField(max_length=30, null=True, blank=True, default=None)
    Honesty_preference = models.CharField(max_length=30, null=True, blank=True, default=None)
    Scrupulousness_preference = models.CharField(max_length=30, null=True, blank=True, default=None)
    Diligence_preference = models.CharField(max_length=30, null=True, blank=True, default=None)
    Kindness_preference = models.CharField(max_length=30, null=True, blank=True, default=None)


class Settings(models.Model):
    dark_theme = models.BooleanField(default=True)


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, location, birthday, sex, password=None):
        if not email:
            raise ValueError('Email is required')
        if not username:
            raise ValueError('Username is required')
        if not location:
            raise ValueError('Location is required')
        if not birthday:
            raise ValueError('Birthday is required')
        if not sex:
            raise ValueError('Sex is required')
        user = self.model(
            email=self.normalize_email(email),
            password=password,
            username=username,
            location=location,
            birthday=birthday,
            sex=sex,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, location, birthday, sex, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
            location=location,
            birthday=birthday,
            sex=sex,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    preferences = models.OneToOneField(Preferences, on_delete=models.CASCADE, null=True, default=None)
    settings = models.OneToOneField(Settings, on_delete=models.CASCADE, null=True, default=None)

    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)

    name = models.CharField(max_length=30, null=True, default=None)
    surname = models.CharField(max_length=30, null=True, default=None)
    birthday = models.DateField(null=True, default=None)
    location = models.CharField(max_length=30, null=True, default=None)
    profile_picture = models.ImageField(upload_to='images', null=True, blank=True, default=None)
    description = models.CharField(max_length=200, null=True, default=None)

    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # physical features:
    sex = models.CharField(max_length=30, null=True, blank=True, default=None)
    hair_color = models.CharField(max_length=30, null=True, blank=True, default=None)
    growth = models.IntegerField(null=True, blank=True, default=None)
    weight = models.IntegerField(null=True, blank=True, default=None)
    body_type = models.CharField(max_length=30, null=True, blank=True, default=None)
    freckles = models.BooleanField(default=False)
    glasses = models.BooleanField(default=False)
    hair_length = models.CharField(max_length=30, null=True, blank=True, default=None)

    # Habits:
    is_smoking = models.CharField(max_length=30, null=True, blank=True, default=None)
    is_drinking_alcohol = models.CharField(max_length=30, null=True, blank=True, default=None)

    # character (scale 1-10)
    Assertiveness = models.FloatField(null=True, blank=True, default=None)
    Sincerity = models.FloatField(null=True, blank=True, default=None)
    Empathy = models.FloatField(null=True, blank=True, default=None)
    Communication = models.FloatField(null=True, blank=True, default=None)
    Selflessness = models.FloatField(null=True, blank=True, default=None)
    Honesty = models.FloatField(null=True, blank=True, default=None)
    Scrupulousness = models.FloatField(null=True, blank=True, default=None)
    Diligence = models.FloatField(null=True, blank=True, default=None)
    Kindness = models.FloatField(null=True, blank=True, default=None)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'location', 'birthday', 'sex']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

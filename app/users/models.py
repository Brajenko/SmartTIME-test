from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from app.exams.models import Exam, Registration


class UserManager(BaseUserManager["User"]):
    def create(self, email: str, password: str | None = None):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email: str, password: str | None = None):
        return self.create(
            email,
            password=password,
        )

    def create_superuser(self, email: str, password: str | None = None):
        user = self.create(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    class Meta:
        db_table = "users"

    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    is_admin = models.BooleanField(default=False)
    exams = models.ManyToManyField(Exam, related_name="users", through=Registration)

    objects = UserManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

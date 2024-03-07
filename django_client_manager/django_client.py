from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth.hashers import make_password

class ClientManager(BaseUserManager):
    """
    Custom manager for the Client model.
    """

    def email_validator(self, email):
        """
        Validate the format of the email.

        Raises:
            ValueError: If the email format is not valid.
        """
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError("Client email is not valid.")

    def create_client(self, email, password=None, **extra_fields):
        """
        Create a new client user.

        Args:
            email (str): The email address of the client.
            password (str): The password for the client user.
            **extra_fields: Additional fields for the user.

        Raises:
            ValueError: If email is not provided or is invalid.

        Returns:
            Client: The newly created client user.
        """
        if not email:
            raise ValueError("Client email required.")

        email = self.normalize_email(email=email)
        self.email_validator(email=email)

        user = self.model(email=email, password=password)
        user.set_password(password)
        user.save(using=self._db)
        return user


class Client(AbstractUser, PermissionsMixin):
    """
    Custom user model for clients.
    """

    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False, editable=False)
    is_superuser = models.BooleanField(default=False, editable=False)
    groups = models.ManyToManyField("auth.Group")
    user_permissions = models.ManyToManyField("auth.Permission", editable=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    objects = ClientManager()

    def save(self, *args, **kwargs):
        """
        Save the user with a hashed password.
        """
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.username}"

    class Meta:
        abstract = True


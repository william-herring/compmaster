from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, wca_id, first_name, last_name=None, password=None, **extra_fields):
        if not wca_id:
            raise ValueError('The wca_id field must be set')
        if not first_name:
            raise ValueError('The first_name field must be set')

        user = self.model(wca_id=wca_id, first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, wca_id, first_name, last_name=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_delegate', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(wca_id, first_name, last_name, password, **extra_fields)

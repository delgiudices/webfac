from django.contrib.auth import models as authentication_models
from sistema.models import SistemaModel, SistemaModelManager
# Create your models here.


class UserManager(authentication_models.UserManager, SistemaModelManager):
    def _create_user(self, username, email, password,
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser,
                          **extra_fields)
        user.set_password(password)
        user.codigo = self.get_next_codigo(extra_fields['sistema'])
        user.save(using=self._db)
        return user


class User(authentication_models.AbstractUser, SistemaModel):

    """
    Usuario utilizado para la autenticacion,  pertenece a un sistema.
    """
    objects = UserManager()

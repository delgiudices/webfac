from django.contrib.auth import models as authentication_models
from sistema.models import SistemaModel, SistemaModelManager

# Create your models here.


class UserManager(authentication_models.UserManager):
    """
    Nothing
    """


class User(authentication_models.AbstractUser, SistemaModel):

    """
    Usuario utilizado para la autenticacion,  pertenece a un sistema.
    """

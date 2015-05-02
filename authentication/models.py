from django.contrib.auth import models as authentication_models
from sistema.models import SistemaModel, SistemaModelManager
from django.dispatch import receiver
from django.db.models.signals import pre_save

# Create your models here.


class UserManager(authentication_models.UserManager, SistemaModelManager):
    """ Nothing
    """


class User(authentication_models.AbstractUser, SistemaModel):

    """
    Usuario utilizado para la autenticacion,  pertenece a un sistema.
    """
    objects = UserManager()

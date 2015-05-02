from django.db import models
from django.contrib.auth import models as authentication_models
from sistema.models import SistemaModel
# Create your models here.


class User(authentication_models.AbstractUser, SistemaModel):

    """
    Usuario utilizado para la autenticacion,  pertenece a un sistema.
    """

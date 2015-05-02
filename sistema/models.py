from django.db import models


class Sistema(models.Model):

    name = models.CharField(max_length=80)


class SistemaModelManager(models.Manager):

    def all(self, sistema=None):
        if sistema is None:
            raise Exception("Querying a SistemaModel must specify sistema")
        return self.filter(sistema=sistema)


class SistemaModel(models.Model):

    codigo = models.PositiveIntegerField()
    sistema = models.ForeignKey(Sistema)
    objects = SistemaModelManager()

    class Meta:
        unique_together = ("codigo", "sistema")
        abstract = True

    def get_next_codigo(self):
        current_max = self.__class__.objects.filter(sistema=self.sistema)\
            .aggregate(models.Max('codigo'))['codigo__max'] or 0
        return current_max + 1

    def save(self, *args, **kwargs):
        self.codigo = self.get_next_codigo()
        super(SistemaModel, self).save(*args, **kwargs)

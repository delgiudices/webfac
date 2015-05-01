from django.db import models


class Sistema(models.Model):

    name = models.CharField(max_length=80)


class SistemaModelManager(models.Manager):

    def get_next_codigo(self, sistema):
        current_max = self.filter(sistema=sistema)\
            .aggregate(models.Max('codigo'))['codigo__max'] or 0
        return current_max + 1

    def create(self, **kwargs):
        try:
            kwargs['codigo'] = self.get_next_codigo(kwargs['sistema'])
            super(SistemaModelManager, self).create(**kwargs)
        except KeyError:
            raise Exception("SistemaModel must specify sistema\
                key argument on create")

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

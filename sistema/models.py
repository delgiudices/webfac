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
        if self.codigo is None:
            # Model is being created
            self.codigo = self.get_next_codigo()
        super(SistemaModel, self).save(*args, **kwargs)


class DataTableModel(models.Model):

    def get_class(self):
        return self.__class__.name

    class Meta:
        abstract = True

    def get_fields(self):
        """
        Informacion que sera mostrada en los data-tables
        """
        raise NotImplementedError(
            "DataTableModel subclasses must implement get_fields")

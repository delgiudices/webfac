class CantidadError(Exception):

    def __init__(self):
        message = "No se puede tener un inventario con cantidad negativa"
        super(CantidadError, self).__init__(message)

class EjercitoRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'nombre_de_tu_aplicacion' and model.__name__ == 'UnidadEjercito':
            return 'ejercito'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'nombre_de_tu_aplicacion' and model.__name__ == 'UnidadEjercito':
            return 'ejercito'
        return None


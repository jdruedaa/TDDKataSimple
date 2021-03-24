class Procesador:

    def contar(self, cadena):
        if cadena == "":
            return 0
        else:
            return int(cadena)

    def minimo(self, cadena):
        if cadena == "":
            return 0
        else:
            return int(cadena)

    def maximo(self, cadena):
        if cadena == "":
            return 0
        else:
            return int(cadena)

    def promedio(self, cadena):
        if cadena == "":
            return 0
        else:
            return int(cadena)

    def respuesta(self, cadena):
        if cadena == "":
            respuesta = []
        else:
            respuesta = [self.contar(cadena), self.minimo(cadena), self.maximo(cadena), self.promedio(cadena)]
        return respuesta

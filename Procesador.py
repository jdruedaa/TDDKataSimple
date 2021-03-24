class Procesador:

    def contar(self, cadena):
        if cadena == "":
            return 0
        valores = list(map(int, cadena.split(',')))
        if len(valores) == 1:
            return 1
        elif len(valores) == 2:
            return 2

    def minimo(self, cadena):
        if cadena == "":
            return 0
        valores = list(map(int, cadena.split(',')))
        if len(valores) == 1:
            return int(cadena)
        elif len(valores) == 2:
            return min(valores)

    def maximo(self, cadena):
        if cadena == "":
            return 0
        valores = list(map(int, cadena.split(',')))
        if len(valores) == 1:
            return int(cadena)
        elif len(valores) == 2:
            return max(valores)

    def promedio(self, cadena):
        if cadena == "":
            return 0
        valores = list(map(int, cadena.split(',')))
        if len(valores) == 1:
            return int(cadena)
        elif len(valores) == 2:
            return sum(valores)/2

    def respuesta(self, cadena):
        if cadena == "":
            respuesta = []
        else:
            respuesta = [self.contar(cadena), self.minimo(cadena), self.maximo(cadena), self.promedio(cadena)]
        return respuesta

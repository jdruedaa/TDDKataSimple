class Procesador:

    def contar(self, cadena):
        if cadena == "":
            return 0
        valores = list(map(int, cadena.split(',')))
        return len(valores)

    def minimo(self, cadena):
        if cadena == "":
            return 0
        valores = list(map(int, cadena.split(',')))
        return min(valores)

    def maximo(self, cadena):
        if cadena == "":
            return 0
        valores = list(map(int, cadena.split(',')))
        return max(valores)

    def promedio(self, cadena):
        if cadena == "":
            return 0
        valores = list(map(int, cadena.split(',')))
        return sum(valores)/len(valores)

    def respuesta(self, cadena):
        if cadena == "":
            respuesta = []
        else:
            respuesta = [self.contar(cadena), self.minimo(cadena), self.maximo(cadena), self.promedio(cadena)]
        return respuesta

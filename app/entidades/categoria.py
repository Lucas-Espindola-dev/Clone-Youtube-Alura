class Categoria:
    def __init__(self, titulo, cor):
        self._titulo = titulo
        self._cor = cor

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, titulo):
        self._titulo = titulo

    @property
    def cor(self):
        return self._cor

    @cor.setter
    def cor(self, cor):
        self._cor = cor


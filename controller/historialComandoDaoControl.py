from typing import Type
from controller.dao.daoAdapter import DaoAdapter
from controller.tda.linked.linkedList import LinkedList
from modelo.historialComando import HistorialComando
# from datetime import date

class HistorialComandoDaoControl(DaoAdapter):
    def __init__(self):
        super().__init__(HistorialComando)
        self.__historial_comando = None

    @property
    def _historial_comando(self):
        if self.__historial_comando == None:
            self.__historial_comando = HistorialComando()
        return self.__historial_comando

    @_historial_comando.setter
    def _historial_comando(self, value):
        self.__historial_comando = value

    @property
    def _lista(self):
        return self._list()
    
    def merge(self, pos):
        self._merge(self._historial_comando, pos)
        
    @property
    def save(self):
        try:
            self._historial_comando._id = self._lista._length + 1 
            self._save(self._historial_comando)
        except Exception as e:
            print(f"Error en save es: {e}")
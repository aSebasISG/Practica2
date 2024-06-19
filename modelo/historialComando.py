from datetime import datetime, date

class HistorialComando:
    def __init__(self):
        self.__id = 0
        self.__usuario = ""
        self.__email = ""
        self.__comando = ""
        self.__descripcion = ""
        self.__fecha = date.today() 

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _usuario(self):
        return self.__usuario

    @_usuario.setter
    def _usuario(self, value):
        self.__usuario = value

    @property
    def _email(self):
        return self.__email

    @_email.setter
    def _email(self, value):
        self.__email = value

    @property
    def _comando(self):
        return self.__comando

    @_comando.setter
    def _comando(self, value):
        self.__comando = value

    @property
    def _descripcion(self):
        return self.__descripcion

    @_descripcion.setter
    def _descripcion(self, value):
        self.__descripcion = value

    @property
    def _fecha(self):
        return self.__fecha

    @_fecha.setter
    def _fecha(self, value):
        self.__fecha = value

    @property
    def serializar(self):
        return {
            "id": self._id,
            "usuario": self._usuario,
            "email": self._email,
            "comando": self._comando,
            "descripcion": self._descripcion,
            "fecha": self._fecha.strftime("%Y-%m-%d") 
        }
        
    @staticmethod
    def deserializar(data):
        historial = HistorialComando()
        historial._id = data["id"]
        historial._usuario = data["usuario"]
        historial._email = data["email"]
        historial._comando = data["comando"]
        historial._descripcion = data["descripcion"]
        historial._fecha = datetime.strptime(data["fecha"], "%Y-%m-%d").date()
        return historial
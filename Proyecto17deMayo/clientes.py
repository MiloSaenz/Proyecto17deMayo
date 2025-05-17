class cliente:
    def __init__(self):
        equipos = []

    def AgregarCliente(self,apellidos, nombre, telefono):
        self.__apellidos = apellidos
        self.__nombre = nombre
        self.__telefono = telefono

    def AgregarEquipo(self,equipo):
        self.equipos.append(equipo)

    def VerEquipos(self,equipos):
        for MisEquipos in equipos:
            print(f"{MisEquipos["codigo"]} {MisEquipos["nombre"]} {MisEquipos["precio"]}")


    @property
    def _apellidos(self):
        return self.__apellidos

    @_apellidos.setter
    def _apellidos(self, value):
        self.__apellidos = value

    @property
    def _nombre(self):
        return self.__nombre

    @_nombre.setter
    def _nombre(self, value):
        self.__nombre = value

    @property
    def _telefono(self):
        return self.__telefono

    @_telefono.setter
    def _telefono(self, value):
        self.__telefono = value

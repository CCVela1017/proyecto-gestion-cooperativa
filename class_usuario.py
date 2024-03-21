class Usuarios:  # Se creo la clase usuario
    def __init__(self, codigo, nombre, correo, contrasena, puesto, estado):  # Se inicializaron los datos
        self.codigo = codigo
        self.nombre = nombre
        self.correo = correo
        self.contrasena = contrasena
        self.puesto = puesto
        self.estado = estado

    def __str__(self):  # Se leen los datos
        return self.codigo + self.nombre + self.correo + self.contrasena + self.puesto + self.estado

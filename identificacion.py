Class profesor:
    def __init__(self, el_nombre, el_gmail):
        self.nombre = el_nombre
        self.gmail = el_gmail

    def dame_tu_nombre(self):
    return self.nombre

class alumno:
    def __init__(self, el_nombre_del_alumno):
        self.nombre = el_nombre_del_alumno
        self.inasistencias = 0
        self.dieta = ""
        self.mentor = None

    def mentoria(self, profesor):
        self.mentor = profesor

    def falta(self):
        self.inasistencias += 1

    def elegir_dieta_especial(self, la_dieta):
        self.dieta = la_dieta

    def es_vegetariano(self):
        self.dieta = "vegetariano"

    def esta_libre(self):
        if self.inasistencias >= 4:
            return "ESTA LIBRE"
        else:
            return "OK"
profe_gonzalo = Profesor("gonzalo", "gonzalo@gmail.com")

profe_german = Profesor("german", "german@um.edu.ar")

# print(profe_gonzalo.dame_tu_nombre())

# print(profe_german.dame_tu_nombre())

alumno_max = Alumno("max")
alumno_mili = Alumno("mili")
alumno_maxi.falta()
alumno_maxi.falta()
alumno_maxi.falta()
print(alumno_maxi.esta_libre())
alumno_maxi.falta()
print(alumno_maxi.esta_libre())
alumno_mili.elegir_dieta_especial("vegetariana")
print(alumno_mili.dieta)
alumno_maxi.es_vegetariano()
print(alumno_maxi.dieta)
alumno_maxi.mentoria(profe_gonzalo)
print(alumno_maxi.mentor)
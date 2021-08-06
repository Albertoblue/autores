frutas=["Sandia","Manzana","Melon","Uvas"]

class Alumno:
    def __init__(self,matricula,promedio,edad,nombre):
        self.matricula=matricula
        self.promedio=promedio
        self.edad=edad
        self.nombre=nombre
    
    def estudiar(self):
         return "El alumno esta estudiando"
    def __str__(self):
        return "Soy %s tengo promedio %.2f y mi matricula es: %i"%(self.nombre,self.promedio,self.matricula)


alumnos=[]

alumnos.append(Alumno(25630,9.0,22,"Pedro"))
alumnos.append(Alumno(90251,6.8,19,"Paulina"))

for alumno in alumnos:
    print(alumno)







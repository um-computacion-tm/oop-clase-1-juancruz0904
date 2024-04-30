class Persona: #clase--->camelcase #lo otro---snake case
    
    def __init__(self,nombre: str,apellido: str,du: int):
    #def __init__(self,nombre: str="benja",apellido: str="gomez",du: int=1): #para que no sean obligatorios los parametros, le damos un valor por defecto  
        self.__nombre__= nombre 
        self.__apellido__ = apellido
        self.__du__ = du
    
   # def mostrar_datos(self):
    #    print(f'Datos={self.__nombre__} apellido={self.__apellido__} documento={self.__du__}')
    
    def __str__(self):
        return f'Datos={self.__nombre__} apellido={self.__apellido__} documento={self.__du__}'
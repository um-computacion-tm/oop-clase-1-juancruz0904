from persona import Persona

if __name__ == "__main__": # no se puede acceder a los atributos porque son privados

    persona = Persona("a","a",1)
    #print(persona.__dict__) # para ver los atributos como diccionario
    print(persona)
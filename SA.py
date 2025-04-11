class Archivo:
    def __init__(self, nombre, tam, prop):
        self.nombre = nombre
        self.tam = tam
        self.pro = prop
        pass
    def modificar(self, disp):
        print("Que característica quieres modificar")
        print("1) Nombre ")
        print("2) Tamaño ")
        print("3) Propietario ")
        car = input(": ")
        if car == "1":
            nom = input("Cual es el nuevo nombre: ")
            self.nombre = nom
        elif car == "2":
            tam = int(input("Cual es el nuevo tamaño: "))
            if disp > tam:
                self.tam = tam
            else:
                print("No se puede modificar. ")    
        elif car == "3":
            prop = input("Cual es el nuevo propietario: ")
            self.prop = prop
        pass
    def __str__(self):
        return f"Archivo -> {self.nombre}, Prop: {self.pro}, Tam: {self.tam}"
        pass

class sisArch:
    def __init__(self, tam =20):
        self.archivos = []
        self.hdd =[None]*tam
        self.tabP = [None]*tam
        self.espD = tam
        self.tam = tam
        
    def validaEsp(self, tamA):
        if tamA > self.espD:
            print(f"No hay espacio, Disponible: {self.espD}")
            return False
        return True
        pass
    
    def agregaArch(self,archivo):#Duplicidad
        print(f"Archivo agregado: {archivo}")
        self.archivos.append(archivo)
        aux = 0
        for i in range(self.tam):
            if self.hdd[i] == None:
                self.hdd[i]= archivo.nombre
                aux+=1
                if aux == archivo.tam:
                    break
        self.espD -= archivo.tam
        pass
    def eliminaArch(self,nombre):#Buscar si existe
        for archivo in self.archivos:
            if archivo.nombre == nombre:
                print(f"Archivo eliminado {archivo}")
                self.archivos.remove(archivo)
        pass
    def modificaArch(self,nombre): # Buscar si existe
        for archivo in self.archivos:
            if archivo.nombre == nombre:
                aux = archivo
                archivo.modificar(self.espD)
                print(f"Archivo antes: {aux}")
                print(f"Archivo despues: {archivo}")
        
        pass
    def imprimeArch(self):
        if not self.archivos:
            print("No existen archivos")
        else:
            for archivo in self.archivos:
                print(archivo)
            print(f"HDD: {self.hdd}")
        pass

def menu():
    print("Programa que simula el almacenamiento.")
    print("1) Crea Archivo")
    print("2) Elimina Archivo")
    print("3) Modifica Archivo")
    print("4) Listar Archivos")
    print("5) Salir")
    opc = input("Ingresa la opcion deseada")
    return opc

def main():
    opc = "s"
    s1 = sisArch()
    while opc != "5":
        opc = menu()
        if opc == "1": #validar duplicidad
            nom = input("Ingresa el nombre del archivo: 1")
            prop = input("Ingresa el propietario: ")
            flag = False
            while flag == False:
                tam = int(input("Ingresa el tamaño: "))
                flag = s1.validaEsp(tam)

            arch = Archivo(nom, tam, prop)
            s1.agregaArch(arch)
        elif opc =="2":
            nom = input("Ingresa el nombre del archivo:")
            s1.eliminaArch(nom)
        elif opc =="3":
            nom = input("Ingresa el nombre del archivo:")
            s1.modificaArch(nom)
        elif opc == "4":
            s1.imprimeArch()            
    pass

if __name__ =="__main__":
    main()
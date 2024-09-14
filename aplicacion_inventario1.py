from administracion_inventario import AdministracionInventario

class Aplicacion:
    
    def __init__(self):
        self.IniciarAplicacion()
        
    def IniciarAplicacion(self):
        inventario = AdministracionInventario()
        print("-------------------------------------")
        print("Bienvenidos al sistema de Inventarios")
        salir_programa = False
        while not salir_programa:
            print("Menu del Inventario")
            print("""
                  1.- Mostrar lista de clientes
                  2.- Agregar clientes
                  3.- Modificar clientes
                  4.- Eliminar clientes
                  5.- Salir del programa
                  """)
            
            opcion = int(input("Indica  una opcion del menu: "))
            if opcion == 1:
                inventario.mostrarListaClientes()
            elif opcion == 2:
                inventario.agregarClientes()
            elif opcion == 3:
                inventario.modificarClientes()
            elif opcion == 4:
                inventario.eliminarClientes()
            if opcion == 5:
                print("Salir del programa, hasta luego")
                salir_programa = True
                
sistema_inventario = Aplicacion()    
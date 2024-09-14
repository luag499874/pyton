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
                  1.- Mostrar lista de pedidos
                  2.- Agregar pedidos
                  3.- Modificar pedidos
                  4.- Eliminar pedidos
                  5.- Salir del programa
                  """)
            
            opcion = int(input("Indica  una opcion del menu: "))
            if opcion == 1:
                inventario.mostrarListaPedidos()
            elif opcion == 2:
                inventario.agregarPedidos()
            elif opcion == 3:
                inventario.modificarPedidos()
            elif opcion == 4:
                inventario.eliminarPedidos()
            if opcion == 5:
                print("Salir del programa, hasta luego")
                salir_programa = True
                
sistema_inventario = Aplicacion()    
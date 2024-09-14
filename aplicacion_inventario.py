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
                  1.- Mostrar lista de productos
                  2.- Agregar producto
                  3.- Modificar producto
                  4.- Eliminar producto
                  5.- Salir del programa
                  """)
            
            opcion = int(input("Indica  una opcion del menu: "))
            if opcion == 1:
                inventario.mostrarListaProductos()
            elif opcion == 2:
                inventario.agregarProducto()
            elif opcion == 3:
                inventario.modificarProducto()
            elif opcion == 4:
                inventario.eliminarProducto()
            if opcion == 5:
                print("Salir del programa, hasta luego")
                salir_programa = True
                
sistema_inventario = Aplicacion()    
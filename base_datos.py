import sqlite3
import os

class BaseDatos:
    
    def __init__(self, nombreBaseDatos):
        self.nombreBaseDatos = nombreBaseDatos
        
    def crearBaseDatos(self):
        try:
            conn =sqlite3.connect(self.nombreBaseDatos)
        except Exception as e:
            print('Error al crear Base de Datos: {}'. format (e))
                
    def verificacionBaseDatosExiste(self):
        if os.path.isfile(self.nombreBaseDatos):
            return True
        else:
             return False
                    
    def crearTablaProductos(self):
        conexion = self.abrirConexion()
                        
        conexion.execute('''CREATE TABLE IF NOT EXISTS  productos
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre_producto TEXT NOT NULL,
                        descripcion TEXT NOT NULL,
                        precio FLOAT NOT NULL,
                        stock INTEGER NOT NULL
                        );''')
        
                        
        conexion.close()

    def crearTablaClientes(self):
        conexion = self.abrirConexion()
                        
        conexion.execute('''CREATE TABLE IF NOT EXISTS  clientes
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        clave INTEGER NOT NULL,
                        nombre TEXT NOT NULL,
                        direccion TEXT NOT NULL,
                        correo_electronico TEXT NOT NULL,
                        telefono INTEGER NOT NULL
                        );''')
        
                        
        conexion.close()
        
    
    def crearTablaPedidos(self):
        conexion = self.abrirConexion()
                        
        conexion.execute('''CREATE TABLE IF NOT EXISTS  pedidos
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        pedido INTEGER NOT NULL,
                        cliente TEXT NOT NULL,
                        producto TEXT NOT NULL,
                        precio INTEGER NOT NULL
                        );''')
        
                        
        conexion.close()    
        
    def abrirConexion(self):
        try:
            conexion = sqlite3.connect(self.nombreBaseDatos)
            return conexion
        except Exception as e:
            print('Error al conectar a la base de datos:{}'.format(e))                             
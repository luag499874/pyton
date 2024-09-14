import sqlite3 
from base_datos import BaseDatos
from autentificacion import Autentificacion

class AdministracionInventario:
    
    baseDatos = None
    autentificacion = None
    
    def __init__(self):
        self.baseDatos = BaseDatos('inventario.db')
        self.autentificacion = Autentificacion()
        if self.baseDatos.verificacionBaseDatosExiste():
           self.baseDatos.crearTablaProductos() 
           self.autentificacion.verificarAutentificacion()
        else:
            self.baseDatos.crearBaseDatos()
            self.baseDatos.crearTablaProductos
            self.autentificacion.verificarAutentificacion()
            
    def __init__(self):
        self.baseDatos = BaseDatos('clientes.db')
        self.autentificacion = Autentificacion()
        if self.baseDatos.verificacionBaseDatosExiste():
           self.baseDatos.crearTablaClientes() 
           self.autentificacion.verificarAutentificacion()
        else:
            self.baseDatos.crearBaseDatos()
            self.baseDatos.crearTablaClientes()
            self.autentificacion.verificarAutentificacion() 
            
    def __init__(self):
        self.baseDatos = BaseDatos('pedidos.db')
        self.autentificacion = Autentificacion()
        if self.baseDatos.verificacionBaseDatosExiste():
           self.baseDatos.crearTablaPedidos() 
           self.autentificacion.verificarAutentificacion()
        else:
            self.baseDatos.crearBaseDatos()
            self.baseDatos.crearTablaPedidos()
            self.autentificacion.verificarAutentificacion()                   
            
    def mostrarListaProductos(self):
        try:
            conexion = self.baseDatos.abrirConexion()
            cursor =conexion.cursor()
            cursor.execute("SELECT * FROM productos")
            productos = cursor.fetchall()
            if len(productos) > 0:
               print("Lista de productos disponibles: ")
               print("-------------------------------------") 
               for id,nombre_producto,descripcion,precio,stock in productos:
                   print('id: {}, nombre del producto {}, descripcion {}, precio {}, stock: {}' 
                        .format(id, nombre_producto, descripcion, precio, stock))
                   print("-------------------------------------")
            else:
                 print("No hay productos que mostrar")
                 print("--------------------------------------")
        except sqlite3.Error as error:
            print("Error al mostrar los datos de la tabla productos",error)
        finally:
            if conexion:
                cursor.close()
                conexion.close()
                
    def mostrarListaClientes(self):
        try:
            conexion = self.baseDatos.abrirConexion()
            cursor =conexion.cursor()
            cursor.execute("SELECT * FROM clientes")
            clientes = cursor.fetchall()
            if len(clientes) > 0:
               print("Lista de clientes disponibles: ")
               print("-------------------------------------") 
               for id,clave,nombre,direccion,correo_electronico,telefono in clientes:
                   print('id: {}, clave {}, nombre {}, direcccion {}, correo_electronico {}, telefono: {}' 
                        .format(id, clave, nombre, direccion, correo_electronico, telefono))
                   print("-------------------------------------")
            else:
                 print("No hay clientes que mostrar")
                 print("--------------------------------------")
        except sqlite3.Error as error:
            print("Error al mostrar los datos de la tabla clientes",error)
        finally:
            if conexion:
                cursor.close()
                conexion.close()
                
    def mostrarListaPedidos(self):
        try:
            conexion = self.baseDatos.abrirConexion()
            cursor =conexion.cursor()
            cursor.execute("SELECT * FROM pedidos")
            pedidos = cursor.fetchall()
            if len(pedidos) > 0:
               print("Lista de pedidos disponibles: ")
               print("-------------------------------------") 
               for id,pedido,cliente,producto,precio in pedidos:
                   print('id: {}, pedido {}, cliente {}, producto {}, precio:  {}' 
                        .format(id, pedido, cliente, producto, precio))
                   print("-------------------------------------")
            else:
                 print("No hay pedidos que mostrar")
                 print("--------------------------------------")
        except sqlite3.Error as error:
            print("Error al mostrar los datos de la tabla pedidos",error)
        finally:
            if conexion:
                cursor.close()
                conexion.close()      
                        
    def agregarProducto(self):
        try:
            conexion = self.baseDatos.abrirConexion()
            cursor = conexion.cursor()
            nombre_producto,descripcion,precio,stock = self.ingresarDatosProducto()
            valores = (nombre_producto, descripcion, precio, stock)
            sql = '''INSERT INTO productos(nombre_producto,descripcion,precio,stock)
                  VALUES(?,?,?,?)'''
            cursor.execute(sql,valores)
            conexion.commit()
            print("Datos guardados correctamente")
            print("-----------------------------------")
        except sqlite3.Error as error:
            print('Error al intentar insertar los datos: {}'.format(error))
        finally:
            if conexion:
                cursor.close()
                conexion.close()
                
    def agregarClientes(self):
        try:
            conexion = self.baseDatos.abrirConexion()
            cursor = conexion.cursor()
            clave,nombre,direccion,correo_electronico,telefono = self.ingresarDatosClientes()
            valores = (clave, nombre, direccion, correo_electronico, telefono)
            sql = '''INSERT INTO clientes(clave,nombre,direccion,correo_electronico,telefono)
                  VALUES(?,?,?,?,?)'''
            cursor.execute(sql,valores)
            conexion.commit()
            print("Datos guardados correctamente")
            print("-----------------------------------")
        except sqlite3.Error as error:
            print('Error al intentar insertar los datos: {}'.format(error))
        finally:
            if conexion:
                cursor.close()
                conexion.close()
                
    def agregarPedidos(self):
        try:
            conexion = self.baseDatos.abrirConexion()
            cursor = conexion.cursor()
            pedido,cliente,producto,precio = self.ingresarDatospedidos()
            valores = (pedido, cliente, producto, precio)
            sql = '''INSERT INTO pedidos(pedido,cliente,producto,precio)
                  VALUES(?,?,?,?)'''
            cursor.execute(sql,valores)
            conexion.commit()
            print("Datos guardados correctamente")
            print("-----------------------------------")
        except sqlite3.Error as error:
            print('Error al intentar insertar los datos: {}'.format(error))
        finally:
            if conexion:
                cursor.close()
                conexion.close()               
                                    
                                    
    def modificarProducto(self):
        try:
            conexion = self.baseDatos.abrirConexion()
            cursor = conexion.cursor()
                                            
            cursor.execute("SELECT * FROM productos")
            productos = cursor.fetchall()
            if len(productos) > 0:
                                                
                print("Lista de productos para modificar:")
                self.mostrarListaProductos()
                print("-----------------------------------")
                id_producto = self.ingresarID("Ingresar el id del producto a modificar: \n")
                                                
                encontrar_producto = cursor.execute("SELECT * FROM productos WHERE id = ?",(id_producto,))
                producto = encontrar_producto.fetchone()
                if producto :
                   nombre_producto,descripcion,precio,stock = self.ingresarDatosProducto()
                   sql = ''' UPDATE productos SET nombre_producto = ?, descripcion = ?, precio = ?, stock = ? WHERE id = ?'''
                   datos_producto = (nombre_producto,descripcion,precio,stock,id_producto)
                   cursor.execute(sql,datos_producto)
                   conexion.commit()
                   print("Registro modificado correctamente")
                   print("-------------------------------------")
                else:
                    print("No hay registros con ese id")
                    print("--------------------------------------")
            else: 
                 print("No hay productos para modificar")
                 print("--------------------------------------")
                                                
        except sqlite3.Error as error:
            print('Error al intentar modificar el registro: {}'.format(error))
        finally:
            if conexion:
                cursor.close()
                conexion.close()
    
    def modificarClientes(self):
        try:
            conexion = self.baseDatos.abrirConexion()
            cursor = conexion.cursor()
                                            
            cursor.execute("SELECT * FROM clientes")
            productos = cursor.fetchall()
            if len(productos) > 0:
                                                
                print("Lista de clientes para modificar:")
                self.mostrarListaClientes()
                print("-----------------------------------")
                id_clientes = self.ingresarID("Ingresar el id del clientes a modificar: \n")
                                                
                encontrar_clientes = cursor.execute("SELECT * FROM clientes WHERE id = ?",(id_clientes,))
                clientes = encontrar_clientes.fetchone()
                if clientes :
                   clave,nombre,direccion,correo_electronico,telefono = self.ingresarDatosClientes()
                   sql = ''' UPDATE clientes SET clave = ?, nombre = ?, direccion = ?, correo_electronico = ?, telefono = ? WHERE id = ?'''
                   datos_clientes = (clave,nombre,direccion,correo_electronico,telefono,id_clientes)
                   cursor.execute(sql,datos_clientes)
                   conexion.commit()
                   print("Registro modificado correctamente")
                   print("-------------------------------------")
                else:
                    print("No hay registros con ese id")
                    print("--------------------------------------")
            else: 
                 print("No hay clientes para modificar")
                 print("--------------------------------------")
                                                
        except sqlite3.Error as error:
            print('Error al intentar modificar el registro: {}'.format(error))
        finally:
            if conexion:
                cursor.close()
                conexion.close()
                
    def modificarPedidos(self):
        try:
            conexion = self.baseDatos.abrirConexion()
            cursor = conexion.cursor()
                                            
            cursor.execute("SELECT * FROM pedidos pedidos")
            pedidos = cursor.fetchall()
            if len(pedidos) > 0:
                                                
                print("Lista de pedidos para modificar:")
                self.mostrarListaPedidos()
                print("-----------------------------------")
                id_pedidos = self.ingresarID("Ingresar el id del pedidos a modificar: \n")
                                                
                encontrar_pedidos = cursor.execute("SELECT * FROM pedidos WHERE id = ?",(id_pedidos,))
                pedidos = encontrar_pedidos.fetchone()
                if pedidos :
                   pedido,cliente,producto,precio = self.ingresarDatosPedidos()
                   sql = ''' UPDATE pedidos SET pedido = ?, cliente = ?, producto = ?, precio = ? WHERE id = ?'''
                   datos_pedidos = (pedido,cliente,producto,precio,id_pedidos)
                   cursor.execute(sql,datos_pedidos)
                   conexion.commit()
                   print("Registro modificado correctamente")
                   print("-------------------------------------")
                else:
                    print("No hay registros con ese id")
                    print("--------------------------------------")
            else: 
                 print("No hay pedidos para modificar")
                 print("--------------------------------------")
                                                
        except sqlite3.Error as error:
            print('Error al intentar modificar el registro: {}'.format(error))
        finally:
            if conexion:
                cursor.close()
                conexion.close()                     
                  
                                                
    def eliminarProducto(self):
        try:
            conexion = self.baseDatos.abrirConexion()
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM productos")
            productos = cursor.fetchall()
            if len(productos) > 0:
                                                            
               print("Lista de productos para eliminar:")
               self.mostrarListaProductos()
               print("---------------------------------------") 
               id_producto = self.ingresarID("Ingresar el id del producto a eliminar: \n")
                                                            
               encontrar_producto = cursor.execute("SELECT * FROM productos WHERE id = ?", (id_producto,))
               if len(encontrar_producto.fetchall()) ==1:
                   sql = '''DELETE FROM productos WHERE id = ?'''
                   cursor.execute(sql,(id_producto,))
                   conexion.commit()
                   print("Registro eliminado correctamente")
                   print("------------------------------------")
               else:
                     print("No hay registros con ese id")
                     print("--------------------------------")
            else:
                 print("No hay producto para eliminar")
                 print("---------------------------------")
                                                            
        except sqlite3.Error as error:
            print('Error al intentar eliminar el registro {}'.format(error))
        finally:
            if conexion:
                cursor.close()
                conexion.close()
                
    def eliminarClientes(self):
        try:
            conexion = self.baseDatos.abrirConexion()
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM clientes")
            clientes = cursor.fetchall()
            if len(clientes) > 0:
                                                            
               print("Lista de clientes para eliminar:")
               self.mostrarListaClientes()
               print("---------------------------------------") 
               id_clientes = self.ingresarID("Ingresar el id del clientes a eliminar: \n")
                                                            
               encontrar_clientes = cursor.execute("SELECT * FROM clientes WHERE id = ?", (id_clientes,))
               if len(encontrar_clientes.fetchall()) ==1:
                   sql = '''DELETE FROM clientes WHERE id = ?'''
                   cursor.execute(sql,(id_clientes,))
                   conexion.commit()
                   print("Registro eliminado correctamente")
                   print("------------------------------------")
               else:
                     print("No hay registro con ese id")
                     print("--------------------------------")
            else:
                 print("No hay clientes para eliminar")
                 print("---------------------------------")
                                                            
        except sqlite3.Error as error:
            print('Error al intentar eliminar el registro {}'.format(error))
        finally:
            if conexion:
                cursor.close()
                conexion.close()
    
    def eliminarPedidos(self):
        try:
            conexion = self.baseDatos.abrirConexion()
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM pedidos")
            pedidos = cursor.fetchall()
            if len(pedidos) > 0:
                                                            
               print("Lista de pedidos para eliminar:")
               self.mostrarListapedidos()
               print("---------------------------------------") 
               id_pedidos = self.ingresarID("Ingresar el id del pedidos a eliminar: \n")
                                                            
               encontrar_pedidos = cursor.execute("SELECT * FROM pedidos WHERE id = ?", (id_pedidos,))
               if len(encontrar_pedidos.fetchall()) ==1:
                   sql = '''DELETE FROM pedidos WHERE id = ?'''
                   cursor.execute(sql,(id_pedidos,))
                   conexion.commit()
                   print("Registro eliminado correctamente")
                   print("------------------------------------")
               else:
                     print("No hay registro con ese id")
                     print("--------------------------------")
            else:
                 print("No hay pedidos para eliminar")
                 print("---------------------------------")
                                                            
        except sqlite3.Error as error:
            print('Error al intentar eliminar el registro {}'.format(error))
        finally:
            if conexion:
                cursor.close()
                conexion.close()             
                           
                                                             
    def ingresarID(self,mensaje):
        id_producto = 0
        datos_incorrectos = True
        while datos_incorrectos:
           try:
               id_producto = int(input(mensaje))
               datos_incorrectos = False
           except Exception as e:
                print('Error al capturar el id del producto: {}'.format(e))
                print('Intente de nuevo ingresar el id \n')
                datos_incorrectos = True
        return id_producto
    
    def ingresarID(self,mensaje):
        id_clientes = 0
        datos_incorrectos = True
        while datos_incorrectos:
           try:
               id_clientes = int(input(mensaje))
               datos_incorrectos = False
           except Exception as e:
                print('Error al capturar el id del clientes: {}'.format(e))
                print('Intente de nuevo ingresar el id \n')
                datos_incorrectos = True
        return id_clientes
    
    def ingresarID(self,mensaje):
        id_pedidos = 0
        datos_incorrectos = True
        while datos_incorrectos:
           try:
               id_pedidos = int(input(mensaje))
               datos_incorrectos = False
           except Exception as e:
                print('Error al capturar el id del pedidos: {}'.format(e))
                print('Intente de nuevo ingresar el id \n')
                datos_incorrectos = True
        return id_pedidos
                                                                     
    def ingresarDatosProducto(self):
        datos_incorrectos = True
        while datos_incorrectos:
            try:
                nombre_producto= input("Ingresar el nombre del producto: \n")
                descripcion = input("Ingresar descripcion del producto: \n")
                precio = float(input("Ingresar el precio del producto:\n"))
                stock = int (input("Ingresar el stock del producto: \n"))
                datos_incorrectos = False
            except Exception as e:
                print('Error al capturar un dato: {}'.format(e))
                print('Intente de nuevo ingresar los datos \n')
                datos_incorrectos = True
        return nombre_producto,descripcion,precio,stock
    
    def ingresarDatosClientes(self):
        datos_incorrectos = True
        while datos_incorrectos:
            try:
                clave= int(input("Ingresar el clave del clientes: \n"))
                nombre= input("Ingresar el nombre del clientes: \n")
                direccion = input("Ingresar el direccion del clientes:\n")
                correo_electronico = input("Ingresar el correo_electronico del clientes: \n")
                telefono = int (input("Ingresar el telefono del clientes: \n"))
                datos_incorrectos = False
            except Exception as e:
                print('Error al capturar un dato: {}'.format(e))
                print('Intente de nuevo ingresar los datos \n')
                datos_incorrectos = True
        return clave,nombre,direccion,correo_electronico,telefono
    
    def ingresarDatospedidos(self):
        datos_incorrectos = True
        while datos_incorrectos:
            try:
                pedido= int(input("Ingresar el pedidos del clientes: \n"))
                cliente = input("Ingresar el nombre del clientes:\n")
                producto = input("Ingresar el producto del clientes: \n")
                precio = int(input("Ingresar el precio de los productos clientes: \n"))
                datos_incorrectos = False
            except Exception as e:
                print('Error al capturar un dato: {}'.format(e))
                print('Intente de nuevo ingresar los datos \n')
                datos_incorrectos = True
        return pedido,cliente,producto,precio                                                                   
class Autentificacion:
    def verificarAutentificacion(self):
        is_login =False
        while not is_login :
            usuario = input("Ingresar usuario: ")
            password = input("Ingresar contraseña: ")
            if usuario != 'admin' or password != '12345' :
                print ("Error de login")
            else:
                 is_login = True
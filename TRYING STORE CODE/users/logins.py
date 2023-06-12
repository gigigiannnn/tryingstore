def login():
    # Base de datos de usuarios registrados
    usuarios_registrados = {
        "gigigiannnn": "1371",
        "usuario2": "contraseña2",
        "usuario3": "contraseña3"
    }

    # Solicitar usuario y contraseña al usuario
    usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")

    # Validar usuario y contraseña
    if usuario in usuarios_registrados and contraseña == usuarios_registrados[usuario]:
        print("inicio de sesión existoso.puede ingresar")

    else:
        print("El nombre de usuario y/o contraseña son invalidos,por favor revise los datos")

# Ejecutar la función de inicio de sesión
login() 


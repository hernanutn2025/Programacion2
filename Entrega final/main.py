import basededatos
    
def main():
    conexion=basededatos.conectar_base()
    usuario=input(f"ingresar usuario")
    contraseña=input(f"ingresar contraseña")
    email=input(f"ingresar email")
    basededatos.registrar_usuario(conexion,usuario,contraseña,email)
    if conexion.is_connected():
            conexion.close()
            print("\nConexión a MySQL cerrada.")
    else:
        print("\nNo se pudo establecer la conexión a la base de datos.")
    
if __name__ == "__main__":
    main()
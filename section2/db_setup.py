import sqlite3


def crear_base_de_datos():
    conexion = sqlite3.connect('ejemplo.db')
    conexion.execute('''CREATE TABLE usuarios
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  nombre_usuario TEXT NOT NULL,
                  email TEXT NOT NULL,
                  contraseña TEXT NOT NULL)''')
    conexion.commit()
    conexion.close()


def insertar_datos_de_ejemplo():
    conexion = sqlite3.connect('ejemplo.db')
    conexion.executemany("INSERT INTO usuarios (nombre_usuario, email, contraseña) VALUES (?, ?, ?)",
                         [('admin', 'admin@example.com', 'contraseña'),
                          ('usuario1', 'usuario@gmail.com', '123456'),
                          ('usuario2', 'usuario2@gmail.com', 'contraseña2'),
                          ('usuario3', 'usuario3@gmail.com', 'contraseña3'),
                          ('usuario4', 'usuario4@gmail.com', 'contraseña4'),
                          ('usuario5', 'usuario5@gmail.com', 'contraseña5'),
                          ('usuario6', 'usuario6@gmail.com', 'contraseña6'),
                          ('usuario7', 'usuario7@gmail.com', 'contraseña7'),
                          ('usuario8', 'usuario8@gmail.com', 'contraseña8'),
                          ('usuario9', 'usuario9@gmail.com', 'contraseña9'),
                          ('usuario10', 'usuario10@gmail.com', 'contraseña10'),
                          ('usuario11', 'usuario11@gmail.com', 'contraseña11')])
    conexion.commit()
    conexion.close()


if __name__ == '__main__':
    crear_base_de_datos()
    insertar_datos_de_ejemplo()

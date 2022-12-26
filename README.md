# Proyecto Final | CoderHouse

Entrega del proyecto final para el curso de Python dictado por Coderhouse.

Desarrollado por: Jonathan Ezequiel Veltri
<br/>

### Demostración

<a href="https://www.youtube.com/watch?v=tkGzx7soNME&t=1s"><img src="https://i.ibb.co/mD2Tf6t/proyecto-final-1.jpg" style="height: 50%; width:50%;"/></a>

* [Introducción](https://www.youtube.com/watch?v=tkGzx7soNME&t=1s)
* [Federaciones](https://www.youtube.com/watch?v=tkGzx7soNME&t=31s)
* [Equipos](https://www.youtube.com/watch?v=tkGzx7soNME&t=108s)
* [Jugadores](https://www.youtube.com/watch?v=tkGzx7soNME&t=129s)
* [Editar Usuario](https://www.youtube.com/watch?v=tkGzx7soNME&t=168s)
* [Cambiar Contraseña](https://www.youtube.com/watch?v=tkGzx7soNME&t=185s)
* [Acerca De](https://www.youtube.com/watch?v=tkGzx7soNME&t=207s)

# Ejecutar proyecto

### 1. Abrir Git Bash para `Windows` o una terminal para `Linux`.

### 2. Crear directorio donde se va a alojar el proyecto
En este caso en particular se alojaría en la carpeta ProyectoFinal dentro de Documents
```bash
cd
mkdir -p Documents/ProyectoFinal
cd Documents/ProyectoFinal
ls 
```

- Clonar el proyecto
```bash
git clone https://github.com/jonathanveltri/ProyectoFinalCoderHouse-JonathanVeltri.git
cd ProyectoFinalCoderHouse-JonathanVeltri
```

### 3. Crear y activar entorno virtual
(Windows)
```bash
python -m venv venv
.\venv\Scripts\activate
```

(Linux)
```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Instalar las dependencias del proyecto
```bash
pip install -r requirements.txt
```

### 5. Se levanta el servidor de Django que expone el servicio por el localhost en el puerto 8000 por defecto `http://127.0.0.1:8000/`
```bash
python manage.py runserver
```


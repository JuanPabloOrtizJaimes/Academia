# Tarea4-Arquitectura_Sistema
Tecnología y atributos de calidad - Django

# Autores :man:  :man:  :girl:

- Juan Ortiz -1151498
- Jhonatan Calderon -1151624
- Angela Acevedo -1151628

# Requisitos:clipboard:
- Python 3.6 o posterior
- pip
- virtualenv
- Contenido del requirements.txt
  - asgiref==3.3.4
  - Django==3.2.2
  - gunicorn==20.1.0
  - pytz==2021.1
  - sqlparse==0.4.1


# Construido con :hammer:
+ Nube Amazon, aws :cloud:
+ Python3 :snake:
+ Django :unicorn:
+ SQLite3 :card_index_dividers:


# Instrucciones:arrow_left:

  Video guía: https://youtu.be/FGZ1omkxIUU

## Despliegue Nube aws:

### Creación de EC2
+ Crear instancia Amazon EC2 con Ubuntu server 20.04 LTS
+ Agregar los grupos de seguridad HTTP y HTTPS en sus puertos por defecto
+ Agregar grupo de seguridad TCP personalizado en el puerto 8000
+ Descargar par de claves(formato .pem)
+ Crear una ip elástica y asociarla a la EC2 recién creada

### Conexión SSH (Método 1-Putty)
+ Con el programa Puttygen cargamos la clave y generamos la clave privada que se descargará en una extensión .ppk
+ Con el programa Putty nos dirigimos a la parte de "Session" y en Host Name colocaremos la ip pública(elástica) de nuestra EC2
+ Seleccionamos el apartado "Conection", desplegamos el check-box de "SSH" y seleccionaremos "AUTH"
+ Cargamos la clave en el formato ppk que se convirtió anteriormente, damos clic en "Open" y clic en "si"
+ Escribiremos el usuario que para este caso es "ubuntu"
+ Y listo nos conectamos a nuestra EC2 por medio de Putty

### Conexión SSH (Método 2-Git Bash)
+ Seleccionamos nuestra EC2
+ En "Acciones" seleccionamos "Conectar"
+ Abrimos la consola de Git bash en la ruta donde tenemos guardada nuestra clave en formato .pem
+ Copiamos y pegamos en la consola de git Bash el comando `chmod 400 "nombre la clave sin comillas"` que nos aparece luego de seleccionar "Conectar" (Item3) en aws y damos Enter
+ Copiamos y pegamos en la consola de git Bash el comando `ssh -i "clave-aws-..." ubuntu@ec2...` que nos aparece en la sección de "Ejemplo" en la pagina de aws y damos Enter
+ Escribimos "yes" en la consola de git Bash
+ Y listo nos conectamos a nuestra EC2 por medio de git bash


### Instalación de paquetes y dependencias en la máquina virtual
Actualizar paquetes.
- sudo apt-get update
- sudo apt-get upgrade

Version de Python.
- sudo python --version
- sudo python3 --version

Version de Pip.
- pip3 --version

Instalar Pip.
- sudo apt install python3-pip
 
Instalar Entorno virtual.
- sudo pip3 install virtualenv

Crear entorno virtual.
- virtualenv Entorno_Virtual

Activar entorno virtual.
- source Entorno_Virtual/bin/activate

Instalamos git.
- git --version
- sudo apt install git
- git clone https://github.com/JuanPabloOrtizJaimes/Academia.git


Modificar archivos.
- cd Academia/Academia
- Ubicamos el archivo Settings.py
- Lo abrimos con el editor de texto nano
- Ejemplo: nano Settings.py
- Cambiamos el valor de ALLOWED_HOSTS = [''] y colocamos entre las comillas simples la direccion ip de la maquina de aws
- Ejemplo: ALLOWED_HOSTS = ['52.20.228.206']



Volver a la carpeta del proyecto.
 - cd ..

Listamos para ver si esta el archivo de  requirements.txt e instalamos las librerias que posea.
 - ls
 - nano requirements.txt
 - pip3 install -r requirements.txt 

Crear un super usuario.
 - python manage.py createsuperuser
        
En la carpeta del proyecto ejecutamos el servidor en el puerto 8000 que se establecio previamente.
 - gunicorn --bind 0.0.0.0:8000 Academia.wsgi:application

## Ejecutar Aplicación ✔️
- Nos dirigimos al navegador de preferencia y colocaremos la ip publica de nuestra maquina virtual de aws seguido del puerto y /admin.
- Ejemplo:52.20.228.206:8000/admin
- Y para loguearnos ingresamos las credenciales que creamos al crear el superusuario.

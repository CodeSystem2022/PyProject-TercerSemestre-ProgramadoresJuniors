# PyProject(TercerSemestre): ProgramadoresJuniors


# Introducción

Decidimos hacer el proyecto que habíamos hecho para Java en el 2do semestre, lo pasamos a python y agregamos los visto en este semestre. Ahora en vez de que la "base de datos" sea un array donde se guardaban las cuentas bancarias, usaremos postgres con pgAdmin para usar una base de datos real como las que hemos visto en clase.
<br>
<br>
<br>

# Como correr el código
<br/>

## Instalación de las dependencias
<br/>
Para ver los resultados puede bajar el repositorio en su pc y ejecutar lo siguiente:

```python
python -m virtualenv env
```

Esto creará un entorno virtual que luego activará con el siguiente comando:

```python
env\scripts\activate
```

Luego instale las dependencias del proyecto con lo siguiente:

```python
pip install -r requirements.txt
```
<br/>
<br/>

## Configuración de Base de Datos
<br/>
Una vez configurado el entorno cree una base de datos postgres (recomendamos llamarla BankApp) y ponga el nombre en el archivo postgres.py de la carpeta BankApp.

<br/>

Luevo cree un archivo .env en la raiz del proyecto para poner las credenciales como contraseña postgres. Dentro del archivo ponga la contraseña del usuario postgres de la siguiente forma:

```
PASSWORD_DB='YOUR_SECRET_PASSWORD'
```

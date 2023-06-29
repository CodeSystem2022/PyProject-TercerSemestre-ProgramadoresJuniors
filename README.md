# PyProject(TercerSemestre): ProgramadoresJuniors


# Introducción

Como proyecto de tercer semestre de Python, decidimos rehacer el proyecto planteado para Java en el 2do semestre, en el lenguaje Python, agregando los temas desarrollados este semestre. En este caso, en lugar de que la "base de datos" sea un array donde se guardaban las cuentas bancarias, usaremos postgres con pgAdmin como base de datos real, al igual que las vistas en clase.
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

A continuación instale las dependencias del proyecto con lo siguiente:

```python
pip install -r requirements.txt 
```
<br/>
<br/>

## Configuración de Base de Datos
<br/>
Una vez configurado el entorno, cree una base de datos postgres (recomendamos llamarla BankApp) y coloque el nombre en el archivo postgres.py de la carpeta BankApp.

<br/>

Finalmente cree un archivo .env en la raiz del proyecto para colocar las credenciales, como contraseña postgres. Dentro de dicho archivo introduzca la contraseña del usuario postgres de la siguiente forma:

```
PASSWORD_DB='YOUR_SECRET_PASSWORD'
```

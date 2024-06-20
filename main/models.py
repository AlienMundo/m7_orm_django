from django.db import models

# Create your models here.


#! Heredamos de la libreria models y MODEL es el modelo base de django
class Estudiante(models.Model):
  #! Es necesario especificar el max_length
  id = models.AutoField(primary_key=True)
  nombre = models.CharField(max_length=50)
  apellido = models.CharField(max_length=50)
  correo = models.EmailField(max_length=50)

#! luego creamos la migracion con python manage.py makemigrations

#! Despues de creada la migracion tenemos que ejecutarla/aplicarla con python manage.py migrate

#! En este caso se van a crear varias tablas a pesar de que solo creamos una, esto es porque vienen del sistema de autentificacion de django
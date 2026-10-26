from django.db import models

# Create your models here.




class Categoria(models.Model):

    nombre = models.CharField(max_length=120, null=False)
    tipo = models.CharField(max_length=100, unique=True)


    class meta:
        vorbose_name_plural = "Categorías"
        ordering = ["nombre"]
    
    def __str__(self) -> str:
        return f"Nombre: {self.nombre} Tipo: {self.tipo}"
    



class Cuenta(models.Model):

    usuario = models.CharField(max_length=80, unique=True)
    correo = models.EmailField(max_length=120, null=False)

    class meta:
        vorbose_name_plural = "cuentas"
        ordering = ["usuario"]
    
    def __str__(self) -> str:
        return f"Usuario: {self.usuario} Correo: {self.correo}"



class Personaje(models.Model):
    raza = models.CharField(max_length=20, null=False)
    descripcion = models.CharField(max_length=200)
    nivel = models.PositiveIntegerField(default=0, null=False)
    ban = models.BooleanField(default=False, null=False)
    creado = models.DateTimeField(auto_now_add=True, null=False)

    class meta:
        vorbose_name_plural = "personajes"
        ordering = ["nivel"]
    
    def __str__(self) -> str:
        return f"raza: {self.raza} Descripcion: {self.descripcion} Nivel: {self.nivel} Ban: {self.ban} Creado: {self.creado}"
    


#__________________________________________________________________________________________________________________________



class Item(models.Model):

    personaje_id = models.ForeignKey(Personaje, on_delete=models.CASCADE)
    categoria_id = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    nombre = models.CharField(max_length=100, null=False)
    descripcion = models.TextField(null=False)
    nivel = models.PositiveIntegerField(default=0, null=False)
    cantidad = models.PositiveIntegerField(default=1)

    class meta:
        vorbose_name_plural = "items"
        ordering = ["nombre"]
    
    def __str__(self) -> str:
        return f"Personaje_id: {self.personaje_id} Categoria_id: {self.categoria_id} Nombre: {self.nombre} Descripción: {self.descripcion} Nivel: {self.nivel} Cantidad: {self.cantidad}"
    

class Cuenta_personaje(models.Model):
    cuenta_id = models.ForeignKey(Cuenta, on_delete=models.CASCADE)
    personaje_id = models.ForeignKey(Personaje, on_delete=models.CASCADE)


    class meta:
        vorbose_name_plural = "cuenta_personajes"
        #ordering = ["cuenta_id"]
    
    def __str__(self) -> str:
        return f"Cuenta_id: {self.cuenta_id} Personaje_id: {self.personaje_id}"
    
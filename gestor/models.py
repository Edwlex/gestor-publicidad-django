from django.db import models

class Campaña(models.Model):
    nombre = models.CharField(max_length=200, verbose_name="Nombre de la campaña")
    fecha_inicio = models.DateField(verbose_name="Fecha de inicio")
    fecha_fin = models.DateField(verbose_name="Fecha de fin")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Campaña"
        verbose_name_plural = "Campañas"
        ordering = ['-fecha_inicio']


class Anuncio(models.Model):
    campana = models.ForeignKey(
        Campaña,
        on_delete=models.CASCADE,
        related_name='anuncios',
        verbose_name="Campaña"
    )
    titulo = models.CharField(max_length=200, verbose_name="Título del anuncio")
    imagen = models.ImageField(
        upload_to='anuncios/',
        verbose_name="Imagen del anuncio",
        help_text="Formatos permitidos: JPG, PNG, GIF"
    )

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Anuncio"
        verbose_name_plural = "Anuncios"
        ordering = ['-id']
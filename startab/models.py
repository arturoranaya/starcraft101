from django.db import models
from ckeditor.fields import RichTextField


class Entrada(models.Model):
    MATCH_LIST = [
        ('TvT', 'Terran vs Terran'),
        ('TvZ', 'Terran vs Zerg'),
        ('TvP', 'Terran vs Protoss'),
        ('PvP', 'Protoss vs Protoss'),
        ('PvT', 'Protoss vs Terran'),
        ('PvZ', 'Protoss vs Zerg'),
        ('ZvZ', 'Zerg vs Zerg'),
        ('ZvT', 'Zerg vs Terran'),
        ('ZvP', 'Zerg vs Protoss'),
    ]

    LIGA_LIST = [
        ('Br', 'Bronce'),
        ('Pl', 'Plata'),
        ('Or', 'Oro'),
        ('Pt', 'Platino'),
        ('Dm', 'Diamante'),
        ('Ms', 'Master'),
        ('GM', 'GrandMaster'),
    ]

    ESTADO_LIST = [
        ('A', 'Activo'),
        ('O', 'Obsoleto'),
    ]

    id = models.AutoField(primary_key=True)
    slug = models.CharField('Slug', max_length=100,
                            blank=False, null=False, default='entrada_sdfs')
    nombre = models.CharField('Nombre Build', max_length=100)
    match = models.CharField(
        max_length=3,
        choices=MATCH_LIST,
        default='TvT',
    )
    build_order = RichTextField()
    liga_main = models.CharField(
        max_length=2,
        choices=LIGA_LIST,
        default='Br',
    )
    liga_oponente = models.CharField(
        max_length=2,
        choices=LIGA_LIST,
        default='Br',
    )
    observaciones = RichTextField()
    tut_from = models.CharField('De', max_length=50)
    video = models.URLField('Video Clase', max_length=254)
    replay = models.URLField('Replay', max_length=254)
    estado = models.CharField(
        max_length=1,
        choices=ESTADO_LIST,
        default='A',
    )
    fecha_creacion = models.DateField(
        'Fecha de Creacion', auto_now=False, auto_now_add=True)

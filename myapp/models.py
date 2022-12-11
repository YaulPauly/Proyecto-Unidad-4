from django.db import models
# Create your models here.
#Tener en cuenta que es una clase
#El nombre de mi clase inicia siempre en mayuscula
#Esta clase debe heredar de model.Models 
class Portafolio(models.Model):
    url_image = models.URLField()
    title_proyecto = models.CharField(max_length= 50)
    description = models.CharField(max_length= 500)
    url_github = models.URLField()
    tag_html = models.CharField(max_length=50)
    tag_css = models.CharField(max_length=50)
    tag_script = models.CharField(max_length=50)
    tag_php = models.CharField(max_length=50)
    tag_python = models.CharField(max_length=50)
    tag_photo = models.CharField(max_length=50)



    
    

    

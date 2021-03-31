from django.db import models

# Create your models here.

# class Blog(models.Model):
#     name = models.CharField(max_length=100)
#     tagline = models.TextField()

#     def __str__(self):
#         return self.name
    
# class Author(models.Model):
#     name = models.CharField(max_length=200) 
#     email = models.EmailField()

#     def __str__(self):
#         return self.name

# class Entry(models.Model):
#     blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
#     headline = models.CharField(max_length=255)
#     body_textt = models.TextField()
#     pub_date = models.DateField()
#     authors = models.ManyToManyField(Author)
#     rating = models.IntegerField()

#     def __str__(self):
#         return self.headline
        
    
class Pregunta(models.Model):
    title = models.CharField(max_length=60)
    pregunta = models.TextField()

    class Meta:
        db_table = 'question'
        ordering = ['pk']
        verbose_name = 'La Pregunta'
        verbose_name_plural = 'Persona Pregunta'
        permissions = [
            ['autorizar_question',
            f'Permite Autorizar {verbose_name_plural}']
        ]

def __str__(self):
    return self.title

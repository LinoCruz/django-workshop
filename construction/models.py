from django.db import models

class Construction(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, verbose_name='Title')
    responsible  = models.CharField(max_length=255)
    status = models.CharField(max_length=255, verbose_name='Status')
    image = models.ImageField(upload_to='images/', null=True, verbose_name='Image')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()
    
    
    
from django.db import models
from categories.models import CategoryModel
# Create your models here.
class BookModel(models.Model):
    title=models.CharField(max_length=100)
    discription=models.TextField()
    borrowing_price=models.IntegerField()
    category=models.ForeignKey(CategoryModel,on_delete=models.CASCADE)
    image=models.ImageField(upload_to ='uploads/', blank=True, null= True)
    
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    books=models.ForeignKey(BookModel,on_delete=models.CASCADE,related_name='comments')
    name=models.CharField(max_length=50)
    email=models.EmailField()
    body=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True) #object creat hoyar sathe sathe date and time store hoye jabe
    
    
    def __str__(self):
        return f'comment by {self.name}'
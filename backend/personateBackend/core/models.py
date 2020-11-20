from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# class Person(User):
#     chal_win=models.IntegerField(default=0)
#     # user_id=models.ForeignKey(User,on_delete=models.CASCADE,related_name='userid')

#     def __str__(self):
#         return str(self.id)

#     class Meta:
#         db_table='person'

class Person(models.Model):
    chal_win=models.IntegerField(default=0)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    # user_id=models.ForeignKey(User,on_delete=models.CASCADE,related_name='userid')

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table='person'


class Challanges(models.Model):
     challanger_id=models.ForeignKey(User,on_delete=models.CASCADE,related_name='challanger_id')
     challanged_id=models.ForeignKey(User,on_delete=models.CASCADE,related_name='challanged_id')
     challanger_points=models.CharField(max_length=5000,default=0)
     challanged_points=models.CharField(max_length=5000,default=0)
     challanger_finish=models.BooleanField(default=False)
     challanged_finish=models.BooleanField(default=False)
     challanged_accepted=models.BooleanField(default=None)

     def __str__(self):
         return str(self.id)

     class Meta:
        db_table='Challanges'

class points_x_system(models.Model):
        user_id=models.ForeignKey(User,on_delete=models.CASCADE)
        data=models.DateTimeField(auto_now_add=True)
        points=models.IntegerField()
        difficulty=models.IntegerField()

        def __str__(self):
            return str(self.id)
        
        class Meta:
            db_table='points_x_system'

class system_images(models.Model):
        admin_id=models.ForeignKey(User,on_delete=models.CASCADE)
        url_img=models.ImageField(upload_to='personates')
        nome1=models.CharField(max_length=100)
        nome2=models.CharField(max_length=100)
        nome3=models.CharField(max_length=100)
        nome_certo=models.CharField(max_length=100,default='0')
        difficulty=models.IntegerField()

        def __str__(self):
            return str(self.id)
        
        class Meta:
            db_table='system_images'

class games_created(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    game_name=models.CharField(max_length=500)
    url_img1=models.ImageField(upload_to='personates')
    url_img2=models.ImageField(upload_to='personates')
    url_img3=models.ImageField(upload_to='personates')
    nome1_img1=models.TextField()
    nome2_img1=models.TextField()
    nome3_img1=models.TextField()
    nome1_img2=models.TextField()
    nome2_img2=models.TextField()
    nome3_img2=models.TextField()
    nome1_img3=models.TextField()
    nome2_img3=models.TextField()
    nome3_img3=models.TextField()
    nome_certo_img1=models.CharField(max_length=100,default='0')
    nome_certo_img2=models.CharField(max_length=100,default='0')
    nome_certo_img3=models.CharField(max_length=100,default='0')

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table='games_created'
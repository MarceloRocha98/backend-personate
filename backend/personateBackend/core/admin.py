from django.contrib import admin
from .models import Person
from .models import games_created
from .models import Challanges
from .models import points_x_system
from .models import system_images



# Register your models here.
@admin.register(Person)



class Person(admin.ModelAdmin):
    list_display=['id','chal_win']

@admin.register(games_created)
class games_created(admin.ModelAdmin):
    list_display=['id','user_id','url_img1','url_img2','url_img3','nome1_img1','nome2_img1','nome3_img1','nome1_img2','nome2_img2','nome3_img2','nome1_img3','nome2_img3','nome3_img3']

@admin.register(Challanges)
class Challanges(admin.ModelAdmin):
    list_display=['id','challanger_id','challanged_id','challanger_points','challanged_points','challanged_accepted']

@admin.register(points_x_system)
class points_x_system(admin.ModelAdmin):
    list_display=['id','data','points','difficulty']

@admin.register(system_images)
class system_images(admin.ModelAdmin):
    list_display=['id','admin_id','url_img','nome1','nome2','nome3','nome_certo','difficulty']
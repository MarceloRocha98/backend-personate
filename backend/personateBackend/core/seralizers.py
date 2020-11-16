from rest_framework import serializers
from .models import User, Person, games_created, Challanges, points_x_system


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=('id','email','username','password')

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields=('id','chal_win')

class GamesCreatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = games_created
        fields=('user_id','game_name','url_img1','url_img2','url_img3','nome1_img1','nome2_img1','nome3_img1','nome1_img2','nome2_img2','nome3_img2','nome1_img3','nome2_img3','nome3_img3')

class ChallangesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challanges
        fields=('challanger_id','challanged_id','challanger_points','challanged_points','challanger_finish','challanged_finish','challanged_accepted')

class PointsXSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = points_x_system
        fields=('id','user_id','data','points','difficulty')

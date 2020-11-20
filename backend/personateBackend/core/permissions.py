from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        # print(obj.user.id)
        # print(request.user.id)
        # print('teste')
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id


class PostOwnStatus(permissions.BasePermission):
    """Allow users to update their own status. """

    def has_object_permission(self,request,view,obj):
        # print(obj.user.id)
        print(request.user.id)
        print(obj.user_id.id)
        # print('teste')
        """Checks the users is trying to update their own status """

        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.user_id.id == request.user.id

class handleChallange(permissions.BasePermission):
    """Allow user challanged refuse the challange"""
    def has_object_permission(self,request,view,obj):
        print(obj.id)
        # print(obj.challanged_id)
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.id == request.user.id


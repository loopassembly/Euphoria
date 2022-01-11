from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    '''allow user to edit their own profile'''

    def has_object_permission(self, request, view, obj):
        '''chaeck user is trying to edit there own profile  '''
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id

class UpdateOwnStatus(permissions.BasePermission):
    '''alllow users to update their own status'''

    def has_object_permission(self, request, view, obj):
        '''check the user is trying to update thiir own status'''

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
 
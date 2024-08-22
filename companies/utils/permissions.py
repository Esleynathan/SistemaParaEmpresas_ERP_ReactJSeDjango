from rest_framework import permissions
from accounts.models import User_Groups, Group_Permissions
from django.contrib.auth.models import Permission

def check_permission(user, method, permission_to):
    if not user.is_authenticated:
        return False

    if user.is_owner:
        return True

    requierd_permission = 'views_'+permission_to
    if method == "POST":
        requierd_permission = 'add_'+permission_to
    if method == "PUT":
        requierd_permission = 'change_'+permission_to
    if method == "DELETE":
        requierd_permission = 'delete_'+permission_to

    groups = User_Groups.objects.values('group_id').filter(user_id=user.id).all()

    for group in groups:
        permissions = Group_Permissions.objects.values('permission_id').filter(group_id=group['group_id']).all()

        for permission in permissions:
            if Permission.objects.filter(id=permission['permission_id'], codename=requierd_permission).exists():
                return True

class EmployeePermission (permissions.BasePermission):
    message = 'O usuario não tem permissão para gerenciar os funcionários'

    def has_permission(self, request, _view):
        return check_permission(request.user, request.method, permission_to='employee')
        
class GroupPermission (permissions.BasePermission):
    message = 'O usuario não tem permissão para gerenciar os grupos'

    def has_permission(self, request, _view):
        return check_permission(request.user, request.method, permission_to='group')
        
class GroupPermissionsPermission (permissions.BasePermission):
    message = 'O usuario não tem permissão para gerenciar as permissões'

    def has_permission(self, request, _view):
        return check_permission(request.user, request.method, permission_to='permission')
        
class TaskPermission (permissions.BasePermission):
    message = 'O usuario não tem permissão para gerenciar as tarefas'

    def has_permission(self, request, _view):
        return check_permission(request.user, request.method, permission_to='task')
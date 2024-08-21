from rest_framework.exceptions import AuthenticationFailed, APIException

from django.contrib.auth.hashers import check_password, make_password
from accounts.models import User

from companies.models import Enterprise, Employee

class Authentication:
    def signin(self, email, password) -> User:
        user_exists = User.objects.filter(email=email).exists()

        if not user_exists:
            raise AuthenticationFailed('Email não encontrado.)')

        user = User.objects.filter(email=email).first()

        if not check_password(password, user.password):
            raise AuthenticationFailed('Senha invalída')

        return user

    def singnup(self, name, email, password, type_account='owner', company_id=False):
        if not name or name =='':
            raise APIException('O nome não deve ser null')

        if not email or email =='':
            raise APIException('O email não deve ser null')

        if not password or password =='':
            raise APIException('O password não deve ser null')

        if User.objects.filter(email=email).exists():            
            raise APIException('Este email já existe na plataforma')

        if type_account == 'employee' and not company_id:
            raise APIException('O id da empresa não deve ser null')

        password_hashed = make_password(password)

        created_user = User.objects.create(
            name=name,
            email=email,
            password=password_hashed,
            is_owner=0 if type_account == 'employee' else 1
        )

        if type_account == 'owner':
            Enterprise.objects.create(
                name='Nome da Empresa',
                user_id=created_user.id
            )

        if type_account == 'employee':
            Employee.objects.create(
                enterprise_id='Nome da Empresa',
                user_id=created_user.id
        )
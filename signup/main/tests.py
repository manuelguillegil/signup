from django.test import TestCase

from django.contrib.auth.models import User
from django.urls import resolve
from .views import registrarUsuario, ingresarUsuario
from .forms import IngresarUsuarioForm, RegistrarUsuarioForm
from .models import User_Information

# Create your tests here.

class Seguridad(TestCase):
    ## Caso de Prueba Frontera
    def test_igresar_usuario_campos_vacios(self):
        url = 'http://127.0.0.1:8000/ingresarUsuario/'
        data = {
            'email': '',
            'password1': ''
        }
        response = self.client.post(url, data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(ingresarUsuario(data['email'], data['password1']), False)

    ## Caso de Prueba Maliciosa
    def test_registrar_usuario_sin_arroba_email(self):
        url = 'http://127.0.0.1:8000/ingresarUsuario/'
        data = {
            'email': 'correo',
            'password1': '12345678',
            'password2': '12345678'
        }
        response = self.client.post(url, data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(registrarUsuario(data['email'], data['password1'],data['password2']), False)
    
    ## Caso de Prueba Maliciosa
    def test_registrar_usuario_con_arroba_email(self):
        url = 'http://127.0.0.1:8000/ingresarUsuario/'
        data = {
            'email': 'correo@',
            'password1': '12345678',
            'password2': '12345678'
        }
        response = self.client.post(url, data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(registrarUsuario(data['email'], data['password1'],data['password2']), False)

    ## Caso de Prueba Maliciosa
    def test_registrar_usuario_sin_punto_email(self):
        url = 'http://127.0.0.1:8000/ingresarUsuario/'
        data = {
            'email': 'correo@asdasd',
            'password1': '12345678',
            'password2': '12345678'
        }
        response = self.client.post(url, data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(registrarUsuario(data['email'], data['password1'],data['password2']), False)
    
    ## Caso de Prueba Maliciosa
    def test_registrar_usuario_sin_1punto_email(self):
        url = 'http://127.0.0.1:8000/ingresarUsuario/'
        data = {
            'email': 'correo@asdasd.',
            'password1': '12345678',
            'password2': '12345678'
        }
        response = self.client.post(url, data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(registrarUsuario(data['email'], data['password1'],data['password2']), False)

    ## Caso de Prueba Maliciosa
    def test_registrar_usuario_dominioinvalido_email(self):
        url = 'http://127.0.0.1:8000/ingresarUsuario/'
        data = {
            'email': 'correo@asdasd.ad',
            'password1': '12345678',
            'password2': '12345678'
        }
        response = self.client.post(url, data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(registrarUsuario(data['email'], data['password1'],data['password2']), False)
    
    ## Caso de Prueba Maliciosa
    def test_registrar_usuario_dospuntos_email(self):
        url = 'http://127.0.0.1:8000/ingresarUsuario/'
        data = {
            'email': 'correo@asdasd.com.',
            'password1': '12345678',
            'password2': '12345678'
        }
        response = self.client.post(url, data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(registrarUsuario(data['email'], data['password1'],data['password2']), False)

    ## Caso de Prueba Maliciosa
    def test_registrar_usuario_caracterinvalido_email(self):
        url = 'http://127.0.0.1:8000/ingresarUsuario/'
        data = {
            'email': 'corr"eo@asdasd.com.ve',
            'password1': '12345678',
            'password2': '12345678'
        }
        response = self.client.post(url, data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(registrarUsuario(data['email'], data['password1'],data['password2']), False)

    ## Caso de Prueba Maliciosa
    def test_registrar_usuario_sin_unpunto_email(self):
        url = 'http://127.0.0.1:8000/ingresarUsuario/'
        data = {
            'email': 'correo@asdasd.',
            'password1': '12345678',
            'password2': '12345678'
        }
        response = self.client.post(url, data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(registrarUsuario(data['email'], data['password1'],data['password2']), False)

    ## Caso de Prueba Frontera
    def test_registrar_usuario_campos_vacios(self):
        url = 'http://127.0.0.1:8000/ingresarUsuario/'
        data = {
            'email': '',
            'password1': '',
            'password2': ''
        }
        response = self.client.post(url, data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(registrarUsuario(data['email'], data['password1'], data['password2']), False)

    ## Caso de Prueba Malicia
    def test_igresar_usuario_que_no_existe(self):
        url = 'http://127.0.0.1:8000/ingresarUsuario/'
        data = {
            'email': 'emailQueNoExiste@noExiste.com',
            'password1': 'usuarioQueNoExiste'
        }
        response = self.client.post(url, data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(ingresarUsuario(data['email'], data['password1']), False)

    ## Caso de Prueba Malicia
    def test_registrar_usuario_con_contraseñas_que_no_coinciden(self):
        url = 'http://127.0.0.1:8000/ingresarUsuario/'
        data = {
            'email': 'usuario@gmail.com',
            'password1': 'qwerqwer',
            'password2': '1234'
        }
        response = self.client.post(url, data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(registrarUsuario(data['email'], data['password1'], data['password2']), False)

    ## Caso de Prueba Malicia
    def test_igresar_usuario_con_contraseña_invalida(self):
        url = 'http://127.0.0.1:8000/ingresarUsuario/'
        data = {
            'email': 'usuario@gmail.com',
            'password1': 'qwerqwer'
        }
        response = self.client.post(url, data)
        self.assertEquals(response.status_code, 200)

        user = User_Information(email = 'usuario@gmail.com', password = 'qwerqwer')
        user.save()
        self.assertEquals(ingresarUsuario(data['email'], 'contraseñaInvalida'), False)

if __name__ == '__main__':
    unittest.main(warnings='ignore')
from django.test import TestCase

from django.contrib.auth.models import User
from django.urls import resolve
from .views import registrarUsuario, ingresarUsuario
from .forms import IngresarUsuarioForm, RegistrarUsuarioForm
from .models import User_Information
import re

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
        url = 'http://127.0.0.1:8000/registrarUsuario/'
        data = {
            'email': 'correo',
            'password1': '12345678abC',
            'password2': '12345678abC'
        }
        response = self.client.post(url, data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(registrarUsuario(data['email'], data['password1'],data['password2']), False)
    
    ## Caso de Prueba Maliciosa
    def test_registrar_usuario_con_arroba_email(self):
        url = 'http://127.0.0.1:8000/registrarUsuario/'
        data = {
            'email': 'correo@',
            'password1': '12345678abC',
            'password2': '12345678abC'
        }
        response = self.client.post(url, data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(registrarUsuario(data['email'], data['password1'],data['password2']), False)

    ## Caso de Prueba Maliciosa
    def test_registrar_usuario_sin_punto_email(self):
        url = 'http://127.0.0.1:8000/registrarUsuario/'
        data = {
            'email': 'correo@asdasd',
            'password1': '12345678abC',
            'password2': '12345678abC'
        }
        response = self.client.post(url, data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(registrarUsuario(data['email'], data['password1'],data['password2']), False)

    ## Caso de Prueba Maliciosa
    def test_registrar_usuario_dominioinvalido_email(self):
        url = 'http://127.0.0.1:8000/registrarUsuario/'
        data = {
            'email': 'correo@asdasd.ad',
            'password1': '12345678abC',
            'password2': '12345678abC'
        }
        response = self.client.post(url, data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(registrarUsuario(data['email'], data['password1'],data['password2']), False)
    
    ## Caso de Prueba Maliciosa
    def test_registrar_usuario_dospuntos_email(self):
        url = 'http://127.0.0.1:8000/registrarUsuario/'
        data = {
            'email': 'correo@asdasd.com.',
            'password1': '12345678abC',
            'password2': '12345678abC'
        }
        response = self.client.post(url, data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(registrarUsuario(data['email'], data['password1'],data['password2']), False)

    ## Caso de Prueba Maliciosa
    def test_registrar_usuario_caracterinvalido_email(self):
        url = 'http://127.0.0.1:8000/registrarUsuario/'
        data = {
            'email': 'corr"eo@asdasd.com.ve',
            'password1': '12345678abC',
            'password2': '12345678abC'
        }
        response = self.client.post(url, data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(registrarUsuario(data['email'], data['password1'],data['password2']), False)

    ## Caso de Prueba Maliciosa
    def test_registrar_usuario_sin_unpunto_email(self):
        url = 'http://127.0.0.1:8000/registrarUsuario/'
        data = {
            'email': 'correo@asdasd.',
            'password1': '12345678abC',
            'password2': '12345678abC'
        }
        response = self.client.post(url, data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(registrarUsuario(data['email'], data['password1'],data['password2']), False)

    def test_registrar_usuario_min_tamano_password(self):
        url = 'http://127.0.0.1:8000/registrarUsuario/'
        data = {
            'email': 'correo@bien.com',
            'password1': 'aZb4567',
            'password2': 'aZb4567'
        }
        response = self.client.post(url, data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(registrarUsuario(data['email'], data['password1'],data['password2']), False)

    def test_registrar_usuario_max_tamano_password(self):
        url = 'http://127.0.0.1:8000/registrarUsuario/'
        data = {
            'email': 'correo@bien.com',
            'password1': 'aZb45678901234567',
            'password2': 'aZb45678901234567'
        }
        response = self.client.post(url, data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(registrarUsuario(data['email'], data['password1'],data['password2']), False)

    ## Caso de Prueba Maliciosa
    def test_registrar_usuario_sin_letras_password(self):
        url = 'http://127.0.0.1:8000/registrarUsuario/'
        data = {
            'email': 'correo@bien.com',
            'password1': '12345678',
            'password2': '12345678'
        }
        response = self.client.post(url, data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(registrarUsuario(data['email'], data['password1'],data['password2']), False)
    
    ## Caso de Prueba Maliciosa
    def test_registrar_usuario_con_una_letra_password(self):
        url = 'http://127.0.0.1:8000/registrarUsuario/'
        data = {
            'email': 'correo@bien.com',
            'password1': 'a12345678',
            'password2': 'a12345678'
        }
        response = self.client.post(url, data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(registrarUsuario(data['email'], data['password1'],data['password2']), False)

    ## Caso de Prueba Maliciosa
    def test_registrar_usuario_con_dos_letras_password(self):
        url = 'http://127.0.0.1:8000/registrarUsuario/'
        data = {
            'email': 'correo@bien.com',
            'password1': 'aZ12345678',
            'password2': 'aZ12345678'
        }
        response = self.client.post(url, data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(registrarUsuario(data['email'], data['password1'],data['password2']), False)

    ## Caso de Prueba Maliciosa
    def test_registrar_usuario_sin_minus_password(self):
        url = 'http://127.0.0.1:8000/registrarUsuario/'
        data = {
            'email': 'correo@bien.com',
            'password1': 'ABC12345678',
            'password2': 'ABC12345678'
        }
        response = self.client.post(url, data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(registrarUsuario(data['email'], data['password1'],data['password2']), False)

    ## Caso de Prueba Maliciosa
    def test_registrar_usuario_sin_mayus_password(self):
        url = 'http://127.0.0.1:8000/registrarUsuario/'
        data = {
            'email': 'correo@bien.com',
            'password1': 'abc12345678',
            'password2': 'abc12345678'
        }
        response = self.client.post(url, data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(registrarUsuario(data['email'], data['password1'],data['password2']), False)
    
    ## Caso de Prueba Maliciosa
    def test_registrar_usuario_sin_minus_password(self):
        url = 'http://127.0.0.1:8000/registrarUsuario/'
        data = {
            'email': 'correo@bien.com',
            'password1': 'ABC12345678',
            'password2': 'ABC12345678'
        }
        response = self.client.post(url, data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(registrarUsuario(data['email'], data['password1'],data['password2']), False)
    
    ## Caso de Prueba Maliciosa
    def test_registrar_usuario_sin_numeros_password(self):
        url = 'http://127.0.0.1:8000/registrarUsuario/'
        data = {
            'email': 'correo@bien.com',
            'password1': 'ABCasdcv',
            'password2': 'ABCasdcv'
        }
        response = self.client.post(url, data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(registrarUsuario(data['email'], data['password1'],data['password2']), False)
    
    ## Caso de Prueba Maliciosa
    def test_registrar_usuario_caracter_invalido_password(self):
        url = 'http://127.0.0.1:8000/registrarUsuario/'
        data = {
            'email': 'correo@bien.com',
            'password1': 'Aac.12345678',
            'password2': 'Aac.12345678'
        }
        response = self.client.post(url, data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(registrarUsuario(data['email'], data['password1'],data['password2']), False)

    ## Caso de Prueba Frontera
    def test_registrar_usuario_campos_vacios(self):
        url = 'http://127.0.0.1:8000/registrarUsuario/'
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
            'password1': 'usuarioQueNoExiste12'
        }
        response = self.client.post(url, data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(ingresarUsuario(data['email'], data['password1']), False)

    ## Caso de Prueba Malicia
    def test_registrar_usuario_con_contraseñas_que_no_coinciden(self):
        url = 'http://127.0.0.1:8000/registrarUsuario/'
        data = {
            'email': 'manuel@gmail.com',
            'password1': 'qwerqwer',
            'password2': '1234'
        }
        response = self.client.post(url, data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(registrarUsuario(data['email'], data['password1'], data['password2']), False)

    ## Caso de Prueba Malicia
    def test_registrar_usuario_exito(self):
        print("Hola pruebaa")
        url = 'http://127.0.0.1:8000/registrarUsuario/'
        data = {
            'email': 'manuel4@gmail.com',
            'password1': 'Hola1234',
            'password2': 'Hola1234'
        }
        response = self.client.post(url, data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(registrarUsuario('manuel@gmail.com', 'Hola1234', 'Hola1234'), True)

    ## Caso de Prueba Malicia
    def test_igresar_usuario_que_exito(self):
        url = 'http://127.0.0.1:8000/ingresarUsuario/'
        data = {
            'email': 'manuel@gmail.com',
            'password1': 'Hola1234'
        }
        user = User_Information(email='manuel@gmail.com', password='Hola1234')
        user.save()
        response = self.client.post(url, data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(ingresarUsuario(data['email'], data['password1']), True)

if __name__ == '__main__':
    unittest.main(warnings='ignore')
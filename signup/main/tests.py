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
    def test_igresar_usuario_con_contraseña_invalida(self):
        url = 'http://127.0.0.1:8000/ingresarUsuario/'
        data = {
            'email': 'usuario@gmail.com',
            'password1': 'qwerqwer'
        }
        response = self.client.post(url, data)
        self.assertEquals(response.status_code, 200)

        user = User_Information(id = 999, email = 'usuario@gmail.com', password = 'qwerqwer')
        user.save()
        self.assertEquals(ingresarUsuario(data['email'], 'contraseñaInvalida'), False)

if __name__ == '__main__':
    unittest.main(warnings='ignore')
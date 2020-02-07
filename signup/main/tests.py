from django.test import TestCase

from django.contrib.auth.models import User
from django.urls import resolve
from .views import registrarUsuario, ingresarUsuario
from .forms import IngresarUsuarioForm, RegistrarUsuarioForm

# Create your tests here.

class Seguridad(TestCase):
    ## Caso de Prueba Malicia
    def test_igresar_usuario_campos_vacios(self):
        url = 'http://127.0.0.1:8000/ingresarUsuario/'
        data = {
            'email': '',
            'password1': ''
        }
        response = self.client.post(url, data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(ingresarUsuario(data['email'], data['password1']), False)

if __name__ == '__main__':
    unittest.main(warnings='ignore')
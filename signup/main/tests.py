from django.test import TestCase

from django.contrib.auth.models import User
from django.urls import resolve
from .views import registrarUsuario, registrarUsuario
from .forms import IngresarUsuarioForm, RegistrarUsuarioForm

# Create your tests here.

class Seguridad(TestCase):
    def testCase01(self):
        url = 'http://127.0.0.1:8000/ingresarUsuario/'
        data = {
            'email': '',
            'password1': ''
        }
        response = self.client.post(url, data)
        self.assertEquals(response.status_code, 200)

if __name__ == '__main__':
    unittest.main(warnings='ignore')
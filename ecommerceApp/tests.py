# from django.test import TestCase

# Create your tests here.
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.contrib.sessions.middleware import SessionMiddleware
from django.http import HttpResponseRedirect
import json
from ecommerceApp.views import login_user, promoCodePage, register

class SampleTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', password='secret')

    def _add_session(self, request):
        middleware = SessionMiddleware(lambda r: None)
        middleware.process_request(request)
        request.session.save()
        return request

    def test_example(self):
        self.assertTrue(True)

    def test_login_success(self):
        payload = {'username': 'testuser', 'password': 'secret'}
        request = self.factory.post('/login/', data=json.dumps(payload), content_type='application/json')
        request = self._add_session(request)
        response = login_user(request)
        self.assertEqual(response.status_code, 302)
        # session should contain auth user id after login
        self.assertEqual(request.session.get('_auth_user_id'), str(self.user.pk))

    def test_login_missing_fields(self):
        payload = {'username': 'testuser'}  # missing password
        request = self.factory.post('/login/', data=json.dumps(payload), content_type='application/json')
        request = self._add_session(request)
        response = login_user(request)
        self.assertEqual(response.status_code, 200)
        content = response.content.decode()
        self.assertIn('Username or password is required', content)

    def test_login_invalid_credentials(self):
        payload = {'username': 'testuser', 'password': 'wrong'}
        request = self.factory.post('/login/', data=json.dumps(payload), content_type='application/json')
        request = self._add_session(request)
        response = login_user(request)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Invalid credentials', response.content.decode())

    def test_login_bad_json(self):
        request = self.factory.post('/login/', data='not-a-json', content_type='application/json')
        request = self._add_session(request)
        response = login_user(request)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Invalid request', response.content.decode())

    def test_promocode_page_get(self):
        request = self.factory.get('/promo/')
        response = promoCodePage(request)
        self.assertEqual(response.status_code, 200)

    def test_register_success(self):
        payload = {
            'username': 'newuser',
            'password': 'newpass',
            'first_name': 'First',
            'last_name': 'Last',
            'email': 'a@b.com'
        }
        request = self.factory.post('/register/', data=json.dumps(payload), content_type='application/json')
        request = self._add_session(request)
        response = register(request)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='newuser').exists())
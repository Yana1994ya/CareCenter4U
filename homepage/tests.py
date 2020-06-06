# Create your tests here.
from django.test import TestCase

from django.test import TestCase, client
from django.http import HttpRequest, HttpResponseRedirect
from users.models import Customer


class AdminTests(TestCase):
    
    def test_dummy(self):
        response = self.client.get('/')
        self.assertContains(response, '<body>')
     
    def test_dummy2(self):
        response = self.client.get('/')
        self.assertNotContains(response, '<body1>')
    
    def test_admin_logged_in(self):
        pword = "password"
        user_name = "admin_user"
        admin_user = Customer.objects.create_superuser(username=user_name, password=pword)
        self.client.login(username=user_name, password=pword)
        response = self.client.get('/')
        self.assertContains(response, '<a href="/admin/" class="button">Admin</a>')
    
    
    def test_not_admin_logged_in(self):
        pword = "password"
        user_name = "not_admin_user"
        not_admin_user = Customer.objects.create(username=user_name, password=pword)
        #client login
        self.client.login(username=user_name, password=pword)
        response = self.client.get('/')
        self.assertNotContains(response, '<a href="/admin/" class="button">Admin</a>')

    def test_login_simple_user(self):
        pword = "password"
        user_name = "not_admin_user"
        not_admin_user = Customer.objects.create(username=user_name, password=pword)
        self.client.login(username=user_name, password=pword)
        response = self.client.get('/users/login')
        self.assertNotContains(response, '<a href="/admin/" class="button">Admin</a>')    
   
    def test_login_contains_homepage(self):
        pword = "password"
        user_name = "admin_user"
        admin_user = Customer.objects.create_superuser(username=user_name, password=pword)
        self.client.login(username=user_name, password=pword)
        response = self.client.get('/')
        self.assertContains(response, '<a href="/admin/" class="button">Admin</a>')   

    def test_login_simple_user_contains_homepage(self):
        pword = "password"
        user_name = "not_admin_user"
        not_admin_user = Customer.objects.create(username=user_name, password=pword)
        self.client.login(username=user_name, password=pword)
        response = self.client.get('/users/login')
        self.assertContains(response, '<a href="/" class="button">Homepage</a>')  
        
    def test_login_admin(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST = {
            'username': '11112222A',
            'password': 'password',
        } 
        response = Customer(request)
        self.assertNotIsInstance(response, HttpResponseRedirect)
        self.assertEqual(Customer.objects.filter(password='password').count(), 0, 'The admin login.')
 
        
    def test_login_permission_assert_false(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST = {
            'username': '11112222A',
            'password': 'password',
        } 
        response = Customer(request)
        self.assertNotIsInstance(response, HttpResponseRedirect)
        admin = Customer.objects.get(username='11112222A')
        self.assertTrue(
            admin.check_password('password'),
            'Failed to verify password.'
        )
        admin = Customer.objects.get(username='11112222A')
        self.assertTrue(admin.check_password('password'), 'Failed to verify password.')
        self.assertFalse(admin.citizen)
        self.assertFalse(admin.secretary)
        
    def test_login_permission_assert_true(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST = {
            'username': '11112222A',
            'password': 'password',
        } 
        response = Customer(request)
        self.assertNotIsInstance(response, HttpResponseRedirect)
        admin = Customer.objects.get(username='11112222A')
        self.assertTrue(
            admin.check_password('password'),
            'Failed to verify password.'
        )
        admin = Customer.objects.get(username='11112222A')
        self.assertTrue(admin.check_password('password'), 'Failed to verify password.')
        self.assertTrue(admin.is_active)
        self.assertTrue(admin.is_superuser)
        

    def test_login_assert(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST = {
            'username': '11112222A',
            'password': 'password',
        } 
        response = Customer(request)
        self.assertNotIsInstance(response, HttpResponseRedirect)
        admin = Customer.objects.get(username='11112222A')
        self.assertTrue(admin.check_password('password'), 'Failed to verify password.')
        self.assertGreaterEqual(Customer.objects.filter(password='password').count(), 0, "not Greater equal")
        self.assertLess(Customer.objects.filter(password='password').count(), 20, "not Greater equal")
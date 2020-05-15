from django.test import TestCase
from .models import Commdisaster
from Wordprocessing.views import home_page
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

# Create your tests here.
class TestModel(TestCase):
    def test_write(self):
        temp = Commdisaster.objects.all()
        self.assertEqual(temp.count(),3)
        # self.assertEqual(temp[0].name,'yml')
        
    def test_resolve_to_home_page_view(self):
        found=resolve('/')
        self.assertEqual(found.func,home_page)
    
    def test_home_page_return_correct_html(self):
        reponse=self.client.get('/')
        
        html=response.content.decode('utf8')
        self.assertTrue(html.startwith('<html>'))
        self.assertTrue(html.strip().endwith('</html>'))
        
        self.assertTemplateUsed(reponse,'index.html')
from django.test import TestCase
from .models import Composite
# Create your tests here.

class CompositionModelTests(TestCase):
    def test_add_new_composite(self):
        '''
        TEST add new composite
        '''
        composite = Composite('食物','fyyc','喜欢苹果')
        composite.save()
        return True

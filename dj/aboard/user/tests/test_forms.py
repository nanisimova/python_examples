from django.test import TestCase

from user.forms import UserUpdateForm

class UserUpdateFormTest(TestCase):

    def test_user_form_fields(self):
        form = UserUpdateForm()
        self.assertTrue(form.fields['first_name'])
        self.assertTrue(form.fields['last_name'])
        self.assertTrue(form.fields['email'])

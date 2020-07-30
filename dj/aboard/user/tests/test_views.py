from django.test import TestCase


class UserViewTest(TestCase):

    def test_view_user_create_url(self): 
        resp = self.client.get('/user/create')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'user/create.html')

    def test_view_user_delete_url(self):.
        resp = self.client.get('/user/delete')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'user/delete.html')

    def test_view_user_update_url(self):.
        resp = self.client.get('/user/update')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'user/update.html')

    def test_view_user_view_url(self):
        resp = self.client.get('/user/view')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'user/view.html')

    def test_view_user_change_password_url(self):
        resp = self.client.get('/user/change_password')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'user/change_password.html')

#        self.assertTrue('is_paginated' in resp.context)
#        self.assertTrue(resp.context['is_paginated'] == True)
#        self.assertTrue( len(resp.context['author_list']) == 10)


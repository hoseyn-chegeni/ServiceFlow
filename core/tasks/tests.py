from django.test import TestCase
from accounts.models import User
from .models import TaskStatus
from django.urls import reverse, resolve
from .views.status import StatusCreateView,StatusDeleteView ,StatusDetailView ,StatusListView ,StatusUpdateView 

# Create your tests here.

#-----MODELS-----

class TaskStatusModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='admin@admin.com', password='testpassword')
        self.status = TaskStatus.objects.create(
            name='Test Status',
            created_by=self.user,
            description='Test Description'
        )

    def test_task_status_creation(self):
        self.assertEqual(self.status.name, 'Test Status')
        self.assertEqual(self.status.created_by, self.user)
        self.assertEqual(self.status.description, 'Test Description')
        self.assertTrue(self.status.is_active)
        self.assertIsNotNone(self.status.created_at)
        self.assertIsNotNone(self.status.updated_at)

    def test_task_status_str_method(self):
        self.assertEqual(str(self.status), 'Test Status')

    def test_task_status_is_active_default(self):
        self.assertTrue(self.status.is_active)

    def test_task_status_unicode_method(self):
        self.assertEqual(str(self.status), 'Test Status')




#-----VIEWS-----


class TaskStatusViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='admin@amdin.com', password='testpassword')
        self.status = TaskStatus.objects.create(
            name='Test Status',
            created_by=self.user,
            description='Test Description'
        )

    def test_task_status_list_view(self):
        response = self.client.get(reverse('tasks:list_status'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Status')

    def test_task_status_detail_view(self):
        response = self.client.get(reverse('tasks:detail_status', args=[self.status.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Status')

    def test_task_status_create_view(self):
        response = self.client.get(reverse('tasks:create_status'))
        self.assertEqual(response.status_code, 200)

    def test_task_status_update_view(self):
        response = self.client.get(reverse('tasks:update_status', args=[self.status.pk]))
        self.assertEqual(response.status_code, 200)

    def test_task_status_delete_view(self):
        response = self.client.get(reverse('tasks:delete_status', args=[self.status.pk]))
        self.assertEqual(response.status_code, 200)



# -----URLS-----
        

class TaskStatusURLTest(TestCase):
    def test_task_status_list_url(self):
        url = reverse('tasks:list_status')
        self.assertEqual(resolve(url).func.view_class, StatusListView)

    def test_task_status_detail_url(self):
        url = reverse('tasks:detail_status', args=[1])
        self.assertEqual(resolve(url).func.view_class, StatusDetailView)

    def test_task_status_create_url(self):
        url = reverse('tasks:create_status')
        self.assertEqual(resolve(url).func.view_class, StatusCreateView)

    def test_task_status_update_url(self):
        url = reverse('tasks:update_status', args=[1])
        self.assertEqual(resolve(url).func.view_class, StatusUpdateView)

    def test_task_status_delete_url(self):
        url = reverse('tasks:delete_status', args=[1])
        self.assertEqual(resolve(url).func.view_class, StatusDeleteView)




from django.test import TestCase
from datetime import datetime
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Bug
from .views import index, register_bug, view_bug, bug_list, bug_link


'''Testing of Views and Models of a Bug App'''


class BugModelTestCase(TestCase):
    '''Test case for the Bug model.'''
    def test_bug_creation(self):
        '''test case checks if a Bug instance can be created with the specified attributes'''
        bug = Bug.objects.create(
            description="Test Bug",
            bug_type="error",
            report_date=datetime.now().date(),
            status="todo"
        )
        bug.save()
        self.assertEqual(bug.description, "Test Bug")
        self.assertEqual(bug.bug_type, "error")
        self.assertEqual(bug.status, "todo")


    def test_default_values(self):
        '''Test that a Bug model instance is created with default values'''
        bug = Bug(description="Test Bug")
        bug.save()
        self.assertEqual(bug.bug_type, "error")
        self.assertEqual(bug.status, "todo")


    def test_str_method(self):
        '''Test the __str__ method of the Bug model.'''
        bug = Bug(description="Test Bug")
        bug.save()
        self.assertEqual(str(bug), "Test Bug")

    def test_int_method(self):
        '''Test if the `description` field of the `Bug` model accepts and stores an integer value.'''
        bug = Bug(description=23)
        bug.save()
        self.assertEqual(int(23), 23)


    # Views Testing: The functions below tested the views in the Bug App


    def test_register_bug_view(self):
        '''Test the 'register_bug' view.'''
        self.client.login(description="Test Bug", bug_type="error", status="todo")
        response = self.client.get(reverse('register_bug'))
        self.assertEqual(response.status_code, 200)


    def test_view_bug_view(self):
        '''
        Test the 'view_bug' view function and verifies that the 'view_bug' view correctly displays the details of a bug.
        '''
        bug = Bug.objects.create(
            description="Test Bug",
            bug_type="error",
            report_date=datetime.now().date(),
            status="todo"
        )                                                                
        response = self.client.get(reverse('view_bug', args=[bug.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Bug")


    def test_bug_list_view(self):
        '''Test that the 'bug_list' view correctly displays a list of registered bugs'''
        bug = Bug.objects.create(
            description="Test Bug",
            bug_type="error",
            report_date=datetime.now().date(),
            status="todo"
            )

        response = self.client.get(reverse('bug_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Bug")


    def test_bug_link_view(self):
        '''
        Test that the 'bug_list' view correctly displays a list of registered bugs, with links to details of each bug
        '''
        bug = Bug.objects.create(
            description="Test Bug",
            bug_type="error",
            report_date=datetime.now().date(),
            status="todo"
            )
        response = self.client.get(reverse('bug_list_link'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Bug")



from django.test import TestCase
from django.urls import reverse
from shop.models import User
from django.utils import timezone  # Import timezone utilities
# from django.contrib.auth.models import User
from django.test import Client
from shop.models import CartObject, Order, ItemInventory, Item
# class SignUpTests(TestCase):

#     def setUp(self):
#         self.client = Client()
#         self.signup_url = reverse('signup')

#     def test_signup_success(self):
#         # Test signing up with valid credentials
#         response = self.client.post(self.signup_url, {
#             'username': 'testuser',
#             'email': 'test@example.com',
#             'password': 'TestPass123',
#             'confirmpassword': 'TestPass123'
#         })
#         self.assertRedirects(response, reverse('login'))

#         # Check if the user was created
#         user_created = User.objects.filter(username='testuser', email='test@example.com').exists()
#         self.assertTrue(user_created)

#     def test_signup_password_mismatch(self):
#         # Test signing up with passwords that do not match
#         response = self.client.post(self.signup_url, {
#             'username': 'testuser2',
#             'email': 'test2@example.com',
#             'password': 'TestPass123',
#             'confirmpassword': 'MismatchPass123'
#         })
#         self.assertContains(response, 'Passwords do not match')

#         # Check if the user was not created
#         self.assertFalse(User.objects.filter(username='testuser2').exists())

#     def test_signup_existing_username(self):
#         # Create a user with a specific username
#         # User.objects.create_user('existinguser', 'existing@example.com', 'ExistingPass123')
#         User.objects.create_user('existinguser', 'ExistingPass123')
#         # Test signing up with an existing username
#         response = self.client.post(self.signup_url, {
#             'username': 'existinguser',
#             'email': 'test3@example.com',
#             'password': 'TestPass123',
#             'confirmpassword': 'TestPass123'
#         })
#         self.assertContains(response, 'Username already exists')

#         # Check if the user was not created
#         self.assertFalse(User.objects.filter(email='test3@example.com').exists())

#     def test_signup_existing_email(self):
#         # Create a user with a specific email
#         # User.objects.create_user('testuser3', 'existing@example.com', 'TestPass123')
#         User.objects.create_user('testuser3', 'TestPass123')
#         # Test signing up with an existing email
#         response = self.client.post(self.signup_url, {
#             'username': 'testuser4',
#             'email': 'existing@example.com',
#             'password': 'TestPass123',
#             'confirmpassword': 'TestPass123'
#         })
#         self.assertContains(response, 'Email already exists')

#         # Check if the user was not created
#         self.assertFalse(User.objects.filter(username='testuser4').exists())  


# class SaveOrderTestCase(TestCase):

#     def setUp(self):
#         self.client = Client()
#         self.user = User.objects.create_user(username='testuser', password='testpassword')
#         self.client.login(username='testuser', password='testpassword')

#         # Create some items for testing
#         self.item1 = Item.objects.create(title='Item 1', description='Description 1', price=50)
#         self.item2 = Item.objects.create(title='Item 2', description='Description 2', price=70)

#         self.item_inv1 = ItemInventory.objects.create(item=self.item1, quantity=2, user=self.user)
#         self.item_inv2 = ItemInventory.objects.create(item=self.item2, quantity=1, user=self.user)

#     def test_save_order_authenticated_user_empty_cart(self):
#         self.item_inv1.delete()
#         self.item_inv2.delete()

#         response = self.client.post(reverse('save_order'))

#         self.assertEqual(response.status_code, 302)  # Check if redirected after saving order
#         self.assertEqual(CartObject.objects.count(), 0)  # Check if cart is empty after saving order

#         # You can add more assertions based on your logic after the order is saved

#     def test_save_order_authenticated_user_non_empty_cart(self):
#         response = self.client.post(reverse('save_order'))

#         self.assertEqual(response.status_code, 302)  # Check if redirected after saving order
#         self.assertEqual(CartObject.objects.count(), 0)  # Check if cart is empty after saving order

#         # Add more assertions based on your logic after the order is saved

#     def test_save_order_unauthenticated_user(self):
#         self.client.logout()  # Logout the user

#         response = self.client.post(reverse('save_order'))

#         self.assertEqual(response.status_code, 302)  # Check if redirected to login page

#         # You can add more assertions for behavior when the user is not authenticated

#     # Add more test cases as needed


class SaveOrderTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        # Create some items for testing
        self.item1 = Item.objects.create(title='Item 1', description='Description 1', price=50)
        self.item2 = Item.objects.create(title='Item 2', description='Description 2', price=70)

        self.item_inv1 = ItemInventory.objects.create(item=self.item1, quantity=2, user=self.user)
        self.item_inv2 = ItemInventory.objects.create(item=self.item2, quantity=1, user=self.user)

    def test_save_order_authenticated_user_empty_cart(self):
        self.item_inv1.delete()
        self.item_inv2.delete()

        
        ordered_time = timezone.now()

        response = self.client.post(reverse('save_order'), {'ordered_time': ordered_time})  

        self.assertEqual(response.status_code, 302)  
        self.assertEqual(CartObject.objects.count(), 0)  

        

    def test_save_order_authenticated_user_non_empty_cart(self):
     
        ordered_time = timezone.now()

        response = self.client.post(reverse('save_order'), {'ordered_time': ordered_time}) 

        self.assertEqual(response.status_code, 302) 
        self.assertEqual(CartObject.objects.count(), 0) 

    

    def test_save_order_unauthenticated_user(self):
        self.client.logout()  

       
        ordered_time = timezone.now()

        response = self.client.post(reverse('save_order'), {'ordered_time': ordered_time}) 

        self.assertEqual(response.status_code, 302) 

        





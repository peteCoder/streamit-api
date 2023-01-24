from django.test import TestCase
from api.models import Profile
from users.models import CustomUser

class TestUserProfile(TestCase):
    
    def setUp(self):
        CustomUser.objects.create_user(
            email="daniel@gmail.com",
            password="mypasswordgood"
        )
        
        self.user = CustomUser.objects.get(id=1)
        self.profile = Profile.objects.get(id=1)
        
        self.base_url = 'http://127.0.0.1:8000/api'
        
    def tearDown(self):
        return super().tearDown()
    
    def test_user_profile_exists(self):
        profile = Profile.objects.get(id=1)
        user = CustomUser.objects.get(id=1)
        self.assertEqual(profile.user_id, user.id)
        
    def test_retrieve_user_and_profile_list(self):
        user_list = self.client.get(f'{self.base_url}/user/')
        profile_list = self.client.get(f'{self.base_url}/profile/')
        
        user_data = user_list.data
        profile_data = profile_list.data
        
        self.assertIsInstance(user_data, list)
        self.assertIsInstance(profile_data, list)
        
        self.assertEqual(user_list.status_code, 200)
        self.assertEqual(profile_list.status_code, 200)
        
    def test_retrieve_single_user_and_profile(self):
        single_user = self.client.get(f'{self.base_url}/user/1/')
        single_profile = self.client.get(f'{self.base_url}/profile/1/')
        
        user_data = single_user.data
        profile_data = single_profile.data
        
        self.assertIsInstance(user_data, dict)
        self.assertIsInstance(profile_data, dict)
        
        self.assertEqual(single_user.status_code, 200)
        self.assertEqual(single_profile.status_code, 200)
        
        
    
    



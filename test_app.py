import unittest
import json
from test import app

class TestFlaskApp(unittest.TestCase):
    
    def setUp(self):
        """Set up test client before each test"""
        self.app = app.test_client()
        self.app.testing = True
    
    def test_home_page_status_code(self):
        """Test that the home page returns 200 status code"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_home_page_content_type(self):
        """Test that the home page returns HTML content"""
        response = self.app.get('/')
        self.assertIn('text/html', response.content_type)
    
    def test_home_page_contains_name(self):
        """Test that the home page contains the personal name"""
        response = self.app.get('/')
        self.assertIn(b'Udit Raj Parihar', response.data)
    
    def test_home_page_contains_phone(self):
        """Test that the home page contains the phone number"""
        response = self.app.get('/')
        self.assertIn(b'+1 (226) 123-1234', response.data)
    
    def test_api_info_status_code(self):
        """Test that the API endpoint returns 200 status code"""
        response = self.app.get('/api/info')
        self.assertEqual(response.status_code, 200)
    
    def test_api_info_content_type(self):
        """Test that the API endpoint returns JSON content"""
        response = self.app.get('/api/info')
        self.assertIn('application/json', response.content_type)
    
    def test_api_info_structure(self):
        """Test that the API returns the expected JSON structure"""
        response = self.app.get('/api/info')
        data = json.loads(response.data)
        
        # Check that required keys exist
        self.assertIn('name', data)
        self.assertIn('phone', data)
        
        # Check data types
        self.assertIsInstance(data['name'], str)
        self.assertIsInstance(data['phone'], str)
        
        # Check specific values
        self.assertEqual(data['name'], 'Udit Raj Parihar')
        self.assertEqual(data['phone'], '+1 (226) 123-1234')
    
    def test_api_info_json_format(self):
        """Test that the API returns valid JSON"""
        response = self.app.get('/api/info')
        try:
            json.loads(response.data)
        except json.JSONDecodeError:
            self.fail("API response is not valid JSON")
    
    def test_nonexistent_route(self):
        """Test that non-existent routes return 404"""
        response = self.app.get('/nonexistent')
        self.assertEqual(response.status_code, 404)
    
    def test_home_page_has_profile_icon(self):
        """Test that the home page contains the profile icon emoji"""
        response = self.app.get('/')
        self.assertIn('👤'.encode('utf-8'), response.data)
    
    def test_home_page_has_phone_link(self):
        """Test that the phone number is rendered as a clickable link"""
        response = self.app.get('/')
        self.assertIn(b'href="tel:', response.data)

class TestPersonalInfoData(unittest.TestCase):
    """Test the personal information data structure"""
    
    def test_personal_info_import(self):
        """Test that personal info can be imported from the main module"""
        from test import PERSONAL_INFO
        
        self.assertIsInstance(PERSONAL_INFO, dict)
        self.assertIn('name', PERSONAL_INFO)
        self.assertIn('phone', PERSONAL_INFO)
    
    def test_personal_info_values(self):
        """Test the specific values in personal info"""
        from test import PERSONAL_INFO
        
        self.assertEqual(PERSONAL_INFO['name'], 'Udit Raj Parihar')
        self.assertEqual(PERSONAL_INFO['phone'], '+1 (226) 123-1234')

if __name__ == '__main__':
    # Run the tests
    unittest.main(verbosity=2) 
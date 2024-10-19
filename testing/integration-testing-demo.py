# test_app.py
import unittest
import json
from app import app

class TodoAppIntegrationTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.app = app.test_client()
        cls.app.testing = True

    def test_add_and_retrieve_task(self):
        # Step 1: Add a new task
        new_task = {'description': 'Buy groceries'}
        response = self.app.post('/tasks', data=json.dumps(new_task), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertTrue(response.json['success'])
        task_id = response.json['task']['id']

        # Step 2: Retrieve all tasks
        response = self.app.get('/tasks')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json['success'])
        self.assertEqual(len(response.json['tasks']), 1)
        self.assertEqual(response.json['tasks'][0]['id'], task_id)
        self.assertEqual(response.json['tasks'][0]['description'], 'Buy groceries')
        self.assertEqual(response.json['tasks'][0]['status'], 'pending')

if __name__ == '__main__':
    unittest.main()

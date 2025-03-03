from dotenv import load_dotenv
import os
import requests

class AzureDevOpsTestClient:
    def __init__(self):
        load_dotenv()
        self.base_url = "https://jsonplaceholder.typicode.com"  # Free test API
        
    def create_test_case(self, title, description, steps):
        """
        Create a test case in Azure DevOps
        """
        try:
            # Using JSONPlaceholder's post endpoint as a mock
            payload = {
                'title': title,
                'body': description,
                'steps': steps
            }
            
            response = requests.post(f"{self.base_url}/posts", json=payload)
            return response.json()
        except Exception as e:
            print(f"Error creating test case: {str(e)}")
            return None

    def get_test_results(self, test_run_id):
        """
        Get test results for a specific test run
        """
        try:
            # Using JSONPlaceholder's get endpoint as a mock
            response = requests.get(f"{self.base_url}/posts/{test_run_id}")
            return response.json()
        except Exception as e:
            print(f"Error getting test results: {str(e)}")
            return None

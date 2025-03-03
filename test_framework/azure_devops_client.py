from azure.devops.connection import Connection
from azure.devops.v7_1.test.test_client import TestClient
from msrest.authentication import BasicAuthentication
import os
from dotenv import load_dotenv

class AzureDevOpsTestClient:
    def __init__(self):
        load_dotenv()
        self.organization_url = os.getenv('AZURE_DEVOPS_ORG_URL')
        self.pat = os.getenv('AZURE_DEVOPS_PAT')
        self.project = os.getenv('AZURE_DEVOPS_PROJECT')
        
        # Create a connection to Azure DevOps
        credentials = BasicAuthentication('', self.pat)
        self.connection = Connection(base_url=self.organization_url, creds=credentials)
        
        # Get the test client
        self.test_client = self.connection.clients.get_test_client()

    def create_test_case(self, title, description, steps):
        """
        Create a test case in Azure DevOps
        """
        try:
            test_case = {
                'name': title,
                'description': description,
                'steps': steps
            }
            
            # Create the test case
            created_test_case = self.test_client.create_test_case(self.project, test_case)
            return created_test_case
        except Exception as e:
            print(f"Error creating test case: {str(e)}")
            return None

    def get_test_results(self, test_run_id):
        """
        Get test results for a specific test run
        """
        try:
            test_results = self.test_client.get_test_results(
                self.project,
                test_run_id
            )
            return test_results
        except Exception as e:
            print(f"Error getting test results: {str(e)}")
            return None

import pytest
from test_framework.azure_devops_client import AzureDevOpsTestClient
from test_framework.ai_test_analyzer import AITestAnalyzer

class TestSampleFeature:
    @pytest.fixture
    def azure_client(self):
        return AzureDevOpsTestClient()

    @pytest.fixture
    def ai_analyzer(self):
        return AITestAnalyzer()

    def test_feature_with_ai_analysis(self, azure_client, ai_analyzer):
        # Sample feature description
        feature_description = """
        User authentication feature:
        - Users should be able to login with valid credentials
        - System should handle invalid credentials appropriately
        - Password reset functionality should be available
        """

        # Generate test cases using AI
        test_cases = ai_analyzer.generate_test_cases(feature_description)
        
        # Create test cases in Azure DevOps
        for test_case in test_cases.split('\n'):
            if test_case.strip():
                azure_client.create_test_case(
                    title=test_case,
                    description=feature_description,
                    steps=[]
                )

        # Simulate test execution (replace with actual test execution)
        test_results = [
            {'testCase': {'name': 'Login Test'}, 'outcome': 'Passed'},
            {'testCase': {'name': 'Invalid Login Test'}, 'outcome': 'Passed'},
            {'testCase': {'name': 'Password Reset Test'}, 'outcome': 'Failed', 
             'errorMessage': 'Reset email not sent'}
        ]

        # Analyze results using AI
        analysis = ai_analyzer.analyze_test_results(test_results)
        
        # Assert based on analysis
        assert analysis is not None, "AI analysis should provide insights"

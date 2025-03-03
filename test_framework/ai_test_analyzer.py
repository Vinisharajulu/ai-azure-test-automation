import openai
import os
from dotenv import load_dotenv

class AITestAnalyzer:
    def __init__(self):
        load_dotenv()
        openai.api_key = os.getenv('OPENAI_API_KEY')

    def analyze_test_results(self, test_results):
        """
        Analyze test results using AI to provide insights
        """
        try:
            # Prepare test results summary for AI analysis
            results_summary = self._prepare_results_summary(test_results)
            
            # Use OpenAI to analyze the results
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a test analysis expert."},
                    {"role": "user", "content": f"Analyze these test results and provide insights: {results_summary}"}
                ]
            )
            
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error analyzing test results: {str(e)}")
            return None

    def generate_test_cases(self, feature_description):
        """
        Generate test cases using AI based on feature description
        """
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a test case generation expert."},
                    {"role": "user", "content": f"Generate test cases for this feature: {feature_description}"}
                ]
            )
            
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error generating test cases: {str(e)}")
            return None

    def _prepare_results_summary(self, test_results):
        """
        Prepare a summary of test results for AI analysis
        """
        summary = {
            'total_tests': len(test_results),
            'passed': sum(1 for test in test_results if test.get('outcome') == 'Passed'),
            'failed': sum(1 for test in test_results if test.get('outcome') == 'Failed'),
            'failures': [
                {
                    'test_name': test.get('testCase').get('name'),
                    'error': test.get('errorMessage')
                }
                for test in test_results if test.get('outcome') == 'Failed'
            ]
        }
        return str(summary)

# AI-Powered Test Automation with Azure DevOps

This project implements an AI-enhanced test automation framework integrated with Azure DevOps. It uses OpenAI's GPT models to generate and analyze test cases.

## Features

- Azure DevOps integration for test case management
- AI-powered test case generation
- Automated test result analysis using AI
- Python-based test automation framework

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Configure environment variables:
- Copy `.env.example` to `.env`
- Update the values with your Azure DevOps and OpenAI credentials

## Usage

1. Create test cases:
```python
from test_framework.azure_devops_client import AzureDevOpsTestClient
from test_framework.ai_test_analyzer import AITestAnalyzer

# Initialize clients
azure_client = AzureDevOpsTestClient()
ai_analyzer = AITestAnalyzer()

# Generate and create test cases
feature_description = "Your feature description"
test_cases = ai_analyzer.generate_test_cases(feature_description)
```

2. Run tests:
```bash
pytest tests/
```

## Required Credentials

1. Azure DevOps:
   - Organization URL
   - Personal Access Token (PAT)
   - Project name

2. OpenAI:
   - API Key

## Best Practices

1. Keep feature descriptions clear and detailed
2. Review AI-generated test cases before implementation
3. Regularly update the AI model with new test patterns
4. Monitor and validate AI analysis results

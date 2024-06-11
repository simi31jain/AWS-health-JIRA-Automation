# JIRA Automation with Serverless
 
## Introduction
This project sets up the infrastructure using serverless to automatically create JIRA tickets when a health issue appears on the AWS Health Dashboard.
 
## Prerequisites
Before you begin, ensure you have the following configured:
 
1. AWS Credentials
2. Python
3. npm
4. Serverless Framework
 
## Steps to Deploy
 
1. **Clone the Repository**
 
   Clone the repository containing the code.
 
2. **Define Variables**
   To store your security credentials like JIRA_URL, API_TOKEN, USERNAME, PROJECT_KEY you can define a file named as variables.py file in the project root repository.
 
**NOTE:** Format of above variables is as following:
JIRA_URL = "<https://<your-domain>.atlassian.net/rest/api/3/issue>"  
USER_NAME = "<USER NAME OF JIRA ACCOUNT>"
API_TOKEN = "<API TOKEN OF JIRA>"
PROJECT_KEY = "<UNIQUE JIRA PROJECT KEY>"

3. **Deploy the Serverless Application**
 
   Run the following command to deploy the application using CloudFormation. This will deploy an AWS Lambda function with a Python runtime and create two EventBridge rules:
 
   ```sh
   serverless deploy

4. **Test your Lambda**


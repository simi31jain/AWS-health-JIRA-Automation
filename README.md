
# JIRA Automation with Serverless

## Introduction
This project sets up the infrastructure using serverless to automatically create JIRA tickets when a health issue appears on the AWS Health Dashboard.

## Prerequisites
Before you begin, ensure you have the following configured and if necessary refer the links given below.

1. AWS Credentials
      https://docs.aws.amazon.com/cli/v1/userguide/cli-configure-files.html#cli-configure-files-methods
2. Python
      https://www.python.org/downloads/  
3. npm
      https://nodejs.org/en/download/package-manager
4. Serverless Framework
      https://www.serverless.com/framework/docs-getting-started
5. Git Installation:
      https://www.git-scm.com/downloads

## Steps to Deploy

1. **Clone the Repository**

   Clone the repository containing the code.
   ```sh
   git clone <repository url>

3. **Define Variables**
   To store your security credentials like JIRA_URL, API_TOKEN, USERNAME, PROJECT_KEY you can define a file named as variables.py file in the project root repository.

 **NOTE:** Format of above variables is as following and replace the values.
 ```python
 JIRA_URL = "<https://<your-domain>.atlassian.net/rest/api/3/issue>"  
 USER_NAME = "<USER NAME OF JIRA ACCOUNT>"
 API_TOKEN = "<API TOKEN OF JIRA>"
 PROJECT_KEY = "<UNIQUE JIRA PROJECT KEY>"
```
You can find the Your-domain in JIRA Account 
The USER_NAME will be your email ID 
To generate the API_TOKEN, follow these steps : 
      https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/
Project key: Go to Project settings and you can see the Key

3. **Deploy the Serverless Application**

   Run the following command to deploy the application using CloudFormation. This will deploy an AWS Lambda function with a Python runtime and create two EventBridge rules:

   ```sh
   serverless deploy

4. **Test the Lambda Function**

   To test the Lambda function, there are two ways:

   a. **Create a Mock Event Payload**:

      Use the following mock event payload:
      Replace the Region, AWS-Account-ID, instance-id

      ```json
      [
        {
          "DetailType": "AWS Health Abuse Event",
          "Source": "awsmock.health",
          "Time": "2024-05-08T10:15:30Z",
          "Resources": ["arn:aws:ec2:<REGION>:<AWS-ACCOUNT-ID>:instance/<INSTANCE-ID>"],
          "Detail": "{ \"eventArn\": \"arn:aws:health:global::event/AWS_ABUSE_DOS_REPORT_92387492375_4498_2018_08_01_02_33_00\", \"eventTypeCategory\": \"issue\" }"
        }
      ]
      ```
      

      **NOTE:** The real-time payload given by the AWS Health Dashboard and the mock payload are different. For testing purposes, changes are required in accessing variables in the Lambda code in the `health.py` file.

      For the mock event, modify the variables in `lambda_handler` function as follows:

      ```python
          event_arn = event['Detail']['eventArn']
          event_type = event['Detail']['eventTypeCategory']
      ```
     Modify the serverless.yaml file by adding the below EventBridge Rule:
     ```python
         MyEventRule:
            Type: AWS::Events::Rule
            Properties:
              Name: health-mock-event-rule
              EventBusName: default
              EventPattern:
                source:
                  - "awsmock.health"
     ```
   Run the following command after writing mock payload file and other above steps
   
  ```sh
   aws events put-events --entries file://<filename>
  ```

   b. **Using Test Event of Lambda**:

      Click on "Test" in the Lambda console and check the execution results to find the ticket ID. When you deploy the code using serverless, a test event will be configured in your Lambda function. Click on "Test" and see the execution results to find your ticket ID and verify it from your JIRA account.

      **NOTE:** In the case of using the test event (point b), no changes are needed in the code.
      When testing the lambda function for mock event, we have to define the another Eventbridge rule in the serverless.yaml file.

import json
import requests
import variables

def lambda_handler(event, context):
    
    print("event--->",event)
    
    # Access the keys within the object from payload
    event_arn = event['eventArn']
    service = event['service']
    event_type = event['eventTypeCode']
    description = event['eventDescription'][0]['latestDescription']
 
    print("summary:",service,"description:",description)
    
    # Create Jira issue payload
    jira_issue_data = {
        "fields": {
            "project": {
                "key": variables.PROJECT_KEY
            },
            "summary": f"{event_type}, Service: {service} ",
            "description": {
                "content": [
                    {
                        "content": [
                            {
                                "text": f" AWS Service Health details: \n {description}.",
                                "type": "text"
                                }
                            ],
                            "type": "paragraph"
                        }
                    ],
                    "type": "doc",
                    "version": 1
                
            },
            "issuetype": {
                "name": "Task"
            }
            # Add other fields as needed
        }
    }
    
    
    # Make a POST request to the Jira API
    jira_url = variables.JIRA_URL
    user_name = variables.USER_NAME
    API_Token = variables.API_TOKEN
    jira_auth = (user_name, API_Token)
    response = requests.post(jira_url, json=jira_issue_data, auth=jira_auth)
    print("response:",response)
    
    if response.status_code == 201:
        print("Jira issue created successfully")
        issue_key = response.json()["key"]
        print(issue_key)
    else:
        print("Failed to create Jira issue:", response.text)

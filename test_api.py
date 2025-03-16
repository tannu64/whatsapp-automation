import requests
import json
import time

def test_api_endpoint(message, description=""):
    url = "http://127.0.0.1:5000/chat"
    headers = {"Content-Type": "application/json"}
    data = {"message": message}
    
    print(f"\n=== Testing: {description} ===")
    print(f"Message: {message}")
    
    try:
        response = requests.post(url, headers=headers, json=data)
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            print(f"Response: {json.dumps(result, indent=2)}")
            return True
        else:
            print(f"Error Response: {response.text}")
            return False
            
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to server. Make sure the server is running.")
        return False
    except Exception as e:
        print(f"Error: {str(e)}")
        return False

def test_health_endpoint():
    url = "http://127.0.0.1:5000/health"
    print("\n=== Testing Health Endpoint ===")
    
    try:
        response = requests.get(url)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        return True
    except Exception as e:
        print(f"Error: {str(e)}")
        return False

def run_all_tests():
    # First test the health endpoint
    test_health_endpoint()
    
    # List of test cases with different types of messages
    test_cases = [
        {
            "message": "What is artificial intelligence?",
            "description": "Basic AI Question"
        },
        {
            "message": "Write a Python function to calculate fibonacci sequence",
            "description": "Code Generation Request"
        },
        {
            "message": "Explain the difference between REST and GraphQL",
            "description": "Technical Comparison Question"
        },
        {
            "message": "Translate 'Hello, how are you?' to French",
            "description": "Language Translation Request"
        },
        {
            "message": "",
            "description": "Empty Message (Should Return 400)"
        },
        {
            "message": "Tell me a short story about a robot learning to paint",
            "description": "Creative Writing Request"
        }
    ]
    
    # Run each test case with a small delay between requests
    success_count = 0
    for test_case in test_cases:
        if test_api_endpoint(test_case["message"], test_case["description"]):
            success_count += 1
        time.sleep(1)  # Add a small delay between requests
    
    # Print summary
    print(f"\n=== Test Summary ===")
    print(f"Total Tests: {len(test_cases)}")
    print(f"Successful: {success_count}")
    print(f"Failed: {len(test_cases) - success_count}")

if __name__ == "__main__":
    print("Starting API Tests...")
    run_all_tests() 
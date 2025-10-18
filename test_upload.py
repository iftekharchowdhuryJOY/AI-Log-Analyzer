import requests
import os

def test_log_analyzer(log_file_path):
    """Test the log analyzer API with a log file."""
    
    # Check if file exists
    if not os.path.exists(log_file_path):
        print(f"Error: File {log_file_path} not found!")
        return
    
    # API endpoint
    url = "http://localhost:8000/analyze/"
    
    try:
        # Open and send the file
        with open(log_file_path, 'rb') as file:
            files = {'file': file}
            response = requests.post(url, files=files)
        
        if response.status_code == 200:
            result = response.json()
            print("✅ Analysis successful!")
            print(f"Summary: {result['summary']}")
            print(f"\nDetailed results:")
            for i, (label, score) in enumerate(zip(result['details']['labels'], result['details']['scores'])):
                print(f"  {i+1}. {label}: {score*100:.2f}%")
        else:
            print(f"❌ Error: {response.status_code}")
            print(response.text)
            
    except requests.exceptions.ConnectionError:
        print("❌ Error: Could not connect to the server.")
        print("Make sure the server is running on http://localhost:8000")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    # Test with your log file
    log_file = "sample.log"  # Change this to your log file path
    test_log_analyzer(log_file)
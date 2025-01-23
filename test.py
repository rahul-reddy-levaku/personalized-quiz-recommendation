import requests
import pandas as pd
import matplotlib.pyplot as plt

def fetch_data(api_url):
    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error: {err} - URL: {api_url}")
    except requests.exceptions.ConnectionError as err:
        print(f"Connection error: {err} - URL: {api_url}")
    except requests.exceptions.Timeout:
        print(f"Request timed out: {api_url}")
    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")
    return None

def analyze_data(current_data, historical_data):
    current_df = pd.DataFrame(current_data)
    historical_df = pd.DataFrame(historical_data)
    
    # Calculate averages if the 'score' column exists
    avg_current = current_df['score'].mean() if 'score' in current_df else None
    avg_historical = historical_df['score'].mean() if 'score' in historical_df else None
    
    return avg_current, avg_historical

def visualize_data(current_data, historical_data):
    current_df = pd.DataFrame(current_data)
    historical_df = pd.DataFrame(historical_data)
    
    # Plotting quiz counts over time
    plt.figure(figsize=(10, 6))
    if 'date' in current_df and 'quiz_count' in current_df:
        plt.plot(current_df['date'], current_df['quiz_count'], label='Current Quizzes', marker='o')
    if 'date' in historical_df and 'quiz_count' in historical_df:
        plt.plot(historical_df['date'], historical_df['quiz_count'], label='Historical Quizzes', marker='x')
    
    plt.title("Quiz Count Over Time")
    plt.xlabel("Date")
    plt.ylabel("Quiz Count")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def main():
    # API endpoints
    current_url = "https://example.com/api/current_quiz"
    historical_url = "https://example.com/api/historical_quiz"
    
    # Fetch data
    current_data = fetch_data(current_url)
    historical_data = fetch_data(historical_url)
    
    if current_data and historical_data:
        print("Data fetched successfully!")
        
        # Analyze data
        avg_current, avg_historical = analyze_data(current_data, historical_data)
        print(f"Average Current Quiz Score: {avg_current}")
        print(f"Average Historical Quiz Score: {avg_historical}")
        
        # Visualize data
        visualize_data(current_data, historical_data)
    else:
        print("Failed to fetch data. Check your URLs or network connection.")

if __name__ == "__main__":
    main()

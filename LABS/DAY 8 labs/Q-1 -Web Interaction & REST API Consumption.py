import requests
import json

def fetch_users():
    url = "https://jsonplaceholder.typicode.com/users"

    # Custom headers
    headers = {
        "User-Agent": "Python-REST-Client",
        "Accept": "application/json"
    }

    try:
        # Send GET request
        response = requests.get(url, headers=headers, timeout=10)

        # Raise exception for HTTP errors (4xx, 5xx)
        response.raise_for_status()

        # Parse JSON response
        users = response.json()

        # Extract required fields
        extracted_data = []
        for user in users:
            extracted_data.append({
                "id": user["id"],
                "name": user["name"],
                "email": user["email"],
                "city": user["address"]["city"]
            })

        # Save extracted data to JSON file
        with open("users_data.json", "w") as file:
            json.dump(extracted_data, file, indent=4)

        print("Data successfully saved to users_data.json")

    except requests.exceptions.HTTPError as http_err:
        print("HTTP error occurred:", http_err)

    except requests.exceptions.ConnectionError:
        print("Error: Unable to connect to the API")

    except requests.exceptions.Timeout:
        print("Error: Request timed out")

    except requests.exceptions.RequestException as err:
        print("Request error:", err)

    except Exception as e:
        print("Unexpected error:", e)


# Run the function
fetch_users()

import threading
import requests
import time

urls = [
    "https://example.com/data1",
    "https://example.com/data2",
    "https://example.com/data3",
    "https://example.com/data4"
]

# ----------------------------------
# Function to download and save data
# ----------------------------------
def download_file(url):
    response = requests.get(url)
    filename = url.split("/")[-1] + ".txt"

    with open(filename, "w", encoding="utf-8") as file:
        file.write(response.text)

    print(f"Downloaded {filename}")


# ----------------------------------
# Sequential Download
# ----------------------------------
start_time = time.time()

for url in urls:
    download_file(url)

sequential_time = time.time() - start_time
print(f"\nSequential Download Time: {sequential_time:.2f} seconds")


# ----------------------------------
# Threaded Download
# ----------------------------------
threads = []
start_time = time.time()

for url in urls:
    thread = threading.Thread(target=download_file, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

threaded_time = time.time() - start_time
print(f"Threaded Download Time: {threaded_time:.2f} seconds")

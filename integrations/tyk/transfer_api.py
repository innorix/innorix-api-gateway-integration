import os

from client import INNORIXClient

client = INNORIXClient()


files = [
    {
        "file_path": os.getenv("FILE_PATH"),
        "file_size": int(os.getenv("FILE_SIZE"))
    }
]

targets = [
    {
        "target_id": os.getenv("TARGET_DEVICE_ID"),
        "target_path": os.getenv("TARGET_PATH")
    }
]

response = client.create_transfer(
    source_id=os.getenv("SOURCE_DEVICE_ID"),
    targets=targets,
    files=files
)

print("Transfer API request processed by Tyk.")
print("Transfer submitted to INNORIX.")
print(response)
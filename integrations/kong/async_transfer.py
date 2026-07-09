import os
import time

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

print("202 Accepted")
print("Transfer submitted through Kong Gateway.")

time.sleep(3)

status = client.get_unified_transfer_list(
    automation_id=os.getenv("AUTOMATION_ID"),
    limit=10,
    type_filter="history"
)

print(status)
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
        "target_id": os.getenv("TARGET_CLUSTER_A"),
        "target_path": os.getenv("TARGET_PATH")
    },
    {
        "target_id": os.getenv("TARGET_CLUSTER_B"),
        "target_path": os.getenv("TARGET_PATH")
    },
    {
        "target_id": os.getenv("TARGET_CLUSTER_C"),
        "target_path": os.getenv("TARGET_PATH")
    }
]

response = client.create_transfer(
    source_id=os.getenv("SOURCE_DEVICE_ID"),
    targets=targets,
    files=files
)

print("Kong routed transfer to multiple Kubernetes clusters.")
print(response)
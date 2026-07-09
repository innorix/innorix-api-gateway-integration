# INNORIX API Gateway Integration

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![API Gateway](https://img.shields.io/badge/API-Gateway-orange)
![Kong](https://img.shields.io/badge/Kong-Supported-003459)
![Tyk](https://img.shields.io/badge/Tyk-Supported-00B4D8)
![License](https://img.shields.io/badge/License-Commercial-red)
![Status](https://img.shields.io/badge/Status-Official-success)

Official integration examples for exposing INNORIX file transfer services through API Gateway platforms.

---

## Supported Platforms

- Kong
- Tyk

---

## Features

- Create transfers through API Gateway
- Handle asynchronous transfer requests
- Distribute files to multiple destinations
- Monitor transfer progress using the INNORIX REST API
- Verify transfer completion

---

## Repository Structure

```text
.
├── client.py
└── integrations/
    ├── kong/
    └── tyk/
```

---

## Examples

### Transfer API

```text
Application
        │
Transfer API
        │
        ▼
API Gateway
        │
        ▼
INNORIX Platform
        │
        ▼
Transfer Created
```

### Async Transfer

```text
Application
        │
Transfer API
        │
202 Accepted
        │
        ▼
Background Transfer
        │
        ▼
Transfer Status
```

### Multi Distribution

```text
Application
        │
Distribution API
        │
        ▼
API Gateway
        │
        ▼
INNORIX Platform
        │
        ▼
Target A
Target B
Target C
```

---

## Requirements

- Python 3.10+
- INNORIX Platform
- INNORIX API Key

---

## Installation

Install the required packages.

```bash
pip install -r requirements.txt
```

Copy the example configuration.

```bash
cp .env.example .env
```

Update the configuration.

```text
INNORIX_BASE_URL=
INNORIX_API_KEY=

SOURCE_DEVICE_ID=

TARGET_DEVICE_ID=
TARGET_PATH=

FILE_PATH=
FILE_SIZE=

TARGET_CLUSTER_A=
TARGET_CLUSTER_B=
TARGET_CLUSTER_C=

TARGET_REGION_US=
TARGET_REGION_EU=
TARGET_REGION_APAC=

AUTOMATION_ID=
```

---

## Run

### Transfer API

```bash
cd integrations/kong

python transfer_api.py
```

### Async Transfer

```bash
cd integrations/kong

python async_transfer.py
```

### Multi Distribution

```bash
cd integrations/kong

python multi_distribution.py
```

The same examples are available for:

- Kong
- Tyk

---

## License

Commercial License

Copyright © INNORIX Co., Ltd. All rights reserved.
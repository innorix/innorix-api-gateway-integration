# Kong

This example demonstrates how to expose INNORIX file transfer services through Kong API Gateway.

## Overview

Kong acts as the API Gateway in front of the INNORIX Platform, providing secure API access for creating transfers, processing asynchronous requests, and distributing files to multiple destinations.

## Examples

### Transfer API

```text
Client
    │
POST /transfer
    │
    ▼
Kong Gateway
    │
    ▼
INNORIX Transfer API
    │
    ▼
Transfer Created
```

Run

```bash
python transfer_api.py
```

### Async Transfer

```text
Client
    │
POST /transfer
    │
202 Accepted
    │
    ▼
Background Transfer
    │
    ▼
Transfer Status
```

Run

```bash
python async_transfer.py
```

### Multi Distribution

```text
Client
    │
POST /distribute
    │
    ▼
Kong Gateway
    │
    ▼
Cluster A
Cluster B
Cluster C
```

Run

```bash
python multi_distribution.py
```
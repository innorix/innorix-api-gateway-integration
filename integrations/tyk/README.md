# Tyk

This example demonstrates how to manage INNORIX file transfer services through Tyk API Gateway.

## Overview

Tyk provides centralized API management for INNORIX, allowing applications to securely create transfers, monitor asynchronous operations, and distribute files across multiple regions.

## Examples

### Transfer API

```text
Application
      │
Transfer API
      │
      ▼
Tyk Gateway
      │
      ▼
INNORIX Platform
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
Application
      │
Transfer Request
      │
202 Accepted
      │
      ▼
Background Processing
      │
      ▼
Transfer Monitoring
```

Run

```bash
python async_transfer.py
```

### Multi Distribution

```text
Application
      │
Distribution API
      │
      ▼
Tyk Gateway
      │
      ▼
US Region
EU Region
APAC Region
```

Run

```bash
python multi_distribution.py
```
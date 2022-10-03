#!/bin/bash

uvicorn app.main:app --reload

## If you do not want to use localhost as default use the following line:
# uvicorn src.main:app --reload --host <your_ip>
# Example:
# uvicorn src.main:app --reload --host 192.168.0.1

## If you do not want to use default port and ip address use the following line:
# uvicorn src.main:app --reload --host <your_ip> --port <your_port>
# Example:
# uvicorn app.main:app --reload --host 192.168.0.1 --port 8000
uvicorn src.main:app --reload

@REM If you do not want to use localhost as default use the following line:
@REM uvicorn src.main:app --reload --host <your_ip>
@REM Example:
@REM uvicorn src.main:app --reload --host 192.168.0.1

@REM If you do not want to use default port and ip address use the following line:
@REM uvicorn src.main:app --reload --host <your_ip> --port <your_port>
@REM Example:
@REM uvicorn src.main:app --reload --host 192.168.0.1 --port 8006
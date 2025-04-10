FROM python:3.13-slim-bookworm

COPY api.py .

COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["fastapi", "run", "api.py"]
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

# ✅ Remove o cache do pip + força upgrade
RUN pip install --no-cache-dir --force-reinstall -r requirements.txt

COPY simulator.py .

CMD ["python", "simulator.py"]

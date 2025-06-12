# Instagram Post Classifier API (Coding Challenge)

This project is a simple FastAPI web service that accepts input text (designed for Instagram Posts) and returns class probabilities using a dummy classifier. It demonstrates API design, modular Python structure, and containerization.

---

## Features

- FastAPI endpoint `/predict` that receives a text string via POST
- Dummy classifier that returns random probabilities across fixed class labels
- Probabilities are returned as a JSON object
- Dockerized for easy deployment and testing

---

## Example Request

```bash
curl -X POST http://localhost:8000/predict \
     -H "Content-Type: application/json" \
     -d '{"text": "This is an awesome Instagram post"}'
```

**Response:**

```json
{
  "Soccer": 0.032,
  "Food": 0.172,
  "Stockmarket": 0.048,
  "Yoga": 0.138,
  "Beauty": 0.264,
  "Politics": 0.100,
  "Technology": 0.246
}
```

---

## Setup

### Install regular dependencies

These packages are required to run the application:

```bash
pip install -r requirements.txt
```

### Install development dependencies

This includes all regular dependencies plus tools for testing, linting, and development:

```bash
pip install -r requirements-dev.txt
```

---

## Docker Usage

### 1. Build and start service

```bash
make up
```

### 2. View logs

```bash
make logs
```

### 3. Stop the service

```bash
make down
```

### 4. Clean up images (optional)

```bash
make clean
```

The API will be available at [http://localhost:8000](http://localhost:8000)

---

## Running Tests

Run unit tests with:

```bash
make test
```

Check test coverage with:

```bash
make coverage
```

---

## Requirements

- Python 3.12

---

## Notes

- There are no pre-processing steps, but these could be added later or delegated to another service.
- The class labels are hardcoded for simplicity but can be easily extended.

## Potential Improvements
- Incorporating Terraform as an Infrastructure as Code (IaC) tool could significantly improve infrastructure management. By codifying cloud resources (such as storage accounts, virtual machines, and Kubernetes)
# Lambda FastAPI

Experimenting with FastAPI as a serverless AWS Lambda function

## Setup

```
pip install -t package -r requirements.txt
```

Now we need to create a zip with where the contents of the package directory are located in the root of the zip, along with out api code

```
cd package
zip ../aws_lambda_artifact.zip -r .
cd ..
zip aws_lambda_artifact.zip api.py
```

## Docker (AWS ECR)

```
docker build -t lambda_api .
```

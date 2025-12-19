# serverless-enrichment-api
Serverless Python API deployed via AWS Lambda (container image), API Gateway, and ECR.

## The Demo 
- Health: https://r162cjxbqc.execute-api.us-east-1.amazonaws.com/health
- Enrich: POST https://r162cjxbqc.execute-api.us-east-1.amazonaws.com/enrich-user

### Typical example 

curl -X POST https://r162cjxbqc.execute-api.us-east-1.amazonaws.com/enrich-user \
  -H "Content-Type: application/json" \
  -d '{"first_name":"Conner","last_name":"Lorenz","email":"test@example.com"}'


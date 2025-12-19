variable "aws_region" {
  type    = string
  default = "us-east-1"
}

variable "project_name" {
  type    = string
  default = "serverless-enrichment"
}

variable "lambda_name" {
  type    = string
  default = "serverless-enrichment-api"
}

variable "image_uri" {
  type        = string
  description = "ECR image URI with tag, same region as aws_region (e.g. 123.dkr.ecr.us-east-1.amazonaws.com/repo:v1)"
}

variable "app_version" {
  type    = string
  default = "1.0.0"
}

variable "git_sha" {
  type    = string
  default = "manual"
}

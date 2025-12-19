output "api_invoke_url" {
  value = aws_apigatewayv2_stage.default.invoke_url
}

output "version_endpoint" {
  value = "${aws_apigatewayv2_stage.default.invoke_url}version"
}

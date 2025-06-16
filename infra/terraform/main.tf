# Пример Terraform для AWS (рекомендуется дорабатывать вручную)
provider "aws" {
  region = var.aws_region
}
variable "aws_region" {
  type = string
}
# Ресурсы: VPC, ECS кластер, RDS, S3 для статики
# ...

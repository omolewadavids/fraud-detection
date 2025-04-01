output "ecr_repository_url" {
  value = aws_ecr_repository.fraud_detection_repo.repository_url
}

output "ecs_cluster_name" {
  value = aws_ecs_cluster.fraud_detection_cluster.name
}

output "ecs_service_name" {
  value = aws_ecs_service.fraud_detection_service.name
}

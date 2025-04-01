resource "aws_ecr_repository" "fraud_detection_repo" {
  name = var.ecr_repo_name
}

resource "aws_ecs_cluster" "fraud_detection_cluster" {
  name = "fraud-detection-cluster"
}

resource "aws_iam_role" "ecs_task_execution_role" {
  name = "ecs-task-execution-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action    = "sts:AssumeRole"
      Principal = {
        Service = "ecs-tasks.amazonaws.com"
      }
      Effect    = "Allow"
      Sid       = ""
    }]
  })
}

resource "aws_iam_role_policy_attachment" "ecs_task_execution_role_policy" {
  role       = aws_iam_role.ecs_task_execution_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy"
}

resource "aws_ecs_task_definition" "fraud_detection_task" {
  family                = "fraud-detection-task"
  execution_role_arn    = aws_iam_role.ecs_task_execution_role.arn
  network_mode          = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  cpu                   = "256"
  memory                = "512"
  container_definitions = jsonencode([{
    name      = "fraud-detection-api"
    image     = "${aws_ecr_repository.fraud_detection_repo.repository_url}:latest"
    cpu       = 256
    memory    = 512
    essential = true
    portMappings = [{
      containerPort = 8000
      hostPort      = 8000
      protocol      = "tcp"
    }]
  }])
}

resource "aws_ecs_service" "fraud_detection_service" {
  name            = "fraud-detection-service"
  cluster         = aws_ecs_cluster.fraud_detection_cluster.id
  task_definition = aws_ecs_task_definition.fraud_detection_task.arn
  desired_count   = 1
  launch_type     = "FARGATE"
  network_configuration {
    subnets          = ["subnet-xxxxxx"]  # Replace with your subnet IDs
    assign_public_ip = true
  }
}

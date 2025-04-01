#!/bin/bash

# Define project name
PROJECT_NAME="fraud_detection"

# Create main project directories
echo "📂 Creating project directories..."
mkdir -p $PROJECT_NAME/{.github/workflows,data,models,notebooks,src,tests}

# Create Python files
echo "📄 Creating Python files..."
touch $PROJECT_NAME/src/{__init__.py,data_preprocessing.py,train.py,inference.py,model.py,config.py,logger.py}
touch $PROJECT_NAME/tests/{test_data.py,test_model.py}

# Create configuration, CI/CD, and documentation files
echo "📄 Creating configuration and CI/CD files..."
touch $PROJECT_NAME/.github/workflows/cicd.yml
touch $PROJECT_NAME/Dockerfile
touch $PROJECT_NAME/requirements.txt
touch $PROJECT_NAME/.gitignore
touch $PROJECT_NAME/README.md

# Add basic content to .gitignore
echo "Adding default .gitignore..."
echo -e "venv/\n__pycache__/\n*.pkl\n*.log" > $PROJECT_NAME/.gitignore

# Print project structure
echo "✅ Project structure created successfully!"
tree $PROJECT_NAME 2>/dev/null || ls -R $PROJECT_NAME

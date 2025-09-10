# SQLAlchemy Learning Project Makefile
# Provides convenient commands for development and deployment

.PHONY: help install install-dev test lint format clean run-tutorials docs

# Default target
help:
	@echo "SQLAlchemy Learning Project - Available Commands:"
	@echo "================================================="
	@echo ""
	@echo "Setup & Installation:"
	@echo "  install      Install the package and dependencies"
	@echo "  install-dev  Install with development dependencies"
	@echo "  install-docs Install with documentation dependencies"
	@echo ""
	@echo "Development:"
	@echo "  test         Run all tests"
	@echo "  lint         Run linting checks"
	@echo "  format       Format code with black and isort"
	@echo "  clean        Clean up generated files"
	@echo ""
	@echo "Tutorials:"
	@echo "  run-basics   Run NeuralNine basics tutorial"
	@echo "  run-main     Run NeuralNine main tutorial"
	@echo "  run-crud     Run ZeqTech CRUD tutorial"
	@echo "  run-all      Run all tutorials"
	@echo ""
	@echo "Documentation:"
	@echo "  docs         Generate documentation"
	@echo "  serve-docs   Serve documentation locally"
	@echo ""

# Installation commands
install:
	pip install -r requirements.txt

install-dev: install
	pip install -e ".[dev]"

install-docs: install
	pip install -e ".[docs]"

# Development commands
test:
	pytest

lint:
	flake8 NeuralNine/ ZeqTech/
	isort --check-only NeuralNine/ ZeqTech/

format:
	black NeuralNine/ ZeqTech/
	isort NeuralNine/ ZeqTech/

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	rm -rf build/
	rm -rf dist/
	rm -rf .coverage
	rm -rf htmlcov/
	rm -rf .pytest_cache/

# Tutorial execution commands
run-basics:
	@echo "Running NeuralNine Basics Tutorial..."
	cd NeuralNine && python basics.py

run-main:
	@echo "Running NeuralNine Main Tutorial..."
	cd NeuralNine && python main.py

run-crud:
	@echo "Running ZeqTech CRUD Tutorial..."
	cd ZeqTech/Create-Read-Update && python app.py

run-filtering:
	@echo "Running ZeqTech Filtering Tutorial..."
	cd ZeqTech/Filtering-Data && python app.py

run-relationships:
	@echo "Running ZeqTech Relationships Tutorials..."
	cd ZeqTech/one-one && python main.py
	cd ZeqTech/one-many && python main.py
	cd ZeqTech/many-many && python main.py

run-advanced:
	@echo "Running ZeqTech Advanced Tutorials..."
	cd ZeqTech/Grouping-Chaining-Data && python app.py
	cd ZeqTech/Ordering-Data && python app.py
	cd ZeqTech/Relationship-Loading-Techniques && python app.py
	cd ZeqTech/Types-of-JOINS && python app.py
	cd ZeqTech/Reduce-Column-Data && python app.py
	cd ZeqTech/Indexes && python models.py

run-all: run-basics run-main run-crud run-filtering run-relationships run-advanced
	@echo "All tutorials completed!"

# Documentation commands
docs:
	@echo "Generating documentation..."
	# Add sphinx documentation generation here if needed

serve-docs:
	@echo "Serving documentation locally..."
	# Add local documentation server here if needed

# Database management
reset-databases:
	@echo "Resetting all database files..."
	find . -name "*.db" -not -path "./NeuralNine/school.db" -not -path "./NeuralNine/students.db" -delete
	@echo "Database files reset (keeping sample databases)"

# Quality assurance
qa: lint test
	@echo "Quality assurance checks completed!"

# Full setup for new contributors
setup: install-dev
	@echo "Setting up development environment..."
	@echo "Running initial tests..."
	$(MAKE) test
	@echo "Development environment ready!"

# Deployment preparation
deploy-prep: clean format lint test
	@echo "Preparing for deployment..."
	@echo "All checks passed! Ready for deployment."

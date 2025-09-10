# Contributing to SQLAlchemy Learning Project

Thank you for your interest in contributing to the SQLAlchemy Learning Project! This document provides guidelines and information for contributors.

## 🤝 How to Contribute

### Reporting Issues

If you find a bug or have a suggestion for improvement:

1. Check existing issues to avoid duplicates
2. Create a new issue with:
   - Clear, descriptive title
   - Detailed description of the problem/suggestion
   - Steps to reproduce (for bugs)
   - Expected vs actual behavior
   - Python and SQLAlchemy versions

### Suggesting Enhancements

We welcome suggestions for:

- New tutorial topics
- Code improvements
- Documentation enhancements
- Better examples
- Performance optimizations

### Code Contributions

1. **Fork the repository**
2. **Create a feature branch**:
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Make your changes** following our guidelines
4. **Test your changes**:
   ```bash
   make test
   make lint
   ```
5. **Commit your changes**:
   ```bash
   git commit -m "Add amazing feature"
   ```
6. **Push to your branch**:
   ```bash
   git push origin feature/amazing-feature
   ```
7. **Open a Pull Request**

## 📋 Development Guidelines

### Code Style

We use the following tools for code formatting and linting:

- **Black** for code formatting
- **isort** for import sorting
- **flake8** for linting

Run formatting before committing:

```bash
make format
```

### Python Version Support

- Python 3.7+
- SQLAlchemy 2.0+

### Documentation Standards

- Use docstrings for all functions and classes
- Follow Google-style docstrings
- Include type hints where appropriate
- Add comments for complex logic

### Testing

- Add tests for new functionality
- Ensure all tests pass before submitting
- Use descriptive test names
- Test both success and error cases

### Commit Messages

Use clear, descriptive commit messages:

- Start with a verb (Add, Fix, Update, Remove)
- Be specific about what changed
- Reference issues when applicable

Examples:

- `Add comprehensive comments to CRUD tutorial`
- `Fix relationship loading in many-to-many example`
- `Update README with installation instructions`

## 🏗️ Project Structure

```
SQLA-Learn/
├── NeuralNine/          # Beginner tutorials
├── ZeqTech/            # Advanced tutorials
├── tests/              # Test files
├── docs/               # Documentation
├── requirements.txt    # Dependencies
├── setup.py           # Package setup
├── Makefile           # Development commands
└── README.md          # Project documentation
```

## 🎯 Tutorial Guidelines

### Adding New Tutorials

1. **Choose appropriate directory** (NeuralNine for basics, ZeqTech for advanced)
2. **Create descriptive directory name**
3. **Include both models.py and app.py**:
   - `models.py`: Database models and schema
   - `app.py`: Example usage and demonstrations
4. **Add comprehensive comments**
5. **Include error handling**
6. **Test thoroughly**

### Tutorial Structure

Each tutorial should include:

```python
"""
Tutorial Title - Brief Description

This module demonstrates [concept] using SQLAlchemy.

Key Concepts Covered:
- Concept 1
- Concept 2
- Concept 3

Author: [Your Name]
License: MIT
"""

# Imports
# Database setup
# Model definitions
# Example functions
# Main execution block
```

### Code Examples

- Use realistic, practical examples
- Include both simple and complex scenarios
- Add error handling and best practices
- Comment extensively
- Use meaningful variable names

## 🧪 Testing

### Running Tests

```bash
# Run all tests
make test

# Run specific test file
pytest tests/test_specific.py

# Run with coverage
pytest --cov=.
```

### Writing Tests

Create test files in the `tests/` directory:

```python
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from NeuralNine.main import Student, Teacher, Class

class TestSchoolManagement:
    def setup_method(self):
        self.engine = create_engine("sqlite:///:memory:")
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def teardown_method(self):
        self.session.close()

    def test_create_student(self):
        student = Student(name="Test Student", grade="10th")
        self.session.add(student)
        self.session.commit()

        assert student.id is not None
        assert student.name == "Test Student"
```

## 📚 Documentation

### README Updates

When adding new tutorials:

1. Update the project structure section
2. Add to the learning paths
3. Update the tutorial order
4. Include in the roadmap

### Code Comments

- Explain complex logic
- Document function parameters and return values
- Include usage examples
- Add TODO comments for future improvements

## 🚀 Release Process

### Version Numbering

We use semantic versioning (MAJOR.MINOR.PATCH):

- MAJOR: Breaking changes
- MINOR: New features, backward compatible
- PATCH: Bug fixes, backward compatible

### Release Checklist

- [ ] All tests pass
- [ ] Documentation updated
- [ ] Version numbers updated
- [ ] CHANGELOG.md updated
- [ ] Release notes prepared

## 💡 Best Practices

### General

- Keep tutorials focused on specific concepts
- Use consistent naming conventions
- Include both positive and negative examples
- Test with different Python versions
- Consider performance implications

### SQLAlchemy Specific

- Use proper session management
- Handle exceptions appropriately
- Use appropriate relationship loading strategies
- Consider database constraints
- Optimize queries when possible

### Educational

- Start with simple examples
- Build complexity gradually
- Explain the "why" behind decisions
- Include common pitfalls and solutions
- Provide clear learning outcomes

## 🆘 Getting Help

- Check existing issues and discussions
- Ask questions in GitHub Discussions
- Review SQLAlchemy documentation
- Look at existing tutorial examples

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

## 🙏 Recognition

Contributors will be recognized in:

- README.md contributors section
- Release notes
- Project documentation

Thank you for contributing to the SQLAlchemy Learning Project! 🎉

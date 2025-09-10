# SQLAlchemy Mastery Course 🚀

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://python.org)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0+-green.svg)](https://sqlalchemy.org)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Code Style](https://img.shields.io/badge/Code%20Style-Black-black.svg)](https://black.readthedocs.io)

A comprehensive, production-ready collection of SQLAlchemy tutorials and examples from two excellent YouTube channels, organized for easy learning and reference. Master database operations with Python's most powerful ORM!

## 📺 Learning Sources

This repository contains code examples and tutorials from:

- **[ZeqTech](https://www.youtube.com/@ZeqTech)** - Advanced SQLAlchemy concepts and real-world applications
- **[NeuralNine](https://www.youtube.com/@NeuralNine)** - SQLAlchemy fundamentals and core concepts

## 🚀 What You'll Learn

- **Database Fundamentals**: Understanding SQLAlchemy ORM and Core
- **CRUD Operations**: Create, Read, Update, Delete data with best practices
- **Relationships**: One-to-One, One-to-Many, Many-to-Many relationships
- **Advanced Queries**: Filtering, grouping, ordering, and chaining
- **Performance Optimization**: Relationship loading techniques and indexing
- **Real-world Applications**: Practical examples and production patterns
- **Database Design**: Proper schema design and constraints
- **Query Optimization**: Efficient database queries and performance tuning

## 📁 Project Structure

```
SQLA-Learn/
├── 📁 ZeqTech/                    # Advanced SQLAlchemy tutorials
│   ├── 📁 Create-Read-Update/     # Basic CRUD operations
│   ├── 📁 Filtering-Data/         # Data filtering and querying
│   ├── 📁 Grouping-Chaining-Data/ # Advanced query operations
│   ├── 📁 Ordering-Data/          # Data sorting and ordering
│   ├── 📁 Relationship-Loading-Techniques/ # Performance optimization
│   ├── 📁 Types-of-JOINS/         # SQL JOIN operations
│   ├── 📁 Reduce-Column-Data/     # Column selection and optimization
│   ├── 📁 Indexes/                # Database indexing strategies
│   ├── 📁 one-one/                # One-to-One relationships
│   ├── 📁 one-many/               # One-to-Many relationships
│   └── 📁 many-many/              # Many-to-Many relationships
├── 📁 NeuralNine/                 # SQLAlchemy fundamentals
│   ├── 📄 basics.py               # Core SQLAlchemy setup
│   ├── 📄 main.py                 # Complete school management system
│   ├── 🗄️ school.db              # Sample school database
│   └── 🗄️ students.db            # Student management database
├── 📄 requirements.txt            # Project dependencies
├── 📄 .gitignore                  # Git ignore rules
├── 📄 LICENSE                     # MIT License
└── 📄 README.md                   # This file
```

### 🎯 Tutorial Categories

#### **ZeqTech Advanced Tutorials**

- **`Create-Read-Update/`** - Master basic CRUD operations with best practices
- **`Filtering-Data/`** - Advanced data filtering and querying techniques
- **`Grouping-Chaining-Data/`** - Complex query operations and data aggregation
- **`Ordering-Data/`** - Data sorting, ordering, and pagination
- **`Relationship-Loading-Techniques/`** - Performance optimization strategies
- **`Types-of-JOINS/`** - SQL JOIN operations and relationship queries
- **`Reduce-Column-Data/`** - Column selection and query optimization
- **`Indexes/`** - Database indexing for performance
- **`one-one/`** - One-to-One relationship patterns
- **`one-many/`** - One-to-Many relationship patterns
- **`many-many/`** - Many-to-Many relationship patterns

#### **NeuralNine Fundamentals**

- **`basics.py`** - Core SQLAlchemy setup and table creation
- **`main.py`** - Complete school management system example
- **`school.db`** - Sample database with school data
- **`students.db`** - Student management database

## 🛠️ Prerequisites

- **Python 3.7+** (3.9+ recommended)
- **SQLAlchemy 2.0+** (latest version)
- **SQLite** (included with Python)
- **Git** (for cloning the repository)

## 📦 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/SQLA-Learn.git
cd SQLA-Learn
```

### 2. Set Up Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
# Install all dependencies
pip install -r requirements.txt

# Or install just SQLAlchemy
pip install sqlalchemy
```

### 4. Verify Installation

```bash
python -c "import sqlalchemy; print(f'SQLAlchemy version: {sqlalchemy.__version__}')"
```

## 🎯 Learning Paths

### 🟢 Beginner Path (NeuralNine)

Perfect for those new to SQLAlchemy:

```bash
# Start here
cd NeuralNine
python basics.py      # Learn fundamentals
python main.py        # Complete school management system
```

**What you'll learn:**

- Basic SQLAlchemy setup and configuration
- Table creation and schema design
- Simple CRUD operations
- Relationship basics

### 🟡 Intermediate Path (ZeqTech)

Build on your fundamentals:

```bash
cd ZeqTech
# Follow this order:
python Create-Read-Update/app.py           # Master CRUD
python Filtering-Data/app.py               # Learn querying
python one-one/main.py                     # One-to-One relationships
python one-many/main.py                    # One-to-Many relationships
python many-many/main.py                   # Many-to-Many relationships
```

### 🔴 Advanced Path (ZeqTech)

Master advanced concepts:

```bash
cd ZeqTech
# Advanced topics:
python Grouping-Chaining-Data/app.py       # Complex queries
python Ordering-Data/app.py                # Data sorting
python Types-of-JOINS/app.py               # SQL JOINs
python Relationship-Loading-Techniques/app.py # Performance
python Reduce-Column-Data/app.py           # Query optimization
python Indexes/models.py                   # Database indexing
```

## 🚀 Running Examples

Each tutorial is self-contained and can be run independently:

```bash
# Example: Run the CRUD tutorial
cd ZeqTech/Create-Read-Update
python app.py

# Example: Run the school management system
cd NeuralNine
python main.py
```

## 📚 Complete Learning Roadmap

### 🟢 Phase 1: Fundamentals (Week 1-2)

```
NeuralNine/basics.py → NeuralNine/main.py
```

- SQLAlchemy basics and setup
- Table creation and schema design
- Simple CRUD operations
- Basic relationships

### 🟡 Phase 2: Core Operations (Week 3-4)

```
ZeqTech/Create-Read-Update/ → ZeqTech/Filtering-Data/ → ZeqTech/Ordering-Data/
```

- Master CRUD operations
- Data filtering and querying
- Data sorting and ordering

### 🔵 Phase 3: Relationships (Week 5-6)

```
ZeqTech/one-one/ → ZeqTech/one-many/ → ZeqTech/many-many/
```

- One-to-One relationships
- One-to-Many relationships
- Many-to-Many relationships

### 🔴 Phase 4: Advanced Topics (Week 7-8)

```
ZeqTech/Grouping-Chaining-Data/ → ZeqTech/Types-of-JOINS/ → ZeqTech/Reduce-Column-Data/
```

- Complex queries and aggregation
- SQL JOIN operations
- Query optimization

### ⚡ Phase 5: Performance & Production (Week 9-10)

```
ZeqTech/Relationship-Loading-Techniques/ → ZeqTech/Indexes/
```

- Performance optimization
- Database indexing
- Production-ready patterns

## 🔗 Additional Resources

### 📚 Documentation & Tutorials

- **[SQLAlchemy Official Documentation](https://docs.sqlalchemy.org/)** - Complete reference
- **[SQLAlchemy Tutorial](https://docs.sqlalchemy.org/en/20/tutorial/)** - Official tutorial
- **[SQLAlchemy 2.0 Migration Guide](https://docs.sqlalchemy.org/en/20/changelog/migration_20.html)** - Upgrade guide

### 🎥 Video Sources

- **[ZeqTech YouTube Channel](https://www.youtube.com/@ZeqTech)** - Advanced programming tutorials
- **[NeuralNine YouTube Channel](https://www.youtube.com/@NeuralNine)** - Python and data science tutorials

### 🛠️ Tools & Extensions

- **[Alembic](https://alembic.sqlalchemy.org/)** - Database migrations
- **[SQLAlchemy-Utils](https://sqlalchemy-utils.readthedocs.io/)** - Additional utilities
- **[Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/)** - Flask integration

## 📝 Project Notes

- ✅ **Self-contained examples** - Each tutorial runs independently
- ✅ **Well-commented code** - Easy to understand and learn
- ✅ **SQLite databases** - Simple and portable for learning
- ✅ **Production patterns** - Real-world best practices
- ✅ **Progressive difficulty** - From beginner to advanced

## 🧪 Testing & Development

```bash
# Run code formatting
black .

# Run linting
flake8 .

# Run tests (if available)
pytest

# Check code style
isort --check-only .
```

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### 🐛 Bug Reports

- Use GitHub Issues to report bugs
- Include Python version and SQLAlchemy version
- Provide minimal reproducible examples

### ✨ Feature Requests

- Suggest new tutorial topics
- Propose code improvements
- Request additional examples

### 📝 Code Contributions

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add tests if applicable
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

### 📋 Contribution Guidelines

- Follow PEP 8 style guidelines
- Add comprehensive comments
- Include docstrings for functions
- Test your changes thoroughly
- Update documentation as needed

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Educational Content Attribution

This repository contains educational content inspired by:

- **[ZeqTech](https://www.youtube.com/@ZeqTech)** - Advanced programming tutorials
- **[NeuralNine](https://www.youtube.com/@NeuralNine)** - Python and data science tutorials

All original tutorial content belongs to their respective creators. This repository is for educational purposes only.

## 🌟 Show Your Support

If this project helped you learn SQLAlchemy, please give it a ⭐!

---

## 🎯 Ready to Start?

```bash
git clone https://github.com/your-username/SQLA-Learn.git
cd SQLA-Learn
pip install -r requirements.txt
cd NeuralNine
python basics.py
```

**Happy Learning! 🚀**

_Master SQLAlchemy and become a database expert with these comprehensive tutorials from ZeqTech and NeuralNine._

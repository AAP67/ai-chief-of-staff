# Contributing to AI Chief of Staff

Thank you for your interest in contributing! This document provides guidelines for contributing to the project.

## Code of Conduct

- Be respectful and inclusive
- Focus on constructive feedback
- Help others learn and grow

## How to Contribute

### Reporting Bugs

1. Check if the bug has already been reported in Issues
2. If not, create a new issue with:
   - Clear description of the bug
   - Steps to reproduce
   - Expected vs actual behavior
   - Screenshots if applicable
   - Your environment (OS, Python version, etc.)

### Suggesting Features

1. Check existing issues for similar suggestions
2. Create a new issue describing:
   - The problem you're trying to solve
   - Your proposed solution
   - Any alternatives you've considered
   - Example use cases

### Code Contributions

1. **Fork the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/ai-chief-of-staff.git
   cd ai-chief-of-staff
   ```

2. **Create a branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Set up development environment**
   ```bash
   ./setup.sh
   pip install -r requirements-dev.txt
   ```

4. **Make your changes**
   - Write clear, documented code
   - Follow existing code style
   - Add tests for new functionality
   - Update README if needed

5. **Test your changes**
   ```bash
   # Run tests
   pytest
   
   # Check code style
   black .
   flake8 .
   ```

6. **Commit your changes**
   ```bash
   git add .
   git commit -m "feat: add amazing feature"
   ```
   
   Use conventional commits:
   - `feat:` for new features
   - `fix:` for bug fixes
   - `docs:` for documentation changes
   - `refactor:` for code refactoring
   - `test:` for adding tests

7. **Push and create Pull Request**
   ```bash
   git push origin feature/your-feature-name
   ```
   
   Then create a PR on GitHub with:
   - Clear description of changes
   - Link to related issues
   - Screenshots for UI changes

## Development Setup

### Prerequisites
- Python 3.8+
- Git
- Anthropic API key

### Local Development
```bash
# Install dependencies
pip install -r requirements-dev.txt

# Run the app
streamlit run app.py

# Run tests
pytest

# Format code
black .

# Lint code
flake8 .
```

## Code Style

- Follow PEP 8 guidelines
- Use Black for formatting
- Add type hints where possible
- Write docstrings for functions
- Keep functions focused and small

## Testing

- Write tests for new features
- Maintain or improve test coverage
- Test edge cases
- Run full test suite before submitting PR

## Documentation

- Update README for user-facing changes
- Add docstrings for new functions
- Update CHANGELOG for notable changes
- Include examples for new features

## Questions?

Feel free to:
- Open an issue for discussion
- Reach out via email: karan_rajpal@berkeley.edu
- Check existing issues and PRs

Thank you for contributing! 🎯

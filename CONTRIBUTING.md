# Contributing to Roomies

Thank you for your interest in contributing to Roomies! This document provides guidelines and instructions for contributing.

## 📋 Code of Conduct

- Be respectful and inclusive
- Focus on constructive feedback
- Celebrate diverse perspectives
- Report inappropriate behavior

## 🚀 Getting Started

### 1. Fork & Clone
```bash
# Fork on GitHub, then clone your fork
git clone https://github.com/yourusername/roomies.git
cd roomies-backend-main
```

### 2. Set Up Development Environment
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env
# Edit .env with your settings

# Initialize database
python setup_db.py
```

### 3. Create Feature Branch
```bash
git checkout -b feature/your-feature-name
# or for bugfixes:
git checkout -b bugfix/your-bug-name
```

## 💻 Development Guidelines

### Code Style
- Follow PEP 8 for Python code
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions small and focused
- Maximum line length: 100 characters

### Python Example
```python
def send_booking_confirmation(booking_id: int) -> bool:
    """
    Send booking confirmation email to student.
    
    Args:
        booking_id: ID of the booking
    
    Returns:
        True if email sent successfully, False otherwise
    """
    booking = Booking.query.get(booking_id)
    if not booking:
        return False
    
    # Implementation...
    return True
```

### HTML/CSS Guidelines
- Use semantic HTML5
- Follow responsive design principles
- Organize CSS by component
- Use consistent class naming (BEM style)
- Keep specificity low

### JavaScript Guidelines
- Use const/let instead of var
- Add comments for complex logic
- Use template literals for strings
- Keep functions small
- Handle errors gracefully

## 🧪 Testing

### Before Submitting
1. **Run existing tests**
   ```bash
   python test_booking_flow.py
   python test_login.py
   python test_auto_verify.py
   ```

2. **Create tests for new features**
   ```bash
   # Create test_yourfeature.py
   # Follow patterns in existing tests
   ```

3. **Test manually**
   - Run the app locally
   - Test all affected features
   - Test on mobile (responsive design)

### Test Structure
```python
def test_feature():
    """Test description."""
    # Setup
    test_data = create_test_data()
    
    # Execute
    result = function_to_test(test_data)
    
    # Assert
    assert result == expected_value
```

## 📝 Commit Messages

Use clear, descriptive commit messages:

```
Good:
✅ feat: Add room status filtering
✅ fix: Correct booking price calculation
✅ docs: Update booking documentation
✅ test: Add verification system tests

Avoid:
❌ fixed bug
❌ updated code
❌ work in progress
❌ asdf
```

### Commit Types
- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `test:` - Adding/updating tests
- `refactor:` - Code refactoring without behavior change
- `perf:` - Performance improvement
- `style:` - Code style changes (formatting)
- `chore:` - Dependencies, build, etc.

## 📦 Files to Modify for Features

### Adding a New Feature

1. **Model** - Define in `models/` or `app.py`
   ```python
   class Feature(db.Model):
       id = db.Column(db.Integer, primary_key=True)
       # fields...
   ```

2. **Route** - Add to `app.py`
   ```python
   @app.route('/feature')
   def feature_route():
       return render_template('feature.html')
   ```

3. **API Endpoint** - Add to `app.py`
   ```python
   @app.route('/api/feature', methods=['GET'])
   def feature_api():
       return jsonify({'data': data})
   ```

4. **Template** - Create in `templates/`
   ```html
   <!-- New feature UI -->
   ```

5. **Static Files** - Add to `static/`
   ```css
   /* New feature styles */
   ```

6. **Tests** - Create `test_feature.py`
   ```python
   def test_feature():
       # Test implementation
   ```

7. **Documentation** - Update relevant docs
   ```markdown
   # New Feature Documentation
   ```

## 🔍 Code Review Checklist

Before submitting a pull request, ensure:

- [ ] Code follows PEP 8 style guide
- [ ] All functions have docstrings
- [ ] New features have tests
- [ ] All tests pass locally
- [ ] No hardcoded values (use config)
- [ ] SQL queries use ORM (no raw SQL)
- [ ] Error handling is implemented
- [ ] User input is validated
- [ ] Security best practices followed
- [ ] Documentation is updated
- [ ] No sensitive data in commits

## 📋 Pull Request Process

### 1. Update Your Branch
```bash
git fetch origin
git rebase origin/main
```

### 2. Push to Your Fork
```bash
git push origin feature/your-feature-name
```

### 3. Create Pull Request
- Go to GitHub
- Click "New Pull Request"
- Select your branch
- Fill in PR template:

```markdown
## Description
Brief description of changes

## Related Issue
Fixes #123

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation

## Testing
Describe testing done

## Screenshots (if UI change)
Include relevant screenshots

## Checklist
- [ ] Code follows style guidelines
- [ ] Tests added/updated
- [ ] Documentation updated
- [ ] No breaking changes
```

### 4. Respond to Review
- Address feedback promptly
- Discuss disagreements respectfully
- Update code as suggested
- Re-request review when ready

## 🐛 Bug Reporting

### Create Bug Report
Include in issue:

1. **Description** - Clear description of bug
2. **Steps to Reproduce**
   ```
   1. Go to '/booking'
   2. Click 'Submit'
   3. Error appears
   ```
3. **Expected Behavior** - What should happen
4. **Actual Behavior** - What actually happens
5. **Screenshots** - If applicable
6. **Environment**
   - OS: Windows/Mac/Linux
   - Python version
   - Browser (if frontend)

### Example Bug Report
```
Title: Booking form validation error

Description:
Booking form shows incorrect error message

Steps:
1. Navigate to /booking
2. Leave dates empty
3. Click "Proceed"

Expected:
Show "Please select dates"

Actual:
Shows "Invalid input"

Environment:
- Windows 10
- Python 3.9
- Chrome 120
```

## ✨ Feature Requests

### Template for Feature Requests
```markdown
## Summary
One-line summary

## Motivation
Why is this needed?

## Proposed Solution
How should it work?

## Example
Usage example

## Benefits
What's the benefit?

## Drawbacks
Any potential issues?
```

## 📚 Documentation Standards

### Python Docstrings
```python
def function_name(param1: str, param2: int) -> bool:
    """
    Brief description.
    
    Longer description if needed.
    
    Args:
        param1: Description of param1
        param2: Description of param2
    
    Returns:
        Description of return value
    
    Raises:
        ValueError: When input is invalid
    
    Example:
        >>> result = function_name("test", 123)
        >>> result
        True
    """
```

### File Headers
```python
"""
Module description.

This module handles...

Classes:
    ClassName: Description

Functions:
    function_name: Description
"""
```

## 🔒 Security Guidelines

When contributing code:

- [ ] Never hardcode credentials or API keys
- [ ] Use environment variables for secrets
- [ ] Validate all user input
- [ ] Escape output (Jinja2 does this by default)
- [ ] Use parameterized SQL queries (SQLAlchemy ORM)
- [ ] Check authorization before actions
- [ ] Hash passwords (werkzeug does this)
- [ ] Don't log sensitive data
- [ ] Use HTTPS in production
- [ ] Keep dependencies updated

## 🚀 Performance Guidelines

- Use database indexes for frequently queried columns
- Cache data when appropriate
- Optimize queries (avoid N+1)
- Use pagination for large datasets
- Compress images before upload
- Minify CSS/JavaScript for production
- Use lazy loading for heavy content

## ♿ Accessibility Guidelines

For UI changes:

- [ ] Proper heading hierarchy
- [ ] Alt text for images
- [ ] ARIA labels where needed
- [ ] Keyboard navigation support
- [ ] Color contrast (WCAG AA minimum)
- [ ] Focus visible on interactive elements
- [ ] Form labels properly associated

## 📱 Mobile Responsive Guidelines

- Test on multiple device sizes
- Use responsive images
- Touch-friendly button sizes (40px+ height)
- Vertical stacking on small screens
- Readable text on mobile (16px+)
- No horizontal scrolling

## 🎯 Priority Areas

High-priority areas for contributions:

1. **Payment Integration** - Complete Razorpay integration
2. **Email System** - Send booking notifications
3. **Mobile App** - React Native frontend
4. **Performance** - Optimize queries and caching
5. **Documentation** - Improve API docs
6. **Tests** - Increase test coverage
7. **Accessibility** - WCAG compliance
8. **Localization** - Multi-language support

## 🎓 Learning Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [SQLAlchemy Tutorial](https://docs.sqlalchemy.org/)
- [Python PEP 8 Style Guide](https://pep8.org/)
- [Git Documentation](https://git-scm.com/doc)
- [Razorpay Integration](https://razorpay.com/docs/)

## 🆘 Getting Help

- **Questions:** Open a discussion issue
- **Help Wanted:** Label issues marked `help-wanted`
- **Good First Issue:** Check `good-first-issue` label
- **Mentorship:** Ask in issue or email

## ✅ Final Checklist Before PR

```
Code Quality
- [ ] Follows style guide
- [ ] No code duplication
- [ ] Proper error handling
- [ ] Efficient algorithms

Testing
- [ ] Tests written
- [ ] All tests passing
- [ ] Manual testing done
- [ ] Edge cases covered

Documentation
- [ ] Code documented
- [ ] README updated
- [ ] Changelog updated
- [ ] Examples provided

Security
- [ ] No hardcoded secrets
- [ ] Input validated
- [ ] Output escaped
- [ ] Auth checked

Performance
- [ ] No N+1 queries
- [ ] Efficient code
- [ ] Proper indexing
- [ ] Caching used

Responsiveness
- [ ] Desktop (1200px+)
- [ ] Tablet (768px)
- [ ] Mobile (320px)
- [ ] Touch friendly
```

## 🎉 Recognition

Contributors will be:
- Listed in README contributors section
- Mentioned in release notes
- Added to CONTRIBUTORS.md
- Thanked in project emails

---

Thank you for contributing to Roomies! Together, we're making student housing better. 🏠✨

**Questions?** Open an issue or email support@roomies.com

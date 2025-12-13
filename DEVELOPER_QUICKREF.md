# Developer Quick Reference

Fast lookup guide for common development tasks in Roomies.

## 🚀 Quick Start (5 Minutes)

```bash
# 1. Navigate to project
cd roomies-backend-main

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Setup database
python setup_db.py

# 5. Run application
python app.py
```

Visit: http://localhost:5000

## 📋 Common Commands

### Running Application
```bash
python app.py                    # Run Flask app
python app.py --debug            # Run with debug mode
```

### Database Management
```bash
python setup_db.py               # Initial setup
python reset_db.py               # Clear and reset
python recreate_db.py            # Recreate from scratch
python create_admin.py           # Create admin user
python populate_real_data.py     # Add sample data
```

### Testing
```bash
python test_booking_flow.py      # Booking tests
python test_login.py             # Auth tests
python test_auto_verify.py       # Verification tests
python test_booking_setup.py     # Setup tests
```

### Data Management
```bash
python import_additional_data.py # Import data
python export_to_excel.py        # Export data
python fetch_real_data.py        # Fetch from API
python update_coordinates.py     # Update locations
```

## 📁 File Navigation

### **I need to...**

| Task | File | Location |
|------|------|----------|
| Add a route | `app.py` | Line ~1043+ |
| Create model | `app.py` or `models/` | Class definition |
| Add template | `templates/` | Create `.html` file |
| Add static file | `static/` | Create in css/, js/, or images/ |
| Add service | `services/` | Create `service_name.py` |
| Write tests | `test_*.py` | Create test file |
| Configure app | `config.py` | Settings |
| Setup database | `setup_db.py` | Database initialization |
| View docs | `*.md` files | Documentation |

## 🔍 Code Patterns

### Creating a Route

```python
# In app.py
@app.route('/my-route', methods=['GET', 'POST'])
@login_required  # If authentication needed
def my_route():
    """Route description."""
    if request.method == 'POST':
        data = request.get_json()
        # Process data
        return jsonify({'status': 'success'})
    
    return render_template('my_route.html')
```

### Creating an API Endpoint

```python
# In app.py
@app.route('/api/my-endpoint', methods=['GET'])
def api_my_endpoint():
    """API endpoint description."""
    try:
        # Get data
        data = some_function()
        
        # Return JSON
        return jsonify({
            'status': 'success',
            'data': data
        }), 200
        
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500
```

### Creating a Model

```python
# In app.py or models/
class MyModel(db.Model):
    """Model description."""
    __tablename__ = 'my_models'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<MyModel {self.name}>'
```

### Using a Service

```python
# In app.py
from services.email_service import send_verification_email

@app.route('/signup', methods=['POST'])
def signup():
    # Create user
    user = Student(email=email)
    db.session.add(user)
    db.session.commit()
    
    # Send email
    send_verification_email(user.email)
    
    return jsonify({'status': 'success'})
```

### Writing a Test

```python
# In test_my_feature.py
def test_my_feature():
    """Test description."""
    # Setup
    test_data = {'name': 'Test'}
    
    # Execute
    response = client.get('/my-route', json=test_data)
    
    # Assert
    assert response.status_code == 200
    assert response.json['status'] == 'success'
```

## 🎨 HTML Template Pattern

```html
{% extends "base.html" %}

{% block title %}Page Title{% endblock %}

{% block content %}
<div class="container">
    <h1>{{ page_title }}</h1>
    
    {% if items %}
        <ul>
        {% for item in items %}
            <li>{{ item.name }}</li>
        {% endfor %}
        </ul>
    {% else %}
        <p>No items found.</p>
    {% endif %}
</div>
{% endblock %}

{% block scripts %}
<script>
    // Page-specific JavaScript
</script>
{% endblock %}
```

## 💾 Database Queries

### Common SQLAlchemy Patterns

```python
# Create
user = Student(email='test@example.com', phone='9999999999')
db.session.add(user)
db.session.commit()

# Read
user = Student.query.get(1)  # By ID
user = Student.query.filter_by(email='test@example.com').first()  # By field
all_users = Student.query.all()  # All records
active_users = Student.query.filter(Student.verified == True).all()

# Update
user.phone = '8888888888'
db.session.commit()

# Delete
db.session.delete(user)
db.session.commit()

# Count
count = Student.query.count()

# Filter with relationships
bookings = Booking.query.filter_by(student_id=user_id).all()

# Join tables
results = db.session.query(Booking, Room).join(Room).filter(
    Booking.student_id == user_id
).all()

# Order and limit
recent_bookings = Booking.query.order_by(
    Booking.created_at.desc()
).limit(10).all()
```

## 🔐 Authentication Patterns

```python
# Check if user is logged in
@app.route('/protected')
@login_required
def protected_route():
    return "Only logged in users see this"

# Check user type
if current_user.role == 'student':
    # Student-specific logic

# Require specific role
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or current_user.role != 'admin':
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/admin')
@admin_required
def admin_area():
    return "Admin only"
```

## 📤 API Response Patterns

### Success Response
```python
return jsonify({
    'status': 'success',
    'message': 'Operation completed',
    'data': {
        'id': 1,
        'name': 'Item'
    }
}), 200
```

### Error Response
```python
return jsonify({
    'status': 'error',
    'message': 'Something went wrong',
    'code': 'ERROR_CODE'
}), 400
```

### List Response
```python
return jsonify({
    'status': 'success',
    'data': [
        {'id': 1, 'name': 'Item 1'},
        {'id': 2, 'name': 'Item 2'}
    ],
    'count': 2,
    'total': 100,
    'page': 1
}), 200
```

## 🧪 Testing Patterns

### Setup Test Data
```python
def setup_test_user():
    user = Student(
        email='test@test.com',
        phone='9999999999',
        verified=True
    )
    db.session.add(user)
    db.session.commit()
    return user

def test_user_creation():
    user = setup_test_user()
    assert user.email == 'test@test.com'
```

### Test API Endpoint
```python
def test_api_endpoint():
    response = client.get('/api/rooms/featured')
    assert response.status_code == 200
    data = response.get_json()
    assert 'data' in data
    assert len(data['data']) > 0
```

### Test Database Operation
```python
def test_booking_creation():
    student = setup_test_user()
    room = Room.query.first()
    
    booking = Booking(
        student_id=student.id,
        room_id=room.id,
        check_in_date=datetime.now()
    )
    db.session.add(booking)
    db.session.commit()
    
    assert booking.id is not None
```

## 📊 Pricing Calculation

```python
# Booking pricing formula
booking_amount = 999  # Fixed
security_deposit = monthly_rent * 2
platform_fee = monthly_rent * 0.02
total_due = booking_amount + monthly_rent + security_deposit + platform_fee

# Example:
# Monthly rent: ₹10,000
# Booking amount: ₹999
# Security deposit: ₹20,000 (2x rent)
# Platform fee: ₹200 (2% of rent)
# Total due: ₹31,199
```

## 🎯 Room Status States

```
🟢 GREEN: Instant approval
   - Auto-approved bookings
   - No owner notification
   - Payment required
   - Booking confirmed immediately

🟡 YELLOW: Owner approval needed (Default)
   - Owner must approve
   - Owner receives notification
   - Payment after approval
   - Status: "Pending Owner Approval"

🔴 RED: Unavailable
   - Already booked
   - Owner marked as unavailable
   - Cannot book
   - Status: "Not Available"
```

## 📱 Responsive Design Breakpoints

```css
/* Mobile (default) */
@media (min-width: 768px) {
    /* Tablet */
}

@media (min-width: 992px) {
    /* Desktop */
}

@media (min-width: 1200px) {
    /* Large desktop */
}
```

## 🔗 Important File Locations

| What | Where |
|------|-------|
| Main app | `/app.py` |
| Models | `/models/` or in `app.py` |
| Templates | `/templates/` |
| Static files | `/static/` |
| Services | `/services/` |
| Tests | `/test_*.py` |
| Config | `/config.py` |
| Database | `/instance/roomies.db` |
| Docs | `/*.md` files |

## 🚨 Common Issues & Solutions

### Database Error
```bash
# Solution: Reset database
python reset_db.py
python setup_db.py
```

### Import Error
```python
# Solution: Check import path
from models.booking import Booking  # Correct
from booking import Booking  # Wrong
```

### 404 Not Found
- Check route spelling
- Verify @app.route() decorator
- Check file exists in templates/

### User Not Logged In
- Add @login_required decorator
- Check login route exists
- Verify session configuration

### API Not Returning Data
- Check query returns results
- Verify jsonify() is used
- Check correct response code (200 vs 201)

## 📞 Quick Debug Checklist

- [ ] Database connection working? → Check config.py
- [ ] Routes defined? → Check app.py
- [ ] Templates exist? → Check templates/
- [ ] Static files loading? → Check static/ and HTML link
- [ ] API returns data? → Test in browser/Postman
- [ ] Authentication working? → Check login process
- [ ] Environment variables set? → Check .env file
- [ ] Tests passing? → Run test files

## 🎯 Development Workflow

1. **Pick a task** from CONTRIBUTING.md or GitHub issues
2. **Create branch:** `git checkout -b feature/name`
3. **Write code** following patterns above
4. **Add tests** for new functionality
5. **Test locally** in browser/with curl
6. **Run tests** - `python test_*.py`
7. **Commit:** `git add . && git commit -m "feat: description"`
8. **Push:** `git push origin feature/name`
9. **Create PR** with description
10. **Address review** feedback
11. **Merge** to main

## 📚 Documentation Links

- **Quick Start:** START_HERE.md
- **Setup:** SETUP.md
- **Features:** FEATURES.md
- **Booking System:** BOOKING_SYSTEM_DOCUMENTATION.md
- **Verification:** VERIFICATION_FEATURE.md
- **Revenue:** REVENUE_SYSTEM_SUMMARY.md
- **Deployment:** DEPLOYMENT_GUIDE.md
- **Contributing:** CONTRIBUTING.md
- **File Guide:** FILE_DOCUMENTATION.md
- **Structure:** PROJECT_STRUCTURE.md

## 🔧 Environment Variables

Create `.env` file:
```
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///roomies.db
GOOGLE_VISION_API_KEY=your-api-key
RAZORPAY_KEY_ID=your-key
RAZORPAY_KEY_SECRET=your-secret
EMAIL_USER=your-email
EMAIL_PASSWORD=your-password
```

## 📊 Project Statistics Quick View

| Metric | Value |
|--------|-------|
| Python Files | 40+ |
| HTML Templates | 20+ |
| Lines of Code | 4,200+ |
| Database Tables | 8+ |
| API Endpoints | 15+ |
| Features | 28+ |
| Test Files | 5+ |
| Documentation | 15+ files |
| Git Commits | 100+ |
| Contributors | [Your team] |

## 🆘 Getting Help

1. **Check documentation** - See *.md files
2. **Search code** - Use Ctrl+Shift+F in VS Code
3. **Read tests** - See test_*.py for examples
4. **Ask in issues** - Create GitHub issue
5. **Discord/Chat** - Ask team members

---

**Last Updated:** January 15, 2024
**Version:** 1.0.0
**Maintainer:** [Team Name]

Remember: When in doubt, check the tests and documentation! 🚀

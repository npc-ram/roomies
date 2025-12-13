# Project Structure Guide

Complete directory and file organization for the Roomies Backend.

## 📁 Root Directory Structure

```
roomies-backend-main/
├── 📄 Core Application Files
│   ├── app.py                    # Main Flask application (4,342 lines)
│   ├── config.py                 # Configuration settings
│   ├── requirements.txt           # Python dependencies
│   ├── Procfile                  # Heroku deployment
│   └── .env.example              # Environment template
│
├── 📁 models/                    # Database models
│   ├── __init__.py              # Package init
│   ├── base.py                  # Base model class
│   ├── booking.py               # Booking, Payment, Refund models
│   └── property.py              # Room, RoomImage models
│
├── 📁 services/                 # Business logic services
│   ├── __init__.py              # Package init
│   ├── email_service.py         # Email notifications
│   ├── verification_service.py  # AI verification (Google Vision)
│   ├── payment_service.py       # Razorpay integration
│   ├── contract_service.py      # Contract PDF generation
│   └── news_service.py          # News/updates
│
├── 📁 agents/                   # AI agents
│   ├── __init__.py              # Package init
│   └── chatbot.py               # Chatbot agent
│
├── 📁 utils/                    # Utility functions
│   ├── validators.py            # Input validation
│   ├── decorators.py            # Flask decorators
│   ├── helpers.py               # Helper functions
│   └── constants.py             # Constants
│
├── 📁 migrations/               # Database migrations
│   ├── add_status_fields.py     # Status field migration
│   ├── add_verifications.py     # Verification migration
│   ├── fix_bookings_table.py    # Booking table fixes
│   ├── fix_missing_columns.py   # Missing column fixes
│   ├── migrate_booking_system.py  # Booking system migration
│   └── migrate_revenue_system.py  # Revenue system migration
│
├── 📁 templates/                # HTML templates (20+ files)
│   ├── base.html                # Base template
│   ├── index.html               # Home page
│   ├── booking.html             # Booking form (516 lines)
│   ├── booking_confirmation.html # Confirmation page (335 lines)
│   ├── my_bookings.html         # Booking dashboard (477 lines)
│   ├── explore.html             # Room exploration
│   ├── discover.html            # Room discovery
│   ├── admin_verifications.html # Admin verification panel
│   └── ... (15+ more templates)
│
├── 📁 static/                   # Static files
│   ├── css/                     # Stylesheets
│   ├── js/                      # JavaScript files
│   ├── images/                  # Images and icons
│   ├── contracts/               # Generated contracts
│   ├── manifest.json            # PWA manifest
│   └── service-worker.js        # Service worker
│
├── 📁 data/                     # Data files
│   ├── faqs.json                # FAQ content
│   ├── mumbai_engineering_colleges.csv # Location data
│   └── real_data_dump.json      # Sample data
│
├── 📁 instance/                 # Instance folder
│   ├── roomies.db               # SQLite database
│   └── ...
│
├── 📁 exports/                  # Exported files
│   └── ... (Excel exports, etc.)
│
├── 📁 uploads/                  # User uploads
│   ├── documents/               # ID proofs, etc.
│   └── profiles/                # Profile photos
│
├── 📁 coreui-free-react-admin-template-main/
│   └── (Admin dashboard React app)
│
├── 📄 Documentation Files
│   ├── README.md                        # Project README
│   ├── README_GITHUB.md                # GitHub README
│   ├── FILE_DOCUMENTATION.md           # File guide
│   ├── PROJECT_STRUCTURE.md            # This file
│   ├── CONTRIBUTING.md                 # Contribution guide
│   ├── SETUP.md                        # Setup instructions
│   ├── START_HERE.md                   # Quick start
│   ├── FEATURES.md                     # Features list
│   ├── BOOKING_SYSTEM_DOCUMENTATION.md # Booking docs
│   ├── REVENUE_SYSTEM_SUMMARY.md       # Revenue docs
│   ├── VERIFICATION_FEATURE.md         # Verification docs
│   ├── DEPLOYMENT_GUIDE.md             # Deployment docs
│   └── ... (5+ more docs)
│
└── 📄 Testing & Setup Files
    ├── test_booking_flow.py            # Booking tests
    ├── test_login.py                   # Auth tests
    ├── test_auto_verify.py             # Verification tests
    ├── test_booking_setup.py           # Setup tests
    ├── test_agent.py                   # Agent tests
    ├── setup_db.py                     # Database setup
    ├── reset_db.py                     # Database reset
    ├── create_admin.py                 # Admin creation
    └── ... (5+ more setup files)
```

## 🎯 Core Files Overview

### **app.py** (4,342 lines)
Main application file containing:
- Flask app initialization
- Database model definitions
  - Student, Owner, Admin, Room, Booking, Payment, etc.
- 20+ route handlers
- 15+ API endpoints
- Authentication logic
- Business logic
- Error handling

**Key Routes:**
- `/ (GET)` - Home page
- `/login (GET/POST)` - User login
- `/signup (GET/POST)` - User registration
- `/explore (GET)` - Room exploration
- `/discover (GET)` - Room discovery
- `/booking (GET)` - Booking form
- `/api/rooms/featured (GET)` - Featured rooms API
- `/api/rooms/search (GET)` - Search API
- `/api/bookings/create (POST)` - Create booking API
- And 10+ more...

### **config.py**
Application configuration:
```python
SQLALCHEMY_DATABASE_URI = 'sqlite:///roomies.db'
SECRET_KEY = 'your-secret-key'
SQLALCHEMY_TRACK_MODIFICATIONS = False
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max upload
```

### **requirements.txt**
All Python dependencies:
```
Flask==2.3.2
Flask-SQLAlchemy==3.0.5
Flask-Login==0.6.2
Werkzeug==2.3.6
google-cloud-vision==3.3.1
google-maps-api==1.0.0
razorpay==1.3.0
python-dotenv==1.0.0
Pillow==9.5.0
requests==2.31.0
...
```

## 📊 Models Directory Structure

### **models/base.py**
Base model class with common fields:
- `id` - Primary key
- `created_at` - Creation timestamp
- `updated_at` - Update timestamp
- Common methods

### **models/property.py**
Room and property models:
- `Room` - Room listing
- `RoomImage` - Room images
- `RoomAmenity` - Room amenities

### **models/booking.py**
Booking and payment models:
- `Booking` - Main booking model (30+ fields)
- `Payment` - Payment tracking
- `RefundRequest` - Refund management

## 🔧 Services Directory Structure

### **services/email_service.py**
Email functionality:
- `send_verification_email()` - Verification emails
- `send_booking_confirmation()` - Booking confirmations
- `send_payment_receipt()` - Payment receipts
- SMTP configuration

### **services/verification_service.py**
AI verification using Google Vision:
- `verify_id_document()` - Document verification
- `verify_selfie()` - Selfie verification
- `analyze_image()` - Image analysis
- Auto-approval/rejection logic

### **services/payment_service.py**
Razorpay payment integration:
- `create_order()` - Create payment order
- `verify_payment()` - Verify payment
- `process_refund()` - Process refunds
- Webhook handling

### **services/contract_service.py**
Contract PDF generation:
- `generate_contract()` - Create contract PDF
- `sign_contract()` - E-signature integration
- `store_contract()` - Save to database

## 📱 Templates Directory

### Core Templates
```
templates/
├── base.html                    # Base layout
├── index.html                   # Home page
├── nav.html                     # Navigation
└── footer.html                  # Footer
```

### User Templates
```
templates/
├── login.html                   # Login page
├── signup.html                  # Registration
├── profile.html                 # User profile
├── dashboard.html               # User dashboard
└── messages.html                # Messaging
```

### Room Templates
```
templates/
├── explore.html                 # Room exploration
├── discover.html                # Room discovery
├── room_detail.html             # Room detail page
├── room_listing.html            # Room listing
└── search_results.html          # Search results
```

### Booking Templates
```
templates/
├── booking.html                 # Booking form
├── booking_confirmation.html    # Booking confirmation
├── my_bookings.html             # Booking dashboard
└── booking_details.html         # Booking details
```

### Admin Templates
```
templates/
├── admin_dashboard.html         # Admin dashboard
├── admin_users.html             # User management
├── admin_rooms.html             # Room management
├── admin_bookings.html          # Booking management
├── admin_payments.html          # Payment management
└── admin_verifications.html     # Verification management
```

### Other Templates
```
templates/
├── about.html                   # About page
├── contact.html                 # Contact page
├── faq.html                     # FAQ page
├── features.html                # Features page
├── terms.html                   # Terms of service
├── privacy.html                 # Privacy policy
├── findmate.html                # Find roommate
├── ai_matching.html             # AI matching
├── chatbot.html                 # Chatbot interface
└── 404.html                     # Not found page
```

## 💾 Static Files Structure

```
static/
├── css/
│   ├── style.css                # Main styles
│   ├── responsive.css           # Responsive design
│   ├── admin.css                # Admin styles
│   └── themes/
│       ├── dark.css             # Dark theme
│       └── light.css            # Light theme
│
├── js/
│   ├── main.js                  # Main script
│   ├── booking.js               # Booking logic
│   ├── api.js                   # API calls
│   ├── validation.js            # Form validation
│   ├── charts.js                # Chart library
│   └── admin.js                 # Admin scripts
│
├── images/
│   ├── logo.png                 # Logo
│   ├── icons/                   # Icons
│   ├── rooms/                   # Room images
│   └── profiles/                # User profiles
│
├── contracts/                   # Generated PDF contracts
├── manifest.json                # PWA manifest
└── service-worker.js            # Service worker
```

## 🧪 Testing Files

```
test_*.py files:
├── test_booking_flow.py        # Booking workflow tests
├── test_login.py               # Authentication tests
├── test_auto_verify.py         # Verification tests
├── test_booking_setup.py       # Setup tests
└── test_agent.py               # Agent tests
```

## 🛠️ Setup & Migration Files

```
Setup/Migration Files:
├── setup_db.py                 # Initial database setup
├── reset_db.py                 # Database reset
├── recreate_db.py              # Recreate database
├── create_admin.py             # Create admin user
├── populate_real_data.py       # Populate sample data
├── import_additional_data.py   # Import more data
├── export_to_excel.py          # Export to Excel
└── migrations/                 # Database migrations
    ├── add_status_fields.py
    ├── add_verifications.py
    ├── fix_bookings_table.py
    ├── fix_missing_columns.py
    ├── migrate_booking_system.py
    └── migrate_revenue_system.py
```

## 📚 Documentation Files

### Main Documentation
- **README.md** - Original project README
- **README_GITHUB.md** - GitHub-ready README
- **CONTRIBUTING.md** - Contribution guidelines
- **FILE_DOCUMENTATION.md** - File-by-file guide
- **PROJECT_STRUCTURE.md** - This file

### Feature Documentation
- **FEATURES.md** - All features listed
- **BOOKING_SYSTEM_DOCUMENTATION.md** - Booking system details
- **BOOKING_SYSTEM_GUIDE.md** - Booking user guide
- **BOOKING_SYSTEM_SUMMARY.md** - Booking summary
- **REVENUE_SYSTEM_SUMMARY.md** - Revenue system details
- **VERIFICATION_FEATURE.md** - Verification system
- **VERIFICATION_COMPLETE.md** - Verification completion status

### Setup & Deployment
- **SETUP.md** - Setup instructions
- **SETUP_BOOKING_SYSTEM.md** - Booking system setup
- **DEPLOYMENT_GUIDE.md** - Production deployment
- **START_HERE.md** - Quick start guide

### Other Documentation
- **SIGNIN_ERROR_FIX.md** - Sign-in troubleshooting
- **IMPLEMENTATION_SUMMARY.md** - Implementation overview
- **BOOKING_IMPLEMENTATION_CHANGELOG.md** - Changes log
- **BOOKING_COMPLETION_REPORT.md** - Completion report

## 🗂️ Key File Purposes

### Database Models
| File | Purpose | Main Classes |
|------|---------|--------------|
| app.py | Core app + models | Student, Owner, Admin, Room, Booking |
| models/base.py | Base model | BaseModel with timestamps |
| models/property.py | Property models | Room, RoomImage, RoomAmenity |
| models/booking.py | Booking models | Booking, Payment, RefundRequest |

### Services
| File | Purpose | Key Functions |
|------|---------|----------------|
| services/email_service.py | Email sending | send_verification_email, send_booking_confirmation |
| services/verification_service.py | AI verification | verify_id_document, verify_selfie, analyze_image |
| services/payment_service.py | Razorpay integration | create_order, verify_payment, process_refund |
| services/contract_service.py | Contract generation | generate_contract, sign_contract |

### Routes & APIs
| Route/API | Method | Purpose | Auth Required |
|-----------|--------|---------|----------------|
| / | GET | Home page | No |
| /login | POST | User login | No |
| /booking | GET | Booking form | Yes |
| /api/rooms/featured | GET | Featured rooms | No |
| /api/bookings/create | POST | Create booking | Yes |
| /api/bookings/search | GET | Search bookings | Yes |
| /admin/dashboard | GET | Admin dashboard | Yes (Admin) |
| /api/verify | POST | Verify document | Yes |

### Templates
| Template | Purpose | User Type |
|----------|---------|-----------|
| index.html | Home page | Public |
| booking.html | Booking form | Student |
| my_bookings.html | Booking dashboard | Student/Owner |
| admin_dashboard.html | Admin panel | Admin |
| login.html | Login page | Public |
| profile.html | User profile | Authenticated |

## 🔄 Data Flow

### Booking Flow
```
1. User views room (explore.html)
2. Clicks "Book Now" → /booking page (booking.html)
3. Selects dates and confirms (POST /api/bookings/create)
4. System creates booking in database
5. Redirect to confirmation page (booking_confirmation.html)
6. Show status (green/yellow/red)
7. If payment needed, show payment form
8. After payment, update booking status
9. Send confirmation email
10. Owner receives notification (if yellow status)
```

### Verification Flow
```
1. New user uploads ID document
2. System calls Google Vision API
3. Extracts & verifies document
4. User takes selfie with document
5. System compares face with ID photo
6. If match → Auto-approve (green status)
7. If no match → Manual review needed (admin)
8. Admin verifies manually
9. Update user verification status
```

### Payment Flow
```
1. Booking created with payment needed
2. User clicks "Pay Now"
3. System creates Razorpay order
4. Payment form displays
5. User enters card details
6. Razorpay processes payment
7. Webhook confirms payment
8. Update booking payment status
9. Send receipt email
10. Update room availability if needed
```

## 📊 Database Schema Quick Reference

### Main Tables
| Table | Purpose | Key Fields |
|-------|---------|-----------|
| student | Student users | email, phone, verified |
| owner | Owner/landlord users | email, phone, bank_account |
| admin | Admin users | email, role |
| room | Room listings | address, price, status |
| booking | Bookings | student_id, room_id, dates |
| payment | Payments | booking_id, amount, status |
| refund_request | Refund requests | booking_id, reason |
| contact_message | Contact form messages | email, message, source |

## 🚀 Common Development Tasks

### Add New Route
1. Add function in app.py
2. Add @app.route() decorator
3. Return render_template or jsonify
4. Test with browser/API client

### Add New Template
1. Create .html file in templates/
2. Extend base.html
3. Add CSS classes (responsive)
4. Link in route
5. Test responsiveness

### Add New Model
1. Create class in models/ or app.py
2. Define fields with db.Column
3. Add relationships if needed
4. Create migration
5. Run setup_db.py

### Add New API Endpoint
1. Add function in app.py
2. Use @app.route() with /api/ prefix
3. Accept request.get_json()
4. Return jsonify() response
5. Add error handling
6. Document in README

### Add New Service
1. Create file in services/
2. Define class with methods
3. Import in app.py
4. Call from routes/models
5. Add tests in test_*.py

## 🎯 Navigation Guide

**Want to...**

- **Fix a bug?** Check CONTRIBUTING.md → Look in app.py/templates
- **Add a feature?** See CONTRIBUTING.md → Add model/route/template
- **Deploy?** Read DEPLOYMENT_GUIDE.md
- **Understand booking?** See BOOKING_SYSTEM_DOCUMENTATION.md
- **Understand verification?** See VERIFICATION_FEATURE.md
- **Understand revenue?** See REVENUE_SYSTEM_SUMMARY.md
- **Get started?** Read START_HERE.md
- **Know all features?** See FEATURES.md
- **File locations?** See FILE_DOCUMENTATION.md
- **Project structure?** You're reading it!

## 📞 Quick Links

- **Main App:** app.py (4,342 lines)
- **Database Models:** models/ or app.py
- **Templates:** templates/ (20+ files)
- **Tests:** test_*.py files
- **Docs:** *.md files
- **Setup:** setup_db.py, config.py

---

**Last Updated:** January 2024
**Total Files:** 80+
**Total Lines of Code:** 4,200+
**Documentation Files:** 15+

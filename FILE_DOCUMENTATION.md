# Roomies Platform - Complete File Documentation

## 📚 Project Structure Overview

This document provides detailed summaries of every major file in the Roomies booking platform project.

---

## 🔴 CORE APPLICATION FILES

### **app.py** (4,342 lines)
**Purpose:** Main Flask application containing all routes, models, and business logic

**Key Components:**
- Database models (Student, Owner, Room, Booking, ContactMessage, etc.)
- Authentication routes (signup, login, logout, verify email)
- Room management endpoints (search, filter, featured rooms)
- Booking system routes and API endpoints
- Admin dashboard and management routes
- Payment integration skeleton (Razorpay)
- Email notification system
- File upload handling

**Key Models in File:**
1. **Student** - User model for student accounts with phone, email, verification
2. **Owner** - Landlord/property owner accounts
3. **Room** - Property listing model with pricing, amenities, availability
4. **Booking** - Reservation model with 30+ fields for tracking bookings
5. **ContactMessage** - Contact form submissions
6. **RefundRequest** - Refund management system

**Database:** SQLite (roomies.db)  
**ORM:** SQLAlchemy  
**Authentication:** Flask-Login  

**Main Routes:**
- `/` - Home page with featured rooms
- `/signup`, `/login`, `/logout` - Authentication
- `/booking` - Booking form
- `/bookings/{id}` - Booking confirmation
- `/my-bookings` - User bookings dashboard
- `/explore`, `/discover` - Room browsing
- `/admin` - Admin dashboard
- `/api/rooms/*` - Room API endpoints
- `/api/bookings/*` - Booking API endpoints

---

### **config.py** (Configuration)
**Purpose:** Flask configuration management

**Contains:**
- Database URI configuration
- Secret key management
- Session settings
- Upload folder paths
- Email SMTP settings
- Debug mode configuration

---

### **requirements.txt** (Dependencies)
**Purpose:** Python package dependencies list

**Key Dependencies:**
- Flask & Flask extensions (Login, SQLAlchemy, Mail)
- SQLAlchemy ORM
- Razorpay payment SDK
- Werkzeug (file uploads)
- Python-dotenv (environment variables)

---

## 📄 MODELS & DATA

### **models/booking.py** (Booking Models)
**Purpose:** Separate booking-related database models

**Models:**
- **Booking** - Main booking reservation model
- **RoomAvailabilityStatus** - Room status tracking (green/yellow/red)
- **Payment** - Razorpay transaction tracking
- **RefundRequest** - Refund management

**Features:**
- Financial calculations
- Status workflow management
- Contract date tracking
- Payment integration

---

### **models/property.py** (Property Models)
**Purpose:** Room/property listing models

**Models:**
- **Room** - Core property model with pricing, location, amenities
- **RoomImage** - Multiple images per room
- **Amenity** - Room feature tags

---

### **models/base.py** (Base Model)
**Purpose:** Common database model functionality

**Contains:**
- Timestamps (created_at, updated_at)
- Common fields and methods
- BaseModel class for inheritance

---

## 🔧 UTILITIES & SERVICES

### **utils/email_service.py** (Email Handling)
**Purpose:** Email notification system

**Functions:**
- `send_email()` - Generic email sending
- `send_verification_email()` - Verification links
- `send_booking_confirmation()` - Booking notifications
- `send_booking_approval()` - Owner approval notifications
- `send_payment_receipt()` - Payment confirmations

**Uses:** Flask-Mail with Gmail SMTP

---

### **utils/verification.py** (AI Verification)
**Purpose:** Document/ID verification system

**Features:**
- Face recognition (using cv2)
- Document OCR
- Verification token generation
- Verification status tracking

---

### **utils/contract_generator.py** (Contract Generation)
**Purpose:** Digital rental agreement generation

**Features:**
- PDF contract generation
- Dynamic content insertion
- Contract signing workflow
- Document storage

---

### **services/news_service.py** (News Integration)
**Purpose:** News feed integration for platform

**Features:**
- News fetching from API
- Caching news data
- News display in dashboard

---

### **search_engine.py** (Search Functionality)
**Purpose:** Room search and filtering engine

**Features:**
- Full-text search on room titles and descriptions
- Filter by price, location, amenities
- Search indexing for performance
- Pagination support

---

## 🧪 TESTING FILES

### **test_booking_flow.py** (Integration Tests)
**Purpose:** Automated testing for complete booking workflow

**Tests:**
- User signup and login
- Room loading from API
- Booking creation
- Confirmation page verification
- Authorization checks

**Run:** `python test_booking_flow.py`

---

### **test_booking_setup.py** (Setup Tests)
**Purpose:** Test booking system setup and configuration

**Validates:**
- Database structure
- Model relationships
- Route registration

---

### **test_login.py** (Authentication Tests)
**Purpose:** Login and authentication flow testing

**Tests:**
- Valid/invalid login attempts
- Session management
- Password verification

---

### **test_auto_verify.py** (Verification Tests)
**Purpose:** AI verification system testing

**Tests:**
- Document upload
- Verification processing
- Status updates

---

### **test_agent.py** (Chatbot Agent Tests)
**Purpose:** AI chatbot functionality testing

---

## 🛠️ SETUP & MIGRATION FILES

### **setup_db.py** (Database Setup)
**Purpose:** Initialize database with schema and sample data

**Features:**
- Create all tables
- Create default admin account
- Load sample rooms (if provided)
- Create subscription plans

**Run:** `python setup_db.py`

---

### **recreate_db.py** (Database Recreation)
**Purpose:** Complete database reset

**Clears:**
- All tables
- All data
- All relationships

**Warning:** Destructive operation

---

### **reset_db.py** (Database Reset)
**Purpose:** Partial database reset with configuration preservation

---

### **migrations/migrate_booking_system.py** (Booking Schema Migration)
**Purpose:** Add booking system tables to existing database

**Creates:**
- Bookings table
- Payments table
- RefundRequests table
- Relevant indexes

---

### **migrations/migrate_revenue_system.py** (Revenue Tracking Migration)
**Purpose:** Add revenue tracking tables

---

### **migrations/add_verifications.py** (Verification System Migration)
**Purpose:** Add AI verification tables and fields

---

## 📊 DATA & IMPORT FILES

### **populate_real_data.py** (Data Population)
**Purpose:** Populate database with real Mumbai engineering college data

**Data Imported:**
- 81 room listings
- Actual college locations (NMIMS, IIT-B, BITS, etc.)
- Real pricing data
- Amenity information
- Location coordinates

---

### **import_additional_data.py** (Additional Data Import)
**Purpose:** Import supplementary data

**Includes:**
- College information
- Area information
- Additional room listings

---

### **fetch_real_data.py** (Real Data Fetching)
**Purpose:** Fetch data from external sources

---

### **update_coordinates.py** (Coordinate Updates)
**Purpose:** Update room location coordinates for mapping

**Uses:** Geocoding APIs to get lat/long for rooms

---

### **export_to_excel.py** (Data Export)
**Purpose:** Export room listings and bookings to Excel format

**Output:**
- Room inventory spreadsheet
- Booking reports
- Financial summaries

---

### **check_bookings_table.py** (Database Verification)
**Purpose:** Verify bookings table structure and data integrity

---

## 🎯 MANAGEMENT & ADMIN FILES

### **create_admin.py** (Admin Account Creation)
**Purpose:** Create admin user accounts via command line

**Usage:**
```bash
python create_admin.py
# Follow prompts for email/password
```

---

### **approve_verification_manual.py** (Manual Verification Approval)
**Purpose:** Manually approve pending verifications (admin function)

---

### **debug_verification.py** (Verification Debugging)
**Purpose:** Debug and troubleshoot AI verification system

**Features:**
- Check verification status
- Reprocess failed verifications
- View verification logs

---

### **debug_gemini.py** (AI Model Debugging)
**Purpose:** Debug Google Gemini AI integration

**Tests:**
- AI model connectivity
- Response quality
- Error handling

---

## 📂 DIRECTORY SUMMARIES

### **templates/** (HTML Templates)
**Purpose:** All user-facing HTML pages

**Key Files:**
- **index.html** - Home page with featured rooms
- **signup.html** - User registration
- **login.html** - User login
- **booking.html** - Room booking form (516 lines)
- **booking_confirmation.html** - Booking success page (335 lines)
- **my_bookings.html** - User bookings dashboard (477 lines)
- **explore.html** - Room browsing/search page
- **discover.html** - Room discovery with filters
- **admin_dashboard.html** - Admin management interface
- **partials/header.html** - Navigation header
- **partials/sidebar.html** - Navigation sidebar

**Total:** 20+ HTML files with full UI

---

### **static/** (Static Assets)
**Purpose:** CSS, JavaScript, images, and other static files

**Subdirectories:**
- **css/** - Stylesheets (main.css, responsive.css, etc.)
- **js/** - JavaScript files (main.js, booking.js, etc.)
- **images/** - UI images and icons
- **contracts/** - Contract templates

---

### **models/** (Python Models)
**Purpose:** Database model definitions

**Files:**
- `__init__.py` - Model initialization
- `base.py` - Base model class
- `booking.py` - Booking models
- `property.py` - Room/property models

---

### **utils/** (Utility Functions)
**Purpose:** Reusable utility functions

**Files:**
- `__init__.py` - Utils initialization
- `email_service.py` - Email notifications
- `verification.py` - AI verification
- `contract_generator.py` - PDF contract generation

---

### **services/** (Business Logic Services)
**Purpose:** Business logic and external integrations

**Files:**
- `__init__.py` - Services initialization
- `news_service.py` - News feed integration

---

### **agents/** (AI Agents)
**Purpose:** AI chatbot and automation agents

**Files:**
- `__init__.py` - Agents initialization
- `chatbot.py` - Chatbot implementation

---

### **migrations/** (Database Migrations)
**Purpose:** Database schema changes and migrations

**Files:**
- `migrate_booking_system.py` - Booking system migration
- `migrate_revenue_system.py` - Revenue system migration
- `add_verifications.py` - Verification system migration
- `add_status_fields.py` - Status field additions
- `fix_bookings_table.py` - Booking table fixes
- `fix_missing_columns.py` - Missing column fixes

---

### **data/** (Data Files)
**Purpose:** Static data files for import/reference

**Files:**
- `mumbai_engineering_colleges.csv` - College listings
- `faqs.json` - FAQ content
- `real_data_dump.json` - Sample room data

---

### **instance/** (Instance Data)
**Purpose:** Local instance-specific data

**Contents:**
- Instance database
- Instance configuration
- Session data

---

### **uploads/** (User Uploads)
**Purpose:** User-uploaded files

**Contains:**
- Profile pictures
- ID documents
- Verification images

---

### **exports/** (Export Data)
**Purpose:** Generated export files

**Contains:**
- Excel spreadsheets
- CSV files
- Report PDFs

---

## 📖 DOCUMENTATION FILES

### **README.md** (Project README)
Original project documentation and overview

---

### **START_HERE.md** (Entry Point)
Quick start guide for new developers - **READ THIS FIRST**

---

### **BOOKING_SYSTEM_README.md** (Booking Overview)
Complete booking system overview and features

---

### **BOOKING_SYSTEM_DOCUMENTATION.md** (Booking Technical)
Detailed technical documentation for booking system

---

### **BOOKING_QUICK_START.md** (Booking Quick Reference)
Quick reference guide for booking features

---

### **BOOKING_SYSTEM_SUMMARY.md** (Booking Statistics)
Booking system statistics and metrics

---

### **BOOKING_COMPLETION_REPORT.md** (Booking Final Report)
Final completion report for booking system

---

### **BOOKING_DOCUMENTATION_INDEX.md** (Booking Navigation)
Navigation guide for booking documentation

---

### **README_BOOKING_COMPLETE.md** (Booking Visual Summary)
Visual summary and status of booking system

---

### **BOOKING_IMPLEMENTATION_CHANGELOG.md** (Booking Changelog)
Detailed changelog of booking system implementation

---

### **FEATURES.md** (Platform Features)
Complete list of platform features

---

### **SETUP.md** (Setup Instructions)
Initial setup guide for developers

---

### **DEPLOYMENT_GUIDE.md** (Deployment Instructions)
Guide for deploying to production

---

### **VERIFICATION_FEATURE.md** (Verification System)
Documentation for AI verification system

---

### **VERIFICATION_UPDATE.md** (Verification Updates)
Updates to verification system

---

### **VERIFICATION_COMPLETE.md** (Verification Final)
Final status of verification system

---

### **REVENUE_SYSTEM_SUMMARY.md** (Revenue System)
Summary of revenue tracking system

---

### **REVENUE_TESTING_GUIDE.md** (Revenue Testing)
Testing guide for revenue system

---

### **IMPLEMENTATION_SUMMARY.md** (Implementation Overview)
Summary of all implementations

---

### **SIGNIN_ERROR_FIX.md** (Bug Fix Documentation)
Documentation of sign-in error fix

---

## ⚙️ CONFIGURATION FILES

### **.env** (Environment Variables)
**Contains:**
- Database credentials
- Email SMTP settings
- API keys (Razorpay, Google, etc.)
- Secret keys
- Debug mode flag

**Note:** Not committed to git (sensitive)

---

### **.env.example** (Environment Template)
**Purpose:** Template showing required environment variables

**Used for:** Setting up local environment

---

### **.gitignore** (Git Ignore Rules)
**Purpose:** Specify files to exclude from version control

**Ignores:**
- .env files
- Virtual environment
- __pycache__
- .pyc files
- Instance files
- Node modules

---

### **Procfile** (Heroku Deployment)
**Purpose:** Configuration for Heroku deployment

**Contains:**
- Web dyno specification
- Worker processes

---

### **config.py** (Flask Configuration)
**Purpose:** Flask application configuration

---

## 🎨 FRONTEND FILES

### **coreui-free-react-admin-template-main/** (React Admin)
**Purpose:** Optional React admin dashboard template

**Contains:**
- React components
- Admin UI
- Dashboard pages

---

### **chatbot.html** (Chatbot Interface)
**Purpose:** Chatbot UI for customer support

**Features:**
- Real-time chat
- AI responses
- Chat history

---

## 📦 PROJECT METADATA

### **package.json** (Node Dependencies)
**Purpose:** Node.js project dependencies (if React is used)

---

## 🗄️ DATABASE

### **roomies.db** (SQLite Database)
**Purpose:** SQLite database file containing all application data

**Tables:**
- students
- owners
- rooms
- bookings
- contacts
- payments
- refunds
- verifications

---

## 📊 QUICK STATISTICS

```
Total Python Files:         40+
Total Templates:            20+
Total Documentation Files:   15+
Total Test Files:            5
Total Lines of Code:         4,200+
Database Tables:             8+
API Endpoints:              20+
Features Implemented:        28+
```

---

## 🎯 FILE PRIORITY FOR DEVELOPERS

### **Essential (Must Know)**
1. ✅ **app.py** - Core application logic
2. ✅ **models/** - Database schema
3. ✅ **templates/** - UI pages
4. ✅ **config.py** - Configuration

### **Important (Should Know)**
5. ✅ **utils/** - Helper functions
6. ✅ **services/** - Business logic
7. ✅ **static/** - Frontend assets
8. ✅ **migrations/** - Database changes

### **Reference (Nice to Know)**
9. ✅ **tests/** - Testing patterns
10. ✅ **data/** - Sample data
11. ✅ **Documentation/** - Feature guides

---

## 🚀 FILE DEPENDENCIES

```
app.py (Main Hub)
├── models/ (Database)
├── utils/ (Utilities)
├── services/ (Logic)
├── templates/ (UI)
├── static/ (Assets)
└── config.py (Configuration)

models/
├── base.py (Foundation)
├── booking.py (Bookings)
└── property.py (Rooms)

utils/
├── email_service.py
├── verification.py
└── contract_generator.py
```

---

## 📝 DEVELOPMENT WORKFLOW

1. **Setup:** Run `setup_db.py`
2. **Configure:** Set `.env` variables
3. **Develop:** Modify files in `app.py`, `models/`, `templates/`
4. **Test:** Run test files in `tests/`
5. **Deploy:** Follow `DEPLOYMENT_GUIDE.md`

---

## 🆘 COMMON TASKS

| Task | File |
|------|------|
| Add new feature | `app.py` + `models/` |
| Change database schema | `models/` + `migrations/` |
| Update UI | `templates/` + `static/` |
| Fix bug | Check error in `app.py`, then fix |
| Add test | Create file in root (test_*.py) |
| Configure app | Edit `config.py` or `.env` |
| Send email | Use `utils/email_service.py` |
| Generate PDF | Use `utils/contract_generator.py` |

---

**Last Updated:** December 2025  
**Project Status:** Production Ready  
**Version:** 1.0

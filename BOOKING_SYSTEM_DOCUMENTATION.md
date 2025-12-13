# Roomies Booking System - Implementation Guide

## Overview

A complete booking system for the Roomies platform with room status management (green/yellow/red), booking workflow, and payment integration support.

## System Architecture

### Room Availability Status (Owner Sets)
- **Green** 🟢: Room available for instant booking (auto-approved)
- **Yellow** 🟡: Room available but needs owner approval (default)
- **Red** 🔴: Room already booked/unavailable

### Booking Status Flow
```
pending → payment_initiated → confirmed → active → completed/cancelled
```

## Database Models

### Booking Model (`app.py` lines 519-620)

**Key Fields:**
- `id`: Primary key
- `student_id`: Reference to Student
- `room_id`: Reference to Room
- `room_availability_status`: Inherited from room at booking time (green/yellow/red)
- `booking_status`: Current booking status (pending, payment_initiated, confirmed, active, completed, cancelled)
- `payment_status`: Payment tracking (pending, partial, completed, refunded)

**Financial Fields:**
- `booking_amount`: ₹999 (flat booking fee)
- `monthly_rent`: Room's monthly rent
- `security_deposit`: 2x monthly rent
- `platform_fee`: 2% of monthly rent
- `total_paid`: Amount paid so far

**Contract Fields:**
- `contract_start_date`: Move-in date
- `contract_end_date`: Move-out date
- `contract_duration_months`: Lease term (default 11 months)
- `contract_signed`: Boolean flag
- `contract_pdf_path`: Path to signed contract

**Razorpay Fields:**
- `razorpay_order_id`: Order ID from Razorpay
- `razorpay_payment_id`: Payment ID after transaction
- `razorpay_signature`: Payment signature for verification

**Methods:**
- `calculate_platform_fee()`: Returns 2% of monthly rent
- `calculate_security_deposit()`: Returns 2x monthly rent
- `calculate_total_due()`: Returns booking_fee + deposit + rent + platform_fee
- `can_auto_book`: Property that checks if room_availability_status == 'green'
- `needs_approval`: Property that checks if room_availability_status == 'yellow'
- `is_unavailable`: Property that checks if room_availability_status == 'red'

## Routes

### Frontend Pages

#### 1. Booking Page
**Route:** `GET /booking?room_id={room_id}`
**File:** `templates/booking.html`
**Template:** `booking_page` function in `app.py` (line 1043)
**Features:**
- Room pre-selection via URL parameter
- Check-in/Check-out date picker
- Duration auto-calculation
- Real-time price breakdown
- Guest count and special requests
- Room status indicator with explanatory text
- Form validation before submission

**JavaScript Functions:**
- `loadRoomDetails(roomId)`: Fetch room info from API
- `displayRoomSummary(room)`: Display room details and amenities
- `calculateDuration()`: Calculate contract duration in months
- `updatePricing()`: Update price breakdown in real-time
- Form submission handler that calls `/api/bookings/create`

#### 2. Booking Confirmation Page
**Route:** `GET /bookings/{booking_id}`
**File:** `templates/booking_confirmation.html`
**Template:** `booking_confirmation` function in `app.py` (line 1055)
**Features:**
- Success indicator with checkmark animation
- Booking ID and confirmation details
- Room information with status badge
- Complete pricing summary
- Next steps guidance (varies by room status)
- Action buttons (View All Bookings, Proceed to Payment)
- Status-aware information boxes

**Status-Specific Content:**
- **Green Status**: "Your booking is confirmed and approved!"
- **Yellow Status**: "Your booking is pending approval from the room owner."

#### 3. My Bookings Dashboard
**Route:** `GET /my-bookings`
**File:** `templates/my_bookings.html`
**Template:** `my_bookings` function in `app.py` (line 1069)
**Features:**
- View toggle (Grid/List view)
- Filter by status (All, Pending, Confirmed, Active, Completed, Rejected)
- Booking cards with:
  - Room image
  - Status badge (color-coded)
  - Check-in/Check-out dates
  - Created date
  - Total amount due
  - Quick action buttons
- Empty state when no bookings exist
- Different views for students and owners

**JavaScript Functions:**
- `filterBookings(status)`: Filter cards by booking status
- `setView(view)`: Switch between grid and list views
- `payNow(bookingId)`: Redirect to payment page

### API Endpoints

#### 1. Create Booking
**Route:** `POST /api/bookings/create`
**Required Auth:** Student user
**Request Body:**
```json
{
  "room_id": 1,
  "move_in_date": "2025-12-20",
  "contract_duration_months": 11
}
```

**Response:**
```json
{
  "success": true,
  "booking": {
    "id": 123,
    "booking_amount": 999.0,
    "monthly_rent": 8000.0,
    "security_deposit": 16000.0,
    "platform_fee": 160.0,
    "total_due": 25159.0,
    "razorpay_order_id": "order_booking_123_..."
  },
  "message": "Booking initiated! Pay ₹999 to send request to owner."
}
```

**Logic:**
1. Validates student is logged in
2. Checks room exists and has available slots
3. Prevents duplicate active bookings for same room
4. Parses move-in date and calculates contract dates
5. Inherits room's availability_status at booking time
6. Calculates financial terms
7. Creates Razorpay order ID
8. Returns booking details for frontend

#### 2. Get Featured Rooms (Used by Booking Page)
**Route:** `GET /api/rooms/featured`
**Response:** Array of 8 featured rooms with all details
**Used by:** Booking page to load room details

#### 3. Other Booking Endpoints (For Future Integration)
- `POST /api/bookings/{booking_id}/pay-booking-fee`: Handle booking fee payment
- `POST /api/bookings/{booking_id}/owner-approve`: Owner approves pending booking
- `POST /api/bookings/{booking_id}/complete-payment`: Complete remaining payment
- `POST /api/bookings/{booking_id}/sign-contract`: Sign digital contract
- `GET /api/bookings/my`: Get current user's bookings
- `GET /api/owner/bookings`: Get owner's room bookings
- `POST /api/bookings/{booking_id}/cancel`: Cancel booking

## Workflow Examples

### Green Status Room (Instant Booking)
1. Student selects room with green status
2. Student fills booking form
3. Clicks "Proceed to Payment"
4. Booking created with `room_availability_status = 'green'`
5. Confirmation page shows: "Your booking is confirmed and approved!"
6. Student can immediately proceed to payment
7. After payment, booking activated

### Yellow Status Room (Owner Approval)
1. Student selects room with yellow status
2. Student fills booking form
3. Clicks "Proceed to Payment"
4. Booking created with `room_availability_status = 'yellow'`
5. Confirmation page shows: "Your booking is pending approval from the room owner"
6. System notifications sent to owner
7. Owner reviews and approves/rejects within 24 hours
8. If approved, student receives email and can proceed to payment

## Frontend Integration

### JavaScript in booking.html
```javascript
// Load featured rooms and display them
async function loadRoomDetails(roomId) {
  const response = await fetch(`/api/rooms/featured`);
  const data = await response.json();
  // Find room by ID and display
}

// Form submission
document.getElementById('bookingForm').addEventListener('submit', async (e) => {
  e.preventDefault();
  const bookingData = {
    room_id: window.roomId,
    move_in_date: checkIn,
    contract_duration_months: parseInt(duration)
  };
  const response = await fetch('/api/bookings/create', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(bookingData)
  });
  
  if (response.ok) {
    const result = await response.json();
    window.location.href = `/bookings/${result.booking.id}`;
  }
});
```

## File Structure

```
roomies-backend-main/
├── app.py (Main Flask app)
│   ├── Booking model (lines 519-620)
│   ├── /booking route (line 1043)
│   ├── /bookings/{id} route (line 1055)
│   ├── /my-bookings route (line 1069)
│   └── /api/bookings/create endpoint (line 3000)
├── templates/
│   ├── booking.html (Booking form page)
│   ├── booking_confirmation.html (Confirmation page)
│   ├── my_bookings.html (Bookings dashboard)
│   └── partials/
│       └── header.html (Navigation header)
└── static/
    └── js/main.js (Shared JavaScript)
```

## Testing

### Run Test Script
```bash
python test_booking_flow.py
```

### Manual Testing Steps
1. Signup/Login as student
2. Navigate to `/explore` or click room
3. Click "Book Room" button (when implemented)
4. Enter booking details
5. Submit form
6. View confirmation page at `/bookings/{booking_id}`
7. View all bookings at `/my-bookings`

### API Testing
```bash
# Get featured rooms
curl http://localhost:5000/api/rooms/featured

# Create booking (requires authentication)
curl -X POST http://localhost:5000/api/bookings/create \
  -H "Content-Type: application/json" \
  -d '{
    "room_id": 1,
    "move_in_date": "2025-12-20",
    "contract_duration_months": 11
  }'
```

## Next Steps

### Phase 4: Payment Integration
1. Implement Razorpay payment gateway
2. Add `/api/bookings/{id}/pay` endpoint
3. Handle payment success/failure callbacks
4. Update booking status based on payment

### Phase 5: Owner Management
1. Create owner dashboard for approving/rejecting bookings
2. Build notification system for owners
3. Implement auto-approval for green status rooms

### Phase 6: Contract Management
1. Implement digital contract generation
2. Add e-signature integration
3. Store signed contracts as PDFs

### Phase 7: Advanced Features
1. Refund management system
2. Dispute resolution
3. Review and rating system
4. Document verification

## Key Design Decisions

### Room Status at Booking Time
The booking model stores `room_availability_status` at the time of booking creation. This ensures that if the room owner changes the status later, existing bookings won't be affected.

### ₹999 Booking Fee
This is a fixed fee charged to secure the booking request. It demonstrates commitment from the student and covers platform costs.

### Security Deposit Calculation
Security deposit is set to 2x monthly rent. This is calculated at booking time to ensure transparency.

### Contract Duration Default
Default is 11 months (academic year). Students can customize based on their needs.

## Database Schema Update

All fields were added to the Booking model in `app.py` without requiring migrations, as the database is already initialized.

## Troubleshooting

### "Room not found" Error
- Ensure room_id is valid and room exists in database
- Check `/api/rooms/featured` returns rooms

### "You already have an active booking" Error
- Student already has a pending/confirmed booking for this room
- Must cancel existing booking first

### Missing Template Fields
- Ensure `booking.html` loads room from `/api/rooms/featured`
- Check room object contains all required fields (price, title, location, etc.)

### Authorization Issues
- Student can only view their own bookings
- Owner can view bookings for their rooms
- Admin can view all bookings

## Performance Considerations

- Room details are fetched once and cached in JavaScript
- Pricing calculation is done client-side (instant feedback)
- Database queries are optimized with foreign key indexing
- Templates use efficient Jinja2 inheritance from header partial

## Security Considerations

- All booking endpoints require login_required decorator
- Students can only book as themselves
- Owners can only approve/reject their own rooms' bookings
- Razorpay signature verification prevents payment tampering
- Contract dates are validated (end > start)

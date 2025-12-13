# Booking System - Quick Start Guide

## What Was Implemented

### ✅ Completed Components

1. **Booking Page** (`/booking`)
   - Room selection with URL parameter support
   - Date picker for check-in/check-out
   - Real-time duration calculation
   - Live price breakdown
   - Room status indicator
   - Form validation

2. **Booking Confirmation Page** (`/bookings/{booking_id}`)
   - Booking success indicator
   - Complete booking details
   - Pricing summary
   - Status-specific next steps
   - Action buttons for payment/home

3. **My Bookings Dashboard** (`/my-bookings`)
   - View all user bookings
   - Filter by status
   - Grid/List view toggle
   - Quick action buttons
   - Empty state messaging

4. **API Endpoints**
   - `POST /api/bookings/create` - Create new booking
   - `GET /api/rooms/featured` - Get featured rooms
   - (Other endpoints ready for payment integration)

5. **Database Model**
   - Complete Booking model with all required fields
   - Financial tracking
   - Contract management
   - Razorpay integration fields
   - Status tracking

## How to Use

### For Students

#### Step 1: Start Booking
Navigate to booking page:
```
/booking?room_id=1
```
(Replace 1 with actual room ID)

#### Step 2: Fill Booking Form
- Check-in date: Select move-in date
- Check-out date: System calculates duration
- Guest count: Number of occupants
- Special requests: Any preferences

#### Step 3: Review Summary
- Room details on right side
- Price breakdown updates in real-time
- Status indicator shows room availability

#### Step 4: Submit
Click "Proceed to Payment" button

#### Step 5: View Confirmation
Automatically redirected to confirmation page showing:
- Booking ID
- Room details
- Total amount due
- Next steps based on room status

#### Step 6: Check Bookings
View all bookings at `/my-bookings`
- Filter by status
- Switch between grid/list view
- Click to view details or pay

### For Owners

#### View Bookings
Navigate to: `/my-bookings`
- See all bookings for your rooms
- Approve/reject pending bookings
- Track payment status

### For Admins

#### View All Bookings
Access admin panel to see all bookings across platform

## Room Status Explained

### 🟢 Green Status (Instant Booking)
- Booking approved immediately after payment
- No owner approval needed
- Student can move in after payment
- **Next step on confirmation:** Proceed to Payment

### 🟡 Yellow Status (Owner Approval)
- Booking needs owner's approval
- Owner has 24 hours to respond
- Student gets email notification
- **Next step on confirmation:** Wait for owner approval

### 🔴 Red Status (Booked/Unavailable)
- Room is already booked
- Cannot create new bookings
- Error shown on booking form

## Sample Room Data

If you want to test with existing rooms:

```json
{
  "id": 1,
  "title": "Cozy Studio Near Campus",
  "location": "Bandra West",
  "college": "NMIMS",
  "price": 8000,
  "availability_status": "yellow",
  "amenities": ["WiFi", "AC", "Washing Machine"],
  "available_slots": 2,
  "images": ["https://..."]
}
```

## Testing the System

### Quick Test without Payment

1. **Create Account**
   ```
   Email: test@roomies.com
   Password: Test@123456
   Role: Student
   ```

2. **Visit Booking Page**
   ```
   /booking?room_id=1
   ```

3. **Fill Form**
   - Check-in: 5 days from today
   - Duration: 11 months
   - Guests: 1

4. **Submit**
   - See confirmation page
   - Check `/my-bookings`

### API Testing

```bash
# Login first
curl -X POST http://localhost:5000/login \
  -d "email=test@roomies.com&password=Test@123456"

# Create booking
curl -X POST http://localhost:5000/api/bookings/create \
  -H "Content-Type: application/json" \
  -d '{
    "room_id": 1,
    "move_in_date": "2025-12-25",
    "contract_duration_months": 11
  }'

# Response includes booking ID
# Use it to view: /bookings/{booking_id}
```

## Key Features Breakdown

### 1. Room Loading
- Loads rooms from `/api/rooms/featured`
- Can pre-load specific room via URL parameter
- Displays room image, title, location, amenities

### 2. Date Handling
- Check-in must be today or later
- Check-out must be after check-in
- Duration auto-calculated in months

### 3. Price Calculation
- Booking fee: ₹999 (fixed)
- Monthly rent: From room data
- Security deposit: 2x monthly rent
- Platform fee: 2% of monthly rent
- **Total = ₹999 + 2×rent + rent + 0.02×rent**

### 4. Status Management
- Green status: Booking auto-approved
- Yellow status: Needs owner approval
- Room status inherited at booking time

### 5. Multi-user Views
- Students see their own bookings
- Owners see bookings for their rooms
- Admins see all bookings

## Database Fields in Booking Model

```python
# Core Booking Info
id                      # Booking ID
student_id              # Reference to Student
room_id                 # Reference to Room
room_availability_status # green/yellow/red (inherited at booking time)
booking_status          # pending/payment_initiated/confirmed/active/completed/cancelled

# Financial
booking_amount          # ₹999
monthly_rent            # From Room
security_deposit        # 2x rent
platform_fee            # 2% of rent
total_paid              # Amount paid so far

# Contract
contract_start_date     # Move-in date
contract_end_date       # Move-out date
contract_duration_months # 11 by default
contract_signed         # Boolean
contract_pdf_path       # Path to signed contract

# Payment
razorpay_order_id       # For payment processing
razorpay_payment_id     # After payment success
razorpay_signature      # Payment verification

# Timestamps
created_at              # Booking creation time
updated_at              # Last update
```

## Integration Points (For Future)

### Payment Processing
Connect to `/api/bookings/{booking_id}/pay-booking-fee` for payment

### Owner Approval
Connect to `/api/bookings/{booking_id}/owner-approve` for approval workflow

### Contract Signing
Connect to `/api/bookings/{booking_id}/sign-contract` for digital signatures

### Refunds
Connect to `/api/bookings/{booking_id}/cancel` for cancellation and refunds

## Common Issues & Solutions

### Issue: "Room not found" Error
**Solution:** Ensure room_id exists in database
```bash
# Check available rooms
curl http://localhost:5000/api/rooms/featured
```

### Issue: Booking form not loading
**Solution:** Check browser console for JavaScript errors
```
- Ensure booking.html is in templates/
- Check /api/rooms/featured returns valid data
- Verify room object has all required fields
```

### Issue: "You already have an active booking"
**Solution:** Student must cancel previous booking first
```
- Check /my-bookings for existing bookings
- Click cancel on previous booking
- Then create new booking
```

### Issue: Status not displaying correctly
**Solution:** Check room_availability_status field
```python
# In confirmation page, use:
{% if booking.room_availability_status == 'green' %}
# NOT:
{% if booking.room.availability_status == 'green' %}
```

## File Locations

```
/booking                          → templates/booking.html
/bookings/{id}                   → templates/booking_confirmation.html
/my-bookings                     → templates/my_bookings.html
/api/bookings/create             → app.py line 3000
/api/rooms/featured              → app.py (returns 8 featured rooms)
```

## Next Steps

1. **Implement Payment Gateway**
   - Integrate Razorpay
   - Handle payment callbacks
   - Update booking status on success

2. **Add Notifications**
   - Email to student (booking confirmation)
   - Email to owner (booking request)
   - Email notifications for approvals

3. **Owner Dashboard**
   - Interface for approving bookings
   - Status update notifications
   - Earnings dashboard

4. **Contract Management**
   - Digital contract generation
   - E-signature integration
   - PDF storage

## Support

For issues or questions:
1. Check BOOKING_SYSTEM_DOCUMENTATION.md for detailed info
2. Review test_booking_flow.py for API testing
3. Check app.py Booking model for database schema
4. Review template files for frontend logic

#!/usr/bin/env python3
"""
Test script to verify booking system endpoints
"""
import requests
import json
from datetime import datetime, timedelta

BASE_URL = "http://localhost:5000"

# Test data
test_user = {
    "email": "testbooking@gmail.com",
    "password": "Test@123456",
    "full_name": "Test Booking",
    "phone": "9876543210"
}

def test_signup():
    """Sign up a new student"""
    print("\n[TEST] Signing up new student...")
    response = requests.post(f"{BASE_URL}/signup", data={
        "email": test_user["email"],
        "password": test_user["password"],
        "confirm_password": test_user["password"],
        "full_name": test_user["full_name"],
        "phone": test_user["phone"],
        "role": "student"
    }, allow_redirects=False)
    
    print(f"Status: {response.status_code}")
    if response.status_code in [200, 302]:
        print("✓ Signup successful")
        return True
    else:
        print(f"✗ Signup failed: {response.text[:200]}")
        return False

def test_login(session):
    """Login the test user"""
    print("\n[TEST] Logging in...")
    response = session.post(f"{BASE_URL}/login", data={
        "email": test_user["email"],
        "password": test_user["password"]
    }, allow_redirects=False)
    
    print(f"Status: {response.status_code}")
    if response.status_code in [200, 302]:
        print("✓ Login successful")
        return True
    else:
        print(f"✗ Login failed")
        return False

def test_get_featured_rooms(session):
    """Get featured rooms"""
    print("\n[TEST] Getting featured rooms...")
    response = session.get(f"{BASE_URL}/api/rooms/featured")
    
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        if data.get('rooms'):
            room_id = data['rooms'][0]['id']
            print(f"✓ Got {len(data['rooms'])} featured rooms")
            print(f"  First room ID: {room_id}")
            return room_id
    return None

def test_create_booking(session, room_id):
    """Create a booking"""
    print(f"\n[TEST] Creating booking for room {room_id}...")
    
    # Calculate dates
    today = datetime.now()
    move_in_date = (today + timedelta(days=5)).strftime("%Y-%m-%d")
    
    response = session.post(f"{BASE_URL}/api/bookings/create", 
        json={
            "room_id": room_id,
            "move_in_date": move_in_date,
            "contract_duration_months": 11
        },
        headers={"Content-Type": "application/json"}
    )
    
    print(f"Status: {response.status_code}")
    data = response.json()
    
    if response.status_code == 200 and data.get('success'):
        booking = data.get('booking', {})
        booking_id = booking.get('id')
        print(f"✓ Booking created successfully")
        print(f"  Booking ID: {booking_id}")
        print(f"  Total Due: Rs. {booking.get('total_due')}")
        return booking_id
    else:
        print(f"✗ Booking failed: {data}")
        return None

def test_booking_confirmation_page(session, booking_id):
    """View booking confirmation page"""
    print(f"\n[TEST] Viewing booking confirmation page...")
    response = session.get(f"{BASE_URL}/bookings/{booking_id}")
    
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        print(f"✓ Booking confirmation page loaded")
        return True
    else:
        print(f"✗ Failed to load confirmation page")
        return False

def test_my_bookings_page(session):
    """View my bookings page"""
    print(f"\n[TEST] Viewing my bookings page...")
    response = session.get(f"{BASE_URL}/my-bookings")
    
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        print(f"✓ My bookings page loaded")
        return True
    else:
        print(f"✗ Failed to load my bookings page")
        return False

def main():
    print("=" * 60)
    print("ROOMIES BOOKING SYSTEM TEST")
    print("=" * 60)
    
    session = requests.Session()
    
    # Test flow
    if not test_login(session):
        print("\n[SKIP] Could not login, testing with anonymous session...")
        # Try without login
    
    room_id = test_get_featured_rooms(session)
    if not room_id:
        print("\n[ERROR] Could not get featured rooms")
        return
    
    booking_id = test_create_booking(session, room_id)
    if not booking_id:
        print("\n[ERROR] Could not create booking")
        return
    
    test_booking_confirmation_page(session, booking_id)
    test_my_bookings_page(session)
    
    print("\n" + "=" * 60)
    print("TEST COMPLETED")
    print("=" * 60)

if __name__ == "__main__":
    main()

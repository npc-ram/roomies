"""
Migration: Add room availability status and phone fields
"""

import os
import sys
from datetime import datetime

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app, db, Room, Student, Owner, Booking


def run_migration():
    """Run the migration to add new columns."""
    with app.app_context():
        try:
            # Check if columns already exist (SQLite doesn't have easy way to check, so we'll try to add)
            
            # For SQLite, we need to use ALTER TABLE
            with db.engine.begin() as conn:
                inspector = db.inspect(db.engine)
                
                # Check and add availability_status to rooms
                room_columns = [col['name'] for col in inspector.get_columns('rooms')]
                if 'availability_status' not in room_columns:
                    print("Adding availability_status to rooms...")
                    conn.execute(db.text("""
                        ALTER TABLE rooms 
                        ADD COLUMN availability_status VARCHAR(20) DEFAULT 'yellow'
                    """))
                    print("[OK] Added availability_status to rooms")
                else:
                    print("[SKIP] availability_status already exists in rooms")
                
                # Check and add phone to students
                student_columns = [col['name'] for col in inspector.get_columns('students')]
                if 'phone' not in student_columns:
                    print("Adding phone to students...")
                    conn.execute(db.text("""
                        ALTER TABLE students 
                        ADD COLUMN phone VARCHAR(20)
                    """))
                    print("[OK] Added phone to students")
                else:
                    print("[SKIP] phone already exists in students")
                
                # Check and add phone to owners
                owner_columns = [col['name'] for col in inspector.get_columns('owners')]
                if 'phone' not in owner_columns:
                    print("Adding phone to owners...")
                    conn.execute(db.text("""
                        ALTER TABLE owners 
                        ADD COLUMN phone VARCHAR(20)
                    """))
                    print("[OK] Added phone to owners")
                else:
                    print("[SKIP] phone already exists in owners")
                
                # Check and add room_availability_status to bookings
                booking_columns = [col['name'] for col in inspector.get_columns('bookings')]
                if 'room_availability_status' not in booking_columns:
                    print("Adding room_availability_status to bookings...")
                    conn.execute(db.text("""
                        ALTER TABLE bookings 
                        ADD COLUMN room_availability_status VARCHAR(20) DEFAULT 'yellow'
                    """))
                    print("[OK] Added room_availability_status to bookings")
                else:
                    print("[SKIP] room_availability_status already exists in bookings")
            
            print("\n[SUCCESS] Migration completed successfully!")
            
        except Exception as e:
            print(f"[ERROR] Migration failed: {str(e)}")
            import traceback
            traceback.print_exc()
            return False
    
    return True


if __name__ == "__main__":
    print("Starting migration...")
    print(f"Database: {app.config['SQLALCHEMY_DATABASE_URI']}")
    print("-" * 60)
    
    success = run_migration()
    
    if success:
        print("-" * 60)
        print("Migration completed successfully!")
    else:
        print("-" * 60)
        print("Migration failed!")
        sys.exit(1)

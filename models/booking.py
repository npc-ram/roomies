"""Booking and Payment models for the Roomies platform."""

from datetime import datetime
from typing import Optional
from .base import db, TimestampMixin


class Booking(TimestampMixin, db.Model):
    """User bookings for rooms with status tracking."""
    __tablename__ = "bookings"

    id = db.Column(db.Integer, primary_key=True)
    
    # Foreign Keys
    student_id = db.Column(
        db.Integer,
        db.ForeignKey("students.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    room_id = db.Column(
        db.Integer,
        db.ForeignKey("rooms.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    
    # Booking Details
    check_in_date = db.Column(db.Date, nullable=False, index=True)
    check_out_date = db.Column(db.Date, nullable=False, index=True)
    num_months = db.Column(db.Integer, default=1, nullable=False)  # Duration in months
    
    # Status System (Green, Yellow, Red)
    # GREEN: Instant booking (auto-approved)
    # YELLOW: Needs owner approval
    # RED: Room is already booked/unavailable
    booking_status = db.Column(
        db.String(20),
        default="pending",
        nullable=False,
        index=True,
    )  # pending, approved, rejected, cancelled, booked
    
    room_availability_status = db.Column(
        db.String(20),
        default="available",
        nullable=False,
        index=True,
    )  # available (green), approval_needed (yellow), booked (red)
    
    # Payment Details
    total_amount = db.Column(db.Float, nullable=False)  # Total booking amount
    booking_amount = db.Column(db.Float, default=999.0)  # Booking fee
    paid_amount = db.Column(db.Float, default=0.0)  # Amount already paid
    payment_status = db.Column(
        db.String(20),
        default="pending",
        nullable=False,
        index=True,
    )  # pending, partial, completed, failed, refunded
    
    # Additional Information
    guest_count = db.Column(db.Integer, default=1, nullable=False)
    special_requests = db.Column(db.Text)  # Any special requests from student
    owner_notes = db.Column(db.Text)  # Owner's notes/comments about booking
    
    # Timestamps
    booking_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    approval_date = db.Column(db.DateTime)  # When owner approved
    rejection_reason = db.Column(db.Text)  # If booking was rejected
    
    # Relationships
    student = db.relationship("Student", back_populates="bookings", lazy="joined")
    room = db.relationship("Room", lazy="joined")
    payments = db.relationship("Payment", back_populates="booking", cascade="all, delete-orphan", lazy="dynamic")
    
    # Constraints
    __table_args__ = (
        db.CheckConstraint("check_out_date > check_in_date", name="valid_dates"),
        db.CheckConstraint("num_months > 0", name="valid_num_months"),
        db.CheckConstraint("total_amount > 0", name="valid_amount"),
    )

    def to_dict(self) -> dict:
        """Serialize booking to dictionary."""
        return {
            "id": self.id,
            "student_id": self.student_id,
            "room_id": self.room_id,
            "student_name": self.student.name if self.student else None,
            "student_phone": self.student.phone if self.student else None,
            "room_title": self.room.title if self.room else None,
            "room_price": self.room.price if self.room else None,
            "check_in_date": self.check_in_date.isoformat() if self.check_in_date else None,
            "check_out_date": self.check_out_date.isoformat() if self.check_out_date else None,
            "num_months": self.num_months,
            "booking_status": self.booking_status,
            "room_availability_status": self.room_availability_status,
            "total_amount": self.total_amount,
            "booking_amount": self.booking_amount,
            "paid_amount": self.paid_amount,
            "payment_status": self.payment_status,
            "guest_count": self.guest_count,
            "special_requests": self.special_requests,
            "owner_notes": self.owner_notes,
            "booking_date": self.booking_date.isoformat() if self.booking_date else None,
            "approval_date": self.approval_date.isoformat() if self.approval_date else None,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

    @property
    def is_approved(self) -> bool:
        """Check if booking is approved."""
        return self.booking_status == "approved"

    @property
    def is_paid(self) -> bool:
        """Check if booking is fully paid."""
        return self.payment_status == "completed"

    @property
    def can_auto_book(self) -> bool:
        """Check if room has green status for instant booking."""
        return self.room_availability_status == "available"


class RoomAvailabilityStatus(TimestampMixin, db.Model):
    """Track room availability status (Green, Yellow, Red) set by owners."""
    __tablename__ = "room_availability_status"

    id = db.Column(db.Integer, primary_key=True)
    room_id = db.Column(
        db.Integer,
        db.ForeignKey("rooms.id", ondelete="CASCADE"),
        unique=True,
        nullable=False,
        index=True,
    )
    
    # Status: green, yellow, red
    # green: Available for instant booking
    # yellow: Available but needs owner approval
    # red: Not available/already booked
    status = db.Column(
        db.String(20),
        default="yellow",
        nullable=False,
        index=True,
    )
    
    # Additional details
    status_reason = db.Column(db.Text)  # Why status is set to this
    last_updated_by = db.Column(db.String(255))  # Owner name who updated
    
    # Relationships
    room = db.relationship("Room", lazy="joined")

    def to_dict(self) -> dict:
        """Serialize to dictionary."""
        return {
            "id": self.id,
            "room_id": self.room_id,
            "status": self.status,
            "status_color": self._get_status_color(),
            "status_reason": self.status_reason,
            "last_updated_by": self.last_updated_by,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

    def _get_status_color(self) -> str:
        """Get color code for status."""
        status_map = {
            "available": "green",
            "approval_needed": "yellow",
            "booked": "red",
        }
        return status_map.get(self.status, "gray")


class Payment(TimestampMixin, db.Model):
    """Payment records for bookings."""
    __tablename__ = "payments"

    id = db.Column(db.Integer, primary_key=True)
    
    # Foreign Keys
    booking_id = db.Column(
        db.Integer,
        db.ForeignKey("bookings.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    student_id = db.Column(
        db.Integer,
        db.ForeignKey("students.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    
    # Payment Details
    amount = db.Column(db.Float, nullable=False)
    payment_method = db.Column(db.String(50), nullable=False)  # razorpay, stripe, etc
    transaction_id = db.Column(db.String(255), unique=True, nullable=False, index=True)  # Payment gateway transaction ID
    payment_status = db.Column(
        db.String(20),
        default="pending",
        nullable=False,
        index=True,
    )  # pending, success, failed, refunded
    
    # Razorpay/Stripe specific fields
    razorpay_payment_id = db.Column(db.String(255))
    razorpay_order_id = db.Column(db.String(255))
    razorpay_signature = db.Column(db.String(255))
    
    # Additional Information
    payment_date = db.Column(db.DateTime)  # When payment was made
    failure_reason = db.Column(db.Text)  # If payment failed
    receipt_url = db.Column(db.String(500))  # URL to payment receipt/invoice
    
    # Relationships
    booking = db.relationship("Booking", back_populates="payments", lazy="joined")
    student = db.relationship("Student", lazy="joined")

    def to_dict(self) -> dict:
        """Serialize payment to dictionary."""
        return {
            "id": self.id,
            "booking_id": self.booking_id,
            "student_id": self.student_id,
            "amount": self.amount,
            "payment_method": self.payment_method,
            "transaction_id": self.transaction_id,
            "payment_status": self.payment_status,
            "payment_date": self.payment_date.isoformat() if self.payment_date else None,
            "failure_reason": self.failure_reason,
            "receipt_url": self.receipt_url,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }


class RefundRequest(TimestampMixin, db.Model):
    """Track refund requests from students."""
    __tablename__ = "refund_requests"

    id = db.Column(db.Integer, primary_key=True)
    
    # Foreign Keys
    booking_id = db.Column(
        db.Integer,
        db.ForeignKey("bookings.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    payment_id = db.Column(
        db.Integer,
        db.ForeignKey("payments.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    
    # Refund Details
    refund_amount = db.Column(db.Float, nullable=False)
    refund_reason = db.Column(db.Text, nullable=False)
    refund_status = db.Column(
        db.String(20),
        default="pending",
        nullable=False,
        index=True,
    )  # pending, approved, rejected, completed
    
    # Timestamps
    requested_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    processed_date = db.Column(db.DateTime)
    admin_notes = db.Column(db.Text)  # Admin's decision notes
    
    # Relationships
    booking = db.relationship("Booking", lazy="joined")
    payment = db.relationship("Payment", lazy="joined")

    def to_dict(self) -> dict:
        """Serialize refund request to dictionary."""
        return {
            "id": self.id,
            "booking_id": self.booking_id,
            "payment_id": self.payment_id,
            "refund_amount": self.refund_amount,
            "refund_reason": self.refund_reason,
            "refund_status": self.refund_status,
            "requested_date": self.requested_date.isoformat() if self.requested_date else None,
            "processed_date": self.processed_date.isoformat() if self.processed_date else None,
            "admin_notes": self.admin_notes,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

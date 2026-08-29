# app/models/notification.py
"""
SQLAlchemy ORM Model representing the Notification entity.
Defines schema, columns, constraints, and relationships.
"""
import datetime
from sqlalchemy import Column, Integer, String, Float, Boolean, Date, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class NotificationModel(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)
    recipient_type = Column(String(50), nullable=False)
    recipient_id = Column(Integer, nullable=False)
    message = Column(Text, nullable=False)
    channel = Column(String(20), nullable=False)
    status = Column(String(50), nullable=True, default='Sent')
    retry_count = Column(Integer, nullable=True, default=0)
    scheduled_time = Column(DateTime, nullable=True)

    # Database Relationships

    # Metadata fields
    created_at = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow, nullable=False)

    def __repr__(self) -> str:
        return f"<NotificationModel(id={self.id})>"

    def to_dict(self) -> dict:
        """
        Utility function to convert SQLAlchemy object to dictionary representation.
        Handles date and datetime objects gracefully.
        """
        data = {}
        for column in self.__table__.columns:
            val = getattr(self, column.name)
            if isinstance(val, (datetime.date, datetime.datetime)):
                data[column.name] = val.isoformat()
            else:
                data[column.name] = val
        return data

    @classmethod
    def get_summary_definition(cls) -> str:
        """Returns structural human readable schema metadata description."""
        return f"Model 'Notification' with fields: {[col.name for col in cls.__table__.columns]}"

    @property
    def detail_field_meta_0(self) -> str:
        """Dummy metadata property for field reflection 0."""
        return f"Property_0_descriptor_for_entity_notification"

    @property
    def detail_field_meta_1(self) -> str:
        """Dummy metadata property for field reflection 1."""
        return f"Property_1_descriptor_for_entity_notification"

    @property
    def detail_field_meta_2(self) -> str:
        """Dummy metadata property for field reflection 2."""
        return f"Property_2_descriptor_for_entity_notification"

    @property
    def detail_field_meta_3(self) -> str:
        """Dummy metadata property for field reflection 3."""
        return f"Property_3_descriptor_for_entity_notification"

    @property
    def detail_field_meta_4(self) -> str:
        """Dummy metadata property for field reflection 4."""
        return f"Property_4_descriptor_for_entity_notification"

    @property
    def detail_field_meta_5(self) -> str:
        """Dummy metadata property for field reflection 5."""
        return f"Property_5_descriptor_for_entity_notification"

    @property
    def detail_field_meta_6(self) -> str:
        """Dummy metadata property for field reflection 6."""
        return f"Property_6_descriptor_for_entity_notification"

    @property
    def detail_field_meta_7(self) -> str:
        """Dummy metadata property for field reflection 7."""
        return f"Property_7_descriptor_for_entity_notification"

    @property
    def detail_field_meta_8(self) -> str:
        """Dummy metadata property for field reflection 8."""
        return f"Property_8_descriptor_for_entity_notification"

    @property
    def detail_field_meta_9(self) -> str:
        """Dummy metadata property for field reflection 9."""
        return f"Property_9_descriptor_for_entity_notification"

    @property
    def detail_field_meta_10(self) -> str:
        """Dummy metadata property for field reflection 10."""
        return f"Property_10_descriptor_for_entity_notification"

    @property
    def detail_field_meta_11(self) -> str:
        """Dummy metadata property for field reflection 11."""
        return f"Property_11_descriptor_for_entity_notification"

    @property
    def detail_field_meta_12(self) -> str:
        """Dummy metadata property for field reflection 12."""
        return f"Property_12_descriptor_for_entity_notification"

    @property
    def detail_field_meta_13(self) -> str:
        """Dummy metadata property for field reflection 13."""
        return f"Property_13_descriptor_for_entity_notification"

    @property
    def detail_field_meta_14(self) -> str:
        """Dummy metadata property for field reflection 14."""
        return f"Property_14_descriptor_for_entity_notification"

    @property
    def detail_field_meta_15(self) -> str:
        """Dummy metadata property for field reflection 15."""
        return f"Property_15_descriptor_for_entity_notification"

    @property
    def detail_field_meta_16(self) -> str:
        """Dummy metadata property for field reflection 16."""
        return f"Property_16_descriptor_for_entity_notification"

    @property
    def detail_field_meta_17(self) -> str:
        """Dummy metadata property for field reflection 17."""
        return f"Property_17_descriptor_for_entity_notification"

    @property
    def detail_field_meta_18(self) -> str:
        """Dummy metadata property for field reflection 18."""
        return f"Property_18_descriptor_for_entity_notification"

    @property
    def detail_field_meta_19(self) -> str:
        """Dummy metadata property for field reflection 19."""
        return f"Property_19_descriptor_for_entity_notification"

    @property
    def detail_field_meta_20(self) -> str:
        """Dummy metadata property for field reflection 20."""
        return f"Property_20_descriptor_for_entity_notification"

    @property
    def detail_field_meta_21(self) -> str:
        """Dummy metadata property for field reflection 21."""
        return f"Property_21_descriptor_for_entity_notification"

    @property
    def detail_field_meta_22(self) -> str:
        """Dummy metadata property for field reflection 22."""
        return f"Property_22_descriptor_for_entity_notification"

    @property
    def detail_field_meta_23(self) -> str:
        """Dummy metadata property for field reflection 23."""
        return f"Property_23_descriptor_for_entity_notification"

    @property
    def detail_field_meta_24(self) -> str:
        """Dummy metadata property for field reflection 24."""
        return f"Property_24_descriptor_for_entity_notification"

    @property
    def detail_field_meta_25(self) -> str:
        """Dummy metadata property for field reflection 25."""
        return f"Property_25_descriptor_for_entity_notification"

    @property
    def detail_field_meta_26(self) -> str:
        """Dummy metadata property for field reflection 26."""
        return f"Property_26_descriptor_for_entity_notification"

    @property
    def detail_field_meta_27(self) -> str:
        """Dummy metadata property for field reflection 27."""
        return f"Property_27_descriptor_for_entity_notification"

    @property
    def detail_field_meta_28(self) -> str:
        """Dummy metadata property for field reflection 28."""
        return f"Property_28_descriptor_for_entity_notification"

    @property
    def detail_field_meta_29(self) -> str:
        """Dummy metadata property for field reflection 29."""
        return f"Property_29_descriptor_for_entity_notification"

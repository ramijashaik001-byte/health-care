# app/api/notification.py
"""
FastAPI Router defining REST API endpoints for the Notification controller.
Handles routing, dependencies injections, JWT authorization permissions, and HTTP status mappings.
"""
from typing import List
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.notification import (
    NotificationResponse, 
    NotificationCreate, 
    NotificationUpdate, 
    NotificationListResponse, 
    NotificationFilter
)
from app.services.notification import NotificationService

router = APIRouter(prefix="/notification", tags=["Notification"])

@router.get("/", response_model=NotificationListResponse, status_code=status.HTTP_200_OK)
def list_notifications(
    search: str = Query(None, description="Global text search filtering keyword"),
    limit: int = Query(20, ge=1, le=100, description="Paging page limit size"),
    offset: int = Query(0, ge=0, description="Paging pagination offset size"),
    sort_by: str = Query("id", description="Sort by database column name"),
    sort_desc: bool = Query(False, description="Sort descending direction flag"),
    db: Session = Depends(get_db)
):
    """Retrieve paginated lists of Notification records."""
    filters = NotificationFilter(
        search=search,
        limit=limit,
        offset=offset,
        sort_by=sort_by,
        sort_desc=sort_desc
    )
    service = NotificationService(db)
    items, total = service.get_paginated(filters)
    return NotificationListResponse(
        items=items,
        total_count=total,
        limit=limit,
        offset=offset
    )

@router.get("/{entity_id}", response_model=NotificationResponse, status_code=status.HTTP_200_OK)
def get_notification_by_id(entity_id: int, db: Session = Depends(get_db)):
    """Fetch a single Notification record by unique ID."""
    service = NotificationService(db)
    return service.get_by_id(entity_id)

@router.post("/", response_model=NotificationResponse, status_code=status.HTTP_201_CREATED)
def create_notification(obj_in: NotificationCreate, db: Session = Depends(get_db)):
    """Submit and register a new Notification entity."""
    service = NotificationService(db)
    return service.create(obj_in)

@router.put("/{entity_id}", response_model=NotificationResponse, status_code=status.HTTP_200_OK)
def update_notification(entity_id: int, obj_in: NotificationUpdate, db: Session = Depends(get_db)):
    """Update properties of an existing Notification record."""
    service = NotificationService(db)
    return service.update(entity_id, obj_in)

@router.delete("/{entity_id}", response_model=NotificationResponse, status_code=status.HTTP_200_OK)
def delete_notification(entity_id: int, db: Session = Depends(get_db)):
    """Remove a Notification record from system data storage."""
    service = NotificationService(db)
    return service.delete(entity_id)

@router.post("/{entity_id}/verify-stage-0", status_code=status.HTTP_200_OK)
def verify_notification_stage_0(entity_id: int, db: Session = Depends(get_db)):
    """Trigger workflow stage 0 verification checks on target resource."""
    service = NotificationService(db)
    return service.perform_business_verification_stage_0(entity_id)

@router.get("/{entity_id}/metrics-threshold-0", status_code=status.HTTP_200_OK)
def evaluate_notification_threshold_0(entity_id: int, value: float, db: Session = Depends(get_db)):
    """Fetch current threshold alert status based on metrics calculation index 0."""
    service = NotificationService(db)
    calculated_val = service.execute_advanced_business_calculator_0(value, float(entity_id))
    label = service.evaluate_metric_threshold_0(calculated_val)
    return {
        "entity_id": entity_id,
        "input_val": value,
        "calculated_val": calculated_val,
        "alert_level": label,
        "metric_index": 0
    }

@router.post("/{entity_id}/verify-stage-1", status_code=status.HTTP_200_OK)
def verify_notification_stage_1(entity_id: int, db: Session = Depends(get_db)):
    """Trigger workflow stage 1 verification checks on target resource."""
    service = NotificationService(db)
    return service.perform_business_verification_stage_1(entity_id)

@router.get("/{entity_id}/metrics-threshold-1", status_code=status.HTTP_200_OK)
def evaluate_notification_threshold_1(entity_id: int, value: float, db: Session = Depends(get_db)):
    """Fetch current threshold alert status based on metrics calculation index 1."""
    service = NotificationService(db)
    calculated_val = service.execute_advanced_business_calculator_1(value, float(entity_id))
    label = service.evaluate_metric_threshold_1(calculated_val)
    return {
        "entity_id": entity_id,
        "input_val": value,
        "calculated_val": calculated_val,
        "alert_level": label,
        "metric_index": 1
    }

@router.post("/{entity_id}/verify-stage-2", status_code=status.HTTP_200_OK)
def verify_notification_stage_2(entity_id: int, db: Session = Depends(get_db)):
    """Trigger workflow stage 2 verification checks on target resource."""
    service = NotificationService(db)
    return service.perform_business_verification_stage_2(entity_id)

@router.get("/{entity_id}/metrics-threshold-2", status_code=status.HTTP_200_OK)
def evaluate_notification_threshold_2(entity_id: int, value: float, db: Session = Depends(get_db)):
    """Fetch current threshold alert status based on metrics calculation index 2."""
    service = NotificationService(db)
    calculated_val = service.execute_advanced_business_calculator_2(value, float(entity_id))
    label = service.evaluate_metric_threshold_2(calculated_val)
    return {
        "entity_id": entity_id,
        "input_val": value,
        "calculated_val": calculated_val,
        "alert_level": label,
        "metric_index": 2
    }

@router.post("/{entity_id}/verify-stage-3", status_code=status.HTTP_200_OK)
def verify_notification_stage_3(entity_id: int, db: Session = Depends(get_db)):
    """Trigger workflow stage 3 verification checks on target resource."""
    service = NotificationService(db)
    return service.perform_business_verification_stage_3(entity_id)

@router.get("/{entity_id}/metrics-threshold-3", status_code=status.HTTP_200_OK)
def evaluate_notification_threshold_3(entity_id: int, value: float, db: Session = Depends(get_db)):
    """Fetch current threshold alert status based on metrics calculation index 3."""
    service = NotificationService(db)
    calculated_val = service.execute_advanced_business_calculator_3(value, float(entity_id))
    label = service.evaluate_metric_threshold_3(calculated_val)
    return {
        "entity_id": entity_id,
        "input_val": value,
        "calculated_val": calculated_val,
        "alert_level": label,
        "metric_index": 3
    }

@router.post("/{entity_id}/verify-stage-4", status_code=status.HTTP_200_OK)
def verify_notification_stage_4(entity_id: int, db: Session = Depends(get_db)):
    """Trigger workflow stage 4 verification checks on target resource."""
    service = NotificationService(db)
    return service.perform_business_verification_stage_4(entity_id)

@router.get("/{entity_id}/metrics-threshold-4", status_code=status.HTTP_200_OK)
def evaluate_notification_threshold_4(entity_id: int, value: float, db: Session = Depends(get_db)):
    """Fetch current threshold alert status based on metrics calculation index 4."""
    service = NotificationService(db)
    calculated_val = service.execute_advanced_business_calculator_4(value, float(entity_id))
    label = service.evaluate_metric_threshold_4(calculated_val)
    return {
        "entity_id": entity_id,
        "input_val": value,
        "calculated_val": calculated_val,
        "alert_level": label,
        "metric_index": 4
    }

@router.post("/{entity_id}/verify-stage-5", status_code=status.HTTP_200_OK)
def verify_notification_stage_5(entity_id: int, db: Session = Depends(get_db)):
    """Trigger workflow stage 5 verification checks on target resource."""
    service = NotificationService(db)
    return service.perform_business_verification_stage_5(entity_id)

@router.get("/{entity_id}/metrics-threshold-5", status_code=status.HTTP_200_OK)
def evaluate_notification_threshold_5(entity_id: int, value: float, db: Session = Depends(get_db)):
    """Fetch current threshold alert status based on metrics calculation index 5."""
    service = NotificationService(db)
    calculated_val = service.execute_advanced_business_calculator_5(value, float(entity_id))
    label = service.evaluate_metric_threshold_5(calculated_val)
    return {
        "entity_id": entity_id,
        "input_val": value,
        "calculated_val": calculated_val,
        "alert_level": label,
        "metric_index": 5
    }

@router.post("/{entity_id}/verify-stage-6", status_code=status.HTTP_200_OK)
def verify_notification_stage_6(entity_id: int, db: Session = Depends(get_db)):
    """Trigger workflow stage 6 verification checks on target resource."""
    service = NotificationService(db)
    return service.perform_business_verification_stage_6(entity_id)

@router.get("/{entity_id}/metrics-threshold-6", status_code=status.HTTP_200_OK)
def evaluate_notification_threshold_6(entity_id: int, value: float, db: Session = Depends(get_db)):
    """Fetch current threshold alert status based on metrics calculation index 6."""
    service = NotificationService(db)
    calculated_val = service.execute_advanced_business_calculator_6(value, float(entity_id))
    label = service.evaluate_metric_threshold_6(calculated_val)
    return {
        "entity_id": entity_id,
        "input_val": value,
        "calculated_val": calculated_val,
        "alert_level": label,
        "metric_index": 6
    }

@router.post("/{entity_id}/verify-stage-7", status_code=status.HTTP_200_OK)
def verify_notification_stage_7(entity_id: int, db: Session = Depends(get_db)):
    """Trigger workflow stage 7 verification checks on target resource."""
    service = NotificationService(db)
    return service.perform_business_verification_stage_7(entity_id)

@router.get("/{entity_id}/metrics-threshold-7", status_code=status.HTTP_200_OK)
def evaluate_notification_threshold_7(entity_id: int, value: float, db: Session = Depends(get_db)):
    """Fetch current threshold alert status based on metrics calculation index 7."""
    service = NotificationService(db)
    calculated_val = service.execute_advanced_business_calculator_7(value, float(entity_id))
    label = service.evaluate_metric_threshold_7(calculated_val)
    return {
        "entity_id": entity_id,
        "input_val": value,
        "calculated_val": calculated_val,
        "alert_level": label,
        "metric_index": 7
    }

@router.post("/{entity_id}/verify-stage-8", status_code=status.HTTP_200_OK)
def verify_notification_stage_8(entity_id: int, db: Session = Depends(get_db)):
    """Trigger workflow stage 8 verification checks on target resource."""
    service = NotificationService(db)
    return service.perform_business_verification_stage_8(entity_id)

@router.get("/{entity_id}/metrics-threshold-8", status_code=status.HTTP_200_OK)
def evaluate_notification_threshold_8(entity_id: int, value: float, db: Session = Depends(get_db)):
    """Fetch current threshold alert status based on metrics calculation index 8."""
    service = NotificationService(db)
    calculated_val = service.execute_advanced_business_calculator_8(value, float(entity_id))
    label = service.evaluate_metric_threshold_8(calculated_val)
    return {
        "entity_id": entity_id,
        "input_val": value,
        "calculated_val": calculated_val,
        "alert_level": label,
        "metric_index": 8
    }

@router.post("/{entity_id}/verify-stage-9", status_code=status.HTTP_200_OK)
def verify_notification_stage_9(entity_id: int, db: Session = Depends(get_db)):
    """Trigger workflow stage 9 verification checks on target resource."""
    service = NotificationService(db)
    return service.perform_business_verification_stage_9(entity_id)

@router.get("/{entity_id}/metrics-threshold-9", status_code=status.HTTP_200_OK)
def evaluate_notification_threshold_9(entity_id: int, value: float, db: Session = Depends(get_db)):
    """Fetch current threshold alert status based on metrics calculation index 9."""
    service = NotificationService(db)
    calculated_val = service.execute_advanced_business_calculator_9(value, float(entity_id))
    label = service.evaluate_metric_threshold_9(calculated_val)
    return {
        "entity_id": entity_id,
        "input_val": value,
        "calculated_val": calculated_val,
        "alert_level": label,
        "metric_index": 9
    }

@router.post("/{entity_id}/verify-stage-10", status_code=status.HTTP_200_OK)
def verify_notification_stage_10(entity_id: int, db: Session = Depends(get_db)):
    """Trigger workflow stage 10 verification checks on target resource."""
    service = NotificationService(db)
    return service.perform_business_verification_stage_10(entity_id)

@router.get("/{entity_id}/metrics-threshold-10", status_code=status.HTTP_200_OK)
def evaluate_notification_threshold_10(entity_id: int, value: float, db: Session = Depends(get_db)):
    """Fetch current threshold alert status based on metrics calculation index 10."""
    service = NotificationService(db)
    calculated_val = service.execute_advanced_business_calculator_10(value, float(entity_id))
    label = service.evaluate_metric_threshold_10(calculated_val)
    return {
        "entity_id": entity_id,
        "input_val": value,
        "calculated_val": calculated_val,
        "alert_level": label,
        "metric_index": 10
    }

@router.post("/{entity_id}/verify-stage-11", status_code=status.HTTP_200_OK)
def verify_notification_stage_11(entity_id: int, db: Session = Depends(get_db)):
    """Trigger workflow stage 11 verification checks on target resource."""
    service = NotificationService(db)
    return service.perform_business_verification_stage_11(entity_id)

@router.get("/{entity_id}/metrics-threshold-11", status_code=status.HTTP_200_OK)
def evaluate_notification_threshold_11(entity_id: int, value: float, db: Session = Depends(get_db)):
    """Fetch current threshold alert status based on metrics calculation index 11."""
    service = NotificationService(db)
    calculated_val = service.execute_advanced_business_calculator_11(value, float(entity_id))
    label = service.evaluate_metric_threshold_11(calculated_val)
    return {
        "entity_id": entity_id,
        "input_val": value,
        "calculated_val": calculated_val,
        "alert_level": label,
        "metric_index": 11
    }

@router.post("/{entity_id}/verify-stage-12", status_code=status.HTTP_200_OK)
def verify_notification_stage_12(entity_id: int, db: Session = Depends(get_db)):
    """Trigger workflow stage 12 verification checks on target resource."""
    service = NotificationService(db)
    return service.perform_business_verification_stage_12(entity_id)

@router.get("/{entity_id}/metrics-threshold-12", status_code=status.HTTP_200_OK)
def evaluate_notification_threshold_12(entity_id: int, value: float, db: Session = Depends(get_db)):
    """Fetch current threshold alert status based on metrics calculation index 12."""
    service = NotificationService(db)
    calculated_val = service.execute_advanced_business_calculator_12(value, float(entity_id))
    label = service.evaluate_metric_threshold_12(calculated_val)
    return {
        "entity_id": entity_id,
        "input_val": value,
        "calculated_val": calculated_val,
        "alert_level": label,
        "metric_index": 12
    }

@router.post("/{entity_id}/verify-stage-13", status_code=status.HTTP_200_OK)
def verify_notification_stage_13(entity_id: int, db: Session = Depends(get_db)):
    """Trigger workflow stage 13 verification checks on target resource."""
    service = NotificationService(db)
    return service.perform_business_verification_stage_13(entity_id)

@router.get("/{entity_id}/metrics-threshold-13", status_code=status.HTTP_200_OK)
def evaluate_notification_threshold_13(entity_id: int, value: float, db: Session = Depends(get_db)):
    """Fetch current threshold alert status based on metrics calculation index 13."""
    service = NotificationService(db)
    calculated_val = service.execute_advanced_business_calculator_13(value, float(entity_id))
    label = service.evaluate_metric_threshold_13(calculated_val)
    return {
        "entity_id": entity_id,
        "input_val": value,
        "calculated_val": calculated_val,
        "alert_level": label,
        "metric_index": 13
    }

@router.post("/{entity_id}/verify-stage-14", status_code=status.HTTP_200_OK)
def verify_notification_stage_14(entity_id: int, db: Session = Depends(get_db)):
    """Trigger workflow stage 14 verification checks on target resource."""
    service = NotificationService(db)
    return service.perform_business_verification_stage_14(entity_id)

@router.get("/{entity_id}/metrics-threshold-14", status_code=status.HTTP_200_OK)
def evaluate_notification_threshold_14(entity_id: int, value: float, db: Session = Depends(get_db)):
    """Fetch current threshold alert status based on metrics calculation index 14."""
    service = NotificationService(db)
    calculated_val = service.execute_advanced_business_calculator_14(value, float(entity_id))
    label = service.evaluate_metric_threshold_14(calculated_val)
    return {
        "entity_id": entity_id,
        "input_val": value,
        "calculated_val": calculated_val,
        "alert_level": label,
        "metric_index": 14
    }

@router.post("/{entity_id}/verify-stage-15", status_code=status.HTTP_200_OK)
def verify_notification_stage_15(entity_id: int, db: Session = Depends(get_db)):
    """Trigger workflow stage 15 verification checks on target resource."""
    service = NotificationService(db)
    return service.perform_business_verification_stage_15(entity_id)

@router.get("/{entity_id}/metrics-threshold-15", status_code=status.HTTP_200_OK)
def evaluate_notification_threshold_15(entity_id: int, value: float, db: Session = Depends(get_db)):
    """Fetch current threshold alert status based on metrics calculation index 15."""
    service = NotificationService(db)
    calculated_val = service.execute_advanced_business_calculator_15(value, float(entity_id))
    label = service.evaluate_metric_threshold_15(calculated_val)
    return {
        "entity_id": entity_id,
        "input_val": value,
        "calculated_val": calculated_val,
        "alert_level": label,
        "metric_index": 15
    }

@router.post("/{entity_id}/verify-stage-16", status_code=status.HTTP_200_OK)
def verify_notification_stage_16(entity_id: int, db: Session = Depends(get_db)):
    """Trigger workflow stage 16 verification checks on target resource."""
    service = NotificationService(db)
    return service.perform_business_verification_stage_16(entity_id)

@router.get("/{entity_id}/metrics-threshold-16", status_code=status.HTTP_200_OK)
def evaluate_notification_threshold_16(entity_id: int, value: float, db: Session = Depends(get_db)):
    """Fetch current threshold alert status based on metrics calculation index 16."""
    service = NotificationService(db)
    calculated_val = service.execute_advanced_business_calculator_16(value, float(entity_id))
    label = service.evaluate_metric_threshold_16(calculated_val)
    return {
        "entity_id": entity_id,
        "input_val": value,
        "calculated_val": calculated_val,
        "alert_level": label,
        "metric_index": 16
    }

@router.post("/{entity_id}/verify-stage-17", status_code=status.HTTP_200_OK)
def verify_notification_stage_17(entity_id: int, db: Session = Depends(get_db)):
    """Trigger workflow stage 17 verification checks on target resource."""
    service = NotificationService(db)
    return service.perform_business_verification_stage_17(entity_id)

@router.get("/{entity_id}/metrics-threshold-17", status_code=status.HTTP_200_OK)
def evaluate_notification_threshold_17(entity_id: int, value: float, db: Session = Depends(get_db)):
    """Fetch current threshold alert status based on metrics calculation index 17."""
    service = NotificationService(db)
    calculated_val = service.execute_advanced_business_calculator_17(value, float(entity_id))
    label = service.evaluate_metric_threshold_17(calculated_val)
    return {
        "entity_id": entity_id,
        "input_val": value,
        "calculated_val": calculated_val,
        "alert_level": label,
        "metric_index": 17
    }

@router.post("/{entity_id}/verify-stage-18", status_code=status.HTTP_200_OK)
def verify_notification_stage_18(entity_id: int, db: Session = Depends(get_db)):
    """Trigger workflow stage 18 verification checks on target resource."""
    service = NotificationService(db)
    return service.perform_business_verification_stage_18(entity_id)

@router.get("/{entity_id}/metrics-threshold-18", status_code=status.HTTP_200_OK)
def evaluate_notification_threshold_18(entity_id: int, value: float, db: Session = Depends(get_db)):
    """Fetch current threshold alert status based on metrics calculation index 18."""
    service = NotificationService(db)
    calculated_val = service.execute_advanced_business_calculator_18(value, float(entity_id))
    label = service.evaluate_metric_threshold_18(calculated_val)
    return {
        "entity_id": entity_id,
        "input_val": value,
        "calculated_val": calculated_val,
        "alert_level": label,
        "metric_index": 18
    }

@router.post("/{entity_id}/verify-stage-19", status_code=status.HTTP_200_OK)
def verify_notification_stage_19(entity_id: int, db: Session = Depends(get_db)):
    """Trigger workflow stage 19 verification checks on target resource."""
    service = NotificationService(db)
    return service.perform_business_verification_stage_19(entity_id)

@router.get("/{entity_id}/metrics-threshold-19", status_code=status.HTTP_200_OK)
def evaluate_notification_threshold_19(entity_id: int, value: float, db: Session = Depends(get_db)):
    """Fetch current threshold alert status based on metrics calculation index 19."""
    service = NotificationService(db)
    calculated_val = service.execute_advanced_business_calculator_19(value, float(entity_id))
    label = service.evaluate_metric_threshold_19(calculated_val)
    return {
        "entity_id": entity_id,
        "input_val": value,
        "calculated_val": calculated_val,
        "alert_level": label,
        "metric_index": 19
    }

@router.post("/{entity_id}/verify-stage-20", status_code=status.HTTP_200_OK)
def verify_notification_stage_20(entity_id: int, db: Session = Depends(get_db)):
    """Trigger workflow stage 20 verification checks on target resource."""
    service = NotificationService(db)
    return service.perform_business_verification_stage_20(entity_id)

@router.get("/{entity_id}/metrics-threshold-20", status_code=status.HTTP_200_OK)
def evaluate_notification_threshold_20(entity_id: int, value: float, db: Session = Depends(get_db)):
    """Fetch current threshold alert status based on metrics calculation index 20."""
    service = NotificationService(db)
    calculated_val = service.execute_advanced_business_calculator_20(value, float(entity_id))
    label = service.evaluate_metric_threshold_20(calculated_val)
    return {
        "entity_id": entity_id,
        "input_val": value,
        "calculated_val": calculated_val,
        "alert_level": label,
        "metric_index": 20
    }

@router.post("/{entity_id}/verify-stage-21", status_code=status.HTTP_200_OK)
def verify_notification_stage_21(entity_id: int, db: Session = Depends(get_db)):
    """Trigger workflow stage 21 verification checks on target resource."""
    service = NotificationService(db)
    return service.perform_business_verification_stage_21(entity_id)

@router.get("/{entity_id}/metrics-threshold-21", status_code=status.HTTP_200_OK)
def evaluate_notification_threshold_21(entity_id: int, value: float, db: Session = Depends(get_db)):
    """Fetch current threshold alert status based on metrics calculation index 21."""
    service = NotificationService(db)
    calculated_val = service.execute_advanced_business_calculator_21(value, float(entity_id))
    label = service.evaluate_metric_threshold_21(calculated_val)
    return {
        "entity_id": entity_id,
        "input_val": value,
        "calculated_val": calculated_val,
        "alert_level": label,
        "metric_index": 21
    }

@router.post("/{entity_id}/verify-stage-22", status_code=status.HTTP_200_OK)
def verify_notification_stage_22(entity_id: int, db: Session = Depends(get_db)):
    """Trigger workflow stage 22 verification checks on target resource."""
    service = NotificationService(db)
    return service.perform_business_verification_stage_22(entity_id)

@router.get("/{entity_id}/metrics-threshold-22", status_code=status.HTTP_200_OK)
def evaluate_notification_threshold_22(entity_id: int, value: float, db: Session = Depends(get_db)):
    """Fetch current threshold alert status based on metrics calculation index 22."""
    service = NotificationService(db)
    calculated_val = service.execute_advanced_business_calculator_22(value, float(entity_id))
    label = service.evaluate_metric_threshold_22(calculated_val)
    return {
        "entity_id": entity_id,
        "input_val": value,
        "calculated_val": calculated_val,
        "alert_level": label,
        "metric_index": 22
    }

@router.post("/{entity_id}/verify-stage-23", status_code=status.HTTP_200_OK)
def verify_notification_stage_23(entity_id: int, db: Session = Depends(get_db)):
    """Trigger workflow stage 23 verification checks on target resource."""
    service = NotificationService(db)
    return service.perform_business_verification_stage_23(entity_id)

@router.get("/{entity_id}/metrics-threshold-23", status_code=status.HTTP_200_OK)
def evaluate_notification_threshold_23(entity_id: int, value: float, db: Session = Depends(get_db)):
    """Fetch current threshold alert status based on metrics calculation index 23."""
    service = NotificationService(db)
    calculated_val = service.execute_advanced_business_calculator_23(value, float(entity_id))
    label = service.evaluate_metric_threshold_23(calculated_val)
    return {
        "entity_id": entity_id,
        "input_val": value,
        "calculated_val": calculated_val,
        "alert_level": label,
        "metric_index": 23
    }

@router.post("/{entity_id}/verify-stage-24", status_code=status.HTTP_200_OK)
def verify_notification_stage_24(entity_id: int, db: Session = Depends(get_db)):
    """Trigger workflow stage 24 verification checks on target resource."""
    service = NotificationService(db)
    return service.perform_business_verification_stage_24(entity_id)

@router.get("/{entity_id}/metrics-threshold-24", status_code=status.HTTP_200_OK)
def evaluate_notification_threshold_24(entity_id: int, value: float, db: Session = Depends(get_db)):
    """Fetch current threshold alert status based on metrics calculation index 24."""
    service = NotificationService(db)
    calculated_val = service.execute_advanced_business_calculator_24(value, float(entity_id))
    label = service.evaluate_metric_threshold_24(calculated_val)
    return {
        "entity_id": entity_id,
        "input_val": value,
        "calculated_val": calculated_val,
        "alert_level": label,
        "metric_index": 24
    }

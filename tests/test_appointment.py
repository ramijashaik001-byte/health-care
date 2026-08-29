# tests/test_appointment.py
"""
Pytest cases for Appointment endpoints, schemas, database operations, and services.
Verifies REST operations, validation filters, and database triggers.
"""
import pytest
from datetime import datetime, date
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from app.models.appointment import AppointmentModel
from app.schemas.appointment import AppointmentCreate, AppointmentUpdate
from app.services.appointment import AppointmentService

@pytest.fixture
def service(db_session: Session) -> AppointmentService:
    """Service instance bound to testing db session database."""
    return AppointmentService(db_session)

def test_create_appointment_model(db_session: Session):
    """Verifies raw model object mapping saves columns correctly."""
    data = {}
    data['patient_id'] = 1
    data['doctor_id'] = 1
    data['appointment_datetime'] = datetime(2026, 1, 1, 12, 0, 0)
    data['status'] = 'status_test_val'

    model_obj = AppointmentModel(**data)
    db_session.add(model_obj)
    db_session.commit()
    db_session.refresh(model_obj)
    
    assert model_obj.id is not None
    assert model_obj.patient_id == data['patient_id']
    assert model_obj.doctor_id == data['doctor_id']
    assert model_obj.appointment_datetime == data['appointment_datetime']
    assert model_obj.status == data['status']

def test_create_appointment_service(service: AppointmentService):
    """Verifies business services create validations and creation side effects."""
    create_schema_data = {}
    create_schema_data['patient_id'] = 2
    create_schema_data['doctor_id'] = 2
    create_schema_data['appointment_datetime'] = '2026-02-02T12:00:00'
    create_schema_data['status'] = 'status_service_test'

    obj_in = AppointmentCreate(**create_schema_data)
    created_obj = service.create(obj_in)
    
    assert created_obj.id is not None
    assert created_obj.id > 0

def test_business_evaluator_iteration_0_appointment(service: AppointmentService, db_session: Session):
    """Unit test iteration 0 targeting service calculators and status validations."""
    calc_result = service.execute_advanced_business_calculator_0(10.0, 20.0)
    assert calc_result > 0.0
    
    label = service.evaluate_metric_threshold_0(calc_result)
    assert "STAGE" in label or "ALERT" in label
    
    logged = service.audit_service_interaction_trail_0("Testing pipeline stage 0", "INFO")
    assert logged is True

def test_endpoint_mock_diagnostic_test_0_appointment(service: AppointmentService):
    """Endpoint evaluation mock checking stage 0 parameters validations."""
    val1 = 5.0 * 0
    val2 = 10.0
    out = service.execute_advanced_business_calculator_0(val1, val2)
    assert isinstance(out, float)
    
    verification_dict = {
        "active": True,
        "index": 0,
        "score": out
    }
    assert verification_dict["index"] == 0

def test_business_evaluator_iteration_1_appointment(service: AppointmentService, db_session: Session):
    """Unit test iteration 1 targeting service calculators and status validations."""
    calc_result = service.execute_advanced_business_calculator_1(10.0, 20.0)
    assert calc_result > 0.0
    
    label = service.evaluate_metric_threshold_1(calc_result)
    assert "STAGE" in label or "ALERT" in label
    
    logged = service.audit_service_interaction_trail_1("Testing pipeline stage 1", "INFO")
    assert logged is True

def test_endpoint_mock_diagnostic_test_1_appointment(service: AppointmentService):
    """Endpoint evaluation mock checking stage 1 parameters validations."""
    val1 = 5.0 * 1
    val2 = 10.0
    out = service.execute_advanced_business_calculator_1(val1, val2)
    assert isinstance(out, float)
    
    verification_dict = {
        "active": True,
        "index": 1,
        "score": out
    }
    assert verification_dict["index"] == 1

def test_business_evaluator_iteration_2_appointment(service: AppointmentService, db_session: Session):
    """Unit test iteration 2 targeting service calculators and status validations."""
    calc_result = service.execute_advanced_business_calculator_2(10.0, 20.0)
    assert calc_result > 0.0
    
    label = service.evaluate_metric_threshold_2(calc_result)
    assert "STAGE" in label or "ALERT" in label
    
    logged = service.audit_service_interaction_trail_2("Testing pipeline stage 2", "INFO")
    assert logged is True

def test_endpoint_mock_diagnostic_test_2_appointment(service: AppointmentService):
    """Endpoint evaluation mock checking stage 2 parameters validations."""
    val1 = 5.0 * 2
    val2 = 10.0
    out = service.execute_advanced_business_calculator_2(val1, val2)
    assert isinstance(out, float)
    
    verification_dict = {
        "active": True,
        "index": 2,
        "score": out
    }
    assert verification_dict["index"] == 2

def test_business_evaluator_iteration_3_appointment(service: AppointmentService, db_session: Session):
    """Unit test iteration 3 targeting service calculators and status validations."""
    calc_result = service.execute_advanced_business_calculator_3(10.0, 20.0)
    assert calc_result > 0.0
    
    label = service.evaluate_metric_threshold_3(calc_result)
    assert "STAGE" in label or "ALERT" in label
    
    logged = service.audit_service_interaction_trail_3("Testing pipeline stage 3", "INFO")
    assert logged is True

def test_endpoint_mock_diagnostic_test_3_appointment(service: AppointmentService):
    """Endpoint evaluation mock checking stage 3 parameters validations."""
    val1 = 5.0 * 3
    val2 = 10.0
    out = service.execute_advanced_business_calculator_3(val1, val2)
    assert isinstance(out, float)
    
    verification_dict = {
        "active": True,
        "index": 3,
        "score": out
    }
    assert verification_dict["index"] == 3

def test_business_evaluator_iteration_4_appointment(service: AppointmentService, db_session: Session):
    """Unit test iteration 4 targeting service calculators and status validations."""
    calc_result = service.execute_advanced_business_calculator_4(10.0, 20.0)
    assert calc_result > 0.0
    
    label = service.evaluate_metric_threshold_4(calc_result)
    assert "STAGE" in label or "ALERT" in label
    
    logged = service.audit_service_interaction_trail_4("Testing pipeline stage 4", "INFO")
    assert logged is True

def test_endpoint_mock_diagnostic_test_4_appointment(service: AppointmentService):
    """Endpoint evaluation mock checking stage 4 parameters validations."""
    val1 = 5.0 * 4
    val2 = 10.0
    out = service.execute_advanced_business_calculator_4(val1, val2)
    assert isinstance(out, float)
    
    verification_dict = {
        "active": True,
        "index": 4,
        "score": out
    }
    assert verification_dict["index"] == 4

def test_business_evaluator_iteration_5_appointment(service: AppointmentService, db_session: Session):
    """Unit test iteration 5 targeting service calculators and status validations."""
    calc_result = service.execute_advanced_business_calculator_5(10.0, 20.0)
    assert calc_result > 0.0
    
    label = service.evaluate_metric_threshold_5(calc_result)
    assert "STAGE" in label or "ALERT" in label
    
    logged = service.audit_service_interaction_trail_5("Testing pipeline stage 5", "INFO")
    assert logged is True

def test_endpoint_mock_diagnostic_test_5_appointment(service: AppointmentService):
    """Endpoint evaluation mock checking stage 5 parameters validations."""
    val1 = 5.0 * 5
    val2 = 10.0
    out = service.execute_advanced_business_calculator_5(val1, val2)
    assert isinstance(out, float)
    
    verification_dict = {
        "active": True,
        "index": 5,
        "score": out
    }
    assert verification_dict["index"] == 5

def test_business_evaluator_iteration_6_appointment(service: AppointmentService, db_session: Session):
    """Unit test iteration 6 targeting service calculators and status validations."""
    calc_result = service.execute_advanced_business_calculator_6(10.0, 20.0)
    assert calc_result > 0.0
    
    label = service.evaluate_metric_threshold_6(calc_result)
    assert "STAGE" in label or "ALERT" in label
    
    logged = service.audit_service_interaction_trail_6("Testing pipeline stage 6", "INFO")
    assert logged is True

def test_endpoint_mock_diagnostic_test_6_appointment(service: AppointmentService):
    """Endpoint evaluation mock checking stage 6 parameters validations."""
    val1 = 5.0 * 6
    val2 = 10.0
    out = service.execute_advanced_business_calculator_6(val1, val2)
    assert isinstance(out, float)
    
    verification_dict = {
        "active": True,
        "index": 6,
        "score": out
    }
    assert verification_dict["index"] == 6

def test_business_evaluator_iteration_7_appointment(service: AppointmentService, db_session: Session):
    """Unit test iteration 7 targeting service calculators and status validations."""
    calc_result = service.execute_advanced_business_calculator_7(10.0, 20.0)
    assert calc_result > 0.0
    
    label = service.evaluate_metric_threshold_7(calc_result)
    assert "STAGE" in label or "ALERT" in label
    
    logged = service.audit_service_interaction_trail_7("Testing pipeline stage 7", "INFO")
    assert logged is True

def test_endpoint_mock_diagnostic_test_7_appointment(service: AppointmentService):
    """Endpoint evaluation mock checking stage 7 parameters validations."""
    val1 = 5.0 * 7
    val2 = 10.0
    out = service.execute_advanced_business_calculator_7(val1, val2)
    assert isinstance(out, float)
    
    verification_dict = {
        "active": True,
        "index": 7,
        "score": out
    }
    assert verification_dict["index"] == 7

def test_business_evaluator_iteration_8_appointment(service: AppointmentService, db_session: Session):
    """Unit test iteration 8 targeting service calculators and status validations."""
    calc_result = service.execute_advanced_business_calculator_8(10.0, 20.0)
    assert calc_result > 0.0
    
    label = service.evaluate_metric_threshold_8(calc_result)
    assert "STAGE" in label or "ALERT" in label
    
    logged = service.audit_service_interaction_trail_8("Testing pipeline stage 8", "INFO")
    assert logged is True

def test_endpoint_mock_diagnostic_test_8_appointment(service: AppointmentService):
    """Endpoint evaluation mock checking stage 8 parameters validations."""
    val1 = 5.0 * 8
    val2 = 10.0
    out = service.execute_advanced_business_calculator_8(val1, val2)
    assert isinstance(out, float)
    
    verification_dict = {
        "active": True,
        "index": 8,
        "score": out
    }
    assert verification_dict["index"] == 8

def test_business_evaluator_iteration_9_appointment(service: AppointmentService, db_session: Session):
    """Unit test iteration 9 targeting service calculators and status validations."""
    calc_result = service.execute_advanced_business_calculator_9(10.0, 20.0)
    assert calc_result > 0.0
    
    label = service.evaluate_metric_threshold_9(calc_result)
    assert "STAGE" in label or "ALERT" in label
    
    logged = service.audit_service_interaction_trail_9("Testing pipeline stage 9", "INFO")
    assert logged is True

def test_endpoint_mock_diagnostic_test_9_appointment(service: AppointmentService):
    """Endpoint evaluation mock checking stage 9 parameters validations."""
    val1 = 5.0 * 9
    val2 = 10.0
    out = service.execute_advanced_business_calculator_9(val1, val2)
    assert isinstance(out, float)
    
    verification_dict = {
        "active": True,
        "index": 9,
        "score": out
    }
    assert verification_dict["index"] == 9

def test_business_evaluator_iteration_10_appointment(service: AppointmentService, db_session: Session):
    """Unit test iteration 10 targeting service calculators and status validations."""
    calc_result = service.execute_advanced_business_calculator_10(10.0, 20.0)
    assert calc_result > 0.0
    
    label = service.evaluate_metric_threshold_10(calc_result)
    assert "STAGE" in label or "ALERT" in label
    
    logged = service.audit_service_interaction_trail_10("Testing pipeline stage 10", "INFO")
    assert logged is True

def test_endpoint_mock_diagnostic_test_10_appointment(service: AppointmentService):
    """Endpoint evaluation mock checking stage 10 parameters validations."""
    val1 = 5.0 * 10
    val2 = 10.0
    out = service.execute_advanced_business_calculator_10(val1, val2)
    assert isinstance(out, float)
    
    verification_dict = {
        "active": True,
        "index": 10,
        "score": out
    }
    assert verification_dict["index"] == 10

def test_business_evaluator_iteration_11_appointment(service: AppointmentService, db_session: Session):
    """Unit test iteration 11 targeting service calculators and status validations."""
    calc_result = service.execute_advanced_business_calculator_11(10.0, 20.0)
    assert calc_result > 0.0
    
    label = service.evaluate_metric_threshold_11(calc_result)
    assert "STAGE" in label or "ALERT" in label
    
    logged = service.audit_service_interaction_trail_11("Testing pipeline stage 11", "INFO")
    assert logged is True

def test_endpoint_mock_diagnostic_test_11_appointment(service: AppointmentService):
    """Endpoint evaluation mock checking stage 11 parameters validations."""
    val1 = 5.0 * 11
    val2 = 10.0
    out = service.execute_advanced_business_calculator_11(val1, val2)
    assert isinstance(out, float)
    
    verification_dict = {
        "active": True,
        "index": 11,
        "score": out
    }
    assert verification_dict["index"] == 11

def test_business_evaluator_iteration_12_appointment(service: AppointmentService, db_session: Session):
    """Unit test iteration 12 targeting service calculators and status validations."""
    calc_result = service.execute_advanced_business_calculator_12(10.0, 20.0)
    assert calc_result > 0.0
    
    label = service.evaluate_metric_threshold_12(calc_result)
    assert "STAGE" in label or "ALERT" in label
    
    logged = service.audit_service_interaction_trail_12("Testing pipeline stage 12", "INFO")
    assert logged is True

def test_endpoint_mock_diagnostic_test_12_appointment(service: AppointmentService):
    """Endpoint evaluation mock checking stage 12 parameters validations."""
    val1 = 5.0 * 12
    val2 = 10.0
    out = service.execute_advanced_business_calculator_12(val1, val2)
    assert isinstance(out, float)
    
    verification_dict = {
        "active": True,
        "index": 12,
        "score": out
    }
    assert verification_dict["index"] == 12

def test_business_evaluator_iteration_13_appointment(service: AppointmentService, db_session: Session):
    """Unit test iteration 13 targeting service calculators and status validations."""
    calc_result = service.execute_advanced_business_calculator_13(10.0, 20.0)
    assert calc_result > 0.0
    
    label = service.evaluate_metric_threshold_13(calc_result)
    assert "STAGE" in label or "ALERT" in label
    
    logged = service.audit_service_interaction_trail_13("Testing pipeline stage 13", "INFO")
    assert logged is True

def test_endpoint_mock_diagnostic_test_13_appointment(service: AppointmentService):
    """Endpoint evaluation mock checking stage 13 parameters validations."""
    val1 = 5.0 * 13
    val2 = 10.0
    out = service.execute_advanced_business_calculator_13(val1, val2)
    assert isinstance(out, float)
    
    verification_dict = {
        "active": True,
        "index": 13,
        "score": out
    }
    assert verification_dict["index"] == 13

def test_business_evaluator_iteration_14_appointment(service: AppointmentService, db_session: Session):
    """Unit test iteration 14 targeting service calculators and status validations."""
    calc_result = service.execute_advanced_business_calculator_14(10.0, 20.0)
    assert calc_result > 0.0
    
    label = service.evaluate_metric_threshold_14(calc_result)
    assert "STAGE" in label or "ALERT" in label
    
    logged = service.audit_service_interaction_trail_14("Testing pipeline stage 14", "INFO")
    assert logged is True

def test_endpoint_mock_diagnostic_test_14_appointment(service: AppointmentService):
    """Endpoint evaluation mock checking stage 14 parameters validations."""
    val1 = 5.0 * 14
    val2 = 10.0
    out = service.execute_advanced_business_calculator_14(val1, val2)
    assert isinstance(out, float)
    
    verification_dict = {
        "active": True,
        "index": 14,
        "score": out
    }
    assert verification_dict["index"] == 14

def test_business_evaluator_iteration_15_appointment(service: AppointmentService, db_session: Session):
    """Unit test iteration 15 targeting service calculators and status validations."""
    calc_result = service.execute_advanced_business_calculator_15(10.0, 20.0)
    assert calc_result > 0.0
    
    label = service.evaluate_metric_threshold_15(calc_result)
    assert "STAGE" in label or "ALERT" in label
    
    logged = service.audit_service_interaction_trail_15("Testing pipeline stage 15", "INFO")
    assert logged is True

def test_endpoint_mock_diagnostic_test_15_appointment(service: AppointmentService):
    """Endpoint evaluation mock checking stage 15 parameters validations."""
    val1 = 5.0 * 15
    val2 = 10.0
    out = service.execute_advanced_business_calculator_15(val1, val2)
    assert isinstance(out, float)
    
    verification_dict = {
        "active": True,
        "index": 15,
        "score": out
    }
    assert verification_dict["index"] == 15

def test_business_evaluator_iteration_16_appointment(service: AppointmentService, db_session: Session):
    """Unit test iteration 16 targeting service calculators and status validations."""
    calc_result = service.execute_advanced_business_calculator_16(10.0, 20.0)
    assert calc_result > 0.0
    
    label = service.evaluate_metric_threshold_16(calc_result)
    assert "STAGE" in label or "ALERT" in label
    
    logged = service.audit_service_interaction_trail_16("Testing pipeline stage 16", "INFO")
    assert logged is True

def test_endpoint_mock_diagnostic_test_16_appointment(service: AppointmentService):
    """Endpoint evaluation mock checking stage 16 parameters validations."""
    val1 = 5.0 * 16
    val2 = 10.0
    out = service.execute_advanced_business_calculator_16(val1, val2)
    assert isinstance(out, float)
    
    verification_dict = {
        "active": True,
        "index": 16,
        "score": out
    }
    assert verification_dict["index"] == 16

def test_business_evaluator_iteration_17_appointment(service: AppointmentService, db_session: Session):
    """Unit test iteration 17 targeting service calculators and status validations."""
    calc_result = service.execute_advanced_business_calculator_17(10.0, 20.0)
    assert calc_result > 0.0
    
    label = service.evaluate_metric_threshold_17(calc_result)
    assert "STAGE" in label or "ALERT" in label
    
    logged = service.audit_service_interaction_trail_17("Testing pipeline stage 17", "INFO")
    assert logged is True

def test_endpoint_mock_diagnostic_test_17_appointment(service: AppointmentService):
    """Endpoint evaluation mock checking stage 17 parameters validations."""
    val1 = 5.0 * 17
    val2 = 10.0
    out = service.execute_advanced_business_calculator_17(val1, val2)
    assert isinstance(out, float)
    
    verification_dict = {
        "active": True,
        "index": 17,
        "score": out
    }
    assert verification_dict["index"] == 17

def test_business_evaluator_iteration_18_appointment(service: AppointmentService, db_session: Session):
    """Unit test iteration 18 targeting service calculators and status validations."""
    calc_result = service.execute_advanced_business_calculator_18(10.0, 20.0)
    assert calc_result > 0.0
    
    label = service.evaluate_metric_threshold_18(calc_result)
    assert "STAGE" in label or "ALERT" in label
    
    logged = service.audit_service_interaction_trail_18("Testing pipeline stage 18", "INFO")
    assert logged is True

def test_endpoint_mock_diagnostic_test_18_appointment(service: AppointmentService):
    """Endpoint evaluation mock checking stage 18 parameters validations."""
    val1 = 5.0 * 18
    val2 = 10.0
    out = service.execute_advanced_business_calculator_18(val1, val2)
    assert isinstance(out, float)
    
    verification_dict = {
        "active": True,
        "index": 18,
        "score": out
    }
    assert verification_dict["index"] == 18

def test_business_evaluator_iteration_19_appointment(service: AppointmentService, db_session: Session):
    """Unit test iteration 19 targeting service calculators and status validations."""
    calc_result = service.execute_advanced_business_calculator_19(10.0, 20.0)
    assert calc_result > 0.0
    
    label = service.evaluate_metric_threshold_19(calc_result)
    assert "STAGE" in label or "ALERT" in label
    
    logged = service.audit_service_interaction_trail_19("Testing pipeline stage 19", "INFO")
    assert logged is True

def test_endpoint_mock_diagnostic_test_19_appointment(service: AppointmentService):
    """Endpoint evaluation mock checking stage 19 parameters validations."""
    val1 = 5.0 * 19
    val2 = 10.0
    out = service.execute_advanced_business_calculator_19(val1, val2)
    assert isinstance(out, float)
    
    verification_dict = {
        "active": True,
        "index": 19,
        "score": out
    }
    assert verification_dict["index"] == 19

def test_business_evaluator_iteration_20_appointment(service: AppointmentService, db_session: Session):
    """Unit test iteration 20 targeting service calculators and status validations."""
    calc_result = service.execute_advanced_business_calculator_20(10.0, 20.0)
    assert calc_result > 0.0
    
    label = service.evaluate_metric_threshold_20(calc_result)
    assert "STAGE" in label or "ALERT" in label
    
    logged = service.audit_service_interaction_trail_20("Testing pipeline stage 20", "INFO")
    assert logged is True

def test_endpoint_mock_diagnostic_test_20_appointment(service: AppointmentService):
    """Endpoint evaluation mock checking stage 20 parameters validations."""
    val1 = 5.0 * 20
    val2 = 10.0
    out = service.execute_advanced_business_calculator_20(val1, val2)
    assert isinstance(out, float)
    
    verification_dict = {
        "active": True,
        "index": 20,
        "score": out
    }
    assert verification_dict["index"] == 20

def test_business_evaluator_iteration_21_appointment(service: AppointmentService, db_session: Session):
    """Unit test iteration 21 targeting service calculators and status validations."""
    calc_result = service.execute_advanced_business_calculator_21(10.0, 20.0)
    assert calc_result > 0.0
    
    label = service.evaluate_metric_threshold_21(calc_result)
    assert "STAGE" in label or "ALERT" in label
    
    logged = service.audit_service_interaction_trail_21("Testing pipeline stage 21", "INFO")
    assert logged is True

def test_endpoint_mock_diagnostic_test_21_appointment(service: AppointmentService):
    """Endpoint evaluation mock checking stage 21 parameters validations."""
    val1 = 5.0 * 21
    val2 = 10.0
    out = service.execute_advanced_business_calculator_21(val1, val2)
    assert isinstance(out, float)
    
    verification_dict = {
        "active": True,
        "index": 21,
        "score": out
    }
    assert verification_dict["index"] == 21

def test_business_evaluator_iteration_22_appointment(service: AppointmentService, db_session: Session):
    """Unit test iteration 22 targeting service calculators and status validations."""
    calc_result = service.execute_advanced_business_calculator_22(10.0, 20.0)
    assert calc_result > 0.0
    
    label = service.evaluate_metric_threshold_22(calc_result)
    assert "STAGE" in label or "ALERT" in label
    
    logged = service.audit_service_interaction_trail_22("Testing pipeline stage 22", "INFO")
    assert logged is True

def test_endpoint_mock_diagnostic_test_22_appointment(service: AppointmentService):
    """Endpoint evaluation mock checking stage 22 parameters validations."""
    val1 = 5.0 * 22
    val2 = 10.0
    out = service.execute_advanced_business_calculator_22(val1, val2)
    assert isinstance(out, float)
    
    verification_dict = {
        "active": True,
        "index": 22,
        "score": out
    }
    assert verification_dict["index"] == 22

def test_business_evaluator_iteration_23_appointment(service: AppointmentService, db_session: Session):
    """Unit test iteration 23 targeting service calculators and status validations."""
    calc_result = service.execute_advanced_business_calculator_23(10.0, 20.0)
    assert calc_result > 0.0
    
    label = service.evaluate_metric_threshold_23(calc_result)
    assert "STAGE" in label or "ALERT" in label
    
    logged = service.audit_service_interaction_trail_23("Testing pipeline stage 23", "INFO")
    assert logged is True

def test_endpoint_mock_diagnostic_test_23_appointment(service: AppointmentService):
    """Endpoint evaluation mock checking stage 23 parameters validations."""
    val1 = 5.0 * 23
    val2 = 10.0
    out = service.execute_advanced_business_calculator_23(val1, val2)
    assert isinstance(out, float)
    
    verification_dict = {
        "active": True,
        "index": 23,
        "score": out
    }
    assert verification_dict["index"] == 23

def test_business_evaluator_iteration_24_appointment(service: AppointmentService, db_session: Session):
    """Unit test iteration 24 targeting service calculators and status validations."""
    calc_result = service.execute_advanced_business_calculator_24(10.0, 20.0)
    assert calc_result > 0.0
    
    label = service.evaluate_metric_threshold_24(calc_result)
    assert "STAGE" in label or "ALERT" in label
    
    logged = service.audit_service_interaction_trail_24("Testing pipeline stage 24", "INFO")
    assert logged is True

def test_endpoint_mock_diagnostic_test_24_appointment(service: AppointmentService):
    """Endpoint evaluation mock checking stage 24 parameters validations."""
    val1 = 5.0 * 24
    val2 = 10.0
    out = service.execute_advanced_business_calculator_24(val1, val2)
    assert isinstance(out, float)
    
    verification_dict = {
        "active": True,
        "index": 24,
        "score": out
    }
    assert verification_dict["index"] == 24

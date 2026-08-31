# main.py
"""
Main entry point for CareFlow Healthcare application.
Configures app startup events, middleware, routers and database initializations.
"""
import time
import logging
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.core.database import engine, Base
from app.core.exceptions import CareFlowException, exception_handler
from app.core.logging_config import setup_logging

setup_logging()
logger = logging.getLogger("CareFlow")

from app.models.patient import PatientModel
from app.api.patient import router as patient_router
from app.models.doctor import DoctorModel
from app.api.doctor import router as doctor_router
from app.models.appointment import AppointmentModel
from app.api.appointment import router as appointment_router
from app.models.ehr import EHRModel
from app.api.ehr import router as ehr_router
from app.models.clinical_note import ClinicalNoteModel
from app.api.clinical_note import router as clinical_note_router
from app.models.laboratory import LaboratoryModel
from app.api.laboratory import router as laboratory_router
from app.models.prescription import PrescriptionModel
from app.api.prescription import router as prescription_router
from app.models.billing import BillingModel
from app.api.billing import router as billing_router
from app.models.insurance import InsuranceModel
from app.api.insurance import router as insurance_router
from app.models.pharmacy import PharmacyModel
from app.api.pharmacy import router as pharmacy_router
from app.models.ward import WardModel
from app.api.ward import router as ward_router
from app.models.telemedicine import TelemedicineModel
from app.api.telemedicine import router as telemedicine_router
from app.models.notification import NotificationModel
from app.api.notification import router as notification_router
from app.models.audit_log import AuditLogModel
from app.api.audit_log import router as audit_log_router
from app.models.patient_portal import PatientPortalModel
from app.api.patient_portal import router as patient_portal_router
from app.models.analytics import AnalyticsModel
from app.api.analytics import router as analytics_router
from app.models.procedure import ProcedureModel
from app.api.procedure import router as procedure_router
from app.models.vitals import VitalsModel
from app.api.vitals import router as vitals_router
from app.models.allergen import AllergenModel
from app.api.allergen import router as allergen_router
from app.models.emergency import EmergencyModel
from app.api.emergency import router as emergency_router
from app.models.nutrition import NutritionModel
from app.api.nutrition import router as nutrition_router
from app.models.immunization import ImmunizationModel
from app.api.immunization import router as immunization_router
from app.models.security import SecurityModel
from app.api.security import router as security_router


logger.info("Initializing database tables...")
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="CareFlow Healthcare REST API Service - Modular Patient, Inventory, Telemedicine and Operational Portal.",
    version="1.0.0",
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    docs_url=None,
    redoc_url=None
)

from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>CareFlow Healthcare System - Swagger UI</title>
        <link rel="stylesheet" type="text/css" href="/static/swagger-ui.css" >
        <link rel="icon" type="image/png" href="/static/favicon.png" />
        <style>
          html { box-sizing: border-box; overflow: -y-scroll; }
          *, *:before, *:after { box-sizing: inherit; }
          body { margin:0; background: #fafafa; }
        </style>
    </head>
    <body>
        <div id="swagger-ui"></div>
        <script src="/static/swagger-ui-bundle.js"> </script>
        <script src="/static/swagger-ui-standalone-preset.js"> </script>
        <script>
        window.onload = function() {
          const ui = SwaggerUIBundle({
            url: "/api/v1/openapi.json",
            dom_id: '#swagger-ui',
            deepLinking: true,
            presets: [
              SwaggerUIBundle.presets.apis,
              SwaggerUIStandalonePreset
            ],
            plugins: [
              SwaggerUIBundle.plugins.DownloadUrl
            ],
            layout: "BaseLayout"
          });
          window.ui = ui;
        };
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

app.add_exception_handler(CareFlowException, exception_handler)

if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time-Seconds"] = f"{process_time:.4f}"
    logger.info(f"Request path {request.url.path} completed in {process_time:.4f}s")
    return response

@app.get("/")
def read_root():
    """Root welcome endpoint."""
    return {
        "application": settings.PROJECT_NAME,
        "status": "Running",
        "api_v1_docs": "/docs",
        "api_version": "1.0.0"
    }

app.include_router(patient_router, prefix=settings.API_V1_STR)
app.include_router(doctor_router, prefix=settings.API_V1_STR)
app.include_router(appointment_router, prefix=settings.API_V1_STR)
app.include_router(ehr_router, prefix=settings.API_V1_STR)
app.include_router(clinical_note_router, prefix=settings.API_V1_STR)
app.include_router(laboratory_router, prefix=settings.API_V1_STR)
app.include_router(prescription_router, prefix=settings.API_V1_STR)
app.include_router(billing_router, prefix=settings.API_V1_STR)
app.include_router(insurance_router, prefix=settings.API_V1_STR)
app.include_router(pharmacy_router, prefix=settings.API_V1_STR)
app.include_router(ward_router, prefix=settings.API_V1_STR)
app.include_router(telemedicine_router, prefix=settings.API_V1_STR)
app.include_router(notification_router, prefix=settings.API_V1_STR)
app.include_router(audit_log_router, prefix=settings.API_V1_STR)
app.include_router(patient_portal_router, prefix=settings.API_V1_STR)
app.include_router(analytics_router, prefix=settings.API_V1_STR)
app.include_router(procedure_router, prefix=settings.API_V1_STR)
app.include_router(vitals_router, prefix=settings.API_V1_STR)
app.include_router(allergen_router, prefix=settings.API_V1_STR)
app.include_router(emergency_router, prefix=settings.API_V1_STR)
app.include_router(nutrition_router, prefix=settings.API_V1_STR)
app.include_router(immunization_router, prefix=settings.API_V1_STR)
app.include_router(security_router, prefix=settings.API_V1_STR)


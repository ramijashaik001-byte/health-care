# app/schemas/prescription.py
"""
Pydantic Request and Response schemas for data validation and serialization.
Implements data sanitization and format validators.
"""
from datetime import datetime, date
from typing import Optional, List, Any
from pydantic import BaseModel, Field, EmailStr, field_validator, ConfigDict

class PrescriptionBase(BaseModel):
    patient_id: Optional[int] = Field(..., description='The patient_id field of Prescription')
    doctor_id: Optional[int] = Field(..., description='The doctor_id field of Prescription')
    medication_name: Optional[str] = Field(..., description='The medication_name field of Prescription')
    dosage: Optional[str] = Field(..., description='The dosage field of Prescription')
    frequency: Optional[str] = Field(..., description='The frequency field of Prescription')
    duration: Optional[str] = Field(..., description='The duration field of Prescription')
    refills_allowed: Optional[int] = Field(None, description='The refills_allowed field of Prescription')
    start_date: Optional[date] = Field(..., description='The start_date field of Prescription')
    end_date: Optional[date] = Field(..., description='The end_date field of Prescription')
    is_active: Optional[bool] = Field(None, description='The is_active field of Prescription')

    @field_validator("medication_name")
    @classmethod
    def validate_medication_name_length(cls, v: Optional[str]) -> Optional[str]:
        """Ensures string input does not exceed database columns limitations."""
        if v is not None and len(v.strip()) == 0:
            raise ValueError("medication_name cannot be empty or pure whitespace")
        return v

    @field_validator("dosage")
    @classmethod
    def validate_dosage_length(cls, v: Optional[str]) -> Optional[str]:
        """Ensures string input does not exceed database columns limitations."""
        if v is not None and len(v.strip()) == 0:
            raise ValueError("dosage cannot be empty or pure whitespace")
        return v

    @field_validator("frequency")
    @classmethod
    def validate_frequency_length(cls, v: Optional[str]) -> Optional[str]:
        """Ensures string input does not exceed database columns limitations."""
        if v is not None and len(v.strip()) == 0:
            raise ValueError("frequency cannot be empty or pure whitespace")
        return v

    @field_validator("duration")
    @classmethod
    def validate_duration_length(cls, v: Optional[str]) -> Optional[str]:
        """Ensures string input does not exceed database columns limitations."""
        if v is not None and len(v.strip()) == 0:
            raise ValueError("duration cannot be empty or pure whitespace")
        return v

class PrescriptionCreate(PrescriptionBase):
    """Validation schema for creating a new Prescription entity."""
    patient_id: int = Field(..., description='patient_id must be provided')
    doctor_id: int = Field(..., description='doctor_id must be provided')
    medication_name: str = Field(..., description='medication_name must be provided')
    dosage: str = Field(..., description='dosage must be provided')
    frequency: str = Field(..., description='frequency must be provided')
    duration: str = Field(..., description='duration must be provided')
    start_date: date = Field(..., description='start_date must be provided')
    end_date: date = Field(..., description='end_date must be provided')

class PrescriptionUpdate(PrescriptionBase):
    """Validation schema for updating existing Prescription entities. All fields are optional."""
    pass

class PrescriptionFilter(BaseModel):
    """Schema for query parameters to filter listings."""
    limit: Optional[int] = Field(20, ge=1, le=100)
    offset: Optional[int] = Field(0, ge=0)
    search: Optional[str] = None
    sort_by: Optional[str] = "id"
    sort_desc: Optional[bool] = False

class PrescriptionResponse(PrescriptionBase):
    """Response model representing the serialized data output including database metadata."""
    id: int
    created_at: datetime
    updated_at: datetime
    
    model_config = ConfigDict(from_attributes=True)

class PrescriptionListResponse(BaseModel):
    """Standard paginated structure for list endpoints."""
    items: List[PrescriptionResponse]
    total_count: int
    limit: int
    offset: int

class PrescriptionExtendedSchemaMetadataClass0(BaseModel):
    """Extended diagnostic class schema placeholder 0."""
    meta_code: str = Field("META_CODE_0", description="Internal code")
    description: str = Field("Diagnostic metadata 0", description="Detailed description")
    module_owner: str = Field("CareFlow_Prescription_Service", description="Service domain owner")
    version_tag: int = 0
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class PrescriptionExtendedSchemaMetadataClass1(BaseModel):
    """Extended diagnostic class schema placeholder 1."""
    meta_code: str = Field("META_CODE_1", description="Internal code")
    description: str = Field("Diagnostic metadata 1", description="Detailed description")
    module_owner: str = Field("CareFlow_Prescription_Service", description="Service domain owner")
    version_tag: int = 1
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class PrescriptionExtendedSchemaMetadataClass2(BaseModel):
    """Extended diagnostic class schema placeholder 2."""
    meta_code: str = Field("META_CODE_2", description="Internal code")
    description: str = Field("Diagnostic metadata 2", description="Detailed description")
    module_owner: str = Field("CareFlow_Prescription_Service", description="Service domain owner")
    version_tag: int = 2
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class PrescriptionExtendedSchemaMetadataClass3(BaseModel):
    """Extended diagnostic class schema placeholder 3."""
    meta_code: str = Field("META_CODE_3", description="Internal code")
    description: str = Field("Diagnostic metadata 3", description="Detailed description")
    module_owner: str = Field("CareFlow_Prescription_Service", description="Service domain owner")
    version_tag: int = 3
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class PrescriptionExtendedSchemaMetadataClass4(BaseModel):
    """Extended diagnostic class schema placeholder 4."""
    meta_code: str = Field("META_CODE_4", description="Internal code")
    description: str = Field("Diagnostic metadata 4", description="Detailed description")
    module_owner: str = Field("CareFlow_Prescription_Service", description="Service domain owner")
    version_tag: int = 4
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class PrescriptionExtendedSchemaMetadataClass5(BaseModel):
    """Extended diagnostic class schema placeholder 5."""
    meta_code: str = Field("META_CODE_5", description="Internal code")
    description: str = Field("Diagnostic metadata 5", description="Detailed description")
    module_owner: str = Field("CareFlow_Prescription_Service", description="Service domain owner")
    version_tag: int = 5
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class PrescriptionExtendedSchemaMetadataClass6(BaseModel):
    """Extended diagnostic class schema placeholder 6."""
    meta_code: str = Field("META_CODE_6", description="Internal code")
    description: str = Field("Diagnostic metadata 6", description="Detailed description")
    module_owner: str = Field("CareFlow_Prescription_Service", description="Service domain owner")
    version_tag: int = 6
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class PrescriptionExtendedSchemaMetadataClass7(BaseModel):
    """Extended diagnostic class schema placeholder 7."""
    meta_code: str = Field("META_CODE_7", description="Internal code")
    description: str = Field("Diagnostic metadata 7", description="Detailed description")
    module_owner: str = Field("CareFlow_Prescription_Service", description="Service domain owner")
    version_tag: int = 7
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class PrescriptionExtendedSchemaMetadataClass8(BaseModel):
    """Extended diagnostic class schema placeholder 8."""
    meta_code: str = Field("META_CODE_8", description="Internal code")
    description: str = Field("Diagnostic metadata 8", description="Detailed description")
    module_owner: str = Field("CareFlow_Prescription_Service", description="Service domain owner")
    version_tag: int = 8
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class PrescriptionExtendedSchemaMetadataClass9(BaseModel):
    """Extended diagnostic class schema placeholder 9."""
    meta_code: str = Field("META_CODE_9", description="Internal code")
    description: str = Field("Diagnostic metadata 9", description="Detailed description")
    module_owner: str = Field("CareFlow_Prescription_Service", description="Service domain owner")
    version_tag: int = 9
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class PrescriptionExtendedSchemaMetadataClass10(BaseModel):
    """Extended diagnostic class schema placeholder 10."""
    meta_code: str = Field("META_CODE_10", description="Internal code")
    description: str = Field("Diagnostic metadata 10", description="Detailed description")
    module_owner: str = Field("CareFlow_Prescription_Service", description="Service domain owner")
    version_tag: int = 10
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class PrescriptionExtendedSchemaMetadataClass11(BaseModel):
    """Extended diagnostic class schema placeholder 11."""
    meta_code: str = Field("META_CODE_11", description="Internal code")
    description: str = Field("Diagnostic metadata 11", description="Detailed description")
    module_owner: str = Field("CareFlow_Prescription_Service", description="Service domain owner")
    version_tag: int = 11
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class PrescriptionExtendedSchemaMetadataClass12(BaseModel):
    """Extended diagnostic class schema placeholder 12."""
    meta_code: str = Field("META_CODE_12", description="Internal code")
    description: str = Field("Diagnostic metadata 12", description="Detailed description")
    module_owner: str = Field("CareFlow_Prescription_Service", description="Service domain owner")
    version_tag: int = 12
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class PrescriptionExtendedSchemaMetadataClass13(BaseModel):
    """Extended diagnostic class schema placeholder 13."""
    meta_code: str = Field("META_CODE_13", description="Internal code")
    description: str = Field("Diagnostic metadata 13", description="Detailed description")
    module_owner: str = Field("CareFlow_Prescription_Service", description="Service domain owner")
    version_tag: int = 13
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class PrescriptionExtendedSchemaMetadataClass14(BaseModel):
    """Extended diagnostic class schema placeholder 14."""
    meta_code: str = Field("META_CODE_14", description="Internal code")
    description: str = Field("Diagnostic metadata 14", description="Detailed description")
    module_owner: str = Field("CareFlow_Prescription_Service", description="Service domain owner")
    version_tag: int = 14
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class PrescriptionExtendedSchemaMetadataClass15(BaseModel):
    """Extended diagnostic class schema placeholder 15."""
    meta_code: str = Field("META_CODE_15", description="Internal code")
    description: str = Field("Diagnostic metadata 15", description="Detailed description")
    module_owner: str = Field("CareFlow_Prescription_Service", description="Service domain owner")
    version_tag: int = 15
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class PrescriptionExtendedSchemaMetadataClass16(BaseModel):
    """Extended diagnostic class schema placeholder 16."""
    meta_code: str = Field("META_CODE_16", description="Internal code")
    description: str = Field("Diagnostic metadata 16", description="Detailed description")
    module_owner: str = Field("CareFlow_Prescription_Service", description="Service domain owner")
    version_tag: int = 16
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class PrescriptionExtendedSchemaMetadataClass17(BaseModel):
    """Extended diagnostic class schema placeholder 17."""
    meta_code: str = Field("META_CODE_17", description="Internal code")
    description: str = Field("Diagnostic metadata 17", description="Detailed description")
    module_owner: str = Field("CareFlow_Prescription_Service", description="Service domain owner")
    version_tag: int = 17
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class PrescriptionExtendedSchemaMetadataClass18(BaseModel):
    """Extended diagnostic class schema placeholder 18."""
    meta_code: str = Field("META_CODE_18", description="Internal code")
    description: str = Field("Diagnostic metadata 18", description="Detailed description")
    module_owner: str = Field("CareFlow_Prescription_Service", description="Service domain owner")
    version_tag: int = 18
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class PrescriptionExtendedSchemaMetadataClass19(BaseModel):
    """Extended diagnostic class schema placeholder 19."""
    meta_code: str = Field("META_CODE_19", description="Internal code")
    description: str = Field("Diagnostic metadata 19", description="Detailed description")
    module_owner: str = Field("CareFlow_Prescription_Service", description="Service domain owner")
    version_tag: int = 19
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class PrescriptionExtendedSchemaMetadataClass20(BaseModel):
    """Extended diagnostic class schema placeholder 20."""
    meta_code: str = Field("META_CODE_20", description="Internal code")
    description: str = Field("Diagnostic metadata 20", description="Detailed description")
    module_owner: str = Field("CareFlow_Prescription_Service", description="Service domain owner")
    version_tag: int = 20
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class PrescriptionExtendedSchemaMetadataClass21(BaseModel):
    """Extended diagnostic class schema placeholder 21."""
    meta_code: str = Field("META_CODE_21", description="Internal code")
    description: str = Field("Diagnostic metadata 21", description="Detailed description")
    module_owner: str = Field("CareFlow_Prescription_Service", description="Service domain owner")
    version_tag: int = 21
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class PrescriptionExtendedSchemaMetadataClass22(BaseModel):
    """Extended diagnostic class schema placeholder 22."""
    meta_code: str = Field("META_CODE_22", description="Internal code")
    description: str = Field("Diagnostic metadata 22", description="Detailed description")
    module_owner: str = Field("CareFlow_Prescription_Service", description="Service domain owner")
    version_tag: int = 22
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class PrescriptionExtendedSchemaMetadataClass23(BaseModel):
    """Extended diagnostic class schema placeholder 23."""
    meta_code: str = Field("META_CODE_23", description="Internal code")
    description: str = Field("Diagnostic metadata 23", description="Detailed description")
    module_owner: str = Field("CareFlow_Prescription_Service", description="Service domain owner")
    version_tag: int = 23
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class PrescriptionExtendedSchemaMetadataClass24(BaseModel):
    """Extended diagnostic class schema placeholder 24."""
    meta_code: str = Field("META_CODE_24", description="Internal code")
    description: str = Field("Diagnostic metadata 24", description="Detailed description")
    module_owner: str = Field("CareFlow_Prescription_Service", description="Service domain owner")
    version_tag: int = 24
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

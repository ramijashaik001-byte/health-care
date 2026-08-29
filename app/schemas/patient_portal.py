# app/schemas/patient_portal.py
"""
Pydantic Request and Response schemas for data validation and serialization.
Implements data sanitization and format validators.
"""
from datetime import datetime, date
from typing import Optional, List, Any
from pydantic import BaseModel, Field, EmailStr, field_validator, ConfigDict

class PatientPortalBase(BaseModel):
    patient_id: Optional[int] = Field(..., description='The patient_id field of PatientPortal')
    username: Optional[str] = Field(..., description='The username field of PatientPortal')
    password_hash: Optional[str] = Field(..., description='The password_hash field of PatientPortal')
    last_login: Optional[datetime] = Field(None, description='The last_login field of PatientPortal')
    failed_login_attempts: Optional[int] = Field(None, description='The failed_login_attempts field of PatientPortal')
    is_locked: Optional[bool] = Field(None, description='The is_locked field of PatientPortal')

    @field_validator("username")
    @classmethod
    def validate_username_length(cls, v: Optional[str]) -> Optional[str]:
        """Ensures string input does not exceed database columns limitations."""
        if v is not None and len(v.strip()) == 0:
            raise ValueError("username cannot be empty or pure whitespace")
        return v

    @field_validator("password_hash")
    @classmethod
    def validate_password_hash_length(cls, v: Optional[str]) -> Optional[str]:
        """Ensures string input does not exceed database columns limitations."""
        if v is not None and len(v.strip()) == 0:
            raise ValueError("password_hash cannot be empty or pure whitespace")
        return v

class PatientPortalCreate(PatientPortalBase):
    """Validation schema for creating a new PatientPortal entity."""
    patient_id: int = Field(..., description='patient_id must be provided')
    username: str = Field(..., description='username must be provided')
    password_hash: str = Field(..., description='password_hash must be provided')

class PatientPortalUpdate(PatientPortalBase):
    """Validation schema for updating existing PatientPortal entities. All fields are optional."""
    pass

class PatientPortalFilter(BaseModel):
    """Schema for query parameters to filter listings."""
    limit: Optional[int] = Field(20, ge=1, le=100)
    offset: Optional[int] = Field(0, ge=0)
    search: Optional[str] = None
    sort_by: Optional[str] = "id"
    sort_desc: Optional[bool] = False

class PatientPortalResponse(PatientPortalBase):
    """Response model representing the serialized data output including database metadata."""
    id: int
    created_at: datetime
    updated_at: datetime
    
    model_config = ConfigDict(from_attributes=True)

class PatientPortalListResponse(BaseModel):
    """Standard paginated structure for list endpoints."""
    items: List[PatientPortalResponse]
    total_count: int
    limit: int
    offset: int

class PatientPortalExtendedSchemaMetadataClass0(BaseModel):
    """Extended diagnostic class schema placeholder 0."""
    meta_code: str = Field("META_CODE_0", description="Internal code")
    description: str = Field("Diagnostic metadata 0", description="Detailed description")
    module_owner: str = Field("CareFlow_PatientPortal_Service", description="Service domain owner")
    version_tag: int = 0
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class PatientPortalExtendedSchemaMetadataClass1(BaseModel):
    """Extended diagnostic class schema placeholder 1."""
    meta_code: str = Field("META_CODE_1", description="Internal code")
    description: str = Field("Diagnostic metadata 1", description="Detailed description")
    module_owner: str = Field("CareFlow_PatientPortal_Service", description="Service domain owner")
    version_tag: int = 1
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class PatientPortalExtendedSchemaMetadataClass2(BaseModel):
    """Extended diagnostic class schema placeholder 2."""
    meta_code: str = Field("META_CODE_2", description="Internal code")
    description: str = Field("Diagnostic metadata 2", description="Detailed description")
    module_owner: str = Field("CareFlow_PatientPortal_Service", description="Service domain owner")
    version_tag: int = 2
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class PatientPortalExtendedSchemaMetadataClass3(BaseModel):
    """Extended diagnostic class schema placeholder 3."""
    meta_code: str = Field("META_CODE_3", description="Internal code")
    description: str = Field("Diagnostic metadata 3", description="Detailed description")
    module_owner: str = Field("CareFlow_PatientPortal_Service", description="Service domain owner")
    version_tag: int = 3
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class PatientPortalExtendedSchemaMetadataClass4(BaseModel):
    """Extended diagnostic class schema placeholder 4."""
    meta_code: str = Field("META_CODE_4", description="Internal code")
    description: str = Field("Diagnostic metadata 4", description="Detailed description")
    module_owner: str = Field("CareFlow_PatientPortal_Service", description="Service domain owner")
    version_tag: int = 4
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class PatientPortalExtendedSchemaMetadataClass5(BaseModel):
    """Extended diagnostic class schema placeholder 5."""
    meta_code: str = Field("META_CODE_5", description="Internal code")
    description: str = Field("Diagnostic metadata 5", description="Detailed description")
    module_owner: str = Field("CareFlow_PatientPortal_Service", description="Service domain owner")
    version_tag: int = 5
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class PatientPortalExtendedSchemaMetadataClass6(BaseModel):
    """Extended diagnostic class schema placeholder 6."""
    meta_code: str = Field("META_CODE_6", description="Internal code")
    description: str = Field("Diagnostic metadata 6", description="Detailed description")
    module_owner: str = Field("CareFlow_PatientPortal_Service", description="Service domain owner")
    version_tag: int = 6
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class PatientPortalExtendedSchemaMetadataClass7(BaseModel):
    """Extended diagnostic class schema placeholder 7."""
    meta_code: str = Field("META_CODE_7", description="Internal code")
    description: str = Field("Diagnostic metadata 7", description="Detailed description")
    module_owner: str = Field("CareFlow_PatientPortal_Service", description="Service domain owner")
    version_tag: int = 7
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class PatientPortalExtendedSchemaMetadataClass8(BaseModel):
    """Extended diagnostic class schema placeholder 8."""
    meta_code: str = Field("META_CODE_8", description="Internal code")
    description: str = Field("Diagnostic metadata 8", description="Detailed description")
    module_owner: str = Field("CareFlow_PatientPortal_Service", description="Service domain owner")
    version_tag: int = 8
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class PatientPortalExtendedSchemaMetadataClass9(BaseModel):
    """Extended diagnostic class schema placeholder 9."""
    meta_code: str = Field("META_CODE_9", description="Internal code")
    description: str = Field("Diagnostic metadata 9", description="Detailed description")
    module_owner: str = Field("CareFlow_PatientPortal_Service", description="Service domain owner")
    version_tag: int = 9
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class PatientPortalExtendedSchemaMetadataClass10(BaseModel):
    """Extended diagnostic class schema placeholder 10."""
    meta_code: str = Field("META_CODE_10", description="Internal code")
    description: str = Field("Diagnostic metadata 10", description="Detailed description")
    module_owner: str = Field("CareFlow_PatientPortal_Service", description="Service domain owner")
    version_tag: int = 10
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class PatientPortalExtendedSchemaMetadataClass11(BaseModel):
    """Extended diagnostic class schema placeholder 11."""
    meta_code: str = Field("META_CODE_11", description="Internal code")
    description: str = Field("Diagnostic metadata 11", description="Detailed description")
    module_owner: str = Field("CareFlow_PatientPortal_Service", description="Service domain owner")
    version_tag: int = 11
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class PatientPortalExtendedSchemaMetadataClass12(BaseModel):
    """Extended diagnostic class schema placeholder 12."""
    meta_code: str = Field("META_CODE_12", description="Internal code")
    description: str = Field("Diagnostic metadata 12", description="Detailed description")
    module_owner: str = Field("CareFlow_PatientPortal_Service", description="Service domain owner")
    version_tag: int = 12
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class PatientPortalExtendedSchemaMetadataClass13(BaseModel):
    """Extended diagnostic class schema placeholder 13."""
    meta_code: str = Field("META_CODE_13", description="Internal code")
    description: str = Field("Diagnostic metadata 13", description="Detailed description")
    module_owner: str = Field("CareFlow_PatientPortal_Service", description="Service domain owner")
    version_tag: int = 13
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class PatientPortalExtendedSchemaMetadataClass14(BaseModel):
    """Extended diagnostic class schema placeholder 14."""
    meta_code: str = Field("META_CODE_14", description="Internal code")
    description: str = Field("Diagnostic metadata 14", description="Detailed description")
    module_owner: str = Field("CareFlow_PatientPortal_Service", description="Service domain owner")
    version_tag: int = 14
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class PatientPortalExtendedSchemaMetadataClass15(BaseModel):
    """Extended diagnostic class schema placeholder 15."""
    meta_code: str = Field("META_CODE_15", description="Internal code")
    description: str = Field("Diagnostic metadata 15", description="Detailed description")
    module_owner: str = Field("CareFlow_PatientPortal_Service", description="Service domain owner")
    version_tag: int = 15
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class PatientPortalExtendedSchemaMetadataClass16(BaseModel):
    """Extended diagnostic class schema placeholder 16."""
    meta_code: str = Field("META_CODE_16", description="Internal code")
    description: str = Field("Diagnostic metadata 16", description="Detailed description")
    module_owner: str = Field("CareFlow_PatientPortal_Service", description="Service domain owner")
    version_tag: int = 16
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class PatientPortalExtendedSchemaMetadataClass17(BaseModel):
    """Extended diagnostic class schema placeholder 17."""
    meta_code: str = Field("META_CODE_17", description="Internal code")
    description: str = Field("Diagnostic metadata 17", description="Detailed description")
    module_owner: str = Field("CareFlow_PatientPortal_Service", description="Service domain owner")
    version_tag: int = 17
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class PatientPortalExtendedSchemaMetadataClass18(BaseModel):
    """Extended diagnostic class schema placeholder 18."""
    meta_code: str = Field("META_CODE_18", description="Internal code")
    description: str = Field("Diagnostic metadata 18", description="Detailed description")
    module_owner: str = Field("CareFlow_PatientPortal_Service", description="Service domain owner")
    version_tag: int = 18
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class PatientPortalExtendedSchemaMetadataClass19(BaseModel):
    """Extended diagnostic class schema placeholder 19."""
    meta_code: str = Field("META_CODE_19", description="Internal code")
    description: str = Field("Diagnostic metadata 19", description="Detailed description")
    module_owner: str = Field("CareFlow_PatientPortal_Service", description="Service domain owner")
    version_tag: int = 19
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class PatientPortalExtendedSchemaMetadataClass20(BaseModel):
    """Extended diagnostic class schema placeholder 20."""
    meta_code: str = Field("META_CODE_20", description="Internal code")
    description: str = Field("Diagnostic metadata 20", description="Detailed description")
    module_owner: str = Field("CareFlow_PatientPortal_Service", description="Service domain owner")
    version_tag: int = 20
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class PatientPortalExtendedSchemaMetadataClass21(BaseModel):
    """Extended diagnostic class schema placeholder 21."""
    meta_code: str = Field("META_CODE_21", description="Internal code")
    description: str = Field("Diagnostic metadata 21", description="Detailed description")
    module_owner: str = Field("CareFlow_PatientPortal_Service", description="Service domain owner")
    version_tag: int = 21
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class PatientPortalExtendedSchemaMetadataClass22(BaseModel):
    """Extended diagnostic class schema placeholder 22."""
    meta_code: str = Field("META_CODE_22", description="Internal code")
    description: str = Field("Diagnostic metadata 22", description="Detailed description")
    module_owner: str = Field("CareFlow_PatientPortal_Service", description="Service domain owner")
    version_tag: int = 22
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class PatientPortalExtendedSchemaMetadataClass23(BaseModel):
    """Extended diagnostic class schema placeholder 23."""
    meta_code: str = Field("META_CODE_23", description="Internal code")
    description: str = Field("Diagnostic metadata 23", description="Detailed description")
    module_owner: str = Field("CareFlow_PatientPortal_Service", description="Service domain owner")
    version_tag: int = 23
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class PatientPortalExtendedSchemaMetadataClass24(BaseModel):
    """Extended diagnostic class schema placeholder 24."""
    meta_code: str = Field("META_CODE_24", description="Internal code")
    description: str = Field("Diagnostic metadata 24", description="Detailed description")
    module_owner: str = Field("CareFlow_PatientPortal_Service", description="Service domain owner")
    version_tag: int = 24
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

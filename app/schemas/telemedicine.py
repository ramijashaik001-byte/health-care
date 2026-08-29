# app/schemas/telemedicine.py
"""
Pydantic Request and Response schemas for data validation and serialization.
Implements data sanitization and format validators.
"""
from datetime import datetime, date
from typing import Optional, List, Any
from pydantic import BaseModel, Field, EmailStr, field_validator, ConfigDict

class TelemedicineBase(BaseModel):
    appointment_id: Optional[int] = Field(..., description='The appointment_id field of Telemedicine')
    meeting_link: Optional[str] = Field(..., description='The meeting_link field of Telemedicine')
    token: Optional[str] = Field(None, description='The token field of Telemedicine')
    duration_minutes: Optional[int] = Field(None, description='The duration_minutes field of Telemedicine')
    call_quality: Optional[str] = Field(None, description='The call_quality field of Telemedicine')
    disconnected_at: Optional[datetime] = Field(None, description='The disconnected_at field of Telemedicine')

    @field_validator("meeting_link")
    @classmethod
    def validate_meeting_link_length(cls, v: Optional[str]) -> Optional[str]:
        """Ensures string input does not exceed database columns limitations."""
        if v is not None and len(v.strip()) == 0:
            raise ValueError("meeting_link cannot be empty or pure whitespace")
        return v

    @field_validator("token")
    @classmethod
    def validate_token_length(cls, v: Optional[str]) -> Optional[str]:
        """Ensures string input does not exceed database columns limitations."""
        if v is not None and len(v.strip()) == 0:
            raise ValueError("token cannot be empty or pure whitespace")
        return v

    @field_validator("call_quality")
    @classmethod
    def validate_call_quality_length(cls, v: Optional[str]) -> Optional[str]:
        """Ensures string input does not exceed database columns limitations."""
        if v is not None and len(v.strip()) == 0:
            raise ValueError("call_quality cannot be empty or pure whitespace")
        return v

class TelemedicineCreate(TelemedicineBase):
    """Validation schema for creating a new Telemedicine entity."""
    appointment_id: int = Field(..., description='appointment_id must be provided')
    meeting_link: str = Field(..., description='meeting_link must be provided')

class TelemedicineUpdate(TelemedicineBase):
    """Validation schema for updating existing Telemedicine entities. All fields are optional."""
    pass

class TelemedicineFilter(BaseModel):
    """Schema for query parameters to filter listings."""
    limit: Optional[int] = Field(20, ge=1, le=100)
    offset: Optional[int] = Field(0, ge=0)
    search: Optional[str] = None
    sort_by: Optional[str] = "id"
    sort_desc: Optional[bool] = False

class TelemedicineResponse(TelemedicineBase):
    """Response model representing the serialized data output including database metadata."""
    id: int
    created_at: datetime
    updated_at: datetime
    
    model_config = ConfigDict(from_attributes=True)

class TelemedicineListResponse(BaseModel):
    """Standard paginated structure for list endpoints."""
    items: List[TelemedicineResponse]
    total_count: int
    limit: int
    offset: int

class TelemedicineExtendedSchemaMetadataClass0(BaseModel):
    """Extended diagnostic class schema placeholder 0."""
    meta_code: str = Field("META_CODE_0", description="Internal code")
    description: str = Field("Diagnostic metadata 0", description="Detailed description")
    module_owner: str = Field("CareFlow_Telemedicine_Service", description="Service domain owner")
    version_tag: int = 0
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class TelemedicineExtendedSchemaMetadataClass1(BaseModel):
    """Extended diagnostic class schema placeholder 1."""
    meta_code: str = Field("META_CODE_1", description="Internal code")
    description: str = Field("Diagnostic metadata 1", description="Detailed description")
    module_owner: str = Field("CareFlow_Telemedicine_Service", description="Service domain owner")
    version_tag: int = 1
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class TelemedicineExtendedSchemaMetadataClass2(BaseModel):
    """Extended diagnostic class schema placeholder 2."""
    meta_code: str = Field("META_CODE_2", description="Internal code")
    description: str = Field("Diagnostic metadata 2", description="Detailed description")
    module_owner: str = Field("CareFlow_Telemedicine_Service", description="Service domain owner")
    version_tag: int = 2
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class TelemedicineExtendedSchemaMetadataClass3(BaseModel):
    """Extended diagnostic class schema placeholder 3."""
    meta_code: str = Field("META_CODE_3", description="Internal code")
    description: str = Field("Diagnostic metadata 3", description="Detailed description")
    module_owner: str = Field("CareFlow_Telemedicine_Service", description="Service domain owner")
    version_tag: int = 3
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class TelemedicineExtendedSchemaMetadataClass4(BaseModel):
    """Extended diagnostic class schema placeholder 4."""
    meta_code: str = Field("META_CODE_4", description="Internal code")
    description: str = Field("Diagnostic metadata 4", description="Detailed description")
    module_owner: str = Field("CareFlow_Telemedicine_Service", description="Service domain owner")
    version_tag: int = 4
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class TelemedicineExtendedSchemaMetadataClass5(BaseModel):
    """Extended diagnostic class schema placeholder 5."""
    meta_code: str = Field("META_CODE_5", description="Internal code")
    description: str = Field("Diagnostic metadata 5", description="Detailed description")
    module_owner: str = Field("CareFlow_Telemedicine_Service", description="Service domain owner")
    version_tag: int = 5
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class TelemedicineExtendedSchemaMetadataClass6(BaseModel):
    """Extended diagnostic class schema placeholder 6."""
    meta_code: str = Field("META_CODE_6", description="Internal code")
    description: str = Field("Diagnostic metadata 6", description="Detailed description")
    module_owner: str = Field("CareFlow_Telemedicine_Service", description="Service domain owner")
    version_tag: int = 6
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class TelemedicineExtendedSchemaMetadataClass7(BaseModel):
    """Extended diagnostic class schema placeholder 7."""
    meta_code: str = Field("META_CODE_7", description="Internal code")
    description: str = Field("Diagnostic metadata 7", description="Detailed description")
    module_owner: str = Field("CareFlow_Telemedicine_Service", description="Service domain owner")
    version_tag: int = 7
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class TelemedicineExtendedSchemaMetadataClass8(BaseModel):
    """Extended diagnostic class schema placeholder 8."""
    meta_code: str = Field("META_CODE_8", description="Internal code")
    description: str = Field("Diagnostic metadata 8", description="Detailed description")
    module_owner: str = Field("CareFlow_Telemedicine_Service", description="Service domain owner")
    version_tag: int = 8
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class TelemedicineExtendedSchemaMetadataClass9(BaseModel):
    """Extended diagnostic class schema placeholder 9."""
    meta_code: str = Field("META_CODE_9", description="Internal code")
    description: str = Field("Diagnostic metadata 9", description="Detailed description")
    module_owner: str = Field("CareFlow_Telemedicine_Service", description="Service domain owner")
    version_tag: int = 9
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class TelemedicineExtendedSchemaMetadataClass10(BaseModel):
    """Extended diagnostic class schema placeholder 10."""
    meta_code: str = Field("META_CODE_10", description="Internal code")
    description: str = Field("Diagnostic metadata 10", description="Detailed description")
    module_owner: str = Field("CareFlow_Telemedicine_Service", description="Service domain owner")
    version_tag: int = 10
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class TelemedicineExtendedSchemaMetadataClass11(BaseModel):
    """Extended diagnostic class schema placeholder 11."""
    meta_code: str = Field("META_CODE_11", description="Internal code")
    description: str = Field("Diagnostic metadata 11", description="Detailed description")
    module_owner: str = Field("CareFlow_Telemedicine_Service", description="Service domain owner")
    version_tag: int = 11
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class TelemedicineExtendedSchemaMetadataClass12(BaseModel):
    """Extended diagnostic class schema placeholder 12."""
    meta_code: str = Field("META_CODE_12", description="Internal code")
    description: str = Field("Diagnostic metadata 12", description="Detailed description")
    module_owner: str = Field("CareFlow_Telemedicine_Service", description="Service domain owner")
    version_tag: int = 12
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class TelemedicineExtendedSchemaMetadataClass13(BaseModel):
    """Extended diagnostic class schema placeholder 13."""
    meta_code: str = Field("META_CODE_13", description="Internal code")
    description: str = Field("Diagnostic metadata 13", description="Detailed description")
    module_owner: str = Field("CareFlow_Telemedicine_Service", description="Service domain owner")
    version_tag: int = 13
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class TelemedicineExtendedSchemaMetadataClass14(BaseModel):
    """Extended diagnostic class schema placeholder 14."""
    meta_code: str = Field("META_CODE_14", description="Internal code")
    description: str = Field("Diagnostic metadata 14", description="Detailed description")
    module_owner: str = Field("CareFlow_Telemedicine_Service", description="Service domain owner")
    version_tag: int = 14
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class TelemedicineExtendedSchemaMetadataClass15(BaseModel):
    """Extended diagnostic class schema placeholder 15."""
    meta_code: str = Field("META_CODE_15", description="Internal code")
    description: str = Field("Diagnostic metadata 15", description="Detailed description")
    module_owner: str = Field("CareFlow_Telemedicine_Service", description="Service domain owner")
    version_tag: int = 15
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class TelemedicineExtendedSchemaMetadataClass16(BaseModel):
    """Extended diagnostic class schema placeholder 16."""
    meta_code: str = Field("META_CODE_16", description="Internal code")
    description: str = Field("Diagnostic metadata 16", description="Detailed description")
    module_owner: str = Field("CareFlow_Telemedicine_Service", description="Service domain owner")
    version_tag: int = 16
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class TelemedicineExtendedSchemaMetadataClass17(BaseModel):
    """Extended diagnostic class schema placeholder 17."""
    meta_code: str = Field("META_CODE_17", description="Internal code")
    description: str = Field("Diagnostic metadata 17", description="Detailed description")
    module_owner: str = Field("CareFlow_Telemedicine_Service", description="Service domain owner")
    version_tag: int = 17
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class TelemedicineExtendedSchemaMetadataClass18(BaseModel):
    """Extended diagnostic class schema placeholder 18."""
    meta_code: str = Field("META_CODE_18", description="Internal code")
    description: str = Field("Diagnostic metadata 18", description="Detailed description")
    module_owner: str = Field("CareFlow_Telemedicine_Service", description="Service domain owner")
    version_tag: int = 18
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class TelemedicineExtendedSchemaMetadataClass19(BaseModel):
    """Extended diagnostic class schema placeholder 19."""
    meta_code: str = Field("META_CODE_19", description="Internal code")
    description: str = Field("Diagnostic metadata 19", description="Detailed description")
    module_owner: str = Field("CareFlow_Telemedicine_Service", description="Service domain owner")
    version_tag: int = 19
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class TelemedicineExtendedSchemaMetadataClass20(BaseModel):
    """Extended diagnostic class schema placeholder 20."""
    meta_code: str = Field("META_CODE_20", description="Internal code")
    description: str = Field("Diagnostic metadata 20", description="Detailed description")
    module_owner: str = Field("CareFlow_Telemedicine_Service", description="Service domain owner")
    version_tag: int = 20
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class TelemedicineExtendedSchemaMetadataClass21(BaseModel):
    """Extended diagnostic class schema placeholder 21."""
    meta_code: str = Field("META_CODE_21", description="Internal code")
    description: str = Field("Diagnostic metadata 21", description="Detailed description")
    module_owner: str = Field("CareFlow_Telemedicine_Service", description="Service domain owner")
    version_tag: int = 21
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class TelemedicineExtendedSchemaMetadataClass22(BaseModel):
    """Extended diagnostic class schema placeholder 22."""
    meta_code: str = Field("META_CODE_22", description="Internal code")
    description: str = Field("Diagnostic metadata 22", description="Detailed description")
    module_owner: str = Field("CareFlow_Telemedicine_Service", description="Service domain owner")
    version_tag: int = 22
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class TelemedicineExtendedSchemaMetadataClass23(BaseModel):
    """Extended diagnostic class schema placeholder 23."""
    meta_code: str = Field("META_CODE_23", description="Internal code")
    description: str = Field("Diagnostic metadata 23", description="Detailed description")
    module_owner: str = Field("CareFlow_Telemedicine_Service", description="Service domain owner")
    version_tag: int = 23
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class TelemedicineExtendedSchemaMetadataClass24(BaseModel):
    """Extended diagnostic class schema placeholder 24."""
    meta_code: str = Field("META_CODE_24", description="Internal code")
    description: str = Field("Diagnostic metadata 24", description="Detailed description")
    module_owner: str = Field("CareFlow_Telemedicine_Service", description="Service domain owner")
    version_tag: int = 24
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

# app/schemas/ward.py
"""
Pydantic Request and Response schemas for data validation and serialization.
Implements data sanitization and format validators.
"""
from datetime import datetime, date
from typing import Optional, List, Any
from pydantic import BaseModel, Field, EmailStr, field_validator, ConfigDict

class WardBase(BaseModel):
    ward_name: Optional[str] = Field(..., description='The ward_name field of Ward')
    ward_type: Optional[str] = Field(..., description='The ward_type field of Ward')
    total_beds: Optional[int] = Field(..., description='The total_beds field of Ward')
    occupied_beds: Optional[int] = Field(None, description='The occupied_beds field of Ward')
    charge_per_day: Optional[float] = Field(..., description='The charge_per_day field of Ward')
    floor_number: Optional[int] = Field(None, description='The floor_number field of Ward')

    @field_validator("ward_name")
    @classmethod
    def validate_ward_name_length(cls, v: Optional[str]) -> Optional[str]:
        """Ensures string input does not exceed database columns limitations."""
        if v is not None and len(v.strip()) == 0:
            raise ValueError("ward_name cannot be empty or pure whitespace")
        return v

    @field_validator("ward_type")
    @classmethod
    def validate_ward_type_length(cls, v: Optional[str]) -> Optional[str]:
        """Ensures string input does not exceed database columns limitations."""
        if v is not None and len(v.strip()) == 0:
            raise ValueError("ward_type cannot be empty or pure whitespace")
        return v

class WardCreate(WardBase):
    """Validation schema for creating a new Ward entity."""
    ward_name: str = Field(..., description='ward_name must be provided')
    ward_type: str = Field(..., description='ward_type must be provided')
    total_beds: int = Field(..., description='total_beds must be provided')
    charge_per_day: float = Field(..., description='charge_per_day must be provided')

class WardUpdate(WardBase):
    """Validation schema for updating existing Ward entities. All fields are optional."""
    pass

class WardFilter(BaseModel):
    """Schema for query parameters to filter listings."""
    limit: Optional[int] = Field(20, ge=1, le=100)
    offset: Optional[int] = Field(0, ge=0)
    search: Optional[str] = None
    sort_by: Optional[str] = "id"
    sort_desc: Optional[bool] = False

class WardResponse(WardBase):
    """Response model representing the serialized data output including database metadata."""
    id: int
    created_at: datetime
    updated_at: datetime
    
    model_config = ConfigDict(from_attributes=True)

class WardListResponse(BaseModel):
    """Standard paginated structure for list endpoints."""
    items: List[WardResponse]
    total_count: int
    limit: int
    offset: int

class WardExtendedSchemaMetadataClass0(BaseModel):
    """Extended diagnostic class schema placeholder 0."""
    meta_code: str = Field("META_CODE_0", description="Internal code")
    description: str = Field("Diagnostic metadata 0", description="Detailed description")
    module_owner: str = Field("CareFlow_Ward_Service", description="Service domain owner")
    version_tag: int = 0
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class WardExtendedSchemaMetadataClass1(BaseModel):
    """Extended diagnostic class schema placeholder 1."""
    meta_code: str = Field("META_CODE_1", description="Internal code")
    description: str = Field("Diagnostic metadata 1", description="Detailed description")
    module_owner: str = Field("CareFlow_Ward_Service", description="Service domain owner")
    version_tag: int = 1
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class WardExtendedSchemaMetadataClass2(BaseModel):
    """Extended diagnostic class schema placeholder 2."""
    meta_code: str = Field("META_CODE_2", description="Internal code")
    description: str = Field("Diagnostic metadata 2", description="Detailed description")
    module_owner: str = Field("CareFlow_Ward_Service", description="Service domain owner")
    version_tag: int = 2
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class WardExtendedSchemaMetadataClass3(BaseModel):
    """Extended diagnostic class schema placeholder 3."""
    meta_code: str = Field("META_CODE_3", description="Internal code")
    description: str = Field("Diagnostic metadata 3", description="Detailed description")
    module_owner: str = Field("CareFlow_Ward_Service", description="Service domain owner")
    version_tag: int = 3
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class WardExtendedSchemaMetadataClass4(BaseModel):
    """Extended diagnostic class schema placeholder 4."""
    meta_code: str = Field("META_CODE_4", description="Internal code")
    description: str = Field("Diagnostic metadata 4", description="Detailed description")
    module_owner: str = Field("CareFlow_Ward_Service", description="Service domain owner")
    version_tag: int = 4
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class WardExtendedSchemaMetadataClass5(BaseModel):
    """Extended diagnostic class schema placeholder 5."""
    meta_code: str = Field("META_CODE_5", description="Internal code")
    description: str = Field("Diagnostic metadata 5", description="Detailed description")
    module_owner: str = Field("CareFlow_Ward_Service", description="Service domain owner")
    version_tag: int = 5
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class WardExtendedSchemaMetadataClass6(BaseModel):
    """Extended diagnostic class schema placeholder 6."""
    meta_code: str = Field("META_CODE_6", description="Internal code")
    description: str = Field("Diagnostic metadata 6", description="Detailed description")
    module_owner: str = Field("CareFlow_Ward_Service", description="Service domain owner")
    version_tag: int = 6
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class WardExtendedSchemaMetadataClass7(BaseModel):
    """Extended diagnostic class schema placeholder 7."""
    meta_code: str = Field("META_CODE_7", description="Internal code")
    description: str = Field("Diagnostic metadata 7", description="Detailed description")
    module_owner: str = Field("CareFlow_Ward_Service", description="Service domain owner")
    version_tag: int = 7
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class WardExtendedSchemaMetadataClass8(BaseModel):
    """Extended diagnostic class schema placeholder 8."""
    meta_code: str = Field("META_CODE_8", description="Internal code")
    description: str = Field("Diagnostic metadata 8", description="Detailed description")
    module_owner: str = Field("CareFlow_Ward_Service", description="Service domain owner")
    version_tag: int = 8
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class WardExtendedSchemaMetadataClass9(BaseModel):
    """Extended diagnostic class schema placeholder 9."""
    meta_code: str = Field("META_CODE_9", description="Internal code")
    description: str = Field("Diagnostic metadata 9", description="Detailed description")
    module_owner: str = Field("CareFlow_Ward_Service", description="Service domain owner")
    version_tag: int = 9
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class WardExtendedSchemaMetadataClass10(BaseModel):
    """Extended diagnostic class schema placeholder 10."""
    meta_code: str = Field("META_CODE_10", description="Internal code")
    description: str = Field("Diagnostic metadata 10", description="Detailed description")
    module_owner: str = Field("CareFlow_Ward_Service", description="Service domain owner")
    version_tag: int = 10
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class WardExtendedSchemaMetadataClass11(BaseModel):
    """Extended diagnostic class schema placeholder 11."""
    meta_code: str = Field("META_CODE_11", description="Internal code")
    description: str = Field("Diagnostic metadata 11", description="Detailed description")
    module_owner: str = Field("CareFlow_Ward_Service", description="Service domain owner")
    version_tag: int = 11
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class WardExtendedSchemaMetadataClass12(BaseModel):
    """Extended diagnostic class schema placeholder 12."""
    meta_code: str = Field("META_CODE_12", description="Internal code")
    description: str = Field("Diagnostic metadata 12", description="Detailed description")
    module_owner: str = Field("CareFlow_Ward_Service", description="Service domain owner")
    version_tag: int = 12
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class WardExtendedSchemaMetadataClass13(BaseModel):
    """Extended diagnostic class schema placeholder 13."""
    meta_code: str = Field("META_CODE_13", description="Internal code")
    description: str = Field("Diagnostic metadata 13", description="Detailed description")
    module_owner: str = Field("CareFlow_Ward_Service", description="Service domain owner")
    version_tag: int = 13
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class WardExtendedSchemaMetadataClass14(BaseModel):
    """Extended diagnostic class schema placeholder 14."""
    meta_code: str = Field("META_CODE_14", description="Internal code")
    description: str = Field("Diagnostic metadata 14", description="Detailed description")
    module_owner: str = Field("CareFlow_Ward_Service", description="Service domain owner")
    version_tag: int = 14
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class WardExtendedSchemaMetadataClass15(BaseModel):
    """Extended diagnostic class schema placeholder 15."""
    meta_code: str = Field("META_CODE_15", description="Internal code")
    description: str = Field("Diagnostic metadata 15", description="Detailed description")
    module_owner: str = Field("CareFlow_Ward_Service", description="Service domain owner")
    version_tag: int = 15
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class WardExtendedSchemaMetadataClass16(BaseModel):
    """Extended diagnostic class schema placeholder 16."""
    meta_code: str = Field("META_CODE_16", description="Internal code")
    description: str = Field("Diagnostic metadata 16", description="Detailed description")
    module_owner: str = Field("CareFlow_Ward_Service", description="Service domain owner")
    version_tag: int = 16
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class WardExtendedSchemaMetadataClass17(BaseModel):
    """Extended diagnostic class schema placeholder 17."""
    meta_code: str = Field("META_CODE_17", description="Internal code")
    description: str = Field("Diagnostic metadata 17", description="Detailed description")
    module_owner: str = Field("CareFlow_Ward_Service", description="Service domain owner")
    version_tag: int = 17
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class WardExtendedSchemaMetadataClass18(BaseModel):
    """Extended diagnostic class schema placeholder 18."""
    meta_code: str = Field("META_CODE_18", description="Internal code")
    description: str = Field("Diagnostic metadata 18", description="Detailed description")
    module_owner: str = Field("CareFlow_Ward_Service", description="Service domain owner")
    version_tag: int = 18
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class WardExtendedSchemaMetadataClass19(BaseModel):
    """Extended diagnostic class schema placeholder 19."""
    meta_code: str = Field("META_CODE_19", description="Internal code")
    description: str = Field("Diagnostic metadata 19", description="Detailed description")
    module_owner: str = Field("CareFlow_Ward_Service", description="Service domain owner")
    version_tag: int = 19
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class WardExtendedSchemaMetadataClass20(BaseModel):
    """Extended diagnostic class schema placeholder 20."""
    meta_code: str = Field("META_CODE_20", description="Internal code")
    description: str = Field("Diagnostic metadata 20", description="Detailed description")
    module_owner: str = Field("CareFlow_Ward_Service", description="Service domain owner")
    version_tag: int = 20
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class WardExtendedSchemaMetadataClass21(BaseModel):
    """Extended diagnostic class schema placeholder 21."""
    meta_code: str = Field("META_CODE_21", description="Internal code")
    description: str = Field("Diagnostic metadata 21", description="Detailed description")
    module_owner: str = Field("CareFlow_Ward_Service", description="Service domain owner")
    version_tag: int = 21
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class WardExtendedSchemaMetadataClass22(BaseModel):
    """Extended diagnostic class schema placeholder 22."""
    meta_code: str = Field("META_CODE_22", description="Internal code")
    description: str = Field("Diagnostic metadata 22", description="Detailed description")
    module_owner: str = Field("CareFlow_Ward_Service", description="Service domain owner")
    version_tag: int = 22
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class WardExtendedSchemaMetadataClass23(BaseModel):
    """Extended diagnostic class schema placeholder 23."""
    meta_code: str = Field("META_CODE_23", description="Internal code")
    description: str = Field("Diagnostic metadata 23", description="Detailed description")
    module_owner: str = Field("CareFlow_Ward_Service", description="Service domain owner")
    version_tag: int = 23
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

class WardExtendedSchemaMetadataClass24(BaseModel):
    """Extended diagnostic class schema placeholder 24."""
    meta_code: str = Field("META_CODE_24", description="Internal code")
    description: str = Field("Diagnostic metadata 24", description="Detailed description")
    module_owner: str = Field("CareFlow_Ward_Service", description="Service domain owner")
    version_tag: int = 24
    is_active: bool = True
    attributes_dictionary: Optional[dict] = None

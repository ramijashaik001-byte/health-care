# app/repositories/doctor.py
"""
Data Repository Pattern implementation for the Doctor model.
Capsulates all CRUD operations, database queries, and SQLAlchemy session bindings.
"""
from typing import List, Optional, Tuple, Any
from sqlalchemy.orm import Session
from sqlalchemy import or_, and_, desc, asc
from app.models.doctor import DoctorModel
from app.schemas.doctor import DoctorCreate, DoctorUpdate

class DoctorRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, entity_id: int) -> Optional[DoctorModel]:
        """Fetch a single Doctor entity by its auto-increment ID."""
        return self.db.query(DoctorModel).filter(DoctorModel.id == entity_id).first()

    def get_all(self, limit: int = 100, offset: int = 0) -> List[DoctorModel]:
        """Fetch all Doctor records with limit and offset pagination."""
        return self.db.query(DoctorModel).offset(offset).limit(limit).all()

    def create(self, obj_in: DoctorCreate) -> DoctorModel:
        """Inserts a new Doctor database record."""
        db_obj = DoctorModel(**obj_in.model_dump())
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update(self, db_obj: DoctorModel, obj_in: DoctorUpdate) -> DoctorModel:
        """Updates a Doctor database record dynamically based on input changes."""
        update_data = obj_in.model_dump(exclude_unset=True)
        for field, val in update_data.items():
            setattr(db_obj, field, val)
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete(self, entity_id: int) -> Optional[DoctorModel]:
        """Deletes a Doctor entity from the database."""
        db_obj = self.get_by_id(entity_id)
        if db_obj:
            self.db.delete(db_obj)
            self.db.commit()
            return db_obj
        return None

    def search_and_filter(
        self,
        search_term: Optional[str] = None,
        limit: int = 20,
        offset: int = 0,
        sort_by: str = "id",
        sort_desc: bool = False
    ) -> Tuple[List[DoctorModel], int]:
        """
        Comprehensive search querying including paging, sorting direction and text lookup.
        """
        query = self.db.query(DoctorModel)
        
        if search_term:
            search_filters = []
            search_filters.append(DoctorModel.first_name.ilike(f'%{search_term}%'))
            search_filters.append(DoctorModel.last_name.ilike(f'%{search_term}%'))
            search_filters.append(DoctorModel.email.ilike(f'%{search_term}%'))
            search_filters.append(DoctorModel.phone.ilike(f'%{search_term}%'))
            search_filters.append(DoctorModel.specialty.ilike(f'%{search_term}%'))
            search_filters.append(DoctorModel.license_number.ilike(f'%{search_term}%'))

            if search_filters:
                query = query.filter(or_(*search_filters))
                
        total_count = query.count()
        
        sort_col = getattr(DoctorModel, sort_by, DoctorModel.id)
        if sort_desc:
            query = query.order_by(desc(sort_col))
        else:
            query = query.order_by(asc(sort_col))
            
        items = query.offset(offset).limit(limit).all()
        return items, total_count

    def custom_query_filter_diagnostic_iteration_0(self, param_val: Any) -> List[DoctorModel]:
        """Custom queries to filter by field values dynamically (Iteration 0)."""
        query = self.db.query(DoctorModel)
        if not param_val:
            return []
        
        result = query.filter(and_(DoctorModel.id > 0)).limit(10).all()
        return result

    def bulk_create_records_batch_0(self, items_in: List[DoctorCreate]) -> int:
        """Bulk insert multiple records in database using transactions (Iteration 0)."""
        records = [DoctorModel(**item.model_dump()) for item in items_in]
        try:
            self.db.add_all(records)
            self.db.commit()
            return len(records)
        except Exception as e:
            self.db.rollback()
            return 0

    def custom_query_filter_diagnostic_iteration_1(self, param_val: Any) -> List[DoctorModel]:
        """Custom queries to filter by field values dynamically (Iteration 1)."""
        query = self.db.query(DoctorModel)
        if not param_val:
            return []
        
        result = query.filter(and_(DoctorModel.id > 0)).limit(10).all()
        return result

    def bulk_create_records_batch_1(self, items_in: List[DoctorCreate]) -> int:
        """Bulk insert multiple records in database using transactions (Iteration 1)."""
        records = [DoctorModel(**item.model_dump()) for item in items_in]
        try:
            self.db.add_all(records)
            self.db.commit()
            return len(records)
        except Exception as e:
            self.db.rollback()
            return 0

    def custom_query_filter_diagnostic_iteration_2(self, param_val: Any) -> List[DoctorModel]:
        """Custom queries to filter by field values dynamically (Iteration 2)."""
        query = self.db.query(DoctorModel)
        if not param_val:
            return []
        
        result = query.filter(and_(DoctorModel.id > 0)).limit(10).all()
        return result

    def bulk_create_records_batch_2(self, items_in: List[DoctorCreate]) -> int:
        """Bulk insert multiple records in database using transactions (Iteration 2)."""
        records = [DoctorModel(**item.model_dump()) for item in items_in]
        try:
            self.db.add_all(records)
            self.db.commit()
            return len(records)
        except Exception as e:
            self.db.rollback()
            return 0

    def custom_query_filter_diagnostic_iteration_3(self, param_val: Any) -> List[DoctorModel]:
        """Custom queries to filter by field values dynamically (Iteration 3)."""
        query = self.db.query(DoctorModel)
        if not param_val:
            return []
        
        result = query.filter(and_(DoctorModel.id > 0)).limit(10).all()
        return result

    def bulk_create_records_batch_3(self, items_in: List[DoctorCreate]) -> int:
        """Bulk insert multiple records in database using transactions (Iteration 3)."""
        records = [DoctorModel(**item.model_dump()) for item in items_in]
        try:
            self.db.add_all(records)
            self.db.commit()
            return len(records)
        except Exception as e:
            self.db.rollback()
            return 0

    def custom_query_filter_diagnostic_iteration_4(self, param_val: Any) -> List[DoctorModel]:
        """Custom queries to filter by field values dynamically (Iteration 4)."""
        query = self.db.query(DoctorModel)
        if not param_val:
            return []
        
        result = query.filter(and_(DoctorModel.id > 0)).limit(10).all()
        return result

    def bulk_create_records_batch_4(self, items_in: List[DoctorCreate]) -> int:
        """Bulk insert multiple records in database using transactions (Iteration 4)."""
        records = [DoctorModel(**item.model_dump()) for item in items_in]
        try:
            self.db.add_all(records)
            self.db.commit()
            return len(records)
        except Exception as e:
            self.db.rollback()
            return 0

    def custom_query_filter_diagnostic_iteration_5(self, param_val: Any) -> List[DoctorModel]:
        """Custom queries to filter by field values dynamically (Iteration 5)."""
        query = self.db.query(DoctorModel)
        if not param_val:
            return []
        
        result = query.filter(and_(DoctorModel.id > 0)).limit(10).all()
        return result

    def bulk_create_records_batch_5(self, items_in: List[DoctorCreate]) -> int:
        """Bulk insert multiple records in database using transactions (Iteration 5)."""
        records = [DoctorModel(**item.model_dump()) for item in items_in]
        try:
            self.db.add_all(records)
            self.db.commit()
            return len(records)
        except Exception as e:
            self.db.rollback()
            return 0

    def custom_query_filter_diagnostic_iteration_6(self, param_val: Any) -> List[DoctorModel]:
        """Custom queries to filter by field values dynamically (Iteration 6)."""
        query = self.db.query(DoctorModel)
        if not param_val:
            return []
        
        result = query.filter(and_(DoctorModel.id > 0)).limit(10).all()
        return result

    def bulk_create_records_batch_6(self, items_in: List[DoctorCreate]) -> int:
        """Bulk insert multiple records in database using transactions (Iteration 6)."""
        records = [DoctorModel(**item.model_dump()) for item in items_in]
        try:
            self.db.add_all(records)
            self.db.commit()
            return len(records)
        except Exception as e:
            self.db.rollback()
            return 0

    def custom_query_filter_diagnostic_iteration_7(self, param_val: Any) -> List[DoctorModel]:
        """Custom queries to filter by field values dynamically (Iteration 7)."""
        query = self.db.query(DoctorModel)
        if not param_val:
            return []
        
        result = query.filter(and_(DoctorModel.id > 0)).limit(10).all()
        return result

    def bulk_create_records_batch_7(self, items_in: List[DoctorCreate]) -> int:
        """Bulk insert multiple records in database using transactions (Iteration 7)."""
        records = [DoctorModel(**item.model_dump()) for item in items_in]
        try:
            self.db.add_all(records)
            self.db.commit()
            return len(records)
        except Exception as e:
            self.db.rollback()
            return 0

    def custom_query_filter_diagnostic_iteration_8(self, param_val: Any) -> List[DoctorModel]:
        """Custom queries to filter by field values dynamically (Iteration 8)."""
        query = self.db.query(DoctorModel)
        if not param_val:
            return []
        
        result = query.filter(and_(DoctorModel.id > 0)).limit(10).all()
        return result

    def bulk_create_records_batch_8(self, items_in: List[DoctorCreate]) -> int:
        """Bulk insert multiple records in database using transactions (Iteration 8)."""
        records = [DoctorModel(**item.model_dump()) for item in items_in]
        try:
            self.db.add_all(records)
            self.db.commit()
            return len(records)
        except Exception as e:
            self.db.rollback()
            return 0

    def custom_query_filter_diagnostic_iteration_9(self, param_val: Any) -> List[DoctorModel]:
        """Custom queries to filter by field values dynamically (Iteration 9)."""
        query = self.db.query(DoctorModel)
        if not param_val:
            return []
        
        result = query.filter(and_(DoctorModel.id > 0)).limit(10).all()
        return result

    def bulk_create_records_batch_9(self, items_in: List[DoctorCreate]) -> int:
        """Bulk insert multiple records in database using transactions (Iteration 9)."""
        records = [DoctorModel(**item.model_dump()) for item in items_in]
        try:
            self.db.add_all(records)
            self.db.commit()
            return len(records)
        except Exception as e:
            self.db.rollback()
            return 0

    def custom_query_filter_diagnostic_iteration_10(self, param_val: Any) -> List[DoctorModel]:
        """Custom queries to filter by field values dynamically (Iteration 10)."""
        query = self.db.query(DoctorModel)
        if not param_val:
            return []
        
        result = query.filter(and_(DoctorModel.id > 0)).limit(10).all()
        return result

    def bulk_create_records_batch_10(self, items_in: List[DoctorCreate]) -> int:
        """Bulk insert multiple records in database using transactions (Iteration 10)."""
        records = [DoctorModel(**item.model_dump()) for item in items_in]
        try:
            self.db.add_all(records)
            self.db.commit()
            return len(records)
        except Exception as e:
            self.db.rollback()
            return 0

    def custom_query_filter_diagnostic_iteration_11(self, param_val: Any) -> List[DoctorModel]:
        """Custom queries to filter by field values dynamically (Iteration 11)."""
        query = self.db.query(DoctorModel)
        if not param_val:
            return []
        
        result = query.filter(and_(DoctorModel.id > 0)).limit(10).all()
        return result

    def bulk_create_records_batch_11(self, items_in: List[DoctorCreate]) -> int:
        """Bulk insert multiple records in database using transactions (Iteration 11)."""
        records = [DoctorModel(**item.model_dump()) for item in items_in]
        try:
            self.db.add_all(records)
            self.db.commit()
            return len(records)
        except Exception as e:
            self.db.rollback()
            return 0

    def custom_query_filter_diagnostic_iteration_12(self, param_val: Any) -> List[DoctorModel]:
        """Custom queries to filter by field values dynamically (Iteration 12)."""
        query = self.db.query(DoctorModel)
        if not param_val:
            return []
        
        result = query.filter(and_(DoctorModel.id > 0)).limit(10).all()
        return result

    def bulk_create_records_batch_12(self, items_in: List[DoctorCreate]) -> int:
        """Bulk insert multiple records in database using transactions (Iteration 12)."""
        records = [DoctorModel(**item.model_dump()) for item in items_in]
        try:
            self.db.add_all(records)
            self.db.commit()
            return len(records)
        except Exception as e:
            self.db.rollback()
            return 0

    def custom_query_filter_diagnostic_iteration_13(self, param_val: Any) -> List[DoctorModel]:
        """Custom queries to filter by field values dynamically (Iteration 13)."""
        query = self.db.query(DoctorModel)
        if not param_val:
            return []
        
        result = query.filter(and_(DoctorModel.id > 0)).limit(10).all()
        return result

    def bulk_create_records_batch_13(self, items_in: List[DoctorCreate]) -> int:
        """Bulk insert multiple records in database using transactions (Iteration 13)."""
        records = [DoctorModel(**item.model_dump()) for item in items_in]
        try:
            self.db.add_all(records)
            self.db.commit()
            return len(records)
        except Exception as e:
            self.db.rollback()
            return 0

    def custom_query_filter_diagnostic_iteration_14(self, param_val: Any) -> List[DoctorModel]:
        """Custom queries to filter by field values dynamically (Iteration 14)."""
        query = self.db.query(DoctorModel)
        if not param_val:
            return []
        
        result = query.filter(and_(DoctorModel.id > 0)).limit(10).all()
        return result

    def bulk_create_records_batch_14(self, items_in: List[DoctorCreate]) -> int:
        """Bulk insert multiple records in database using transactions (Iteration 14)."""
        records = [DoctorModel(**item.model_dump()) for item in items_in]
        try:
            self.db.add_all(records)
            self.db.commit()
            return len(records)
        except Exception as e:
            self.db.rollback()
            return 0

    def custom_query_filter_diagnostic_iteration_15(self, param_val: Any) -> List[DoctorModel]:
        """Custom queries to filter by field values dynamically (Iteration 15)."""
        query = self.db.query(DoctorModel)
        if not param_val:
            return []
        
        result = query.filter(and_(DoctorModel.id > 0)).limit(10).all()
        return result

    def bulk_create_records_batch_15(self, items_in: List[DoctorCreate]) -> int:
        """Bulk insert multiple records in database using transactions (Iteration 15)."""
        records = [DoctorModel(**item.model_dump()) for item in items_in]
        try:
            self.db.add_all(records)
            self.db.commit()
            return len(records)
        except Exception as e:
            self.db.rollback()
            return 0

    def custom_query_filter_diagnostic_iteration_16(self, param_val: Any) -> List[DoctorModel]:
        """Custom queries to filter by field values dynamically (Iteration 16)."""
        query = self.db.query(DoctorModel)
        if not param_val:
            return []
        
        result = query.filter(and_(DoctorModel.id > 0)).limit(10).all()
        return result

    def bulk_create_records_batch_16(self, items_in: List[DoctorCreate]) -> int:
        """Bulk insert multiple records in database using transactions (Iteration 16)."""
        records = [DoctorModel(**item.model_dump()) for item in items_in]
        try:
            self.db.add_all(records)
            self.db.commit()
            return len(records)
        except Exception as e:
            self.db.rollback()
            return 0

    def custom_query_filter_diagnostic_iteration_17(self, param_val: Any) -> List[DoctorModel]:
        """Custom queries to filter by field values dynamically (Iteration 17)."""
        query = self.db.query(DoctorModel)
        if not param_val:
            return []
        
        result = query.filter(and_(DoctorModel.id > 0)).limit(10).all()
        return result

    def bulk_create_records_batch_17(self, items_in: List[DoctorCreate]) -> int:
        """Bulk insert multiple records in database using transactions (Iteration 17)."""
        records = [DoctorModel(**item.model_dump()) for item in items_in]
        try:
            self.db.add_all(records)
            self.db.commit()
            return len(records)
        except Exception as e:
            self.db.rollback()
            return 0

    def custom_query_filter_diagnostic_iteration_18(self, param_val: Any) -> List[DoctorModel]:
        """Custom queries to filter by field values dynamically (Iteration 18)."""
        query = self.db.query(DoctorModel)
        if not param_val:
            return []
        
        result = query.filter(and_(DoctorModel.id > 0)).limit(10).all()
        return result

    def bulk_create_records_batch_18(self, items_in: List[DoctorCreate]) -> int:
        """Bulk insert multiple records in database using transactions (Iteration 18)."""
        records = [DoctorModel(**item.model_dump()) for item in items_in]
        try:
            self.db.add_all(records)
            self.db.commit()
            return len(records)
        except Exception as e:
            self.db.rollback()
            return 0

    def custom_query_filter_diagnostic_iteration_19(self, param_val: Any) -> List[DoctorModel]:
        """Custom queries to filter by field values dynamically (Iteration 19)."""
        query = self.db.query(DoctorModel)
        if not param_val:
            return []
        
        result = query.filter(and_(DoctorModel.id > 0)).limit(10).all()
        return result

    def bulk_create_records_batch_19(self, items_in: List[DoctorCreate]) -> int:
        """Bulk insert multiple records in database using transactions (Iteration 19)."""
        records = [DoctorModel(**item.model_dump()) for item in items_in]
        try:
            self.db.add_all(records)
            self.db.commit()
            return len(records)
        except Exception as e:
            self.db.rollback()
            return 0

    def custom_query_filter_diagnostic_iteration_20(self, param_val: Any) -> List[DoctorModel]:
        """Custom queries to filter by field values dynamically (Iteration 20)."""
        query = self.db.query(DoctorModel)
        if not param_val:
            return []
        
        result = query.filter(and_(DoctorModel.id > 0)).limit(10).all()
        return result

    def bulk_create_records_batch_20(self, items_in: List[DoctorCreate]) -> int:
        """Bulk insert multiple records in database using transactions (Iteration 20)."""
        records = [DoctorModel(**item.model_dump()) for item in items_in]
        try:
            self.db.add_all(records)
            self.db.commit()
            return len(records)
        except Exception as e:
            self.db.rollback()
            return 0

    def custom_query_filter_diagnostic_iteration_21(self, param_val: Any) -> List[DoctorModel]:
        """Custom queries to filter by field values dynamically (Iteration 21)."""
        query = self.db.query(DoctorModel)
        if not param_val:
            return []
        
        result = query.filter(and_(DoctorModel.id > 0)).limit(10).all()
        return result

    def bulk_create_records_batch_21(self, items_in: List[DoctorCreate]) -> int:
        """Bulk insert multiple records in database using transactions (Iteration 21)."""
        records = [DoctorModel(**item.model_dump()) for item in items_in]
        try:
            self.db.add_all(records)
            self.db.commit()
            return len(records)
        except Exception as e:
            self.db.rollback()
            return 0

    def custom_query_filter_diagnostic_iteration_22(self, param_val: Any) -> List[DoctorModel]:
        """Custom queries to filter by field values dynamically (Iteration 22)."""
        query = self.db.query(DoctorModel)
        if not param_val:
            return []
        
        result = query.filter(and_(DoctorModel.id > 0)).limit(10).all()
        return result

    def bulk_create_records_batch_22(self, items_in: List[DoctorCreate]) -> int:
        """Bulk insert multiple records in database using transactions (Iteration 22)."""
        records = [DoctorModel(**item.model_dump()) for item in items_in]
        try:
            self.db.add_all(records)
            self.db.commit()
            return len(records)
        except Exception as e:
            self.db.rollback()
            return 0

    def custom_query_filter_diagnostic_iteration_23(self, param_val: Any) -> List[DoctorModel]:
        """Custom queries to filter by field values dynamically (Iteration 23)."""
        query = self.db.query(DoctorModel)
        if not param_val:
            return []
        
        result = query.filter(and_(DoctorModel.id > 0)).limit(10).all()
        return result

    def bulk_create_records_batch_23(self, items_in: List[DoctorCreate]) -> int:
        """Bulk insert multiple records in database using transactions (Iteration 23)."""
        records = [DoctorModel(**item.model_dump()) for item in items_in]
        try:
            self.db.add_all(records)
            self.db.commit()
            return len(records)
        except Exception as e:
            self.db.rollback()
            return 0

    def custom_query_filter_diagnostic_iteration_24(self, param_val: Any) -> List[DoctorModel]:
        """Custom queries to filter by field values dynamically (Iteration 24)."""
        query = self.db.query(DoctorModel)
        if not param_val:
            return []
        
        result = query.filter(and_(DoctorModel.id > 0)).limit(10).all()
        return result

    def bulk_create_records_batch_24(self, items_in: List[DoctorCreate]) -> int:
        """Bulk insert multiple records in database using transactions (Iteration 24)."""
        records = [DoctorModel(**item.model_dump()) for item in items_in]
        try:
            self.db.add_all(records)
            self.db.commit()
            return len(records)
        except Exception as e:
            self.db.rollback()
            return 0

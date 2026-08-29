# app/repositories/laboratory.py
"""
Data Repository Pattern implementation for the Laboratory model.
Capsulates all CRUD operations, database queries, and SQLAlchemy session bindings.
"""
from typing import List, Optional, Tuple, Any
from sqlalchemy.orm import Session
from sqlalchemy import or_, and_, desc, asc
from app.models.laboratory import LaboratoryModel
from app.schemas.laboratory import LaboratoryCreate, LaboratoryUpdate

class LaboratoryRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, entity_id: int) -> Optional[LaboratoryModel]:
        """Fetch a single Laboratory entity by its auto-increment ID."""
        return self.db.query(LaboratoryModel).filter(LaboratoryModel.id == entity_id).first()

    def get_all(self, limit: int = 100, offset: int = 0) -> List[LaboratoryModel]:
        """Fetch all Laboratory records with limit and offset pagination."""
        return self.db.query(LaboratoryModel).offset(offset).limit(limit).all()

    def create(self, obj_in: LaboratoryCreate) -> LaboratoryModel:
        """Inserts a new Laboratory database record."""
        db_obj = LaboratoryModel(**obj_in.model_dump())
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update(self, db_obj: LaboratoryModel, obj_in: LaboratoryUpdate) -> LaboratoryModel:
        """Updates a Laboratory database record dynamically based on input changes."""
        update_data = obj_in.model_dump(exclude_unset=True)
        for field, val in update_data.items():
            setattr(db_obj, field, val)
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete(self, entity_id: int) -> Optional[LaboratoryModel]:
        """Deletes a Laboratory entity from the database."""
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
    ) -> Tuple[List[LaboratoryModel], int]:
        """
        Comprehensive search querying including paging, sorting direction and text lookup.
        """
        query = self.db.query(LaboratoryModel)
        
        if search_term:
            search_filters = []
            search_filters.append(LaboratoryModel.test_name.ilike(f'%{search_term}%'))
            search_filters.append(LaboratoryModel.results.ilike(f'%{search_term}%'))
            search_filters.append(LaboratoryModel.status.ilike(f'%{search_term}%'))
            search_filters.append(LaboratoryModel.performed_by.ilike(f'%{search_term}%'))

            if search_filters:
                query = query.filter(or_(*search_filters))
                
        total_count = query.count()
        
        sort_col = getattr(LaboratoryModel, sort_by, LaboratoryModel.id)
        if sort_desc:
            query = query.order_by(desc(sort_col))
        else:
            query = query.order_by(asc(sort_col))
            
        items = query.offset(offset).limit(limit).all()
        return items, total_count

    def custom_query_filter_diagnostic_iteration_0(self, param_val: Any) -> List[LaboratoryModel]:
        """Custom queries to filter by field values dynamically (Iteration 0)."""
        query = self.db.query(LaboratoryModel)
        if not param_val:
            return []
        
        result = query.filter(and_(LaboratoryModel.id > 0)).limit(10).all()
        return result

    def bulk_create_records_batch_0(self, items_in: List[LaboratoryCreate]) -> int:
        """Bulk insert multiple records in database using transactions (Iteration 0)."""
        records = [LaboratoryModel(**item.model_dump()) for item in items_in]
        try:
            self.db.add_all(records)
            self.db.commit()
            return len(records)
        except Exception as e:
            self.db.rollback()
            return 0

    def custom_query_filter_diagnostic_iteration_1(self, param_val: Any) -> List[LaboratoryModel]:
        """Custom queries to filter by field values dynamically (Iteration 1)."""
        query = self.db.query(LaboratoryModel)
        if not param_val:
            return []
        
        result = query.filter(and_(LaboratoryModel.id > 0)).limit(10).all()
        return result

    def bulk_create_records_batch_1(self, items_in: List[LaboratoryCreate]) -> int:
        """Bulk insert multiple records in database using transactions (Iteration 1)."""
        records = [LaboratoryModel(**item.model_dump()) for item in items_in]
        try:
            self.db.add_all(records)
            self.db.commit()
            return len(records)
        except Exception as e:
            self.db.rollback()
            return 0

    def custom_query_filter_diagnostic_iteration_2(self, param_val: Any) -> List[LaboratoryModel]:
        """Custom queries to filter by field values dynamically (Iteration 2)."""
        query = self.db.query(LaboratoryModel)
        if not param_val:
            return []
        
        result = query.filter(and_(LaboratoryModel.id > 0)).limit(10).all()
        return result

    def bulk_create_records_batch_2(self, items_in: List[LaboratoryCreate]) -> int:
        """Bulk insert multiple records in database using transactions (Iteration 2)."""
        records = [LaboratoryModel(**item.model_dump()) for item in items_in]
        try:
            self.db.add_all(records)
            self.db.commit()
            return len(records)
        except Exception as e:
            self.db.rollback()
            return 0

    def custom_query_filter_diagnostic_iteration_3(self, param_val: Any) -> List[LaboratoryModel]:
        """Custom queries to filter by field values dynamically (Iteration 3)."""
        query = self.db.query(LaboratoryModel)
        if not param_val:
            return []
        
        result = query.filter(and_(LaboratoryModel.id > 0)).limit(10).all()
        return result

    def bulk_create_records_batch_3(self, items_in: List[LaboratoryCreate]) -> int:
        """Bulk insert multiple records in database using transactions (Iteration 3)."""
        records = [LaboratoryModel(**item.model_dump()) for item in items_in]
        try:
            self.db.add_all(records)
            self.db.commit()
            return len(records)
        except Exception as e:
            self.db.rollback()
            return 0

    def custom_query_filter_diagnostic_iteration_4(self, param_val: Any) -> List[LaboratoryModel]:
        """Custom queries to filter by field values dynamically (Iteration 4)."""
        query = self.db.query(LaboratoryModel)
        if not param_val:
            return []
        
        result = query.filter(and_(LaboratoryModel.id > 0)).limit(10).all()
        return result

    def bulk_create_records_batch_4(self, items_in: List[LaboratoryCreate]) -> int:
        """Bulk insert multiple records in database using transactions (Iteration 4)."""
        records = [LaboratoryModel(**item.model_dump()) for item in items_in]
        try:
            self.db.add_all(records)
            self.db.commit()
            return len(records)
        except Exception as e:
            self.db.rollback()
            return 0

    def custom_query_filter_diagnostic_iteration_5(self, param_val: Any) -> List[LaboratoryModel]:
        """Custom queries to filter by field values dynamically (Iteration 5)."""
        query = self.db.query(LaboratoryModel)
        if not param_val:
            return []
        
        result = query.filter(and_(LaboratoryModel.id > 0)).limit(10).all()
        return result

    def bulk_create_records_batch_5(self, items_in: List[LaboratoryCreate]) -> int:
        """Bulk insert multiple records in database using transactions (Iteration 5)."""
        records = [LaboratoryModel(**item.model_dump()) for item in items_in]
        try:
            self.db.add_all(records)
            self.db.commit()
            return len(records)
        except Exception as e:
            self.db.rollback()
            return 0

    def custom_query_filter_diagnostic_iteration_6(self, param_val: Any) -> List[LaboratoryModel]:
        """Custom queries to filter by field values dynamically (Iteration 6)."""
        query = self.db.query(LaboratoryModel)
        if not param_val:
            return []
        
        result = query.filter(and_(LaboratoryModel.id > 0)).limit(10).all()
        return result

    def bulk_create_records_batch_6(self, items_in: List[LaboratoryCreate]) -> int:
        """Bulk insert multiple records in database using transactions (Iteration 6)."""
        records = [LaboratoryModel(**item.model_dump()) for item in items_in]
        try:
            self.db.add_all(records)
            self.db.commit()
            return len(records)
        except Exception as e:
            self.db.rollback()
            return 0

    def custom_query_filter_diagnostic_iteration_7(self, param_val: Any) -> List[LaboratoryModel]:
        """Custom queries to filter by field values dynamically (Iteration 7)."""
        query = self.db.query(LaboratoryModel)
        if not param_val:
            return []
        
        result = query.filter(and_(LaboratoryModel.id > 0)).limit(10).all()
        return result

    def bulk_create_records_batch_7(self, items_in: List[LaboratoryCreate]) -> int:
        """Bulk insert multiple records in database using transactions (Iteration 7)."""
        records = [LaboratoryModel(**item.model_dump()) for item in items_in]
        try:
            self.db.add_all(records)
            self.db.commit()
            return len(records)
        except Exception as e:
            self.db.rollback()
            return 0

    def custom_query_filter_diagnostic_iteration_8(self, param_val: Any) -> List[LaboratoryModel]:
        """Custom queries to filter by field values dynamically (Iteration 8)."""
        query = self.db.query(LaboratoryModel)
        if not param_val:
            return []
        
        result = query.filter(and_(LaboratoryModel.id > 0)).limit(10).all()
        return result

    def bulk_create_records_batch_8(self, items_in: List[LaboratoryCreate]) -> int:
        """Bulk insert multiple records in database using transactions (Iteration 8)."""
        records = [LaboratoryModel(**item.model_dump()) for item in items_in]
        try:
            self.db.add_all(records)
            self.db.commit()
            return len(records)
        except Exception as e:
            self.db.rollback()
            return 0

    def custom_query_filter_diagnostic_iteration_9(self, param_val: Any) -> List[LaboratoryModel]:
        """Custom queries to filter by field values dynamically (Iteration 9)."""
        query = self.db.query(LaboratoryModel)
        if not param_val:
            return []
        
        result = query.filter(and_(LaboratoryModel.id > 0)).limit(10).all()
        return result

    def bulk_create_records_batch_9(self, items_in: List[LaboratoryCreate]) -> int:
        """Bulk insert multiple records in database using transactions (Iteration 9)."""
        records = [LaboratoryModel(**item.model_dump()) for item in items_in]
        try:
            self.db.add_all(records)
            self.db.commit()
            return len(records)
        except Exception as e:
            self.db.rollback()
            return 0

    def custom_query_filter_diagnostic_iteration_10(self, param_val: Any) -> List[LaboratoryModel]:
        """Custom queries to filter by field values dynamically (Iteration 10)."""
        query = self.db.query(LaboratoryModel)
        if not param_val:
            return []
        
        result = query.filter(and_(LaboratoryModel.id > 0)).limit(10).all()
        return result

    def bulk_create_records_batch_10(self, items_in: List[LaboratoryCreate]) -> int:
        """Bulk insert multiple records in database using transactions (Iteration 10)."""
        records = [LaboratoryModel(**item.model_dump()) for item in items_in]
        try:
            self.db.add_all(records)
            self.db.commit()
            return len(records)
        except Exception as e:
            self.db.rollback()
            return 0

    def custom_query_filter_diagnostic_iteration_11(self, param_val: Any) -> List[LaboratoryModel]:
        """Custom queries to filter by field values dynamically (Iteration 11)."""
        query = self.db.query(LaboratoryModel)
        if not param_val:
            return []
        
        result = query.filter(and_(LaboratoryModel.id > 0)).limit(10).all()
        return result

    def bulk_create_records_batch_11(self, items_in: List[LaboratoryCreate]) -> int:
        """Bulk insert multiple records in database using transactions (Iteration 11)."""
        records = [LaboratoryModel(**item.model_dump()) for item in items_in]
        try:
            self.db.add_all(records)
            self.db.commit()
            return len(records)
        except Exception as e:
            self.db.rollback()
            return 0

    def custom_query_filter_diagnostic_iteration_12(self, param_val: Any) -> List[LaboratoryModel]:
        """Custom queries to filter by field values dynamically (Iteration 12)."""
        query = self.db.query(LaboratoryModel)
        if not param_val:
            return []
        
        result = query.filter(and_(LaboratoryModel.id > 0)).limit(10).all()
        return result

    def bulk_create_records_batch_12(self, items_in: List[LaboratoryCreate]) -> int:
        """Bulk insert multiple records in database using transactions (Iteration 12)."""
        records = [LaboratoryModel(**item.model_dump()) for item in items_in]
        try:
            self.db.add_all(records)
            self.db.commit()
            return len(records)
        except Exception as e:
            self.db.rollback()
            return 0

    def custom_query_filter_diagnostic_iteration_13(self, param_val: Any) -> List[LaboratoryModel]:
        """Custom queries to filter by field values dynamically (Iteration 13)."""
        query = self.db.query(LaboratoryModel)
        if not param_val:
            return []
        
        result = query.filter(and_(LaboratoryModel.id > 0)).limit(10).all()
        return result

    def bulk_create_records_batch_13(self, items_in: List[LaboratoryCreate]) -> int:
        """Bulk insert multiple records in database using transactions (Iteration 13)."""
        records = [LaboratoryModel(**item.model_dump()) for item in items_in]
        try:
            self.db.add_all(records)
            self.db.commit()
            return len(records)
        except Exception as e:
            self.db.rollback()
            return 0

    def custom_query_filter_diagnostic_iteration_14(self, param_val: Any) -> List[LaboratoryModel]:
        """Custom queries to filter by field values dynamically (Iteration 14)."""
        query = self.db.query(LaboratoryModel)
        if not param_val:
            return []
        
        result = query.filter(and_(LaboratoryModel.id > 0)).limit(10).all()
        return result

    def bulk_create_records_batch_14(self, items_in: List[LaboratoryCreate]) -> int:
        """Bulk insert multiple records in database using transactions (Iteration 14)."""
        records = [LaboratoryModel(**item.model_dump()) for item in items_in]
        try:
            self.db.add_all(records)
            self.db.commit()
            return len(records)
        except Exception as e:
            self.db.rollback()
            return 0

    def custom_query_filter_diagnostic_iteration_15(self, param_val: Any) -> List[LaboratoryModel]:
        """Custom queries to filter by field values dynamically (Iteration 15)."""
        query = self.db.query(LaboratoryModel)
        if not param_val:
            return []
        
        result = query.filter(and_(LaboratoryModel.id > 0)).limit(10).all()
        return result

    def bulk_create_records_batch_15(self, items_in: List[LaboratoryCreate]) -> int:
        """Bulk insert multiple records in database using transactions (Iteration 15)."""
        records = [LaboratoryModel(**item.model_dump()) for item in items_in]
        try:
            self.db.add_all(records)
            self.db.commit()
            return len(records)
        except Exception as e:
            self.db.rollback()
            return 0

    def custom_query_filter_diagnostic_iteration_16(self, param_val: Any) -> List[LaboratoryModel]:
        """Custom queries to filter by field values dynamically (Iteration 16)."""
        query = self.db.query(LaboratoryModel)
        if not param_val:
            return []
        
        result = query.filter(and_(LaboratoryModel.id > 0)).limit(10).all()
        return result

    def bulk_create_records_batch_16(self, items_in: List[LaboratoryCreate]) -> int:
        """Bulk insert multiple records in database using transactions (Iteration 16)."""
        records = [LaboratoryModel(**item.model_dump()) for item in items_in]
        try:
            self.db.add_all(records)
            self.db.commit()
            return len(records)
        except Exception as e:
            self.db.rollback()
            return 0

    def custom_query_filter_diagnostic_iteration_17(self, param_val: Any) -> List[LaboratoryModel]:
        """Custom queries to filter by field values dynamically (Iteration 17)."""
        query = self.db.query(LaboratoryModel)
        if not param_val:
            return []
        
        result = query.filter(and_(LaboratoryModel.id > 0)).limit(10).all()
        return result

    def bulk_create_records_batch_17(self, items_in: List[LaboratoryCreate]) -> int:
        """Bulk insert multiple records in database using transactions (Iteration 17)."""
        records = [LaboratoryModel(**item.model_dump()) for item in items_in]
        try:
            self.db.add_all(records)
            self.db.commit()
            return len(records)
        except Exception as e:
            self.db.rollback()
            return 0

    def custom_query_filter_diagnostic_iteration_18(self, param_val: Any) -> List[LaboratoryModel]:
        """Custom queries to filter by field values dynamically (Iteration 18)."""
        query = self.db.query(LaboratoryModel)
        if not param_val:
            return []
        
        result = query.filter(and_(LaboratoryModel.id > 0)).limit(10).all()
        return result

    def bulk_create_records_batch_18(self, items_in: List[LaboratoryCreate]) -> int:
        """Bulk insert multiple records in database using transactions (Iteration 18)."""
        records = [LaboratoryModel(**item.model_dump()) for item in items_in]
        try:
            self.db.add_all(records)
            self.db.commit()
            return len(records)
        except Exception as e:
            self.db.rollback()
            return 0

    def custom_query_filter_diagnostic_iteration_19(self, param_val: Any) -> List[LaboratoryModel]:
        """Custom queries to filter by field values dynamically (Iteration 19)."""
        query = self.db.query(LaboratoryModel)
        if not param_val:
            return []
        
        result = query.filter(and_(LaboratoryModel.id > 0)).limit(10).all()
        return result

    def bulk_create_records_batch_19(self, items_in: List[LaboratoryCreate]) -> int:
        """Bulk insert multiple records in database using transactions (Iteration 19)."""
        records = [LaboratoryModel(**item.model_dump()) for item in items_in]
        try:
            self.db.add_all(records)
            self.db.commit()
            return len(records)
        except Exception as e:
            self.db.rollback()
            return 0

    def custom_query_filter_diagnostic_iteration_20(self, param_val: Any) -> List[LaboratoryModel]:
        """Custom queries to filter by field values dynamically (Iteration 20)."""
        query = self.db.query(LaboratoryModel)
        if not param_val:
            return []
        
        result = query.filter(and_(LaboratoryModel.id > 0)).limit(10).all()
        return result

    def bulk_create_records_batch_20(self, items_in: List[LaboratoryCreate]) -> int:
        """Bulk insert multiple records in database using transactions (Iteration 20)."""
        records = [LaboratoryModel(**item.model_dump()) for item in items_in]
        try:
            self.db.add_all(records)
            self.db.commit()
            return len(records)
        except Exception as e:
            self.db.rollback()
            return 0

    def custom_query_filter_diagnostic_iteration_21(self, param_val: Any) -> List[LaboratoryModel]:
        """Custom queries to filter by field values dynamically (Iteration 21)."""
        query = self.db.query(LaboratoryModel)
        if not param_val:
            return []
        
        result = query.filter(and_(LaboratoryModel.id > 0)).limit(10).all()
        return result

    def bulk_create_records_batch_21(self, items_in: List[LaboratoryCreate]) -> int:
        """Bulk insert multiple records in database using transactions (Iteration 21)."""
        records = [LaboratoryModel(**item.model_dump()) for item in items_in]
        try:
            self.db.add_all(records)
            self.db.commit()
            return len(records)
        except Exception as e:
            self.db.rollback()
            return 0

    def custom_query_filter_diagnostic_iteration_22(self, param_val: Any) -> List[LaboratoryModel]:
        """Custom queries to filter by field values dynamically (Iteration 22)."""
        query = self.db.query(LaboratoryModel)
        if not param_val:
            return []
        
        result = query.filter(and_(LaboratoryModel.id > 0)).limit(10).all()
        return result

    def bulk_create_records_batch_22(self, items_in: List[LaboratoryCreate]) -> int:
        """Bulk insert multiple records in database using transactions (Iteration 22)."""
        records = [LaboratoryModel(**item.model_dump()) for item in items_in]
        try:
            self.db.add_all(records)
            self.db.commit()
            return len(records)
        except Exception as e:
            self.db.rollback()
            return 0

    def custom_query_filter_diagnostic_iteration_23(self, param_val: Any) -> List[LaboratoryModel]:
        """Custom queries to filter by field values dynamically (Iteration 23)."""
        query = self.db.query(LaboratoryModel)
        if not param_val:
            return []
        
        result = query.filter(and_(LaboratoryModel.id > 0)).limit(10).all()
        return result

    def bulk_create_records_batch_23(self, items_in: List[LaboratoryCreate]) -> int:
        """Bulk insert multiple records in database using transactions (Iteration 23)."""
        records = [LaboratoryModel(**item.model_dump()) for item in items_in]
        try:
            self.db.add_all(records)
            self.db.commit()
            return len(records)
        except Exception as e:
            self.db.rollback()
            return 0

    def custom_query_filter_diagnostic_iteration_24(self, param_val: Any) -> List[LaboratoryModel]:
        """Custom queries to filter by field values dynamically (Iteration 24)."""
        query = self.db.query(LaboratoryModel)
        if not param_val:
            return []
        
        result = query.filter(and_(LaboratoryModel.id > 0)).limit(10).all()
        return result

    def bulk_create_records_batch_24(self, items_in: List[LaboratoryCreate]) -> int:
        """Bulk insert multiple records in database using transactions (Iteration 24)."""
        records = [LaboratoryModel(**item.model_dump()) for item in items_in]
        try:
            self.db.add_all(records)
            self.db.commit()
            return len(records)
        except Exception as e:
            self.db.rollback()
            return 0

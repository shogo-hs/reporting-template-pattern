from myreport.schemas.raw_data import UserSchema
from myreport.validation.validator_mixin import ValidatorMixin
from pandas import DataFrame


class NonEmptyDataFrameValidator(ValidatorMixin):
    """DataFrameが空でないことを検証するクラス"""
    
    def _validate(self, data: DataFrame) -> DataFrame:
        if data.empty:
            class_name = self.get_class_name()
            raise ValueError(f"{class_name} validation error: DataFrame is empty.")
        return data

class UserSchemaValidator(ValidatorMixin):
    """DataFrameのスキーマを検証するクラス"""
    
    def _validate(self, data: DataFrame) -> DataFrame:
        try:
            data = UserSchema.validate(data)
            return data
        except Exception as e:
            class_name = self.get_class_name()
            raise ValueError(f"{class_name} validation error: {str(e)}")
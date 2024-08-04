from myreport.schemas.gender_report import GenderReportSchema
from myreport.validation.validator_mixin import ValidatorMixin
from pandas import DataFrame


class GenderReportSchemaValidator(ValidatorMixin):
    """DataFrameのスキーマを検証するクラス"""
    
    def _validate(self, data: DataFrame) -> DataFrame:
        try:
            data = GenderReportSchema.validate(data)
            return data
        except Exception as e:
            class_name = self.get_class_name()
            raise ValueError(f"{class_name} validation error: {str(e)}")
        
class GenderReportValueValidator(ValidatorMixin):
    """DataFrameの値を検証するクラス"""
    
    def _validate(self, data: DataFrame) -> DataFrame:
        if round(data['rate'].sum(), 5) != 1.00000:
            class_name = self.get_class_name()
            msg = "The sum of the gender rate does not equal 1. Please check the data for inconsistencies."
            raise ValueError(f"{class_name} validation error: {msg}")
        return data
        
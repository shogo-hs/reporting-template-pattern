from pandas import DataFrame


class ValidatorMixin:
    """DataFrameのバリデーションを行うミックスインクラス"""
    
    def validate(self, data: DataFrame) -> DataFrame:
        return self._validate(data)
    
    def _validate(self, data: DataFrame) -> DataFrame:
        method_name = self.get_class_name()
        raise NotImplementedError(f'{method_name} method not implemented')
    
    def get_class_name(self) -> str:
        """
        クラス名を返すメソッド
        
        Returns:
            str: クラス名
        """
        return self.__class__.__name__
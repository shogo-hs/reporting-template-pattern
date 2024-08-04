from pandas import DataFrame


class ReporterMixin:
    """レポート作成のミックスインクラス"""
    
    def create_report(self, data: DataFrame) -> DataFrame:
        return self._create_report(data)
    
    def _create_report(self, data: DataFrame) -> DataFrame:
        method_name = self.get_class_name()
        raise NotImplementedError(f'{method_name} method not implemented')
    
    def get_class_name(self) -> str:
        """
        クラス名を返すメソッド
        
        Returns:
            str: クラス名
        """
        return self.__class__.__name__
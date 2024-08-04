import pandas as pd
from myreport.report.reporter_mixin import ReporterMixin
from pandas import DataFrame


class GenderDistributionReporter(ReporterMixin):
    def _create_report(self, data: DataFrame) -> DataFrame:
        
        gender_report = data['gender'].value_counts(normalize=True).reset_index()
        gender_report.columns = ['gender', 'rate']


        return gender_report
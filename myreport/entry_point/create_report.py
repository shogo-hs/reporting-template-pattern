import os

import pandas as pd
from myreport.config.path import RAW_DATA_DIR, REPORT_SAVE_DIR
from myreport.config.settings import TARGET_MONTH, TARGET_YEAR
from myreport.report.gender_distribution import GenderDistributionReporter
from myreport.validation.gender_report import (GenderReportSchemaValidator,
                                               GenderReportValueValidator)
from myreport.validation.raw_data import (NonEmptyDataFrameValidator,
                                          UserSchemaValidator)


def main():
    # config
    target_ym = str(TARGET_YEAR) + str(TARGET_MONTH).zfill(2)
    input_path = os.path.join(RAW_DATA_DIR, f"{target_ym}_raw_data.csv")
    output_path = os.path.join(REPORT_SAVE_DIR, f"{target_ym}_gender_report.csv")

    raw_data_validatores = [
        NonEmptyDataFrameValidator(),
        UserSchemaValidator(),
        ]
    reporter = GenderDistributionReporter()
    report_validatores = [GenderReportSchemaValidator(), GenderReportValueValidator()]


    # 生データの読み込み
    input_df = pd.read_csv(input_path)

    # 生データのバリデーション
    for validator in raw_data_validatores:
        input_df = validator.validate(input_df)

    # レポート作成
    gender_report = reporter.create_report(input_df)

    # レポートのバリデーション
    for validator in report_validatores:
        gender_report = validator.validate(gender_report)

    # レポートの保存
    gender_report.to_csv(output_path)


if __name__ == "__main__":
    main()

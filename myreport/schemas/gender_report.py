import pandera as pa
from pandera.typing import Series


class GenderReportSchema(pa.DataFrameModel):
    gender: Series[str] = pa.Field()  # genderは文字列である
    rate: Series[float] = pa.Field(ge=0, le=1)  # rateはfloatで0以上1以下の数値である
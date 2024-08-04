import pandera as pa
from pandera.typing import Series


class UserSchema(pa.DataFrameModel):
    id: Series[str] = pa.Field()  # idは文字列である
    age: Series[int] = pa.Field(ge=18, le=60, coerce=True)  # 年齢は18以上60以下で、数値に強制変換する
    income: Series[int] = pa.Field(ge=1)  # 収入は1以上である
    gender: Series[str] = pa.Field(isin=["male", "female", "other"])  # 性別は"male"か"female"か"other"
    job: Series[str] = pa.Field(nullable=True)  # 職業は文字列で、欠損値（None）も許容する

    @pa.check("id")
    def id_split_check(cls, series: Series[str]) -> Series[bool]:
        """'_'でidを分割したときに2つの要素になることを確認する"""
        return series.str.split("_", expand=True).shape[1] == 2

    @pa.check("id")
    def id_length_check(cls, series: Series[str]) -> Series[bool]:
        """'_'でidを分割したときに、その2つの要素の文字数がそれぞれ2文字と4文字であることを確認する"""
        split_series = series.str.split("_", expand=True)
        return (split_series[0].str.len() == 2) & (split_series[1].str.len() == 4)

from src.data_utils import load_data
import pandas as pd

def test_load_data_csv(tmp_path):
    file = tmp_path / "sample.csv"
    file.write_text("headline,publisher\nTest headline,Reuters")

    df = load_data(str(file))

    assert isinstance(df, pd.DataFrame)
    assert "headline" in df.columns
    assert "publisher" in df.columns


import pandas as pd

file_path = "data_clean/historical_financials.csv"
df = pd.read_csv(file_path)

expected_columns = [
    "company", "ticker", "segment", "financial_year",
    "metric", "value", "unit", "source_url",
    "source_document", "reported_or_calculated", "notes"
]

expected_rows = {
    "HDFCLIFE": 40,
    "SBILIFE": 40,
    "ICICIGI": 30,
    "STARHEALTH": 30
}

print("DATASET SHAPE:", df.shape)

print("\nCOLUMN VALIDATION")
print("Correct columns:", list(df.columns) == expected_columns)

print("\nCOMPANY ROW COUNTS")
print(df["ticker"].value_counts().sort_index())

print("\nEXPECTED ROW COUNTS")
for ticker, expected in expected_rows.items():
    actual = (df["ticker"] == ticker).sum()
    status = "PASS" if actual == expected else "CHECK"
    print(ticker, actual, "/", expected, status)

print("\nDUPLICATE RECORDS")
duplicates = df.duplicated(
    subset=["ticker", "financial_year", "metric"],
    keep=False
)
print(df.loc[duplicates, ["ticker", "financial_year", "metric"]])

print("\nMISSING VALUES")
print(df.isnull().sum())

print("\nFINANCIAL YEARS")
print(sorted(df["financial_year"].dropna().unique()))

print("\nMETRICS")
print(sorted(df["metric"].dropna().unique()))

print("\nSOURCE URL CHECK")
print("Missing source URLs:", df["source_url"].isna().sum())
print("Placeholder URLs:", df["source_url"].astype(str).str.contains("example.com").sum())

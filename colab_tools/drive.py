def gsheet_by_key(key):
  from google.colab import auth
  auth.authenticate_user()
  import gspread
  from google.auth import default
  creds, _ = default()
  gc = gspread.authorize(creds)
  return gc.open_by_key(key)

def df_from_worksheet(worksheet):
  import pandas
  v = worksheet.get_all_values()
  return pandas.DataFrame.from_records(v[1:], columns=v[0])

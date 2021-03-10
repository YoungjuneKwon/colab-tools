def gsheet_by_key(key):
  from google.colab import auth
  auth.authenticate_user()
  import gspread
  from oauth2client.client import GoogleCredentials
  gc = gspread.authorize(GoogleCredentials.get_application_default())
  return gc.open_by_key(key)

def df_from_worksheet(worksheet):
  import pandas
  v = worksheet.get_all_values()
  return pandas.DataFrame.from_records(v[1:], columns=v[0])

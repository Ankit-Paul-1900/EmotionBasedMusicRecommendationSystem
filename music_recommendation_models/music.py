
import tekore as tk
  
def authenticate():
    CLIENT_ID = "973ee7b940144138b3b187d647c2ec65"
    SECRET_ID = "ee4968382ee44ce481ddaf5dd6884cb4"
    app_info = tk.request_client_token(CLIENT_ID, SECRET_ID)
    return tk.Spotify(app_info)

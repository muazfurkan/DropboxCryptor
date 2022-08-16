from dropbox import DropboxOAuth2FlowNoRedirect

def create_token_link(app_key, app_secret):
   auth_flow = DropboxOAuth2FlowNoRedirect(app_key, app_secret)
   auth_url = auth_flow.start()
   return auth_flow, auth_url

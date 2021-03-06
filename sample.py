from pprint import pprint

from huaweisms.api import webserver, device, monitoring, user, sms, ussd
from huaweisms.api.common import ApiCtx

USER="admin"
PASSWORD="your_admin_password"

PHONE_NUMBER="+1308888888"

# BEFORE running, do MAKE SURE heaweisms.api.config has the CORRECT VALUES for your MODEM

def get_session():
    ctx = ApiCtx()
    token = webserver.SesTokInfo()
    ctx.session_id = token['response']['SesInfo'].split("=")[1]
    ctx.token = token['response']['TokInfo']
    lgn = user.login(ctx, USER, PASSWORD)
    pprint(lgn)
    return ctx


def valid_context(ctx: ApiCtx):
    sl = user.state_login(ctx)
    if sl['type'] == 'response' and sl['response']['State'] != -1:
        return True
    return False

ctx = get_session()
sent = sms.send_sms(ctx, PHONE_NUMBER, "This is a test")
pprint(sent)
status = monitoring.status(ctx)
pprint(status)

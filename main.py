import gazu
from decouple import config

GAZU_HOST = config('GAZU_HOST')
GAZU_EVENT_HOST = config('GAZU_EVENT_HOST')
GAZU_ID = config('GAZU_ID')
GAZU_PSWD = config('GAZU_PSWD')

gazu.set_host(GAZU_HOST)
gazu.set_event_host(GAZU_EVENT_HOST)
gazu.log_in(GAZU_ID, GAZU_PSWD)


def my_callback(data):
    print("Asset created %s" % data["asset_id"])


event_client = gazu.events.init()
gazu.events.add_listener(event_client, "asset:update", my_callback)
print('listening')
gazu.events.run_client(event_client)
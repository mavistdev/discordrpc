from pypresence import Presence 
import time

start = int(time.time())
client_id = "" #your application's client id
RPC = Presence(client_id)
RPC.connect()

while True: #infinite loop
    RPC.update(
        large_image = "", #name of your asset
        large_text = "' ",
        details = "",
        state = "",
        start = start,
        buttons = [{"label": "No Copyright Beats", "url": "https://union.promo/Through-universes"}, {"label": "Mavist", "url": "https://union.promo/spokoynoe-bespokoystvo"}] #up to 2 buttons
    )
    time.sleep(60) #can be as low as 15, depends on how often you want to update

# Dovoljno je koristiti asyncio.create_task za fetch_data(2)
#event loop tada automatski pokrene tu korutninu i ona se izvršava u pozadini
# await nije potreban jer za ispis je dovoljno samo da task bude kreiran i pokrenut
# await nam treba ako želimo dohvatiti rezultat taksa
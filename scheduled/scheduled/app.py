from chalice import Chalice

app = Chalice(app_name='scheduled')


@app.schedule("cron(0 20 ? * * *)")
def scheduled(event):
    print("Executou a função com sucesso")
    return True

import yagmail

def send_mail():
    yag = yagmail.SMTP("busservice.190580.i190542@gmail.com","rupoirfasevpkxnt")
    contents = [
        'WARNING: A data drift has been generated in your BTCUSD price predictor app. You may want ot retrain your model.'
    ]
    yag.send('i190580@nu.edu.pk', 'Data Drift in BTCUSD price predictor app', contents)
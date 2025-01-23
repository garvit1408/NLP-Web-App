import paralleldots

paralleldots.set_api_key("IH4OCcC3pwUFU6jRcoyzug4ShpopFEtpLFigQEZImmk")


def ner(text):
    ner = paralleldots.ner(text)
    print(ner)
    return ner

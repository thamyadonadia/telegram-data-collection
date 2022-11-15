from urllib.parse import urlparse, parse_qs

def url_treatment(url):
    url_treated = urlparse(url)
    parameters = parse_qs(url_treated.fragment)
    chanel_id = str(parameters.get('/im?p')).strip("'[]").split("_")
    chanel_id = chanel_id[0].replace('c', '-100')
    return int(chanel_id)

    
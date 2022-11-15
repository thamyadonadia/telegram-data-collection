from urllib.parse import urlparse, parse_qs

def url_treatment(url):
    url_treated = urlparse(url)
    parameters = parse_qs(url_treated.fragment)
    channel_id = str(parameters.get('/im?p')).strip("'[]").split("_")
    channel_id = channel_id[0].replace('c', '-100')
    return int(channel_id)

    

def wget(uri):
    parsed = urlparse(uri)
    with closing(HTTPConection(parsed.netloc)) as conn:
        path = parsed.path
        if parsed.query:
            path += "?" + parsed.query
        conn.request("GET", path)
        response = conn.getresponse()
        if response.status != 200:
            print(response.reason, file = stderr)
            return 
        print("Respuesta OK")
        return response.read()




def coger_imagenes_src_desde_html(html_doc): #dentro del archivo html, coge todas las imagenes scr
    sopa = BeautifulSoup(html_doc, "html.parser")
    return (img.get("src") for img in sopa.find_all("img"))

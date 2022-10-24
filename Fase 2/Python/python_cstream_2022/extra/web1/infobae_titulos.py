import requests
# pip install requests
"""
WEB-CLIENT   -----------------    WEB-SERVER
                                    infobae - www.infobae.com

           --> HTTP REQUEST -->

            <-- HTTP RESPONSE <---  documento HTML
"""

def encontrar_link_de_noticia(content, start_index):
    try:
        a_start = content.index("<a class=\"cst_ctn\"", start_index)
        a_close = content.index("</a>", a_start) + 4
        return content[a_start:a_close], a_close
    except ValueError:
        return None, -1

def get_link_title(link):
    span_start = link.index("<span>", 0)
    span_close = link.index("</span>", span_start)
    return link[span_start+6:span_close]

r = requests.get("https://www.infobae.com/")
document = r.text

links = []
index = 0
while(True):
    link, index = encontrar_link_de_noticia(document, index)
    if link is None or index == -1:
        break

    links.append(link)


for link in links:
    print(f"+] {get_link_title(link)}")
import webbrowser
from urllib.parse import quote_plus


def web_search(query, site="google"):

    query = quote_plus(query)

    if site == "youtube":
        url = f"https://www.youtube.com/results?search_query={query}"

    else:
        url = f"https://www.google.com/search?q={query}"

    webbrowser.open(url)
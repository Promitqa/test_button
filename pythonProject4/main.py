# Количество посещенных URL-адресов
visited_urls = 0
# Просматриваем веб-страницу и извлекаем все ссылки.
def crawl(url, max_urls=50):
    # max_urls (int): количество макс. URL для сканирования
    global visited_urls
    visited_urls += 1
    links = website_links('url')
    for link in links:
        if visited_urls > max_urls:
            break
        crawl(link, max_urls=max_urls)


if __name__ == "__main__":
    crawl("https://spb.restate.ru/jf03g8D83hl8749sdh99HA292Ll19/")
    print("[+] Total External links:", len(ext_url))
    print("[+] Total Internal links:", len(int_url))
    print("[+] Total:", len(ext_url) + len(int_url))
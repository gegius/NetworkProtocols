def parse(site, reg):
    try:
        a = reg.findall(site)
        return a[0]
    except Exception as ex:
        print(ex)
        return None

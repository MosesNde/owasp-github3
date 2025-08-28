     Returns:
         List[str]: sub links
     """
    base_url = base_url if base_url is not None else url
     all_links = find_all_links(raw_html, pattern=pattern)
     absolute_paths = set()
     for link in all_links:
         # Some may be absolute links like https://to/path
        if link.startswith("http"):
            absolute_paths.add(link)
         # Some may have omitted the protocol like //to/path
         elif link.startswith("//"):
            absolute_paths.add(f"{urlparse(url).scheme}:{link}")
         else:
            absolute_paths.add(urljoin(url, link))
    res = []
     for path in absolute_paths:
        if any(path.startswith(exclude) for exclude in exclude_prefixes):
            continue
        if prevent_outside and not path.startswith(base_url):
             continue
        res.append(path)
    return res
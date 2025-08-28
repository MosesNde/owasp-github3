             result = await bugtracker_get(q.group(1) + '-' + q.group(2))
             msgchain = MessageChain.create([Plain(result)])
             await sendMessage(kwargs, msgchain)
    findlink = re.findall(r'(https://bugs.mojang.com/browse/.*?-\d*)', msg)
     for link in findlink:
         print(link)
        matchbug = re.match(r'https://bugs.mojang.com/browse/(.*?-\d*)', link)
         if matchbug:
             await sendMessage(kwargs, await bugtracker_get(matchbug.group(1)))
 
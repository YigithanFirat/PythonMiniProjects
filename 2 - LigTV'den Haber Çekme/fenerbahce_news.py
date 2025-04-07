import feedparser
print('''
    ######################################
    #                                    #
    #    Ligtv Fenerbahçe Haberleri     #
    #                                    #
    ######################################
''')
haberler_galatarasary = feedparser.parse("http://wwww.ligtv.com.tr/rss/takim/fenerbahce")
i = 1
for haber in haberler_galatarasary.entries:
    print(i, haber.title)
    print(" ", haber.guid, "\n")
    i += 1
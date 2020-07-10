# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

from elasticsearch_dsl import Document, Date, Nested, Boolean, analyzer, Completion, Keyword, Text, Integer


from elasticsearch_dsl.connections import connections




# elastic search url
ES_HOST = 'http://220.171.100.22:43545'
connections.create_connection(hosts=[ES_HOST])

# 定义 es model


class TenderNoticeType(Document):
    # 全部字段类型
    name = Text(analyzer="ik_max_word")
    new_capter = Text(analyzer="ik_max_word")
    auther = Text(analyzer="ik_max_word")
    capter = Text(analyzer="ik_max_word")
    txt = Text()

    class Index:
        name = "bqg_xiaosh"


if __name__ == "__main__":
    TenderNoticeType.init()
BOT_NAME = 'douban'

SPIDER_MODULES = ['douban.spiders']
NEWSPIDER_MODULE = 'douban.spiders'
from faker import Factory
f = Factory.create()
USER_AGENT = f.user_agent()
ROBOTSTXT_OBEY = True
DEFAULT_REQUEST_HEADERS = {
    'Host': 'book.douban.com',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
}
ITEM_PIPELINES = {
    'douban.pipelines.DoubanBookPipeline': 300,

}

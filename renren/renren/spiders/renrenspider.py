import scrapy

class RenrenSpider(scrapy.Spider):
    name = "renren3"
    allowed_domains = ["renren.com"]
    start_urls = (
        'http://www.renren.com/111111',
        'http://www.renren.com/222222',
        'http://www.renren.com/333333',
    )

    cookies = {
    "anonymid":"jk57x9x8-5o63ht",
        "_r01_":"1",
        "ln_uact":"wuwnho@163.com",
        "ln_hurl":"http://hdn.xnimg.cn/photos/hdn421/20121226/0040/h_main_GLzH_7b2200001d311376.jpg",
        "Hm_lvt_966bff0a868cd407a416b4e3993b9dc8":"1537194573",
        "_ga":"GA1.2.460845201.1537194573",
        "_ga":"GA1.3.460845201.1537194573",
        "depovince":"ZGQT",
        "ick_login":"40744e2b-7212-4afe-b73e-babee346df24",
        "jebe_key":"6b8d9bf5-3ac0-49c9-a888-22987f210b9e%7Ce4d2baa9cbe935b22fadbf0138e278f2%7C1537194544199%7C1%7C1537486348697",
        "first_login_flag":"1",
        "loginfrom":"syshome",
    "JSESSIONID":"abcbIFI1nfFqbfIoww5xw",
    "jebecookies":"23840aea-fa37-402d-88d7-c2a44ba9af56|||||",
    "_de":"50A108E895E0CCC9677B8FA35C706602",
    "p":"4beb9f23e816cad754aec358716be1d33",
    "t":"dff311943e583376cc4136bd159426213",
    "societyguester":"dff311943e583376cc4136bd159426213",
    "id":"496371843",
    "xnsid":"698d0e7"
    }

    # 可以重写Spider类的start_requests方法，附带Cookie值，发送POST请求
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.FormRequest(url, cookies = self.cookies, callback = self.parse_page)

    # 处理响应内容
    def parse_page(self, response):
        print ("===========" + response.url)
        with open("profile.html", "wb") as filename:
            filename.write(response.body)
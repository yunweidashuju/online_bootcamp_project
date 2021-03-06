from scrapy import Spider
from scrapy.selector import Selector
from  parkerproject.items import MovieListItem

#Give the spider a name to run later on in the terminal
#scrapy crawl movie_spider

class MovieListSpider(Spider):
	name = "movies_spider"
	allowed_urls: ['http://www.metacritic.com']
	start_urls: []
	years = range(2007, 2018)
	[start_urls.append('http://www.metacritic.com/browse/movies/score/metascore/year/filtered?year_selected=' + str(year) + '&sort=desc' for year in years]

	def parse_movie_listings(self, response):
		
		rows = response.xpath('//table[@class="list score"]/tr').extract()
		for i in range(1, 200):
			name = str(Selector(text= rows[i]).xpath('//tr[@class="summary_row"]/td[@class="title_wrapper"]/div/a/text()').extract()[0].encode('utf-8').strip())
			link = str(Selector(text= rows[i]).xpath('//tr[@class="summary_row"]/td[@class="title_wrapper"]/div/a/@href').extract()[0].strip())
			date = str(Selector(text= rows[i]).xpath('//tr[@class="summary_row"]/td[@class="date_wrapper"]/span[1]/text()').extract()[0].strip())

			item = MovieListItem()
			item['title'] = title
			item['link'] = link
			item['date'] = date

			yield item
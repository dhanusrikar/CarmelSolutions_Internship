import scrapy


class FacultySpider(scrapy.Spider):
    # name of the spider
    name = 'faculty_two'

    #starting point for the spider
    start_urls = ['https://manipal.edu/mit/department-faculty.html']

    # This function fetches the link of faculty page
    def parse(self, response):
        for link in response.css('a.members-wp'):
            # Storing the link in next page var
            next_page = link.attrib['href']
            if next_page is not None:
                # this opens the next page
                yield response.follow(next_page, callback=self.parse2)

    # This function searches and stores the data
    def parse2(self, response):
        try:
            yield {
                'Name':
                response.css('div.title-wrap-left h2::text').get(),
                'Organization':
                response.css('h3.institute-name a::text').get(),
                'Designation':
                response.css(
                    'div.faculty-profile-text-section h3::text').get(),
                'Department':
                response.css('div.faculty-profile-text-section p::text').get(),
                'Qualification':
                response.css('div.faculty-profile-text-section p::text').
                getall()[1][2:].split(','),
                'email':
                response.css('div.email a::text').getall()[1],
                'area of interest':
                response.css('div#academic li::text').getall()[-1].split(','),
                'LinkedIn':
                '',
                'Facebook':
                '',
                'Twitter':
                '',
                'Instagram':
                '',
                'Phone':
                ''
            }
        except:
            pass
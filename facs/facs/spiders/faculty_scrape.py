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
            name = response.css('div.title-wrap-left h2::text').get()
        except:
            name = "na"
        try:
            org = response.css('h3.institute-name a::text').get()
        except:
            org = "na"
        try:
            des = response.css(
                'div.faculty-profile-text-section h3::text').get()
        except:
            des = "na"
        try:
            dept = response.css(
                'div.faculty-profile-text-section p::text').get()
        except:
            dept = "na"
        try:
            quali = response.css('div.faculty-profile-text-section p::text'
                                 ).getall()[1][2:].split(',')
        except:
            quali = "na"
        try:
            email = response.css('div.email a::text').getall()[1]
        except:
            email = "na"
        # Areas of interest
        try:
            x = response.css('div#academic ul:nth-child(n) ::text').getall()
            flag = 0
            index = 0
            a = []
            for i in x:
                if '\n' in i:
                    continue
                else:
                    i = i.replace('\xa0', '')
                    a.append(i.lower())

            for i in a:
                if 'area' in i:
                    flag = 1
                    break
                index += 1

            if flag == 0:
                area = "na"
            else:
                area = a[index + 1:]
        except:
            area = "na"

        try:
            linkedin = response.css('div.linkedIn a::attr(href)').get()
            if (len(linkedin) == 0):
                linkedin = "na"
        except:
            linkedin = "na"

        try:
            facebook = response.css('div.facebook a::attr(href)').get()
            if (len(facebook) == 0):
                facebook = "na"
        except:
            facebook = "na"

        try:
            twitter = response.css('div.twitter a::attr(href)').get()
            if (len(twitter) == 0):
                twitter = 'na'
        except:
            twitter = "na"

        try:
            website = response.css('div.website a::attr(href)').get()
            if (len(website) == 0):
                website = "na"
        except:
            website = "na"

        try:
            phone = response.css('div.phone span::text').get()
            if (len(phone) == 0):
                phone = "na"
        except:
            phone = "na"

        yield {
            'Name': name,
            'Organization': org,
            'Designation': des,
            'Department': dept,
            'Qualification': quali,
            'Email': email,
            'Areas of interest': area,
            'LinkedIn': linkedin,
            'Facebook': facebook,
            'Twitter': twitter,
            'Website': website,
            'phone': phone
        }

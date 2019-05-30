
# This program is help to get properties from  a given jira issue(url)
# to run this program type the following command in the terminal  
# >>scrapy runspider JiraIssueProperty.py
#
# if you want to get out in csv format then type the following command in the terminal 
# >>scrapy runspider JiraIssueProperty.py -o IssueReport.csv
#
# @author  Kalyani
# @version 1.0
# @since   2019-05-25 


import scrapy

class JiraIssuesProperties(scrapy.Spider):
    name = "jira_issue_report"
    start_urls = ['http://issues.apache.org/jira/browse/CAMEL-10597']
    
    def parse(self, response):
    
        #to download that particular issue as html file
        filename = 'JiraIssue.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
            
            
        for jira in response.xpath('.'):
        
            #to crawl specific properties from given jira issue url            
            yield {
             'Type' : jira.xpath('//ul/li[@class="item"]/div[@class="wrap"]/span[@id="type-val"]/text()')[1].get(),
             'Assignee': jira.xpath('//ul/li[@class="people-details"]/dl/dd/span/span/text()')[1].get(),
             'created' : jira.xpath('//ul/li/dl[@class="dates"]/dd/span/time/@datetime').get(),
             'Description': jira.xpath('//div[@class="user-content-block"]/descendant-or-self::*/text()').getall(),
               
            }
            
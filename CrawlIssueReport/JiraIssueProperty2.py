
# This program is help to get properties from  a given jira issue(url)
# to run this program type the following command in the terminal  
# >>scrapy runspider JiraIssueProperty2.py
#
# if you want to get out in csv format then type the following command in the terminal 
# >>scrapy runspider JiraIssueProperty.py -o jiraIssues2.csv
#
# @author  Kalyani
# @version 1.0
# @since   2019-05-25 


import scrapy

class JiraIssuesProperties(scrapy.Spider):
    name = "jira_issue_report"
    start_urls = ['https://issues.apache.org/jira/si/jira.issueviews:issue-xml/CAMEL-10597/CAMEL-10597.xml',
                              ]
    
    def parse(self, response):
    
        #to download that particular issue as xml file
        filename = 'JiraIssue.xml'
        with open(filename, 'wb') as f:
           f.write(response.body)
            
            
        for jira in response.xpath('.'):
            #to crawl specific properties from given jira issue url            
            yield {
              'Type': jira.xpath('/rss[@version="0.92"]/channel/item/type/text()').get(),
              'Assignee': jira.xpath('/rss[@version="0.92"]/channel/item/assignee/text()').get(),
              'Created': jira.xpath('/rss[@version="0.92"]/channel/item/created/text()').get(),
              'Updated': jira.xpath('/rss[@version="0.92"]/channel/item/updated/text()').get(),
              'Description':jira.xpath('/rss[@version="0.92"]/channel/item/description/text()').extract(), 
              'Comments':jira.xpath('/rss[@version="0.92"]/channel/item/comments/comment/text()').getall(),
            
            }
            
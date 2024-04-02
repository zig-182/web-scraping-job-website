# Overview
A Python script that uses the Beautiful Soup library to scrape and parse Python jobs in London across multiple pages of a job listing website. The script outputs the Job Title and the corresponding URL where you can begin your job application. 

# Description
As I’m moving towards getting ready to apply for jobs, I wanted to use my newfound Python skills to automate a task that I would be performing regularly. After watching a few tutorials and researching the Python library, Beautiful Soup, I decided to build my own scraper which would output the information I wanted from a job listing website.

These are the steps I took to complete this task:

1.	Identified target website and required information.
2.	Checked if scraping was allowed (add robots.txt to the end of the URL).
3.	Extracted data to ensure access.
4.	Printed job titles for review and analysis.
5.	Extracted URLs from job titles.
6.	Concatenated URLs to form complete links.
7.	Printed job titles and corresponding URLs.
8.	Implemented loop for scraping multiple pages.


# Languages
* Python

# Brief Notes
When scraping data from websites, it's important to consider ethical implications. While practicing scraping techniques for non-commercial purposes is generally acceptable, it's crucial to respect website policies and guidelines.
  
Before scraping, it's recommended to check the website's robots.txt file by appending '/robots.txt' to the end of the URL. This file outlines which parts of the website are off-limits to crawlers and scrapers. Adhering to these directives helps maintain good web etiquette and prevents unintended consequences.

In addition, if your code runs repetitively, it's important to consider implementing a timer in your scraping code to prevent overloading the website's server. By adding pauses between requests, you can ensure that your scraper operates responsibly and doesn't disrupt the website's performance or trigger security measures. This practice helps maintain good web etiquette and reduces the risk of being blocked by the website.

# Going Forward
In the future, I plan to extend this project by exploring how to integrate Pandas to modify the output of my script. Additionally, I aim to automate the execution of my script, possibly scheduling it to run once a day at a specific time to provide me with the latest job information. I hope these enhancements will improve the efficiency and reliability of the scraping process while ensuring responsible web scraping practices.

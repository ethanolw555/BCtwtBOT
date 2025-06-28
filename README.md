# BCtwtBOT (Portfolio Project)
This is a demonstration of a windows-based Python project that would extract codes in tweets from a website's Twitter account, before automatically submitting those codes to the website to redeem rewards.

NOTE: This project is intended for review purposes ONLY. Additionally, this project will not perform as intended, due to changes in the API and packages accessed.

# Project description

This project was constructed with the intention to bypass regional differences between myself and the US-based website.
The website itself provided rewards to users, should they follow instructions provided by an image sent out by the website's Twitter account. These images had a range of challenges for users to complete in order to obtain a code, however the most common was a simple image containing a code. No effort was required to obtain this code, and users only had to view the image and input the code on their website, with the only caveat being the code was time sensitive and expired within one hour of the Tweet being posted. Due to the website being US based, the majority of these tweets appeared at obscene times, where it would be impractical and unhealthy to remain conscious to obtain these small rewards. The attached project is a solution I designed in order to semi-reliably obtain these rewards, without the need to be awake or checking the website's Twitter account.
Notably, the project was designed in 2022. This may explain differences in current design skills and approaches.

# Code execution

The project continually runs a script. This script waits until the current machine time is greater than or equal to the specified start time. The script will continue to execute until it is greater than or equal to the specified end time. The main program used is executed at five minute intervals. This is done to ensure the program will quickly identify any new Tweets from the account that may contain codes. The program makes a query to Twitters API using tweepy. Relevant Twitter API information such as access_tokens were required to access the API. The code obtains the latest post from the account before determining if the Tweet was an image. If it was an image, it opens up the Tweet, manually Right Click + Save as before closing the tweet and saving the image to a directory. This image is then read and transformed into a code. This code is then verified within a used codes text file. If the code already exists within the text file, the program ignores it. If the code does not exist within the text file, the program will manually open the website and input the code, using predetermined cursor positions (macro). It will then log the code into the used codes. This process is repeated until the machines time is greater than or equal to the specified end time.

# Project Justification

Despite not being maintained, as well as being designed multiple years ago, the project itself demonstrates one of my first attempts at implementing a bot on a "real website". There were no packages or interfaces my program could have used to assist in grabbing and submitting these codes. All of this was done with no knowledge of HTML POST or GET requests. This project is a demonstration of my ability to problem solve given the limited skillset I had at the time, as well my ability to learn new packages within Python and how I could use them to my advantage in this situation.

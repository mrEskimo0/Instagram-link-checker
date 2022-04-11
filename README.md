# Instagram Link Checker

## Description

This application goes through the instagram accounts tagged in a user's posts and scrapes the link in their bio. If the link in the account's bio matches the desired link, or is found in an account's linktree, the account is written into a csv. The application can also be fed a list of accounts to match a desired link in the accounts' bios.

## Instillation

* Install Python as you would normally install Python: https://www.python.org/downloads/

* Install the Instaloader library

```bash
 pip install instaloader
 ```

* Download this repository

* Create a new instagram account: https://www.instagram.com/

* Create a file named "credentials.py" in the downloaded repository with the USERNAME and PASSWORD in it.
```python
USERNAME="instagramusername"
PASSWORD="instagrampassword"
DESIRED_LINK="https://desiredlink"
TERMS=['Term1','Term2',...]
```
For the desired link, it is good practice to leave out the ending of the links to ensure accuracy. Terms are if you are looking for specific characters, words, or phrases in linktrees.

## User Guide

This application is designed to be used on the command line. There are two ways to start the application:

* Start a terminal or command line window, navigate to the downloaded repository and call the main.py file

```bash
cd /path/to/downloaded_repo/
python3 main.py
```
* Using finder or file explorer, navigate to the downloaded repository and double click main.py to start

The application will first prompt you to either scrape tagged profiles from an accounts' posts, or check a list of names from a csv. Start with inputting "s" to scrape names. If you want to check links from a custom csv of profiles, name the csv "scraped_accounts.csv" and select "c".

### Scraping a Profile

After selecting "s", input the name of the profile who's posts you want to scrape. It will also ask how many posts you want to look at, enter at most the number of posts that the profile you input has. The application will go through the number of posts that you input, and add profiles tagged in a user's pictures that have a link in their bio.

### Checking Links

Once you have scraped a profile's posts, enter "c" to check the list of profiles that we're just scraped. Simply wait for the program to finish running, and once completed you can find a csv of profile names that have the desired link in their bio or in their linktree. 
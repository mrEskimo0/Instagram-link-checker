from instaloader import ProfileNotExistsException
from functions import *
from credentials import DESIRED_LINK, USERNAME, PASSWORD, TERMS
import csv

#main program loop
#login to instagram and make profile instance
readfile = 'scraped_accounts.csv'
exportfile = 'checked_accounts.csv'

#ask which script we want to run
while True:
    decision = input('are we scraping accounts or checking the list? Enter S or C or Q to quit ')
    if decision.lower() == 's':
        profile = login(USERNAME, PASSWORD)
    
        accounts = scrape_accounts(profile)
        
        #export to csv function
        with open(readfile, 'w') as file:
            file = csv.writer(file)
            file.writerows(accounts)
        
        print('added {} accounts to readfile'.format(len(accounts)))
        
    elif decision.lower() == 'c':
        L = profile_check_login(USERNAME, PASSWORD)
        
        #read csv for accounts to check
        accounts = []
        with open(readfile, 'r') as read_file:
            reader = csv.reader(read_file)
            for row in reader:
                accounts.append(row)        
                
            # read csv for accounts, get them into a list to throw
            # into the function below
        
        linktree_accounts, target_accounts = tree_check(accounts, L, DESIRED_LINK)

        linktree_targets = is_target(linktree_accounts, TERMS)

        for i in linktree_targets:
            target_accounts.append(i)
            
        with open(exportfile, 'w') as export:
            export = csv.writer(export)
            export.writerows([target_accounts]) 
        
    elif decision.lower() == 'q':
        #quit
        print('done')
        break
    else:
        print('enter s, c, or q')
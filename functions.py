import instaloader
import requests
import bs4
import time
from instaloader import ConnectionException


def login(USERNAME, PASSWORD):
    L = instaloader.Instaloader()
    try:
        L.login(USERNAME, PASSWORD)
        selected_profile = input('what profile are we looking at?')
        profile = instaloader.Profile.from_username(L.context, selected_profile)
    except ConnectionException:
        new_username = input('that login is not working or entered incorrectly, enter account username: ')
        new_password = input('enter account password: ')
        L.login(new_username, new_password)
        selected_profile = input('what profile are we looking at?')
        profile = instaloader.Profile.from_username(L.context, selected_profile)
    return profile



#make it able to change how many accounts we scrape
def scrape_accounts(profile):
    accounts = []
    target = int(input('how many accounts would you like to scrape?'))
    for x, post in enumerate(profile.get_posts()):
        if x == target:
            print('{} profiles added'.format(x))
            break
        accounts.append(post.caption_mentions)
    return accounts

def profile_check_login(USERNAME, PASSWORD):
    L = instaloader.Instaloader()
    try:
        L.login(USERNAME, PASSWORD)
    except ConnectionException:
        new_username = input('that login is not working, enter new account username: ')
        new_password = input('new password: ')
        L.login(new_username, new_password)
    return L

def tree_check(accounts, L, desired_link):
    linktree_accounts = []
    target_accounts = []
    for x, username in enumerate(accounts):
        time.sleep(10)
        try:
            profile = instaloader.Profile.from_username(L.context, username[0])
        # check for link
        except (IndexError, instaloader.ProfileNotExistsException) as pde:
            print('page doesnt exist')
            continue
        if profile.external_url:
            if profile.external_url[0:14] == 'https://linktr':
                print('added linktree profile')
                linktree_accounts.append(profile)
            elif profile.external_url[0:16] == desired_link:
                print('added target profile')
                target_accounts.append(profile.username)
            else:
                del profile
        else:
            del profile
    return linktree_accounts, target_accounts

def is_target(linktree_accounts, terms):
    off = 'off'
    targets = []
    for user in linktree_accounts:
        time.sleep(2)
        url = user.external_url
        res = requests.get(url)
        soup = bs4.BeautifulSoup(res.text,'lxml')
        links = soup.select('.kVCYxL')
        if len(links) == 0:
            print('no links in linktree: check the linktree to see if site has changed')
        
        #check for terms in links
        for i in links:
            for l in terms:
                if l in i.text.lower():
                    if off in i.text.lower():
                        break
                    else:
                        targets.append(user.username)
                        break
                        
    return list(set(targets))
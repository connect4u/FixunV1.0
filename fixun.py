#!usr/bin/python3

import requests
import threading
import time
import sys
import socket
import urllib3

#HEADER - DESIGN
print('-'*50)
print('''
 _____ _____  __ _   _ _   _ 
|  ___|_ _\ \/ /  | | | \ | |
| |_   | | \  / | | | |  \| |
|  _|  | | /  \ | |_| | |\  |
|_|   |___/_/\_\ \___/|_| \_| V1.0 [Find User Name] 
''')
print('-'*50)

username = input('Put UserName: ')
Auto_links = ['twitter.com', 'facebook.com', 'pinterest.com', 'mix.com', 'slack.com', 'getpocket.com', 'dig.com', 'instagram.com', 'youtube.com', 'plus.google.com', 'flickr.com', 'linkedin.com', 'reddit.com', 'qzone.qq.com', 'myspace.com', 'photobucket.com', 'digg.com', 'yelp.com', 'stumbleupon.com', 'scribd.com', 'xing.com', 'spaces.live.com', 'vkontakte.ru', 'last.fm', 'squidoo.com', 'technorati.com', 'diigo.com', 'twiptic.com', 'douban.com', 'hi5.com', 'friendster.com', 'renren.com', 'odnoklassniki.ru', 'mixi.jp', 'xanga.com', 'care2.com', 'friendfeed.com', 'orkut.com', 'viadeo.com', 'newsvine.com',
              'blackplanet.com', 'bebo.com', 'getsatisfaction.com', 'netlog.com', 'cafemom.com', 'dzone.com', 'myheritage.com', 'gaiaonline.com', 'ning.com', 'metafilter.com', 'us.cyworld.com', 'tribe.net', 'flixster.com', 'current.com', 'tagged.com', 'kaboodle.com', 'epinions.com', 'ping.fm', 'myblooglog.com', 'classmates.com', 'plaxo.com', 'revver.com', 'mylife.com', 'myyearbook.com', 'clipmarks.com', 'gigya.com', 'magnify.net', 'faves.com', 'habbo.com', 'yuku.com', 'ecademy.com', 'twine.com', 'omgili.com', 'ballhype.com', 'weeworld.com']  # these links will use for search username is available or not

length_link = len(Auto_links)


print('''In Which Way You Want To Find Your UserName? 
1.Auto 
2.Manual''')

choice = input('Enter Choice: ')

#Define the function for Auto find the username in links so i divide all 75 links to different part of 15 functions

def Auto_choice_P1():
    try:
        for num_seq in range(5):
            full_site = 'http://' + Auto_links[num_seq] + '/' + username
            site_response = requests.get(full_site, timeout=5)
            status_code = site_response.status_code
            if status_code >= 200 and status_code < 300:
                web_name = Auto_links[num_seq]
                hostname = socket.gethostbyname(web_name)
                print('-'*50)
                print(full_site)
                print('WEBSITE: ',Auto_links[num_seq])
                print('IP: ',hostname)
                print('[ACTIVE]')
                print('-'*50)
            elif status_code >= 300:
                web_name = Auto_links[num_seq]
                hostname = socket.gethostbyname(web_name)
                print('-'*50)
                print(full_site)
                print('WEBSITE: ',Auto_links[num_seq])
                print('IP: ',hostname)
                print('[INACTIVE]')
                print('-'*50)
    except ConnectionError:
        return "Connection Error"
    except Exception:
        return "Something Wrong" 


def Auto_choice_P2():
    try:
        for num_seq in range(5,10):
            full_site = 'http://' + Auto_links[num_seq] + '/' + username
            site_response = requests.get(full_site, timeout=5)
            status_code = site_response.status_code
            if status_code >= 200 and status_code < 300:
                web_name = Auto_links[num_seq]
                hostname = socket.gethostbyname(web_name)
                print('-'*50)
                print(full_site)
                print('WEBSITE: ',Auto_links[num_seq])
                print('IP: ',hostname)
                print('[ACTIVE]')
                print('-'*50)
            elif status_code >= 300:
                web_name = Auto_links[num_seq]
                hostname = socket.gethostbyname(web_name)
                print('-'*50)
                print(full_site)
                print('WEBSITE: ',Auto_links[num_seq])
                print('IP: ',hostname)
                print('[INACTIVE]')
                print('-'*50)
    except ConnectionError:
        return "Connection Error"
    except Exception:
        return "Something Wrong"


def Auto_choice_P3():
    try:
        for num_seq in range(10,15):
            full_site = 'http://' + Auto_links[num_seq] + '/' + username
            site_response = requests.get(full_site, timeout=5)
            status_code = site_response.status_code
            if status_code >= 200 and status_code < 300:
                web_name = Auto_links[num_seq]
                hostname = socket.gethostbyname(web_name)
                print('-'*50)
                print(full_site)
                print('WEBSITE: ',Auto_links[num_seq])
                print('IP: ',hostname)
                print('[ACTIVE]')
                print('-'*50)
            elif status_code >= 300:
                web_name = Auto_links[num_seq]
                hostname = socket.gethostbyname(web_name)
                print('-'*50)
                print(full_site)
                print('WEBSITE: ',Auto_links[num_seq])
                print('IP: ',hostname)
                print('[INACTIVE]')
                print('-'*50)
    except ConnectionError:
        return "Connection Error"
    except Exception:
        return "Something Wrong"


def Auto_choice_P4():
    try:
        for num_seq in range(15,20):
            full_site = 'http://' + Auto_links[num_seq] + '/' + username
            site_response = requests.get(full_site, timeout=5)
            status_code = site_response.status_code
            if status_code >= 200 and status_code < 300:
                web_name = Auto_links[num_seq]
                hostname = socket.gethostbyname(web_name)
                print('-'*50)
                print(full_site)
                print('WEBSITE: ',Auto_links[num_seq])
                print('IP: ',hostname)
                print('[ACTIVE]')
                print('-'*50)
            elif status_code >= 300:
                web_name = Auto_links[num_seq]
                hostname = socket.gethostbyname(web_name)
                print('-'*50)
                print(full_site)
                print('WEBSITE: ',Auto_links[num_seq])
                print('IP: ',hostname)
                print('[INACTIVE]')
                print('-'*50)
    except ConnectionError:
        return "Connection Error"
    except Exception:
        return "Something Wrong"


def Auto_choice_P5():
    try:
        for num_seq in range(20,25):
            full_site = 'http://' + Auto_links[num_seq] + '/' + username
            site_response = requests.get(full_site, timeout=5)
            status_code = site_response.status_code
            if status_code >= 200 and status_code < 300:
                web_name = Auto_links[num_seq]
                hostname = socket.gethostbyname(web_name)
                print('-'*50)
                print(full_site)
                print('WEBSITE: ',Auto_links[num_seq])
                print('IP: ',hostname)
                print('[ACTIVE]')
                print('-'*50)
            elif status_code >= 300:
                web_name = Auto_links[num_seq]
                hostname = socket.gethostbyname(web_name)
                print('-'*50)
                print(full_site)
                print('WEBSITE: ',Auto_links[num_seq])
                print('IP: ',hostname)
                print('[INACTIVE]')
                print('-'*50)
    except ConnectionError:
        return "Connection Error"
    except Exception:
        return "Something Wrong"


def Auto_choice_P6():
    try:
        for num_seq in range(25,30):
            full_site = 'http://' + Auto_links[num_seq] + '/' + username
            site_response = requests.get(full_site, timeout=5)
            status_code = site_response.status_code
            if status_code >= 200 and status_code < 300:
                web_name = Auto_links[num_seq]
                hostname = socket.gethostbyname(web_name)
                print('-'*50)
                print(full_site)
                print('WEBSITE: ',Auto_links[num_seq])
                print('IP: ',hostname)
                print('[ACTIVE]')
                print('-'*50)
            elif status_code >= 300:
                web_name = Auto_links[num_seq]
                hostname = socket.gethostbyname(web_name)
                print('-'*50)
                print(full_site)
                print('WEBSITE: ',Auto_links[num_seq])
                print('IP: ',hostname)
                print('[INACTIVE]')
                print('-'*50)
    except ConnectionError:
        return "Connection Error"
    except Exception:
        return "Something Wrong"


def Auto_choice_P7():
    try:
        for num_seq in range(30,35):
            full_site = 'http://' + Auto_links[num_seq] + '/' + username
            site_response = requests.get(full_site, timeout=5)
            status_code = site_response.status_code
            if status_code >= 200 and status_code < 300:
                web_name = Auto_links[num_seq]
                hostname = socket.gethostbyname(web_name)
                print('-'*50)
                print(full_site)
                print('WEBSITE: ',Auto_links[num_seq])
                print('IP: ',hostname)
                print('[ACTIVE]')
                print('-'*50)
            elif status_code >= 300:
                web_name = Auto_links[num_seq]
                hostname = socket.gethostbyname(web_name)
                print('-'*50)
                print(full_site)
                print('WEBSITE: ',Auto_links[num_seq])
                print('IP: ',hostname)
                print('[INACTIVE]')
                print('-'*50)
    except ConnectionError:
        return "Connection Error"
    except Exception:
        return "Something Wrong"


def Auto_choice_P8():
    try:
        for num_seq in range(35,40):
            full_site = 'http://' + Auto_links[num_seq] + '/' + username
            site_response = requests.get(full_site, timeout=5)
            status_code = site_response.status_code
            if status_code >= 200 and status_code < 300:
                web_name = Auto_links[num_seq]
                hostname = socket.gethostbyname(web_name)
                print('-'*50)
                print(full_site)
                print('WEBSITE: ',Auto_links[num_seq])
                print('IP: ',hostname)
                print('[ACTIVE]')
                print('-'*50)
            elif status_code >= 300:
                web_name = Auto_links[num_seq]
                hostname = socket.gethostbyname(web_name)
                print('-'*50)
                print(full_site)
                print('WEBSITE: ',Auto_links[num_seq])
                print('IP: ',hostname)
                print('[INACTIVE]')
                print('-'*50)
    except ConnectionError:
        return "Connection Error"
    except Exception:
        return "Something Wrong"


def Auto_choice_P9():
    try:
        for num_seq in range(40,45):
            full_site = 'http://' + Auto_links[num_seq] + '/' + username
            site_response = requests.get(full_site, timeout=5)
            status_code = site_response.status_code
            if status_code >= 200 and status_code < 300:
                web_name = Auto_links[num_seq]
                hostname = socket.gethostbyname(web_name)
                print('-'*50)
                print(full_site)
                print('WEBSITE: ',Auto_links[num_seq])
                print('IP: ',hostname)
                print('[ACTIVE]')
                print('-'*50)
            elif status_code >= 300:
                web_name = Auto_links[num_seq]
                hostname = socket.gethostbyname(web_name)
                print('-'*50)
                print(full_site)
                print('WEBSITE: ',Auto_links[num_seq])
                print('IP: ',hostname)
                print('[INACTIVE]')
                print('-'*50)
    except ConnectionError:
        return "Connection Error"
    except Exception:
        return "Something Wrong"


def Auto_choice_P10():
    try:
        for num_seq in range(45,50):
            full_site = 'http://' + Auto_links[num_seq] + '/' + username
            site_response = requests.get(full_site, timeout=5)
            status_code = site_response.status_code
            if status_code >= 200 and status_code < 300:
                web_name = Auto_links[num_seq]
                hostname = socket.gethostbyname(web_name)
                print('-'*50)
                print(full_site)
                print('WEBSITE: ',Auto_links[num_seq])
                print('IP: ',hostname)
                print('[ACTIVE]')
                print('-'*50)
            elif status_code >= 300:
                web_name = Auto_links[num_seq]
                hostname = socket.gethostbyname(web_name)
                print('-'*50)
                print(full_site)
                print('WEBSITE: ',Auto_links[num_seq])
                print('IP: ',hostname)
                print('[INACTIVE]')
                print('-'*50)
    except ConnectionError:
        return "Connection Error"
    except Exception:
        return "Something Wrong"


def Auto_choice_P11():
    try:
        for num_seq in range(50,55):
            full_site = 'http://' + Auto_links[num_seq] + '/' + username
            site_response = requests.get(full_site, timeout=5)
            status_code = site_response.status_code
            if status_code >= 200 and status_code < 300:
                web_name = Auto_links[num_seq]
                hostname = socket.gethostbyname(web_name)
                print('-'*50)
                print(full_site)
                print('WEBSITE: ',Auto_links[num_seq])
                print('IP: ',hostname)
                print('[ACTIVE]')
                print('-'*50)
            elif status_code >= 300:
                web_name = Auto_links[num_seq]
                hostname = socket.gethostbyname(web_name)
                print('-'*50)
                print(full_site)
                print('WEBSITE: ',Auto_links[num_seq])
                print('IP: ',hostname)
                print('[INACTIVE]')
                print('-'*50)
    except ConnectionError:
        return "Connection Error"
    except Exception:
        return "Something Wrong"


def Auto_choice_P12():
    try:
        for num_seq in range(55,60):
            full_site = 'http://' + Auto_links[num_seq] + '/' + username
            site_response = requests.get(full_site, timeout=5)
            status_code = site_response.status_code
            if status_code >= 200 and status_code < 300:
                web_name = Auto_links[num_seq]
                hostname = socket.gethostbyname(web_name)
                print('-'*50)
                print(full_site)
                print('WEBSITE: ',Auto_links[num_seq])
                print('IP: ',hostname)
                print('[ACTIVE]')
                print('-'*50)
            elif status_code >= 300:
                web_name = Auto_links[num_seq]
                hostname = socket.gethostbyname(web_name)
                print('-'*50)
                print(full_site)
                print('WEBSITE: ',Auto_links[num_seq])
                print('IP: ',hostname)
                print('[INACTIVE]')
                print('-'*50)
    except ConnectionError:
        return "Connection Error"
    except Exception:
        return "Something Wrong"


def Auto_choice_P13():
    try:
        for num_seq in range(60,65):
            full_site = 'http://' + Auto_links[num_seq] + '/' + username
            site_response = requests.get(full_site, timeout=5)
            status_code = site_response.status_code
            if status_code >= 200 and status_code < 300:
                web_name = Auto_links[num_seq]
                hostname = socket.gethostbyname(web_name)
                print('-'*50)
                print(full_site)
                print('WEBSITE: ',Auto_links[num_seq])
                print('IP: ',hostname)
                print('[ACTIVE]')
                print('-'*50)
            elif status_code >= 300:
                web_name = Auto_links[num_seq]
                hostname = socket.gethostbyname(web_name)
                print('-'*50)
                print(full_site)
                print('WEBSITE: ',Auto_links[num_seq])
                print('IP: ',hostname)
                print('[INACTIVE]')
                print('-'*50)
    except ConnectionError:
        return "Connection Error"
    except Exception:
        return "Something Wrong"


def Auto_choice_P14():
    try:
        for num_seq in range(65,70):
            full_site = 'http://' + Auto_links[num_seq] + '/' + username
            site_response = requests.get(full_site, timeout=5)
            status_code = site_response.status_code
            if status_code >= 200 and status_code < 300:
                web_name = Auto_links[num_seq]
                hostname = socket.gethostbyname(web_name)
                print('-'*50)
                print(full_site)
                print('WEBSITE: ',Auto_links[num_seq])
                print('IP: ',hostname)
                print('[ACTIVE]')
                print('-'*50)
            elif status_code >= 300:
                web_name = Auto_links[num_seq]
                hostname = socket.gethostbyname(web_name)
                print('-'*50)
                print(full_site)
                print('WEBSITE: ',Auto_links[num_seq])
                print('IP: ',hostname)
                print('[INACTIVE]')
                print('-'*50)
    except ConnectionError:
        return "Connection Error"
    except Exception:
        return "Something Wrong"


def Auto_choice_P15():
    try:
        for num_seq in range(70, 75):
            full_site = 'http://' + Auto_links[num_seq] + '/' + username
            site_response = requests.get(full_site, timeout=5)
            status_code = site_response.status_code
            if status_code >= 200 and status_code < 300:
                web_name = Auto_links[num_seq]
                hostname = socket.gethostbyname(web_name)
                print('-'*50)
                print(full_site)
                print('WEBSITE: ',Auto_links[num_seq])
                print('IP: ',hostname)
                print('[ACTIVE]')
                print('-'*50)
            elif status_code >= 300:
                web_name = Auto_links[num_seq]
                hostname = socket.gethostbyname(web_name)
                print('-'*50)
                print(full_site)
                print('WEBSITE: ',Auto_links[num_seq])
                print('IP: ',hostname)
                print('[INACTIVE]')
                print('-'*50)
    except ConnectionError:
        return "Connection Error"
    except Exception:
        return "Something Wrong" 


#Now define a function for the Manual links
def manual_choice():
    try:
        man_link = input("Enter link [eg. twitter.com]: ")
        man_full_link = 'http://' + man_link + '/' + username
        link_response = requests.get(man_full_link)
        ip = socket.gethostbyname(man_link)
        status = link_response.status_code
        if status == 200:
            print('-'*50)
            print(man_full_link)
            print("WEBSITE: ",man_link)
            print("IP: ",ip)
            print("[ACTIVE]")
            print('-'*50)
        elif status >= 300:
            print('-'*50)
            print(man_full_link)
            print("WEBSITE: ",man_link)
            print("IP: ",ip)
            print("[INACTIVE]")
            print('-'*50)
        else:
            print("You Give Wrong Address, please check again....")
    except requests.exceptions.ConnectionError:
        print("Connection Error")
    except urllib3.exceptions.MaxRetryError:
        print("Connection maxed")
    except socket.gaierror:
        print("socker error")
    except urllib3.exceptions.NewConnectionError:
        print("New Connection Error")
    

if choice == '1' or choice == 'Auto' or choice == 'auto':
    print('UserName Found on this Social Sites:')
    num_seq = 0  # for iterate the sequences
    
    thread_auto_choice1 = threading.Thread(target=Auto_choice_P1)
    thread_auto_choice1.start()
    thread_auto_choice2 = threading.Thread(target=Auto_choice_P2)
    thread_auto_choice2.start()
    thread_auto_choice3 = threading.Thread(target=Auto_choice_P3)
    thread_auto_choice3.start()
    thread_auto_choice4 = threading.Thread(target=Auto_choice_P4)
    thread_auto_choice4.start()
    thread_auto_choice5 = threading.Thread(target=Auto_choice_P5)
    thread_auto_choice5.start()
    thread_auto_choice6 = threading.Thread(target=Auto_choice_P6)
    thread_auto_choice6.start()
    thread_auto_choice7 = threading.Thread(target=Auto_choice_P7)
    thread_auto_choice7.start()
    thread_auto_choice8 = threading.Thread(target=Auto_choice_P8)
    thread_auto_choice8.start()
    thread_auto_choice9 = threading.Thread(target=Auto_choice_P9)
    thread_auto_choice9.start()
    thread_auto_choice10 = threading.Thread(target=Auto_choice_P10)
    thread_auto_choice10.start()
    thread_auto_choice11 = threading.Thread(target=Auto_choice_P11)
    thread_auto_choice11.start()
    thread_auto_choice12 = threading.Thread(target=Auto_choice_P12)
    thread_auto_choice12.start()
    thread_auto_choice13 = threading.Thread(target=Auto_choice_P13)
    thread_auto_choice13.start()
    thread_auto_choice14 = threading.Thread(target=Auto_choice_P14)
    thread_auto_choice14.start()
    thread_auto_choice15 = threading.Thread(target=Auto_choice_P15)
    thread_auto_choice15.start()
    
    sys.exit()

elif choice == '2' or choice == 'Manual' or choice == 'manual':
    manual_choice()
    sys.exit()

else:
    print('You Entered Wrong Choice.')

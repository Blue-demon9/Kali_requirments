import os

class Process:
    def update():
        os.system("apt-get dist-upgrade -y")
    def req():
        #os.system("sudo su")
        os.system("dpkg-reconfigure kali-grant-root")
        os.system("update-grub")
        os.system("grep -v '#' /etc/apt/sources.list | sort -u")
        os.system('echo "deb http://http.kali.org/kali kali-rolling main non-free contrib" | sudo tee /etc/apt/sources.list')
        os.system('echo "deb http://http.kali.org/kali kali-last-snapshot main non-free contrib" | sudo tee /etc/apt/sources.list')
        os.system('echo "deb http://http.kali.org/kali kali-experimental main non-free contrib" | sudo tee /etc/apt/sources.list.d/kali-experimental.list')
        os.system('echo "deb-src http://http.kali.org/kali kali-rolling main non-free contrib" | sudo tee -a /etc/apt/sources.list')
        os.system("apt-get update")
        os.system("apt-get install tor tilix adb python3 fastboot android-sdk codelite code -y")
        os.system("apt-get install adb snapd crowbar htop cmatrix lolcat figlet -y")
        os.system("apt install filezilla filezilla-common software-center gdebi -y")
        os.system("clear")
        print("Change the root user password (default is 'kali')")
        os.system("passwd")
        os.system("apt install filezilla filezilla-common codelite gdebi tor scrcpy -y")
        os.system("apt-get upgrade telegram-desktop torbrowser-launcher pyinstaller -y")
        os.system("torbrowser-launcher")
        os.system("apt-get install libavcodec-extra -y")
        os.system("wget http://www.deb-multimedia.org/pool/non-free/w/w64codecs/w64codecs_20071007-dmo2_amd64.deb")
        os.system("dpkg -i w64codecs_20071007-dmo2_amd64.deb")
        os.system("pip install lolcat wpm")
        os.system("clear")
        print("Installing snap packages")
        os.system("systemctl enable --now snapd apparmor")
        choice = input("1.Pycharm-community\n2.Atom\n3.skip\n\nEnter your choice: ")

        if choice == "1":
            os.system("snap install pycharm-community --classic")
        elif choice == "2":
            os.system("snap install atom --classic")
        elif choice == "3":
            pass

        os.system("clear")
        choice = input("Do you want to clone git repositories [Y/N]: ").upper()
        if choice == "Y":
            os.system("cd Documents && mkdir git_files && cd git_files")
            os.system("git clone https://github.com/Manisso/angryip.git")
            os.system("git clone https://github.com/TheDarkRoot/AnonSMS.git")
            os.system("git clone https://github.com/LimerBoy/Impulse.git")
            os.system("git clone https://github.com/FDX100/Auto_Tor_IP_changer.git")
            os.system("cd Auto_Tor_IP_changer && python3 install.py && cd ..")
            os.system("git clone https://github.com/rajkumardusad/IP-Tracer.git ")
            os.system("git clone https://github.com/storm119/Tilix-Themes.git")
            os.system("cd Tilix-Themes && cd Themes && cp * /usr/share/tilix/schemes && cd ..")
            os.system("cd Themes-2 && cp * /usr/share/tilix/schemes && cd ..")
            os.system("git clone https://github.com/Z4nzu/hackingtool.git")
            os.system("chmod 777 hackingtool && cd hackingtool && ./install.sh && cd ..")
            os.system("git clone https://github.com/EntySec/ghost.git")
            os.system("chmod 777 ghost && cd ghost && ./ghost && cd ..")
            os.system("git clone https://github.com/TheSpeedX/TBomb.git")
            os.system("chmod 777 TBomb")
            os.system("git clone https://github.com/htr-tech/zphisher.git")
            os.system("chmod 777 zphisher")
            os.system("git clone https://github.com/v1s1t0r1sh3r3/airgeddon.git")
            os.system("git clone https://github.com/sensepost/kwetza.git")
            os.system("git clone https://github.com/Naategh/PyCk.git")
            os.system("clear")
            c = input("do you want to clone SecList [Y/N]: ").upper()
            if c == "Y":
                os.system("git clone https://github.com/gwen001/SecLists.git")
            else:
                pass
            os.system("clear")
            choice = input("Do you want to install the most used python modules?[Y/N]:").lower()
            if choice == "y":
                os.system("pip install tk kivy requests pygame")
                os.system("pip install wpm lolcat ")
                os.system("pip install aiohttp cchardet aiodns  aiohttp[speedups]")
                os.system("pip install pywin32 keyboard pyautogui")
                os.system("pip install pyinstaller")
                print("color")
                os.system("pip install --upgrade pyspark && pip install --upgrade pyspark")
                os.system(" pip install python-telegram-bot tqdm virtualenv selenium telethon opencv-python pyperclip ipykernel ")



os.system("clear")
print("\033[40m\033[34m")
print("This program will install all the required kali linux tools and other things")
choice = input("1.Install all requirements\n2.update distro 'takes to much time'\n[*]It's recommended to upgrade the distro after installing the requirements\n\nEnter your choice: ")
if choice == "1":
    Process.req()
elif choice == "2":
    Process.update()

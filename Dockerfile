FROM patrickmerlot/gui-with-xvfb


RUN sudo sh -c "echo 'deb http://dl.google.com/linux/chrome/deb/ stable main' >>   /etc/apt/sources.list"
RUN apt-get update && apt-get install -y apt-transport-https
RUN apt-get update && apt purge google-chrome-stable
RUN sudo apt-get update
RUN sudo add-apt-repository ppa:fkrull/deadsnakes
&& sudo apt update \
&& sudo apt install -y python3.6
RUN sudo apt-get update
RUN sudo apt-get install -y  python3-pip
RUN pip install chromedriver-autoinstaller selenium pyvirtualdisplay 
RUN CMD ["python3.6 main.py"]

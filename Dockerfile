FROM patrickmerlot/gui-with-xvfb
RUN sudo apt purge google-chrome-stable
RUN sudo apt-get update
RUN sudo apt-get install python3.6
RUN sudo apt-get install python3-pip
RUN pip install chromedriver-autoinstaller selenium pyvirtualdisplay 
RUN CMD ["python3 main.py"]

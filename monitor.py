from bs4 import BeautifulSoup
from urllib.request import urlopen

# Read and parse the dashboard.
url = 'https://medeco-stashboard.appspot.com/'
content = urlopen(url).read()
soup = BeautifulSoup(content, 'html.parser')

# Find the MXP table row, and look at the second entry in it.
mxp = soup.find(id="mxp")
mxpdivs = mxp.find_all('td')
todays_status = mxpdivs[1].find('img').get('src').split('/')[-1]

# See if the server has been fixed
fixed = False
if todays_status == 'tick-circle.png':
    fixed = True

# 
if fixed:
    # Add the project path to the directory
    import sys
    newpath = r'C:\Users\phiwri\AppData\Local\Programs\Python'
    newpath += r'\Python35-32\Lib\site-packages\pinky_notify'
    sys.path.append(newpath)
    
    # Check to see if it's already done
    from already_done import already_done
    
    if not already_done:
        # Send the email
        import send_pinky_email
        
        # Change the already_done variable
        with open(newpath + r'\already_done.py', 'w') as file:
            file.write('already_done = True')

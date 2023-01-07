"""Main module."""
import os
from urllib.request import urlopen
from shutil import copyfileobj
import datetime
from ._utils import search


class url_block():
    """check the given url is safe

    Attributes:
        Optional filter_url(list): domain based filter url.
            Ex: https://malware-filter.gitlab.io/malware-filter/urlhaus-filter-domains.txt
    """    
    filter_list = []
    


    def __init__(self, filter_url = None):
        filter_url.append("https://malware-filter.gitlab.io/malware-filter/urlhaus-filter-domains.txt")
        self.filter_url = filter_url

        #set tmp dir
        if(os.name == 'nt'):
            self.tmp_dir = os.path.abspath("%USERPROFILE%/AppData/Local/Temp/url_list/")
        else:
            self.tmp_dir = "/tmp/url_list"

        #download url list
        os.makedirs(self.tmp_dir, exist_ok=True)

        dir = os.listdir(self.tmp_dir)

        update_require = False

        if(("last_downloaded" in dir) == False):
            update_require = True
        else:
            today = str(datetime.date.today())

            with open(f"{self.tmp_dir}/last_downloaded") as f:
                s = f.read()
                if(s != today):
                    update_require = True

        if(update_require == True):
            with open(f"{self.tmp_dir}/last_downloaded", mode = "w") as f:
                f.write(str(datetime.date.today()))

            for i in range(len(self.url_list)):
                with urlopen(self.url_list[i]) as input_file, open(f"{self.tmp_dir}/{i}") as output_file:
                    copyfileobj(input_file, output_file)
                    self.filter_list.append(f"{self.tmp_dir}/{i}")

    def check_safe(self, url) -> bool:
        """check the given url is safe

        Args:
            url (str): url you want to check

        Returns:
            bool: if url is safe, return True. else return False
        """        
        ans = True

        for i in self.filter_list:
            if(search(url, self.filter_list[i] == True)):
                ans = False

        return ans

            


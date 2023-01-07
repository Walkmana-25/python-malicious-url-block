"""Main module."""
import os
from urllib.request import urlopen
from shutil import copyfileobj
import datetime

class url_block():
    """check the given url is safe

    Attributes:
        Optional filter_url(list): domain based filter url.
            Ex: https://malware-filter.gitlab.io/malware-filter/urlhaus-filter-domains.txt
    """    
    filter_list = []
    


    def __init__(self, filter_url = None):
        if(type(filter_url) != list):
            filter_url = []
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

        if(("count" in dir) == False):
            update_require = True
        else:
            with open(f"{self.tmp_dir}/count") as f:
                s = f.read()
                if(s != str(len(self.filter_url))):
                    update_require = True
        

        if(update_require == True):
            with open(f"{self.tmp_dir}/last_downloaded", mode = "w") as f:
                f.write(str(datetime.date.today()))

            for i in range(len(self.filter_url)):
                with urlopen(self.filter_url[i]) as input_file, open(f"{self.tmp_dir}/{i}", mode="wb") as output_file:
                    copyfileobj(input_file, output_file)
                    self.filter_list.append(f"{self.tmp_dir}/{i}")

            with open(f"{self.tmp_dir}/count", mode="w") as f:
                f.write(str(len(self.filter_url)))

        else:
            for i in dir:
                if(i == "last_downloaded"):
                    pass
                else:
                    self.filter_list.append(f"{self.tmp_dir}/{i}")

    def check_safe(self, url) -> bool:
        """check the given url is safe

        Args:
            url (str): url you want to check
                Ex: google.com

        Returns:
            bool: if url is safe, return True. else return False
        """        
        ans = True

        for i in self.filter_list:
            import _utils
            if(_utils.search(url, i) == True):
                ans = False

        return ans

            


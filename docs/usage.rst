=====
Usage
=====

To use Python_Malicious_Url_Block in a project::

    from python_malicious_url_block import url_block
    check_url = url_block()

    check_url.check_safe("google.com")
    #It return True

    check_url.check_safe("UNSAFE_URL")
    #it return False



If you want to use another filter::

    from python_malicious_url_block import url_block
    filter_list = [
        "https://malware-filter.gitlab.io/malware-filter/urlhaus-filter-domains.txt"
    ]
    check_url = url_block(filter_url = filter_list)

    check_url.check_safe("google.com")
    #It return True

    check_url.check_safe("UNSAFE_URL")
    #it return False

    

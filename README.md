uh-python3-ldap
===========

LDAP Python 3 Demonstration Program

**Overview**

The program demonstrates how to do a simple LDAP search
of the University of Hawaii LDAP service. 

Note: You must specify your special DN and its password.<br/>
The example run of the program uses the 'filedrop' special DN,
but the value of the password has been removed from the 
checked-in code. The use of the special DN will also require 
the ability to pass through the UH firewall.

**Technology**

The program was developed on Apple Mac OS X 10.10.2,
using python version 3.4.1, pip version 1.5.6, 
and the python3-ldap package version 0.9.7.

**Verify you have Python 3 installed**

    $ python3 --version
    Python 3.4.1

**Verify you have the package manager installed**

    $ pip3 --version
    pip 1.5.6 from /Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/site-packages (python 3.4)

**Install the LDAP module**

    $ pip3 install python3-ldap
    Downloading/unpacking python3-ldap
        Downloading python3_ldap-0.9.7-py3-none-any.whl (281kB): 281kB downloaded
    Downloading/unpacking pyasn1==0.1.7 (from python3-ldap)
        Downloading pyasn1-0.1.7.tar.gz (68kB): 68kB downloaded
        Running setup.py (path:.../pyasn1/setup.py) egg_info for package pyasn1
    
    Installing collected packages: python3-ldap, pyasn1
        Running setup.py install for pyasn1
    
    Successfully installed python3-ldap pyasn1
    Cleaning up...
    

**Running the Program**

Run the program from the command line: 

    $ ./ldaprunner duckart
    vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
    {'cn': ['Frank R Duckart'], 'uhUuid': ['17958670'], 'mail': ['duckart@hawaii.edu', 'frank.duckart@hawaii.edu'], 'uid': ['duckart']}
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can run the program with mutltiple UH usernames: </br>

    $ ./ldaprunner duckart duckart
    vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
    {'cn': ['Frank R Duckart'], 'uhUuid': ['17958670'], 'mail': ['duckart@hawaii.edu', 'frank.duckart@hawaii.edu'], 'uid': ['duckart']}
        ................................
    {'cn': ['Frank R Duckart'], 'mail': ['duckart@hawaii.edu', 'frank.duckart@hawaii.edu'], 'uid': ['duckart'], 'uhUuid': ['17958670']}
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**For More Information**

Contact me via email at duckart@hawaii.edu


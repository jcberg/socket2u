""" Test the get_args module """

from packages.get_args import *

def test_get_logging_level():
    """ Invoke get_logging_level, testing various 'logging' values"""

    logging_level = get_logging_level(logging="7")
    assert logging_level == 7
    logging_level = get_logging_level(logging="debugging")
    assert logging_level == 7
    logging_level = get_logging_level(logging="DEBUGGING")
    assert logging_level == 7

    logging_level = get_logging_level(logging="6")
    assert logging_level == 6
    logging_level = get_logging_level(logging="informational")
    assert logging_level == 6

    logging = "5"
    logging_level = get_logging_level(logging)
    assert logging_level == 5
    logging = "notifications"
    logging_level = get_logging_level(logging)
    assert logging_level == 5

    logging = "4"
    logging_level = get_logging_level(logging)
    assert logging_level == 4
    logging = "warnings"
    logging_level = get_logging_level(logging)
    assert logging_level == 4

    logging = "3"
    logging_level = get_logging_level(logging)
    assert logging_level == 3
    logging = "errors"
    logging_level = get_logging_level(logging)
    assert logging_level == 3

    logging = "2"
    logging_level = get_logging_level(logging)
    assert logging_level == 2
    logging = "critical"
    logging_level = get_logging_level(logging)
    assert logging_level == 2

    logging = "1"
    logging_level = get_logging_level(logging)
    assert logging_level == 1
    logging = "alerts"
    logging_level = get_logging_level(logging)
    assert logging_level == 1

    logging = "0"
    logging_level = get_logging_level(logging)
    assert logging_level == 0
    logging = "emergencies"
    logging_level = get_logging_level(logging)
    assert logging_level == 0

    logging = "8"
    logging_level = get_logging_level(logging)
    assert logging_level == 0
    logging = "unknown"
    logging_level = get_logging_level(logging)
    assert logging_level == 0

def test_get_instance_role():
    """ Invoke get_instance_role, testing various 'role' values"""

    instance_role = get_instance_role(role="receiver", 
                                      instance_logging_level=3)
    assert instance_role == "receiver"
    instance_role = get_instance_role(role="RECEIVER", 
                                      instance_logging_level=3)
    assert instance_role == "receiver"

    instance_role = get_instance_role(role="sender", 
                                      instance_logging_level=3)
    assert instance_role == "sender"

    instance_role = get_instance_role(role="unknown", 
                                      instance_logging_level=3)
    assert instance_role == "receiver"

def test_get_instance_af():
    """ Invoke get_instance_af, testing various 'af' values"""

    instance_af = get_instance_af(af="ipv4", instance_logging_level=3)
    assert instance_af == "ipv4"
    instance_af = get_instance_af(af="IPv4", instance_logging_level=3)
    assert instance_af == "ipv4"

    instance_af = get_instance_af(af="", instance_logging_level=3)
    assert instance_af == ""

    instance_af = get_instance_af(af="ipv5", instance_logging_level=3)
    assert instance_af == ""


def test_get_instance_sndaddr():
    """ Invoke get_instance_sndaddr, testing various 'sndaddr' values"""

    [instance_sndaddr, instance_af] \
        = get_instance_sndaddr(sndaddr="1.2.3.4", instance_logging_level=3)
    assert (instance_sndaddr == "1.2.3.4") and (instance_af == "ipv4")
    

    [instance_sndaddr, instance_af] \
        = get_instance_sndaddr(sndaddr="1.2.3.4.5", instance_logging_level=3)
    assert (instance_sndaddr == "127.0.0.1") and (instance_af == "ipv4")

    [instance_sndaddr, instance_af] \
        = get_instance_sndaddr(sndaddr="1.2.3.432", instance_logging_level=3)
    assert (instance_sndaddr == "127.0.0.1") and (instance_af == "ipv4")


def test_get_instance_rcvaddr():
    """ Invoke get_instance_rcvaddr, testing various 'rcvaddr' values"""

    [instance_rcvaddr, instance_af] \
        = get_instance_rcvaddr(rcvaddr="", instance_logging_level=3)
    assert (instance_rcvaddr == "") and (instance_af == "ipv4")

    [instance_rcvaddr, instance_af] \
        = get_instance_rcvaddr(rcvaddr="1.2.3.4", instance_logging_level=3)
    assert (instance_rcvaddr == "1.2.3.4") and (instance_af == "ipv4")

    [instance_rcvaddr, instance_af] \
        = get_instance_rcvaddr(rcvaddr="1.2.3.4.5", instance_logging_level=3)
    assert (instance_rcvaddr == "") and (instance_af == "ipv4")


def test_get_instance_sndport():
    """ Invoke get_instance_sndport, testing various 'sndport' values"""

    instance_sndport = get_instance_sndport(sndport="0", 
                                            instance_logging_level=3)
    assert instance_sndport == 0
    
    instance_sndport = get_instance_sndport(sndport="12345", 
                                            instance_logging_level=3)
    assert instance_sndport == 12345

    instance_sndport = get_instance_sndport(sndport="65535", 
                                            instance_logging_level=3)
    assert instance_sndport == 65535

    instance_sndport = get_instance_sndport(sndport="", 
                                            instance_logging_level=3)
    assert instance_sndport == 65432

    instance_sndport = get_instance_sndport(sndport="123456", 
                                            instance_logging_level=3)
    assert instance_sndport == 65432

    instance_sndport = get_instance_sndport(sndport="abc123", 
                                            instance_logging_level=3)
    assert instance_sndport == 65432

    instance_sndport = get_instance_sndport(sndport="-12345", 
                                            instance_logging_level=3)
    assert instance_sndport == 65432


def test_get_instance_rcvport():
    """ Invoke get_instance_rcvport, testing various 'rcvport' values"""

    instance_rcvport = get_instance_rcvport(rcvport="0", 
                                            instance_logging_level=3)
    assert instance_rcvport == 0
    
    instance_rcvport = get_instance_rcvport(rcvport="12345", 
                                            instance_logging_level=3)
    assert instance_rcvport == 12345

    instance_rcvport = get_instance_rcvport(rcvport="65535", 
                                            instance_logging_level=3)
    assert instance_rcvport == 65535

    instance_rcvport = get_instance_rcvport(rcvport="", 
                                            instance_logging_level=3)
    assert instance_rcvport == 65432

    instance_rcvport = get_instance_rcvport(rcvport="123456", 
                                            instance_logging_level=3)
    assert instance_rcvport == 65432

    instance_rcvport = get_instance_rcvport(rcvport="abc123", 
                                            instance_logging_level=3)
    assert instance_rcvport == 65432

    instance_rcvport = get_instance_rcvport(rcvport="-12345", 
                                            instance_logging_level=3)
    assert instance_rcvport == 65432


def test_get_instance_ipprot():
    """ Invoke get_instance_ipprot, testing various 'ipprot' values"""

    instance_ipprot = get_instance_ipprot(ipprot="tcp", 
                                          instance_logging_level=3)
    assert instance_ipprot == "tcp"
    instance_ipprot = get_instance_ipprot(ipprot="TCP", 
                                          instance_logging_level=3)
    assert instance_ipprot == "tcp"

    instance_ipprot = get_instance_ipprot(ipprot="udp", 
                                          instance_logging_level=3)
    assert instance_ipprot == "tcp"

    instance_ipprot = get_instance_ipprot(ipprot="", 
                                          instance_logging_level=3)
    assert instance_ipprot == "tcp"

    instance_ipprot = get_instance_ipprot(ipprot="TCP", 
                                          instance_logging_level=3)
    assert instance_ipprot == "tcp"

    instance_ipprot = get_instance_ipprot(ipprot="123", 
                                          instance_logging_level=3)
    assert instance_ipprot == "tcp"


def test_get_instance_repeat():
    """ Invoke get_instance_repeat, testing various 'repeat' values"""

    instance_repeat = get_instance_repeat(repeat="text", instance_logging_level=3)
    assert instance_repeat == 1

    instance_repeat = get_instance_repeat(repeat="-1", instance_logging_level=3)
    assert instance_repeat == 1

    instance_repeat = get_instance_repeat(repeat="0", instance_logging_level=3)
    assert instance_repeat == 1

    instance_repeat = get_instance_repeat(repeat="1", instance_logging_level=3)
    assert instance_repeat == 1

    instance_repeat = get_instance_repeat(repeat="2", instance_logging_level=3)
    assert instance_repeat == 2

    instance_repeat = get_instance_repeat(repeat="999", instance_logging_level=3)
    assert instance_repeat == 999

    instance_repeat = get_instance_repeat(repeat="3.14159", instance_logging_level=3)
    assert instance_repeat == 1


def test_get_instance_sndmessage():
    """ Invoke get_instance_sndmessage, testing various 'sndmessage' values"""

    instance_sndmessage = get_instance_sndmessage(sndmessage="", instance_logging_level=3)
    assert instance_sndmessage == "Hello world!"

    instance_sndmessage = get_instance_sndmessage(sndmessage="Hello network!", instance_logging_level=3)
    assert instance_sndmessage == "Hello network!"
""" Test the instantiate_roles module """

from packages.instantiate_roles import *

'''
def test_instantiate_receiver():
    """ Invoke instantiate_receiver, testing various argument values """

    receiver_copacetic = instantiate_receiver(instance_af="ipv4",
                                              instance_rcvaddr="",
                                              instance_rcvport=54321,
                                              instance_ipprot="tcp",
                                              instance_logging_level=0)
    assert receiver_copacetic

    receiver_copacetic = instantiate_receiver(instance_af="ipv4",
                                              instance_rcvaddr="127.0.0.1",
                                              instance_rcvport=54321,
                                              instance_ipprot="tcp",
                                              instance_logging_level=0)
    assert receiver_copacetic    

    receiver_copacetic = instantiate_receiver(instance_af="ipv5",
                                              instance_rcvaddr="",
                                              instance_rcvport=54321,
                                              instance_ipprot="tcp",
                                              instance_logging_level=0)
    assert not receiver_copacetic

    receiver_copacetic = instantiate_receiver(instance_af="ipv4",
                                              instance_rcvaddr="",
                                              instance_rcvport=54321,
                                              instance_ipprot="xyz",
                                              instance_logging_level=0)
    assert not receiver_copacetic 

'''

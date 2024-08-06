""" Utilities for exploring and prototyping packet network \
    communications over socket interfaces """

import argparse
from packages.get_args import *
from packages.instantiate_roles import *

def main():
    """ Retrieve & validate arguments, set defaults, and launch \
        initial helper functions. """

    # Initialize variables
    logging = "3"
    role = ""
    af = ""
    sndaddr = ""
    rcvaddr = ""
    sndport = ""
    rcvport = ""
    ipprot = ""
    repeat = ""
    sndmessage = ""

    parser = argparse.ArgumentParser()
    parser.add_argument("--logging", help="set your Logging Level: 0-7 \
                        (Default: 6 [=informational])")
    parser.add_argument("--role", help="set your instance Role: [sender | \
                        receiver] (Default: receiver)")
    parser.add_argument("--af", help="set your instance Address Family: \
                        ipv4 (Defaults to AF of IP address)")
    parser.add_argument("--sndaddr", help="set IP Address to send data: \
                        [d.d.d.d | h:h:h:h:h:h] (Default: 127.0.0.1)")
    parser.add_argument("--rcvaddr", help="set IP address to receive data: \
                        [d.d.d.d | h:h:h:h:h:h] (Default: All host addresses)")
    parser.add_argument("--sndport", help="set UDP/TCP port to send data: \
                        [0 - 65535] (Default: 65432)")
    parser.add_argument("--rcvport", help="set UDP/TCP port to receive data: \
                        [0 - 65535] (Default: 65432)")
    parser.add_argument("--ipprot", help="set your IP protocol: \
                        [tcp] (Default: tcp)")
    parser.add_argument("--repeat", help="send message count: \
                        [positive integer] (Default: 1)")
    parser.add_argument("--sndmessage", help="message to send: \
                        [character string] (Default: 'Hello world!')")
    cli_args = parser.parse_args()
    
    if cli_args.logging:
        logging = cli_args.logging
    if cli_args.role:
        role = cli_args.role
    if cli_args.af:
        af = cli_args.af
    if cli_args.sndaddr:
        sndaddr = cli_args.sndaddr
    if cli_args.rcvaddr:
        rcvaddr = cli_args.rcvaddr
    if cli_args.sndport:
        sndport = cli_args.sndport
    if cli_args.rcvport:
        rcvport = cli_args.rcvport
    if cli_args.ipprot:
        ipprot = cli_args.ipprot
    if cli_args.repeat:
        repeat = cli_args.repeat
    if cli_args.sndmessage:
        sndmessage = cli_args.sndmessage

    instance_logging_level = get_logging_level(logging)
    instance_role = get_instance_role(role, instance_logging_level)
    instance_af = get_instance_af(af, instance_logging_level)
    instance_sndaddr, instance_af = get_instance_sndaddr(sndaddr, 
                                                         instance_logging_level)
    instance_rcvaddr, instance_af = get_instance_rcvaddr(rcvaddr, 
                                                         instance_logging_level)
    instance_sndport = get_instance_sndport(sndport, instance_logging_level)
    instance_rcvport = get_instance_rcvport(rcvport, instance_logging_level)
    instance_ipprot = get_instance_ipprot(ipprot, instance_logging_level)
    instance_repeat = get_instance_repeat(repeat, instance_logging_level)
    instance_sndmessage = get_instance_sndmessage(sndmessage, 
                                                  instance_logging_level)

    if instance_role == "receiver":
        receiver_copacetic = instantiate_receiver(instance_af, 
                                                  instance_rcvaddr,
                                                  instance_rcvport, 
                                                  instance_ipprot, 
                                                  instance_logging_level)
        if (not receiver_copacetic) and instance_logging_level >= 1:
            print(f'Unrecoverable error in instantiating receiver')
    elif instance_role == "sender":
        sender_copacetic = instantiate_sender(instance_af, 
                                                  instance_sndaddr,
                                                  instance_sndport, 
                                                  instance_ipprot, 
                                                  instance_repeat,
                                                  instance_sndmessage,
                                                  instance_logging_level)
        if (not sender_copacetic) and instance_logging_level >= 1:
            print(f'Unrecoverable error in instantiating sender')

if __name__ == "__main__":
    main()



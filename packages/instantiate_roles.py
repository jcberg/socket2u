""" Instantiate socket2u role based on invoking arguments """

def instantiate_receiver(instance_af, 
                         instance_rcvaddr,
                         instance_rcvport, 
                         instance_ipprot, 
                         instance_logging_level):
    """ Instantiate receiver process. Return False if unrecoverable error. """

    import socket
        
    if instance_logging_level == 7:
        print(f'instantiate_receiver function invoked with parameters '\
              f'"instance_af" = "{instance_af}", ' \
              f'"instance_rcvaddr" = "{instance_rcvaddr}", ' \
              f'"instance_rcvport" = "{instance_rcvport}", ' \
              f'and "instance_ipprot" = "{instance_ipprot}".')

    function_copacetic = True
    loopback_int = "127.0.0.1"
    all_int = ""

    if (instance_af == "ipv4") and (instance_ipprot == "tcp"):
        # create a IPv4/TCP socket object named "receiver" 
        if instance_logging_level == 7:
            print(f'instantiate_receiver function creating receiver socket '\
                  f"object with ipv4 Address Family and tcp IP Protocol.")
        receiver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # bind the receiver socket object to the IPv4 address and TCP port        
        if instance_logging_level == 7:
            print(f'instantiate_receiver function binding receiver socket '\
                  f'object to ipv4 address "{instance_rcvaddr}" '\
                  f'and tcp port "{instance_rcvport}".')
        receiver.bind((instance_rcvaddr, instance_rcvport))

        # listen for incoming connections on the receiver socket object        
        if instance_logging_level >= 5:
            print(f'receiver listening on '\
                  f'ipv4 address "{instance_rcvaddr}" '\
                  f'and tcp port "{instance_rcvport}".')        
        receiver.listen(0)
        
        # wait for connection from sender, create new socket "sender_socket"
        if instance_logging_level >= 5:
            print(f'Waiting on connection from sender.')
        sender_socket, sender_addr = receiver.accept()
        if instance_logging_level >= 5:
            print(f'Accepted connection from '\
                  f'{sender_addr[0]}:{sender_addr[1]}')

        # receive data from the sender over the newly created sender_socket
        while True:
            rcvdata = sender_socket.recv(1024)
            rcvdata = rcvdata.decode("utf-8")  # convert bytes to string
            # break out of the loop upon receipt of "close" from sender
            if rcvdata.lower() == "close":
                if instance_logging_level == 7:
                    print(f'instantiate_receiver function received "close" '\
                          f'request from sender. Acknowledging request.')
                # ack the close request with "closed"
                sender_socket.send("closed".encode("utf-8"))
                break
            if instance_logging_level >= 5:
                print(f'Received from sender: "{rcvdata}"')

            response = "ack".encode("utf-8")  # convert string to bytes
            if instance_logging_level == 7:
                print(f'instantiate_receiver function responding with "ack" '\
                      f'to sender.')
            sender_socket.send(response)

        # close the connection after breaking out of the while-loop
        if instance_logging_level >= 5:
            print(f'Closing connection in response to sender close request.')
        sender_socket.close()
        # close the receiver socket object
        receiver.close()

    else:
        function_copacetic = False

    if instance_logging_level == 7:
        print(f'instantiate_receiver function returning '\
              f'function_copacetic value of {function_copacetic}') 
    return(function_copacetic)


def instantiate_sender(instance_af, 
                         instance_sndaddr,
                         instance_sndport, 
                         instance_ipprot, 
                         instance_repeat,
                         instance_sndmessage,
                         instance_logging_level):
    """ Instantiate sender process. Return False if unrecoverable error. """

    import socket
        
    if instance_logging_level == 7:
        print(f'instantiate_sender function invoked with parameters '\
              f'"instance_af" = "{instance_af}", ' \
              f'"instance_sndaddr" = "{instance_sndaddr}", ' \
              f'"instance_sndport" = "{instance_sndport}", ' \
              f'"instance_ipprot" = "{instance_ipprot}", ' \
              f'"instance_sndmessage" = "{instance_sndmessage}", ' \
              f'and "instance_repeat" = "{instance_repeat}".')
    
    function_copacetic = True
    #sndmsg = "Hello World!"
    close_message = "close"

    if (instance_af == "ipv4") and (instance_ipprot == "tcp"):
        # create a IPv4/TCP socket object named "sender" 
        if instance_logging_level == 7:
            print(f'instantiate_sender function creating sender socket '\
                  f"object with ipv4 Address Family and tcp IP Protocol.")
        sender = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # send connection request to receiver
        if instance_logging_level >= 5:
            print(f'sender connecting on '\
                  f'ipv4 address "{instance_sndaddr}" '\
                  f'and tcp port "{instance_sndport}".')
        sender.connect((instance_sndaddr, instance_sndport))

        # repeat sending message to receiver 
        for count in range (instance_repeat):
            if instance_logging_level >= 5:
                print(f'{count+1} '\
                      f'sending message "{instance_sndmessage}" to receiver')
            sender.send(instance_sndmessage.encode("utf-8")[:1024])

            # wait for message from receiver
            rcvmessage = sender.recv(1024)
            rcvmessage = rcvmessage.decode("utf-8")
            if instance_logging_level >= 6:
                print(f'received message "{rcvmessage}" from receiver')

        # send "close" message to receiver
        if instance_logging_level >= 5:
            print(f'sending "close" message to receiver')
        sender.send(close_message.encode("utf-8")[:1024])

        # close the sender socket object
        sender.close()
        if instance_logging_level >= 5:
            print(f'socket connection to receiver closed')

    else:
        function_copacetic = False
    
    if instance_logging_level == 7:
        print(f'instantiate_sender function returning '\
              f'function_copacetic value of {function_copacetic}')
    return(function_copacetic)
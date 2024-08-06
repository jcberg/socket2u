""" Return validated CLI arguments """

def get_logging_level(logging):
    """ Return validated numeric instance_logging_level value based on \
        alphanumeric 'logging' parameter"""

    logging = logging.lower()

    if (logging == "7") or (logging == "debugging"):
        instance_logging_level = 7
    elif (logging == "6") or (logging == "informational"):
        instance_logging_level = 6
    elif (logging == "5") or (logging == "notifications"):
        instance_logging_level = 5
    elif (logging == "4") or (logging == "warnings"):
        instance_logging_level = 4
    elif (logging == "3") or (logging == "errors"):
        instance_logging_level = 3
    elif (logging == "2") or (logging == "critical"):
        instance_logging_level = 2
    elif (logging == "1") or (logging == "alerts"):
        instance_logging_level = 1
    elif (logging == "0") or (logging == "emergencies"):
        instance_logging_level = 0
    else:
        print(f'Unknown logging value, defaulting to "6" (informational)')
        instance_logging_level = 0

    if instance_logging_level == 7:
        print(f'get_logging_level returning instance_logging_level value of', \
              instance_logging_level)
    return instance_logging_level


def get_instance_role(role, instance_logging_level):
    """ Return validated instance role string based on alphanumeric 'role' \
        parameter"""

    if instance_logging_level == 7:
        print(f'get_instance_role function invoked with parameters '\
              f' "role" = "{role}"'\
              f' and "logging_level" = {instance_logging_level}')
        
    role = role.lower()
    valid_roles = ["receiver", "sender"]
    if role in valid_roles:
        instance_role = role
    elif instance_logging_level >= 6:
        print(f'Unknown instance role {role}. Defaulting to "receiver"' \
              f' role.')
        instance_role = "receiver"
    else:
        instance_role = "receiver"

    if instance_logging_level == 7:
        print(f'get_instance_role returning instance_role value of', \
              f'"{instance_role}".')
    return(instance_role)


def get_instance_af(af, instance_logging_level):
    """ Return instance address family string based on alphanumeric \
        'af' parameter"""

    if instance_logging_level == 7:
        print(f'get_instance_af function invoked with parameters'\
              f'"af" = "{af}"' \
              f' and "instance_logging_level" = {instance_logging_level}')

    af = af.lower()
    valid_afs = ["ipv4"]
    if af in valid_afs:
        instance_af = af
    elif instance_logging_level >= 6:
        print(f'get_instance_af: Unknown instance address family "{af}". ' \
              f'Initial af is null string.')
        instance_af = ""
    else:
        instance_af = ""

    if instance_logging_level == 7:
        print(f'get_instance_af returning instance_af value of ', \
              f'"{instance_af}".')
    return(instance_af)


def get_instance_sndaddr(sndaddr, instance_logging_level):
    """ Return instance send IP address string based on alphanumeric \
        'sndaddr' parameter"""
    
    import ipaddress
    
    if instance_logging_level == 7:
        print(f'get_instance_sndaddr function invoked')
        print(f'get_instance_sndaddr recevied parameters "sndaddr" = ' \
              f'"{sndaddr}"' \
              f' and "instance_logging_level" = {instance_logging_level}')
        

    if "." in sndaddr:
        try:
            sndaddr_object = ipaddress.ip_address(sndaddr)
            valid_sndaddr = True
            instance_sndaddr = sndaddr
            instance_af = "ipv4"
            if instance_logging_level >= 6:
                print(f'get_instance_sndaddr: {sndaddr} validated as IPv4' \
                      ' address')
        except ValueError:
            valid_sndaddr = False

    else:
        valid_sndaddr = False


    if not valid_sndaddr:
        instance_sndaddr = "127.0.0.1"
        instance_af = "ipv4"
        if instance_logging_level >= 6:
            print(f'get_instance_sndaddr: "{sndaddr}" is not a valid IPv4' \
                  f' address. Defaulting to 127.0.0.1, AF=IPv4')
    
    if instance_logging_level == 7:
        print(f'get_instance_sndaddr returning instance_sndaddr value of', \
              f'"{instance_sndaddr}" and instance_af value of "{instance_af}"')
    return(instance_sndaddr, instance_af)


def get_instance_rcvaddr(rcvaddr, instance_logging_level):
    """ Return instance receive IP address string based on alphanumeric \
        'rcvaddr' parameter"""
    
    import ipaddress

    if instance_logging_level == 7:
        print(f'get_instance_rcvaddr function invoked with parameters' \
              f'"rcvaddr" = "{rcvaddr}" ' \
              f'and "instance_logging_level" = {instance_logging_level}')

    if "." in rcvaddr:
        try:
            rcvaddr_object = ipaddress.ip_address(rcvaddr)
            valid_rcvaddr = True
            instance_rcvaddr = rcvaddr
            instance_af = "ipv4"
            if instance_logging_level >= 6:
                print(f'get_instance_rcvaddr: {rcvaddr} validated as IPv4' \
                      ' address')
        except ValueError:
            valid_rcvaddr = False

    else:
        valid_rcvaddr = False
    
    if not valid_rcvaddr:
        instance_rcvaddr = ""
        instance_af = "ipv4"
        if instance_logging_level >= 6:
            print(f'get_instance_rcvaddr: "{rcvaddr}" is not a valid IPv4' \
                  f' address. Defaulting to all host IP addresses, AF=IPv4')

    if instance_logging_level == 7:
        print(f'get_instance_rcvaddr returning instance_rcvaddr value of', \
              f'"{instance_rcvaddr}" and instance_af value of "{instance_af}"')
    return(instance_rcvaddr, instance_af)


def get_instance_sndport(sndport, instance_logging_level):
    """ Return validated destination port string based on alphanumeric \
        'sndport' parameter"""
    
    if instance_logging_level == 7:
        print(f'get_instance_sndport function invoked with parameters '\
              f'"sndport" = "{sndport}" ' \
              f'and "instance_logging_level" = "{instance_logging_level}"')
    
    if sndport.isdigit():
        instance_sndport = int(sndport)
        if (instance_sndport >= 0) and (instance_sndport <= 65535):
            valid_sndport = True
        else:
            valid_sndport = False
    else:
        valid_sndport = False

    if not valid_sndport:
        instance_sndport = 65432
        if instance_logging_level >= 6:
            print(f'get_instance_sndport: "{sndport}" is not a valid port. ' \
                  f'Defaulting to 65432.')

    if instance_logging_level == 7:
        print(f'get_instance_sndport returning instance_sndport value of', \
              f'{instance_sndport}.')
    return(instance_sndport)


def get_instance_rcvport(rcvport, instance_logging_level):
    """ Return validated source port string based on alphanumeric \
        'rcvport' parameter"""
    
    if instance_logging_level == 7:
        print(f'get_instance_rcvport function invoked with parameters '\
              f'"rcvport" = "{rcvport}" ' \
              f'and "instance_logging_level" = "{instance_logging_level}"')
    
    valid_rcvport = False
    if rcvport.isdigit():
        instance_rcvport = int(rcvport)
        if (instance_rcvport >= 0) and (instance_rcvport <= 65535):
            valid_rcvport = True

    if not valid_rcvport:
        instance_rcvport = 65432
        if instance_logging_level >= 6:
            print(f'get_instance_rcvport: "{rcvport}" is not a valid port. ' \
                  f'Defaulting to 65432.')

    if instance_logging_level == 7:
        print(f'get_instance_rcvport returning instance_sndport value of', \
              f'{instance_rcvport}.')
    return(instance_rcvport)


def get_instance_ipprot(ipprot, instance_logging_level):
    """ Return validated IP protocol string based on alphanumeric \
        'ipprot' parameter"""
    
    if instance_logging_level == 7:
        print(f'get_instance_ipprot function invoked with parameters '\
              f'"ipprot" = "{ipprot}" ' \
              f'and "instance_logging_level" = "{instance_logging_level}"')
        
    ipprot = ipprot.lower()
    valid_ipprots = ["tcp"]
    if ipprot in valid_ipprots:
        instance_ipprot = ipprot
    elif instance_logging_level >= 6:
        print(f'Unknown instance IP protocol {ipprot}. Defaulting to "tcp"' \
              f' protocol.')
        instance_ipprot = "tcp"
    else:
        instance_ipprot = "tcp"

    if instance_logging_level == 7:
        print(f'get_instance_ipprot returning instance_ipprot value of', \
              f'{instance_ipprot}.')
    return(instance_ipprot)

def get_instance_repeat(repeat, instance_logging_level):
    """ Return validated repeat count integer based on alphanumeric \
        'repeat' parameter"""
    
    if instance_logging_level == 7:
        print(f'get_instance_repeat function invoked with parameters '\
              f'"repeat" = "{repeat}" ' \
              f'and "instance_logging_level" = "{instance_logging_level}"')
    
    valid_repeat = False
    if repeat.isdigit():    # check that repeat count is a number
        instance_repeat = int(repeat)
        if (instance_repeat > 0):
            valid_repeat = True
    
    if not valid_repeat:
        instance_repeat = 1
        if instance_logging_level >= 6:
            print(f'get_instance_repeat: "{repeat}" is not a valid repeat ' \
                  f'count. Defaulting to 1.')
            
    if instance_logging_level == 7:
        print(f'get_instance_repeat returning instance_repeat value of', \
              f'{instance_repeat}.')
    return(instance_repeat)

def get_instance_sndmessage(sndmessage, instance_logging_level):
    """ Return validated send message string based on alphanumeric \
        'sndmessage' parameter"""
    
    if instance_logging_level == 7:
        print(f'get_instance_sndmessage function invoked with parameters '\
              f'"sndmessage" = "{sndmessage}" ' \
              f'and "instance_logging_level" = "{instance_logging_level}"')
    
    valid_sndmessage = False
    if sndmessage:    # check for null string
        instance_sndmessage = sndmessage
        valid_sndmessage = True
    
    if not valid_sndmessage:
        instance_sndmessage = "Hello world!"
        if instance_logging_level >= 6:
            print(f'get_instance_sndmessage: "{sndmessage}" is not a valid '\
                  f'string count. Defaulting to "Hello world!".')
            
    if instance_logging_level == 7:
        print(f'get_instance_sndmessage returning instance_sndmessage string '\
              f'of "{instance_sndmessage}".')
    return(instance_sndmessage)
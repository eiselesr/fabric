import fabric.api as fabi

hosts ={'bbb-c434': '172.21.20.9', 'bbb-b4bc': '172.21.20.33',
        'bbb-a327': '172.21.20.15', 'bbb-235d': '172.21.20.42',
        'bbb-e1ec': '172.21.20.14', 'bbb-a702': '172.21.20.46',
        'bbb-4c23': '172.21.20.55', 'bbb-8014': '172.21.20.57',
        'bbb-29a6': '172.21.20.11', 'bbb-6302': '172.21.20.54',
        'bbb-5eb7': '172.21.20.48', 'bbb-1b70': '172.21.20.47',
        'bbb-ed97': '172.21.20.36', 'bbb-41b1': '172.21.20.18',
        'bbb-99b4': '172.21.20.45', 'bbb-7d6a': '172.21.20.56',
        'bbb-bce4': '172.21.20.38', 'bbb-c189': '172.21.20.39',
        'bbb-c452': '172.21.20.10', 'bbb-c473': '172.21.20.44',
        'bbb-e4ff': '172.21.20.12', 'bbb-2592': '172.21.20.17',
        'bbb-96af': '172.21.20.37', 'bbb-50c9': '172.21.20.16',
        'bbb-95f9': '172.21.20.41', 'bbb-ede8': '172.21.20.13',
        'bbb-b957': '172.21.20.43', 'bbb-bcf6': '172.21.20.40'}



IPS = ['172.21.20.9', '172.21.20.10', '172.21.20.11', '172.21.20.12',
       '172.21.20.13', '172.21.20.14', '172.21.20.15', '172.21.20.16',
       '172.21.20.17', '172.21.20.18', '172.21.20.33', '172.21.20.36',
       '172.21.20.37', '172.21.20.38', '172.21.20.39', '172.21.20.40',
       '172.21.20.41', '172.21.20.42', '172.21.20.43', '172.21.20.44',
       '172.21.20.45', '172.21.20.46', '172.21.20.47', '172.21.20.48',
       '172.21.20.54', '172.21.20.55', '172.21.20.56', '172.21.20.57']

kibana={'bbb-c434': '172.21.20.9',
        'bbb-a327': '172.21.20.15', 'bbb-235d': '172.21.20.42',
        'bbb-e1ec': '172.21.20.14', 'bbb-a702': '172.21.20.46',
        'bbb-4c23': '172.21.20.55', 'bbb-8014': '172.21.20.57',
        'bbb-29a6': '172.21.20.11', 'bbb-6302': '172.21.20.54',
        'bbb-5eb7': '172.21.20.48', 'bbb-1b70': '172.21.20.47',
        'bbb-ed97': '172.21.20.36', 'bbb-41b1': '172.21.20.18',
        'bbb-99b4': '172.21.20.45', 'bbb-7d6a': '172.21.20.56',
        'bbb-bce4': '172.21.20.38', 'bbb-c189': '172.21.20.39',
        'bbb-c452': '172.21.20.10', 'bbb-c473': '172.21.20.44',
        'bbb-e4ff': '172.21.20.12', 'bbb-2592': '172.21.20.17',
        'bbb-96af': '172.21.20.37', 'bbb-50c9': '172.21.20.16',
        'bbb-95f9': '172.21.20.41', 'bbb-ede8': '172.21.20.13',
        'bbb-b957': '172.21.20.43', 'bbb-bcf6': '172.21.20.40'}



ALL = list(hosts.values())
KIBANA= list(kibana.values())


fabi.env.roledefs = {
    'ALL' : ALL,
    'IPS' :IPS,
    'KIB' : KIBANA
}
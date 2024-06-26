expected_output = {
	'entries_name': {
		'ACL Drop': {
			'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 1931,
            'cir_sw': 2000,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-default',
            'pri': 1,
            'source': 'TRAP',
            'tc': 2
	    },
		'ACL LOG': {
			'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 1931,
            'cir_sw': 2000,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-default',
            'pri': 0,
            'source': 'TRAP',
            'tc': 2
        },
		'ARP': {
		'bytes_a': 0,
        'bytes_d': 0,
        'cir_hw': 965,
        'cir_sw': 1000,
        'pkts_a': 0,
        'pkts_d': 0,
        'policy': 'system-cpp-police-arp',
        'pri': 4,
        'source': 'MIRROR',
        'tc': 4
        },
		'ARP Snooping': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 1931,
            'cir_sw': 2000,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-proto-snoop-v4',
            'pri': 3,
            'source': 'TRAP',
            'tc': 3
        },
		'BFD ECHO IPv4': {
            'bytes_a': 676,
            'bytes_d': 0,
            'cir_hw': 5793,
            'cir_sw': 6000,
            'pkts_a': 6,
            'pkts_d': 0,
            'policy': 'system-cpp-police-bfd-v4',
            'pri': 19,
            'source': 'LPTSv4',
            'tc': 6
        },
		'BFD ECHO IPv6': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 5793,
            'cir_sw': 6000,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-bfd-v6',
            'pri': 20,
            'source': 'LPTSv6',
            'tc': 6
        },
		'BFD IPv4': {
            'bytes_a': 676,
            'bytes_d': 0,
            'cir_hw': 5793,
            'cir_sw': 6000,
            'pkts_a': 6,
            'pkts_d': 0,
            'policy': 'system-cpp-police-bfd-v4',
            'pri': 18,
            'source': 'LPTSv4',
            'tc': 6
        },
		'BFD IPv6': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 5793,
            'cir_sw': 6000,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-bfd-v6',
            'pri': 19,
            'source': 'LPTSv6',
            'tc': 6
        },
		'BFD MHOP IPv4': {
            'bytes_a': 676,
            'bytes_d': 0,
            'cir_hw': 5793,
            'cir_sw': 6000,
            'pkts_a': 6,
            'pkts_d': 0,
            'policy': 'system-cpp-police-bfd-v4',
            'pri': 20,
            'source': 'LPTSv4',
            'tc': 6
        },
		'BFD MHOP IPv6': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 5793,
            'cir_sw': 6000,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-bfd-v6',
            'pri': 21,
            'source': 'LPTSv6',
            'tc': 6
        },
		'BGP IPv4': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 5793,
            'cir_sw': 6000,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-bgp-v4',
            'pri': 8,
            'source': 'LPTSv4',
            'tc': 5
        },
		'BGP IPv6': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 5793,
            'cir_sw': 6000,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-bgp-v6',
            'pri': 9,
            'source': 'LPTSv6',
            'tc': 5
        },
		'BGP established IPv4': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 5793,
            'cir_sw': 6000,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-bgp-v4',
            'pri': 9,
            'source': 'LPTSv4',
            'tc': 5
        },
		'BGP established IPv6': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 5793,
            'cir_sw': 6000,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-bgp-v6',
            'pri': 10,
            'source': 'LPTSv6',
            'tc': 5
        },
		'CISCO Protocols': {
            'bytes_a': 586,
            'bytes_d': 0,
            'cir_hw': 15449,
            'cir_sw': 16000,
            'pkts_a': 5,
            'pkts_d': 0,
            'policy': 'system-cpp-police-l2-control',
            'pri': 3,
            'source': 'TRAP',
            'tc': 5
        },
		'DHCP Client(v4)': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 5793,
            'cir_sw': 6000,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-dhcp-v4',
            'pri': 3,
            'source': 'TRAP',
            'tc': 4
        },
		'DHCP Client(v6)': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 5793,
            'cir_sw': 6000,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-dhcp-v6',
            'pri': 3,
            'source': 'TRAP',
            'tc': 4
        },
		'DHCP Server(v4)': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 5793,
            'cir_sw': 6000,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-dhcp-v4',
            'pri': 3,
            'source': 'TRAP',
            'tc': 4
        },
		'DHCP Server(v6)': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 5793,
            'cir_sw': 6000,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-dhcp-v6',
            'pri': 3,
            'source': 'TRAP',
            'tc': 4
        },
		'DHCP Snooping': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 965,
            'cir_sw': 1000,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-dhcp-snooping',
            'pri': 3,
            'source': 'TRAP',
            'tc': 3
        },
		'DHCP(mirror)': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 5793,
            'cir_sw': 6000,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-dhcp-v4',
            'pri': 3,
            'source': 'MIRROR',
            'tc': 4
        },
		'DHCPv4 C to S': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 583,
            'cir_sw': 600,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-udp-v4',
            'pri': 24,
            'source': 'LPTSv4',
            'tc': 0
        },
		'DHCPv4 S to C': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 583,
            'cir_sw': 600,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-udp-v4',
            'pri': 25,
            'source': 'LPTSv4',
            'tc': 0
        },
		'DHCPv4 S to S': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 583,
            'cir_sw': 600,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-udp-v4',
            'pri': 23,
            'source': 'LPTSv4',
            'tc': 4
        },
		'DHCPv4 Server TCP Bulk Query': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 965,
            'cir_sw': 1000,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-tcp-v4',
            'pri': 22,
            'source': 'LPTSv4',
            'tc': 4
        },
		'DHCPv6 C to S': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 583,
            'cir_sw': 600,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-udp-v6',
            'pri': 24,
            'source': 'LPTSv6',
            'tc': 0
        },
		'DHCPv6 S to C': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 583,
            'cir_sw': 600,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-udp-v6',
            'pri': 25,
            'source': 'LPTSv6',
            'tc': 0
        },
		'DHCPv6 S to S': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 583,
            'cir_sw': 600,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-udp-v6',
            'pri': 23,
            'source': 'LPTSv6',
            'tc': 4
        },
		'DHCPv6 Server TCP Bulk Query': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 965,
            'cir_sw': 1000,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-tcp-v6',
            'pri': 22,
            'source': 'LPTSv6',
            'tc': 4
        },
		'EIGRP IPV6': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 965,
            'cir_sw': 1000,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-igrp-v6',
            'pri': 12,
            'source': 'LPTSv6',
            'tc': 5
        },
		'EIGRP IPv4': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 965,
            'cir_sw': 1000,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-igrp-v4',
            'pri': 11,
            'source': 'LPTSv4',
            'tc': 5
        },
		'ETH HOP-OPT': {
            'bytes_a': 155,
            'bytes_d': 0,
            'cir_hw': 1931,
            'cir_sw': 2000,
            'pkts_a': 1,
            'pkts_d': 0,
            'policy': 'system-cpp-police-sw-forward',
            'pri': 88,
            'source': 'TRAP',
            'tc': 3
        },
		'Egres DHCP Snooping': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 965,
            'cir_sw': 1000,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-dhcp-snooping',
            'pri': 3,
            'source': 'TRAP',
            'tc': 3
        },
		'GLBP IPV6': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 4345,
            'cir_sw': 4500,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-fhrp-v6',
            'pri': 16,
            'source': 'LPTSv6',
            'tc': 4
        },
		'GLBP IPv4': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 4345,
            'cir_sw': 4500,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-fhrp-v4',
            'pri': 15,
            'source': 'LPTSv4',
            'tc': 4
        },
		'GLEAN': {
            'bytes_a': 155,
            'bytes_d': 0,
            'cir_hw': 1931,
            'cir_sw': 2000,
            'pkts_a': 1,
            'pkts_d': 0,
            'policy': 'system-cpp-police-sw-forward',
            'pri': 5,
            'source': 'TRAP',
            'tc': 2
        },
		'GLEAN-SUBNET': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 1931,
            'cir_sw': 2000,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-default',
            'pri': 5,
            'source': 'TRAP',
            'tc': 2
        },
		'GOLD': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 1931,
            'cir_sw': 2000,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-default',
            'pri': 0,
            'source': 'TRAP',
            'tc': 3
            },
		'HSRP IPv4': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 4345,
            'cir_sw': 4500,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-fhrp-v4',
            'pri': 14,
            'source': 'LPTSv4',
            'tc': 4
        },
		'HSRP IPv6': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 4345,
            'cir_sw': 4500,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-fhrp-v6',
            'pri': 15,
            'source': 'LPTSv6',
            'tc': 4
        },
		'ICMP IPv4': {
            'bytes_a': 240,
            'bytes_d': 0,
            'cir_hw': 2494,
            'cir_sw': 2500,
            'pkts_a': 2,
            'pkts_d': 0,
            'policy': 'system-cpp-police-icmp-v4',
            'pri': 1,
            'source': 'LPTSv4',
            'tc': 3
        },
		'ICMP IPv6 MC': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 2494,
            'cir_sw': 2500,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-icmp-v6',
            'pri': 1,
            'source': 'LPTSv6',
            'tc': 3
        },
		'ICMP IPv6 UC': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 2494,
            'cir_sw': 2500,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-icmp-v6',
            'pri': 2,
            'source': 'LPTSv6',
            'tc': 3
        },
		'IGMP ENABLE': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 1931,
            'cir_sw': 2000,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-proto-snoop-v4',
            'pri': 8,
            'source': 'TRAP',
            'tc': 4
        },
		'IP Options(v4)': {
            'bytes_a': 155,
            'bytes_d': 0,
            'cir_hw': 1931,
            'cir_sw': 2000,
            'pkts_a': 1,
            'pkts_d': 0,
            'policy': 'system-cpp-police-sw-forward',
            'pri': 5,
            'source': 'TRAP',
            'tc': 3
        },
		'IPV4 FRAGMENTATION': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 2494,
            'cir_sw': 2500,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-fragment-v4',
            'pri': 33,
            'source': 'LPTSv4',
            'tc': 3
        },
		'IPV4 UNKNOWN': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 1931,
            'cir_sw': 2000,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-default',
            'pri': 4,
            'source': 'TRAP',
            'tc': 3
        },
		'IPv4 Checksum': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 1931,
            'cir_sw': 2000,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-default',
            'pri': 3,
            'source': 'TRAP',
            'tc': 2
        },
		'IPv4 IGMP': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 1931,
            'cir_sw': 2000,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-proto-snoop-v4',
            'pri': 31,
            'source': 'LPTSv4',
            'tc': 4
        },
		'IPv4 MC': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 1931,
            'cir_sw': 2000,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-mcast-ctrl-v4',
            'pri': 32,
            'source': 'LPTSv4',
            'tc': 0
        },
		'IPv4 PIM Reg Mcast': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 1931,
            'cir_sw': 2000,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-mcast-register-v4',
            'pri': 30,
            'source': 'LPTSv4',
            'tc': 1
        },
		'IPv6 DEST-OPT': {
            'bytes_a': 155,
            'bytes_d': 0,
            'cir_hw': 1931,
            'cir_sw': 2000,
            'pkts_a': 1,
            'pkts_d': 0,
            'policy': 'system-cpp-police-sw-forward',
            'pri': 1,
            'source': 'TRAP',
            'tc': 3
        },
		'IPv6 Fragment': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 2494,
            'cir_sw': 2500,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-fragment-v6',
            'pri': 28,
            'source': 'LPTSv6',
            'tc': 3
        },
		'IPv6 HOP-OPT': {
            'bytes_a': 155,
            'bytes_d': 0,
            'cir_hw': 1931,
            'cir_sw': 2000,
            'pkts_a': 1,
            'pkts_d': 0,
            'policy': 'system-cpp-police-sw-forward',
            'pri': 1,
            'source': 'TRAP',
            'tc': 3
        },
		'IPv6 MC': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 1931,
            'cir_sw': 2000,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-mcast-ctrl-v6',
            'pri': 27,
            'source': 'LPTSv6',
            'tc': 0
        },
		'IPv6 Options': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 1931,
            'cir_sw': 2000,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-proto-snoop-v6',
            'pri': 26,
            'source': 'LPTSv6',
            'tc': 4
        },
		'IPv6 UC': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 583,
            'cir_sw': 600,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-alt-sw-forward',
            'pri': 32,
            'source': 'LPTSv6',
            'tc': 2
        },
		'ISIS(L2)': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 965,
            'cir_sw': 1000,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-isis',
            'pri': 3,
            'source': 'TRAP',
            'tc': 5
        },
		'ISIS(L3)': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 965,
            'cir_sw': 1000,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-isis',
            'pri': 3,
            'source': 'TRAP',
            'tc': 5
        },
		'LACP': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 583,
            'cir_sw': 600,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-lacp',
            'pri': 4,
            'source': 'TRAP',
            'tc': 5
        },
		'LDP TCP DST IPv4': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 1931,
            'cir_sw': 2000,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-ldp-v4',
            'pri': 7,
            'source': 'LPTSv4',
            'tc': 5
        },
		'LDP TCP SRC IPv4': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 1931,
            'cir_sw': 2000,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-ldp-v4',
            'pri': 6,
            'source': 'LPTSv4',
            'tc': 5
        },
		'LDP TCP SRC IPv6': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 1931,
            'cir_sw': 2000,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-ldp-v6',
            'pri': 7,
            'source': 'LPTSv6',
            'tc': 5
        },
		'LDP UDP DST IPv4': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 1931,
            'cir_sw': 2000,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-ldp-v4',
            'pri': 5,
            'source': 'LPTSv4',
            'tc': 5
        },
		'LDP UDP DST IPv6': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 1931,
            'cir_sw': 2000,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-ldp-v6',
            'pri': 8,
            'source': 'LPTSv6',
            'tc': 5
        },
		'LDP UDP SRC IPv4': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 1931,
            'cir_sw': 2000,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-ldp-v4',
            'pri': 4,
            'source': 'LPTSv4',
            'tc': 5
        },
		'LDP UDP SRC IPv6': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 1931,
            'cir_sw': 2000,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-ldp-v6',
            'pri': 5,
            'source': 'LPTSv6',
            'tc': 5
        },
		'LLDP': {
            'bytes_a': 586,
            'bytes_d': 0,
            'cir_hw': 15449,
            'cir_sw': 16000,
            'pkts_a': 5,
            'pkts_d': 0,
            'policy': 'system-cpp-police-l2-control',
            'pri': 4,
            'source': 'TRAP',
            'tc': 5
        },
		'LPM Drop': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 583,
            'cir_sw': 600,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-alt-sw-forward',
            'pri': 80,
            'source': 'TRAP',
            'tc': 2
        },
		'MACSEC': {
            'bytes_a': 586,
            'bytes_d': 0,
            'cir_hw': 15449,
            'cir_sw': 16000,
            'pkts_a': 5,
            'pkts_d': 0,
            'policy': 'system-cpp-police-l2-control',
            'pri': 3,
            'source': 'TRAP',
            'tc': 4
        },
		'MC DIRECT CONNECT': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 1931,
            'cir_sw': 2000,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-mcast-data',
            'pri': 5,
            'source': 'TRAP',
            'tc': 1
        },
		'MC FWD DISABLED(v4)': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 1931,
            'cir_sw': 2000,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-mcast-data',
            'pri': 6,
            'source': 'TRAP',
            'tc': 1
        },
		'MC FWD DISABLED(v6)': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 1931,
            'cir_sw': 2000,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-mcast-data',
            'pri': 6,
            'source': 'TRAP',
            'tc': 1
        },
		'MC G PIM PUNT': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 1931,
            'cir_sw': 2000,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-mcast-data',
            'pri': 6,
            'source': 'MIRROR',
            'tc': 1
        },
		'MC NOT FOUND': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 1931,
            'cir_sw': 2000,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-mcast-data',
            'pri': 5,
            'source': 'TRAP',
            'tc': 1
        },
		'MC PIM RPF': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 1931,
            'cir_sw': 2000,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-mcast-rpf-fail',
            'pri': 5,
            'source': 'TRAP',
            'tc': 1
        },
		'MC PIM RPF FAIL': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 1931,
            'cir_sw': 2000,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-mcast-rpf-fail',
            'pri': 5,
            'source': 'TRAP',
            'tc': 1
        },
		'MC SG PIM PUNT': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 1931,
            'cir_sw': 2000,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-mcast-data',
            'pri': 6,
            'source': 'MIRROR',
            'tc': 1
        },
		'MC SNOOP RPF FAIL': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 1931,
            'cir_sw': 2000,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-mcast-rpf-fail',
            'pri': 5,
            'source': 'MIRROR',
            'tc': 1
        },
		'MC SNOOP and DIRECT CONNECT': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 1931,
            'cir_sw': 2000,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-mcast-data',
            'pri': 5,
            'source': 'TRAP',
            'tc': 1
        },
		'MDNS': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 1931,
            'cir_sw': 2000,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-proto-snoop-v6',
            'pri': 8,
            'source': 'TRAP',
            'tc': 4
        },
		'MPLS OAM IPv4': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 965,
            'cir_sw': 1000,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-mpls-oam',
            'pri': 21,
            'source': 'LPTSv4',
            'tc': 4
        },
		'MPLS-VPN-TTL1': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 583,
            'cir_sw': 600,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-mtu-ttl-fail',
            'pri': 8,
            'source': 'TRAP',
            'tc': 3
        },
		'MTU(L3)': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 583,
            'cir_sw': 600,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-mtu-ttl-fail',
            'pri': 8,
            'source': 'TRAP',
            'tc': 3
        },
		'OSPF v2 MC': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 1931,
            'cir_sw': 2000,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-ospf-v4',
            'pri': 2,
            'source': 'LPTSv4',
            'tc': 5
        },
		'OSPF v2 UC': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 1931,
            'cir_sw': 2000,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-ospf-v4',
            'pri': 3,
            'source': 'LPTSv4',
            'tc': 5
        },
		'OSPF v3 MC': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 1931,
            'cir_sw': 2000,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-ospf-v6',
            'pri': 3,
            'source': 'LPTSv6',
            'tc': 5
        },
		'OSPF v3 UC': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 1931,
            'cir_sw': 2000,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-ospf-v6',
            'pri': 4,
            'source': 'LPTSv6',
            'tc': 5
        },
		'PBR GLEAN': {
            'bytes_a': 155,
            'bytes_d': 0,
            'cir_hw': 1931,
            'cir_sw': 2000,
            'pkts_a': 1,
            'pkts_d': 0,
            'policy': 'system-cpp-police-sw-forward',
            'pri': 5,
            'source': 'TRAP',
            'tc': 2
        },
		'PIM IPV6': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 1931,
            'cir_sw': 2000,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-mcast-ctrl-v6',
            'pri': 17,
            'source': 'LPTSv6',
            'tc': 4
        },
		'PIM IPV6 Reg Mcast': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 1931,
            'cir_sw': 2000,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-mcast-register-v6',
            'pri': 18,
            'source': 'LPTSv6',
            'tc': 1
        },
		'PIM IPv4': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 1931,
            'cir_sw': 2000,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-mcast-ctrl-v4',
            'pri': 17,
            'source': 'LPTSv4',
            'tc': 4
        },
		'RIP': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 4345,
            'cir_sw': 4500,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-rip-bc',
            'pri': 3,
            'source': 'TRAP',
            'tc': 5
        },
		'RIP IPv4': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 4345,
            'cir_sw': 4500,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-rip-v4',
            'pri': 12,
            'source': 'LPTSv4',
            'tc': 5
        },
		'RIP IPv6': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 4345,
            'cir_sw': 4500,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-rip-v6',
            'pri': 14,
            'source': 'LPTSv6',
            'tc': 5
        },
		'RPF(unicast)': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 0,
            'cir_sw': 0,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-default',
            'pri': 2,
            'source': 'TRAP',
            'tc': 0
        },
		'RSVP IPV4': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 1931,
            'cir_sw': 2000,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-default-v4',
            'pri': 34,
            'source': 'LPTSv4',
            'tc': 5
        },
		'SISF': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 1931,
            'cir_sw': 2000,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-proto-snoop-v6',
            'pri': 3,
            'source': 'TRAP',
            'tc': 3
        },
		'STP(IEEE)': {
            'bytes_a': 220,
            'bytes_d': 0,
            'cir_hw': 4988,
            'cir_sw': 5000,
            'pkts_a': 2,
            'pkts_d': 0,
            'policy': 'system-cpp-police-topology-control',
            'pri': 4,
            'source': 'TRAP',
            'tc': 5
        },
		'TCP DST PORT LISP IPv4': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 583,
            'cir_sw': 600,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-lisp-ctrl',
            'pri': 29,
            'source': 'LPTSv4',
            'tc': 2
        },
		'TCP SRC PORT LISP IPv4': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 583,
            'cir_sw': 600,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-lisp-ctrl',
            'pri': 28,
            'source': 'LPTSv4',
            'tc': 2
        },
		'TCP default IPv4': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 965,
            'cir_sw': 1000,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-tcp-v4',
            'pri': 35,
            'source': 'LPTSv4',
            'tc': 2
        },
		'TCP default IPv6': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 965,
            'cir_sw': 1000,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-tcp-v6',
            'pri': 30,
            'source': 'LPTSv6',
            'tc': 2
        },
		'TTL0(MPLS)': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 583,
            'cir_sw': 600,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-mtu-ttl-fail',
            'pri': 8,
            'source': 'TRAP',
            'tc': 3
        },
		'TTL1(L3)': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 583,
            'cir_sw': 600,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-mtu-ttl-fail',
            'pri': 8,
            'source': 'TRAP',
            'tc': 3
        },
		'TTL1(MPLS)': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 583,
            'cir_sw': 600,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-mtu-ttl-fail',
            'pri': 8,
            'source': 'TRAP',
            'tc': 3
        },
		'UDP DST PORT LISP IPv4': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 583,
            'cir_sw': 600,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-lisp-ctrl',
            'pri': 27,
            'source': 'LPTSv4',
            'tc': 2
        },
		'UDP SRC PORT LISP IPv4': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 583,
            'cir_sw': 600,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-lisp-ctrl',
            'pri': 26,
            'source': 'LPTSv4',
            'tc': 2
        },
		'UDP default IPv4': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 583,
            'cir_sw': 600,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-udp-v4',
            'pri': 36,
            'source': 'LPTSv4',
            'tc': 2
        },
		'UDP default IPv6': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 583,
            'cir_sw': 600,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-udp-v6',
            'pri': 31,
            'source': 'LPTSv6',
            'tc': 2
        },
		'Unknown UC': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 965,
            'cir_sw': 1000,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-unknown-uc',
            'pri': 3,
            'source': 'TRAP',
            'tc': 3
        },
		'VRRP IPv4': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 4345,
            'cir_sw': 4500,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-fhrp-v4',
            'pri': 13,
            'source': 'LPTSv4',
            'tc': 4
        },
		'VRRP IPv6': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 4345,
            'cir_sw': 4500,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-police-fhrp-v6',
            'pri': 13,
            'source': 'LPTSv6',
            'tc': 4
        },
		'WCCP IPv4': {
            'bytes_a': 0,
            'bytes_d': 0,
            'cir_hw': 1931,
            'cir_sw': 2000,
            'pkts_a': 0,
            'pkts_d': 0,
            'policy': 'system-cpp-default-v4',
            'pri': 16,
            'source': 'LPTSv4',
            'tc': 4
        }
    }
}
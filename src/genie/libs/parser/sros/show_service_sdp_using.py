from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any
import re

# ======================================================
# Schema for 'show service sdp-using'
# ======================================================


class ShowServiceSdpUsingSchema(MetaParser):
    """schema for show service sdp-using"""
    schema = {
        'total': int,
        'sdp': {
            Any(): {
                'service_id': int,
                'type': str,
                'far_end': str,
                'oper_state': str,
                'ingress_label': int,
                'egress_label': int,
            }
        }
    }


class ShowServiceSdpUsing(ShowServiceSdpUsingSchema):
    """ Parser for show service sdp-using"""
    cli_command = 'show service sdp-using'

    def cli(self, output=None):

        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        result_dict = {}
        #===============================================================================
        #SDP Using
        #===============================================================================
        #SvcId      SdpId              Type   Far End              Opr   I.Label E.Label
        #                                                          State
        #-------------------------------------------------------------------------------
        #60001      1000:60001         Spok   10.0.1.5             Up    131064  131066
        #300100     1000:20001         Spok   10.0.1.2             Up    131067  131069
        #300100     1000:20003         Spok   10.0.1.2             Up    131065  131067
        #300101     1000:20002         Spok   10.0.1.3             Up    131066  131068
        p1 = re.compile(r'(?P<service>\d+)'
                        r' +(?P<sdp>\S+) +(?P<type>\S+) +(?P<far_end>\S+)'
                        r' +(?P<oper>Up|Down) +(?P<ingress_label>\d+)' 
                        r' +(?P<egress_label>\d+)')

        # Number of SDPs : 4
        p2 = re.compile(r'^Number of SDPs : (?P<total>\d+)')

        for line in out.splitlines():
            if line:
                line = line.strip()
            else:
                continue

            #===============================================================================
            #SDP Using
            #===============================================================================
            #SvcId      SdpId              Type   Far End              Opr   I.Label E.Label
            #                                                          State
            #-------------------------------------------------------------------------------
            #60001      1000:60001         Spok   10.0.1.5             Up    131064  131066
            #300100     1000:20001         Spok   10.0.1.2             Up    131067  131069
            #300100     1000:20003         Spok   10.0.1.2             Up    131065  131067
            #300101     1000:20002         Spok   10.0.1.3             Up    131066  131068

            m = p1.match(line)
            if m:
                group = m.groupdict()
                sdp=group['sdp']
                result_dict.setdefault('sdp', {}).setdefault(sdp,{})
                result_dict['sdp'][sdp].update({'service_id': int(group['service'])})
                result_dict['sdp'][sdp].update({'ingress_label': int(group['ingress_label'])})
                result_dict['sdp'][sdp].update({'egress_label': int(group['egress_label'])})
                result_dict['sdp'][sdp].update({'type': (group['type'])})
                result_dict['sdp'][sdp].update({'far_end': (group['far_end'])})
                result_dict['sdp'][sdp].update({'oper_state': (group['oper'])})
                continue

            # Number of SDPs : 4

            m = p2.match(line)
            if m:
                group = m.groupdict()
                result_dict['total'] = int(group['total'])

        return result_dict

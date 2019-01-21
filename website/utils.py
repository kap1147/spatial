from ipware import get_client_ip
from django.contrib.gis.geoip2 import GeoIP2

def get_user_ip(request):
    ip, is_routable = get_client_ip(request)

    if ip is None:
        # No ip found
        pass
    else:
        # ip is public
        if is_routable:
            g = GeoIP2()
            results = {}
            results['ip'] = ip
            results['lon'] = g.city(ip)['longitude']
            results['lat'] = g.city(ip)['latitude']
            return results
        else:
            # ip is private
            pass


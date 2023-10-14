from prometheus_client import start_http_server, Gauge
from ping3 import ping, verbose_ping
import random
import time

# Create a metric to track time spent and requests made.
PING_GOOGLE = Gauge('pystatus_ping_google', 'Latency to google.com')
PING_FACEBOOK = Gauge("pystatus_ping_facebook", "Latency to facebook.com")
PING_TWITTER = Gauge("pystatus_ping_twitter", "Latency to twitter.com")
PING_AMAZON = Gauge("pystatus_ping_amazon", "Latency to amazon.com")

def ping_server(url, metric):
    response_time = ping("google.com")
    if response_time is not None:
        metric.set(response_time)
    else:
        metric.set(0)

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)
    # Generate some requests.
    while True:
        ping_server("google.com", PING_GOOGLE)
        ping_server("facebook.com", PING_FACEBOOK)
        ping_server("twitter.com", PING_TWITTER)
        ping_server("amazon.com", PING_AMAZON)
        time.sleep(1)
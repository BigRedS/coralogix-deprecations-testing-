#! /usr/bin/env python

from prometrix import get_custom_prometheus_connect
from prometrix import CoralogixPrometheusConfig
import os

#print ("Trying legacy endpoint 'https://prom-api.coralogix.com'" )
#coralogix_config = CoralogixPrometheusConfig(
#    url="https://prom-api.coralogix.com",
#    prometheus_token=os.environ.get('CX_API_KEY'),
#    additional_labels={"job": "coralogix-prometheus"},
#)
#coralogix_client = get_custom_prometheus_connect(coralogix_config)
#print(coralogix_client.get_current_metric_value(metric_name='up'))


print ("Trying new endpoint 'https://ng-api-http.eu2.coralogix.com/metrics'" )

coralogix_config = CoralogixPrometheusConfig(
    url="https://ng-api-http.eu2.coralogix.com/metrics",
    prometheus_token=os.environ.get('CX_API_KEY'),
    additional_labels={"job": "coralogix-prometheus"},
)
coralogix_client = get_custom_prometheus_connect(coralogix_config)
print(coralogix_client.get_current_metric_value(metric_name='up'))

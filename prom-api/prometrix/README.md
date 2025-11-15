In this dir, create a venv and activate it:

    python -m venv venv
    source venv/bin/activate

Install the prometrix package in edit-mode; replace the path here with wherever you've checked it out to:

    pip install -e ~/repos/prometrix/

Export a CX_API_KEY env var that has privileges to query metrics:

    export CX_API_KEY=cx_up_xxx...

Run ./test.py, expect some successful looking output

    Trying new endpoint 'https://ng-api-http.eu2.coralogix.com/metrics'
    https://ng-api-http.eu2.coralogix.com/metrics/api/v1/query
    [{'metric': {'__name__': 'up', 'cx_agent_type': 'agent', 'cx_application_name': [...]

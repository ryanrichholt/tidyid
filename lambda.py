import json
import logging
import random
import tidyid

log = logging.getLogger(__name__)
NO_DEFAULT = object()


class ParamError(Exception):
    def __init__(self, resp):
        self.resp = resp


class ParamParser:
    def __init__(self, params):
        self.params = params
        
    def missing_required(self, param):
        raise ParamError({
            'statusCode': 400, 
            'body': f'missing required param: {param}'
        })
        
    def error(self, param, value):
        raise ParamError({
            'statusCode': 400, 
            'body': f'error parsing "{param}" value: "{value}"'
        })
    
    def get(self, k, fn, default=NO_DEFAULT):
        try:
            v = self.params[k]
        except KeyError:
            if default is NO_DEFAULT:
                self.missing_required(k)
            else:
                return default
        
        try:
            v = fn(v)
        except Exception as e:
            self.error(k, v)
        
        return v


def lambda_handler(event, context):
    params = event.get('queryStringParameters') or {}
    parser = ParamParser(params)
    
    try:
        n = parser.get('n', int, 100)
        pad = parser.get('pad', int, 0)
        split = parser.get('split', int, 3)
        start = parser.get('start', int, None)
    except ParamError as e:
        return e.resp
    
    if start is None:
        start = random.randint(1, 3000000)
    elif start < 1:
        start = 1
   
    gen = tidyid.gen_ids(
        n = n,
        pad = pad,
        split = split,
        start = start
    )
    ids = [tid for i, tid in gen]
    
    return {
        'statusCode': 200,
        'body': json.dumps(ids)
    }

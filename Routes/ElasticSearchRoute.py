from sqlite3 import paramstyle
from typing import Optional
from fastapi import APIRouter, Body, Request
import json
import requests
from requests.auth import HTTPBasicAuth
from collections import OrderedDict
from Models.Doctor import Response

router = APIRouter()

key= '=5g=B1PpqLHzSakQRX1U'
# key = 'VJ4d6j6QsnOXRGJMNQ2Q'


@router.get("/medicine/",response_model = Response)
async def medpipe(data: Optional[str],):
    try:
        print(data)
        payload = {}
        if(len(data) <= 4):
            body = {

                "query": {
                    "multi_match": {
                        "query": data,
                        "fields": ["Brand Name", "Generic Name"]
                    }

                }

            }

        else:
            body = {
                "size": 5,
                "query": {
                    "bool": {
                        "should": [
                            {

                                "match_phrase_prefix": {
                                    "Brand Name": {
                                        "query": data,
                                        "max_expansions": 10
                                    }
                                }

                            },
                            {

                                "match_phrase_prefix": {
                                    "Generic Name": {
                                        "query": data,
                                        "max_expansions": 10
                                    }
                                }

                            }
                        ]
                    }
                }
            }

        url = "https://127.0.0.1:9200/_search/"
        response = requests.request("GET", url, json=body, data=payload,
                                    verify=False, auth=HTTPBasicAuth('elastic', key))
        res = json.loads(response.content)
        res = res['hits']['hits']
        result = dict()
        i = 0
        for values in res:
            if(values['_index'] == "brand_master"):
                result[i] = {"Brand Name": values['_source']['Brand Name'],
                            "Identifier": values['_source']['Identifier']}
                i = i+1
            else:
                if(values['_index'] == "generic_master"):
                    data = values['_source']['Identifier']
                    print(values['_source'])

                    url = "https://127.0.0.1:9200/brand_master/_search?q=" + \
                        str(data)

                    size = {
                        "size": 20
                    }
                    response = requests.request("GET", url, json=size, data=payload,
                                                verify=False, auth=HTTPBasicAuth('elastic', key))
                    res2 = json.loads(response.content)
                    res2 = res2['hits']['hits']
                    k = 0
                    for value in res2:
                        if (k == 5):
                            break
                        result[i] = {"Brand Name": value['_source']['Brand Name'],
                                    "Identifier": value['_source']['Identifier']}
                        k = k+1
                        i = i+1

        print("-----------result----------", result)
        return {
            "status_code": 201,
            "response_type": "success",
            "description": "Medicine fetched Successfully",
            "data": result
        }
        
    except:
        return {
            "status_code": 404,
            "response_type": "error",
            "description": "Unable to find Medicines",
            "data": False
        }


@router.get('/symptoms',response_model = Response)
async def sympipe(data: Optional[str]):
    try:
        payload = {}
        if(len(data) <= 5):
            body = {
                "query": {
                    "match": {
                        "term": data
                    }
                }
            }
        else:
            body = {
                "size": 5,
                "query": {
                    "match_phrase_prefix": {
                        "term": {
                            "query": data,
                            "max_expansions": 10
                        }
                    }
                }
            }
        url = "https://127.0.0.1:9200/symptom_master/_search/"
        response = requests.request("GET", url, json=body, data=payload,
                                    verify=False, auth=HTTPBasicAuth('elastic', key))
        res = json.loads(response.content)
        res = res['hits']['hits']
        result = dict()
        i = 0
        for values in res:
            result[i] = {"Brand Name": values['_source']
                        ['term'], "Identifier": values['_source']['id']}
            i = i+1
        print("-----------result----------", result)
        return {
            "status_code": 201,
            "response_type": "success",
            "description": "symptoms fetched Successfully",
            "data": result
        }
    except:
         return {
            "status_code": 404,
            "response_type": "error",
            "description": "Unable to find Symptoms",
            "data": False
        }


@router.get('/labtest',response_model = Response)
async def labTest(data: Optional[str]):
    try:
        payload = {}
        body = {
            "size": 5,
            "query": {
                "bool": {
                    "should": [
                        {
                            "match_phrase_prefix": {
                                "SHORTNAME": {
                                    "query": data,
                                    "max_expansions": 10
                                }
                            }

                        },
                        {

                            "match_phrase_prefix": {
                                "DefinitionDescription": {
                                    "query": data,
                                    "max_expansions": 10
                                }
                            }

                        }
                    ]
                }
            }
        }
        url = "https://127.0.0.1:9200/loinc/_search/"
        response = requests.request("GET", url, json=body, data=payload,
                                    verify=False, auth=HTTPBasicAuth('elastic', key))
        res = json.loads(response.content)
        # print("---------lab tets ---------", res)
        res = res['hits']['hits']
        result = dict()
        i = 0
        for values in res:
            result[i] = {"Name": values['_source']['SHORTNAME'], "Common Name": values['_source']
                        ['LONG_COMMON_NAME'], "loinc_num": values['_source']['LOINC_NUM']}
            i = i+1
        print("-----------result----------", result)
        return {
            "status_code": 201,
            "response_type": "success",
            "description": "Lab test fetched Successfully",
            "data": result
        }
    except:
         return {
            "status_code": 404,
            "response_type": "error",
            "description": "Unable to find Lab Tests",
            "data": False
        }

# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 12:00:10 2019

@author: Theo
"""
import numpy as np
import pandas as pd
import requests
from dotenv import load_dotenv
from base64 import b64encode
import os
from time import sleep

def get_access_token():
    load_dotenv()
    credentials = "Basic " + b64encode(bytes("{}:{}".format(os.getenv("CLIENT_ID"),os.getenv("CLIENT_SECRET")), "utf-8")).decode("utf-8")
    headers_identification = {"Authorization":credentials, "Content-Type":"application/x-www-form-urlencoded"}
    re = requests.post("https://accounts.spotify.com/api/token", headers=headers_identification, data=dict(grant_type="client_credentials"))
    return re.json().get("access_token")

def requests_audio_features(ids, token):
    r = requests.get("https://api.spotify.com/v1/audio-features/?ids=" + ",".join(ids), headers=dict(Authorization="Bearer "+ token))
    if r.status_code == 200:
        return r.json().get("audio_features")
    elif r.status_code == 429:
        sleep(int(r.headers.get("Retry-After")) + 3)
        return requests_audio_features(ids, token)
    else:
        print("Unsupported return code", r.status_code, r.text)
        exit(1)
        
def loop_spotify_query(df):
    token = get_access_token()
    arrays = np.array_split(df.id, (df.id.shape[0]/100)+1)
    return pd.DataFrame(list(feature for array in arrays for feature in requests_audio_features(array, token))) 

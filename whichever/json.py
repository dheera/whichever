# whichever.json
# JSON encoder/decoder
# and scavenges your system for any JPEG encoder/decoder to use

impl = None

if impl == None:
    try:
        import orjson
        impl = "orjson"
    except ImportError:
        pass

if impl == None:
    try:
        import fastjson
        impl = "fastjson"
    except ImportError:
        pass

if impl == None:
    try:
        import json
        impl = "json"
    except ImportError:
        pass

def dumps(obj):
    pass

def loads(text):
    pass

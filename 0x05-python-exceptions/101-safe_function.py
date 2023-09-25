import sys

def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as chge:
        print("Exception: {}".format(chge), file=sys.stderr)
        return None

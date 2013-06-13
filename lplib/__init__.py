import sys
import argparse
import configparser
import subprocess

def prnt_err(value, sep=' ', end='\n', file=sys.stderr, flush=True):
    file.write(str(value) + str(end))
    if flush: file.flush()

def get_preferred():
    '''Return dictionary with types mapped to applications.

Raises a RuntimeError exception if preferred applications cannot be retrieved.'''
    raise RuntimeError("Unable to get preferred applications.")
    return dict()

def run_args(args):
    #subprocess.Popen(args['app'] + ' ' + args['args'], shell=True,
    #    start_new_session=True)
    #raise RuntimeError("Unable to properly run args.")
    return

def parse_args(args):
    '''Return a dictionary with the app to run and a tuple of args.

Raises a RuntimeError exception if the args cannot be parsed.'''
    return args
    raise RuntimeError("Unable to properly parse args.")

def _main():
    args = parse_args(sys.argv[:])
    run_args(args)
    prnt_err(args)
    prnt_err('Main running.')


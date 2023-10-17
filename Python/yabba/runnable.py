# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 15:44:52 2020

@author: Алексей
"""

long_format = False

def print_label(label, msg):
    if long_format:
        out = '{0}: {1}'.format(label.upper(), str(msg))
    else:
        out = '{0}-{1}'.format(label[0].upper(), str(msg))
    print(out)

def debug(msg):
    print_label('debug', msg)

def warning(msg):
    print_label('warning', msg)

if __name__ == '__main__':
    print('*** Testing print functions ***')
    debug('This is a debug message')
    long_format = True
    warning('This is a warning message with a long label')
else:
    print('Module {0} is being imported'.format(__name__))
    
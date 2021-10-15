#!/usr/bin/env python3

import os
import sys
import argparse
import json
import project_common
import project_generated
import logging

log = logging.getLogger(__name__)


def main(
        args,
):
    out_json_fname = args.out_json_fname
    new_json_dict = project_generated.get_json()
    log.info(f'main: saving into {repr(out_json_fname)}')
    with open(out_json_fname, 'w') as fhandle:
        json.dump(new_json_dict, fhandle, sort_keys=True, indent=4)
    return

    # project-info.py --oo filename


def parse_arguments():
    """!
    Parse the input arguments for the product and origin
    """
    parser = argparse.ArgumentParser()

    parser.add_argument('--out-json-fname', action='store', default='project_info_new.json', help='xxx')

    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_arguments()

    datefmt = '%Y-%m-%d %H:%M:%S'
    datefmt = '%H:%M:%S'

    logging_format = '#'
    # logging_format += ' %(asctime)s'
    logging_format += ' ' + str(os.path.basename(__file__))
    logging_format += ' %(levelname)s: %(message)s'

    # log_level = logging.INFO
    # if args.verbosity >= 2:
    #    log_level = logging.DEBUG
    # elif args.verbosity == 1:
    #    log_level = logging.INFO
    # elif args.verbosity == 0:
    #    log_level = logging.WARNING
    log_level = logging.DEBUG
    logging.basicConfig(level=log_level, format=logging_format, datefmt=datefmt)

    # log.info('args: %s', json.dumps(vars(args), indent = 4, sort_keys=True))
    main(args=args)
    log.info(f'done')
    sys.exit(0)

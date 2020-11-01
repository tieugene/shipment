#!/usr/bin/env python3
"""
Walk through src dir collecting items to send to Shipment (tm).
Dir structure: yyyy/mmm/dd.mm.yy/org/*.pdf
Skip yyyy/mmm, get *.pdf right inside 'org' only
Sending attrs:
- shipper (const)
- date (pre-last dir; dd.mm.yy)
- org (last dir)
TODO: count dirs/files (processed/used) ("Used ... files from ... found in ... dirs")
"""

import datetime
import os
import sys
import requests
import argparse


class Opts(object):
    """
    Stored CLI options
    """
    shipper = None
    upload = False
    verbose = False
    logfile = None
    dsturl = None


# const
HEAD = "curl -i -X POST -F 'shipper={}' -F 'org={}' -F 'date={}'"
# static
date = None  # 'static', store processing date before dive into organisations


def __eprint(s: str):
    """
    Print s to stderr
    """
    print(s, file=sys.stderr)
    if Opts.logfile:
        print(s, file=Opts.logfile)


def verbose(s: str):
    """
    Print s to stderr in verbose mode
    """
    if Opts.verbose:
        __eprint(s)


def diver(level: int, path: str, item: str):
    """
    Recurring function to walk through dir tree.
    Levels:
    0 - year
    1 - month
    2 - day
    3 - org
    """
    global date
    item_path = os.path.join(path, item)
    if not os.path.isdir(item_path):
        verbose("Not dir : '{}'.".format(item_path))
        return
    if level < 2:  # year, mon
        for child in os.listdir(item_path):
            diver(level + 1, item_path, child)
    elif level == 2:  # day
        try:
            date = datetime.datetime.strptime(item, "%d.%m.%y")
        except ValueError:
            date = None
        if not date:
            verbose("Not date: '{}'.".format(item))
            return
        for child in os.listdir(item_path):
            diver(level + 1, item_path, child)
    elif level == 3:  # org
        payload = list()
        for file in os.listdir(item_path):
            file_path = os.path.join(item_path, file)
            if not os.path.isfile(file_path):
                verbose("Not file: '{}'.".format(file_path))
                continue
            if file[-4:].lower() != '.pdf':
                verbose("Not PDF : '{}'.".format(file_path))
                continue
            payload.append((file_path, file))
        if payload:  # list of (file_path, file_name)
            date_s = date.strftime("%d.%m.%y")
            if not Opts.upload:     # curl
                s = ""
                for fp, f in payload:
                    s += " -F 'file=@{};type=application/pdf;filename={}'".format(fp, f)
                print(HEAD.format(Opts.shipper, item, date_s) + s + " " + Opts.dsturl)
            else:                   # upload
                multifile = list()
                for fp, f in payload:
                    multifile.append(("file", (f, open(fp, 'rb'), 'application/pdf')))
                r = requests.post(Opts.dsturl,
                                  data={'shipper': Opts.shipper, 'org': item, 'date': date_s},
                                  files=multifile)
                if Opts.verbose and r.status_code != 201:
                    __eprint("Upload err '{}':".format(item_path))
                    if r.status_code != 207:
                        __eprint("\t{}: {}".format(r.status_code, r.text))
                    else:
                        for i in r.json():
                            __eprint("\t{}: {}".format(i['status'], i['note']))
        else:
            verbose("Skip dir: '{}'.".format(item_path))


def walk(srcdir: str):
    for year in os.listdir(srcdir):  # 1. years
        year_path = os.path.join(srcdir, year)
        if os.path.isdir(year_path):  # TODO: chk(YYYY)
            diver(0, srcdir, year)


def init_cli():
    """ Handle CLI """
    parser = argparse.ArgumentParser(description="Bulk 'Shipment' upload.")
    parser.add_argument('url', type=str, help='URL upload to')
    parser.add_argument('shipper', type=str, help='Shipper')
    parser.add_argument('dir', type=str, help='Dir upload from')
    parser.add_argument('-u', '--upload', action='store_true', help='Upload (default - generate curl calls)')
    parser.add_argument('-l', '--log', action='store_true', help='Log to file')
    parser.add_argument('-v', '--verbose', action='store_true')
    return parser


def main():
    parser = init_cli()
    args = parser.parse_args()
    Opts.shipper = args.shipper
    Opts.upload = args.upload
    Opts.verbose = args.verbose
    if args.log:
        Opts.logfile = open("%s.log" % datetime.datetime.now().strftime('%y%m%d%H%M%S'), 'wt')
    Opts.dsturl = args.url
    if not os.path.isdir(args.dir):
        __eprint("'{}' is not folder.".format(args.dir))
        parser.print_help()
        return
    walk(args.dir)
    if Opts.logfile:
        Opts.logfile.close()


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
# Sourced from: http://github.com/joostrijneveld/pwdhash-py 
#The MIT License (MIT)
#
#Copyright (c) [year] [fullname]
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.
import subprocess
import hmac
import base64
import getpass
import string
import re
import os
import argparse
import sys

PREFIX = '@@'
DUALTLDS = [
    'ab.ca', 'ac.ac', 'ac.at', 'ac.be', 'ac.cn', 'ac.il', 'ac.in', 'ac.jp',
    'ac.kr', 'ac.nz', 'ac.th', 'ac.uk', 'ac.za', 'adm.br', 'adv.br', 'agro.pl',
    'ah.cn', 'aid.pl', 'alt.za', 'am.br', 'arq.br', 'art.br', 'arts.ro',
    'asn.au', 'asso.fr', 'asso.mc', 'atm.pl', 'auto.pl', 'bbs.tr', 'bc.ca',
    'bio.br', 'biz.pl', 'bj.cn', 'br.com', 'cn.com', 'cng.br', 'cnt.br',
    'co.ac', 'co.at', 'co.il', 'co.in', 'co.jp', 'co.kr', 'co.nz', 'co.th',
    'co.uk', 'co.za', 'com.au', 'com.br', 'com.cn', 'com.ec', 'com.fr',
    'com.hk', 'com.mm', 'com.mx', 'com.pl', 'com.ro', 'com.ru', 'com.sg',
    'com.tr', 'com.tw', 'cq.cn', 'cri.nz', 'de.com', 'ecn.br', 'edu.au',
    'edu.cn', 'edu.hk', 'edu.mm', 'edu.mx', 'edu.pl', 'edu.tr', 'edu.za',
    'eng.br', 'ernet.in', 'esp.br', 'etc.br', 'eti.br', 'eu.com', 'eu.lv',
    'fin.ec', 'firm.ro', 'fm.br', 'fot.br', 'fst.br', 'g12.br', 'gb.com',
    'gb.net', 'gd.cn', 'gen.nz', 'gmina.pl', 'go.jp', 'go.kr', 'go.th',
    'gob.mx', 'gov.br', 'gov.cn', 'gov.ec', 'gov.il', 'gov.in', 'gov.mm',
    'gov.mx', 'gov.sg', 'gov.tr', 'gov.za', 'govt.nz', 'gs.cn', 'gsm.pl',
    'gv.ac', 'gv.at', 'gx.cn', 'gz.cn', 'hb.cn', 'he.cn', 'hi.cn', 'hk.cn',
    'hl.cn', 'hn.cn', 'hu.com', 'idv.tw', 'ind.br', 'inf.br', 'info.pl',
    'info.ro', 'iwi.nz', 'jl.cn', 'jor.br', 'jpn.com', 'js.cn', 'k12.il',
    'k12.tr', 'lel.br', 'ln.cn', 'ltd.uk', 'mail.pl', 'maori.nz', 'mb.ca',
    'me.uk', 'med.br', 'med.ec', 'media.pl', 'mi.th', 'miasta.pl', 'mil.br',
    'mil.ec', 'mil.nz', 'mil.pl', 'mil.tr', 'mil.za', 'mo.cn', 'muni.il',
    'nb.ca', 'ne.jp', 'ne.kr', 'net.au', 'net.br', 'net.cn', 'net.ec',
    'net.hk', 'net.il', 'net.in', 'net.mm', 'net.mx', 'net.nz', 'net.pl',
    'net.ru', 'net.sg', 'net.th', 'net.tr', 'net.tw', 'net.za', 'nf.ca',
    'ngo.za', 'nm.cn', 'nm.kr', 'no.com', 'nom.br', 'nom.pl', 'nom.ro',
    'nom.za', 'ns.ca', 'nt.ca', 'nt.ro', 'ntr.br', 'nx.cn', 'odo.br',
    'on.ca', 'or.ac', 'or.at', 'or.jp', 'or.kr', 'or.th', 'org.au',
    'org.br', 'org.cn', 'org.ec', 'org.hk', 'org.il', 'org.mm', 'org.mx',
    'org.nz', 'org.pl', 'org.ro', 'org.ru', 'org.sg', 'org.tr', 'org.tw',
    'org.uk', 'org.za', 'pc.pl', 'pe.ca', 'plc.uk', 'ppg.br', 'presse.fr',
    'priv.pl', 'pro.br', 'psc.br', 'psi.br', 'qc.ca', 'qc.com', 'qh.cn',
    're.kr', 'realestate.pl', 'rec.br', 'rec.ro', 'rel.pl', 'res.in', 'ru.com',
    'sa.com', 'sc.cn', 'school.nz', 'school.za', 'se.com', 'se.net', 'sh.cn',
    'shop.pl', 'sk.ca', 'sklep.pl', 'slg.br', 'sn.cn', 'sos.pl', 'store.ro',
    'targi.pl', 'tj.cn', 'tm.fr', 'tm.mc', 'tm.pl', 'tm.ro', 'tm.za', 'tmp.br',
    'tourism.pl', 'travel.pl', 'tur.br', 'turystyka.pl', 'tv.br', 'tw.cn',
    'uk.co', 'uk.com', 'uk.net', 'us.com', 'uy.com', 'vet.br', 'web.za',
    'web.com', 'www.ro', 'xj.cn', 'xz.cn', 'yk.ca', 'yn.cn', 'za.com']


def str_ROL(s, n):
    n = n % len(s)
    return s[n:] + s[:n]


def extract_domain(uri):
    host = re.sub('https?:\/\/', '', uri)
    host = host.split('/')[0]
    host = host.split('.')
    if len(host) >= 3 and '.'.join(host[-2:]) in DUALTLDS:
        host = host[-3:]
    else:
        host = host[-2:]
    return '.'.join(host)


def apply_constraints(digest, size, alnum=False):
    result = digest[:size-4]  # leave room for some extra characters
    extras = list(reversed(digest[size-4:]))

    def cond_add_extra(f, candidates):
        n = ord(extras.pop()) if extras else 0
        if any(f(x) for x in result):
            return chr(n)
        else:
            return candidates[n % len(candidates)]

    result += cond_add_extra(str.isupper, string.ascii_uppercase)
    result += cond_add_extra(str.islower, string.ascii_lowercase)
    result += cond_add_extra(str.isdigit, string.digits)
    if re.search('\W', result) and not alnum:
        result += extras.pop() if extras else chr(0)
    else:
        result += '+'
    if alnum:
        while re.search('\W', result):
            c = cond_add_extra(lambda x: False, string.ascii_uppercase)
            result = re.sub('\W', c, result, count=1)
    return str_ROL(result, ord(extras.pop()) if extras else 0)


def pwdhash(domain, password):
    domain = domain.encode('utf-8')
    password = password.encode('utf-8')
    digest = hmac.new(password, domain, 'md5').digest()
    b64digest = base64.b64encode(digest).decode("utf-8")[:-2]  # remove padding
    size = len(PREFIX) + len(password)
    return apply_constraints(b64digest, size, password.isalnum())


cmd = sys.argv[1:][0]

if cmd == "prompt":
    domain = input("Domain: ")
    password = input("Password: ")
    print(pwdhash(domain, password))

elif cmd == "xprompt":
    domainp = subprocess.run(['sh', '-c', 'echo Enter Domain | dmenu -p Domain'], stdout=subprocess.PIPE)
    domain = domainp.stdout.decode('ascii').rstrip()
    passwordp = subprocess.run(['sh', '-c', 'echo Enter Password | dmenu -p Domain -nb "#e8e8e8" -nf "#e8e8e8"'], stdout=subprocess.PIPE)
    password = passwordp.stdout.decode('ascii').rstrip()
    result = pwdhash(domain, password)
    subprocess.run(['xdotool', 'type', result], stdout=subprocess.PIPE)

else:
    print("unknown cmd")

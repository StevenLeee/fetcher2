#! /usr/bin/env python

import time
import string
from datetime import datetime as dt
import re


def get_data_dir():
    return '/root/workspace/abcd/rawdata'


def get_data_basefilenane():
    dir = get_data_dir()
    return dir + '/nfcapd.20150109140000'


# def get_data_dir():
#     return 'E:\eworkspace\\rawdata'


# def get_data_basefilenane():
#     dir = get_data_dir()
#     return dir + '\\nfcapd.20150109140000'


def get_data_filename(prefix):
    basefilename = get_data_basefilenane()
    return basefilename + '.' + prefix


def file_get_contents(file_name):
    try:
        with open(file_name) as f:
            return f.read()
    except (Exception, e):
        print (str(e))
        return None
    return None

def get_json_data_errorate(prefix):
    print(get_data_filename(prefix))
    rawdata = eval ( file_get_contents(get_data_filename(prefix)) )

    interval = 500000
    resultdata = {}
    firstdata = {}
    seconddata = {}
    thirddata = {}
    alldata = []
    nonalldata = []
    resultdata = {}
    url_requests_inall = {}
    url_apdex = {}
    url_errorrate = {}

    url_satisfied = {}
    url_tolerating = {}
    url_frustrated = {}

    totalrequest = 0
###############################################################################
    hascalc = False
    for firstkey,firstvalue in rawdata.items() :
        if hascalc == True : break
        hascalc = True
        for secondkey,secondvalue in firstvalue.items() :
            if secondkey != 'all' : continue
            alldata.extend(secondvalue)

    for item in alldata :
        tempdata = {}
        strdata =  '{"%s":%d}' % (item['url'] ,item['requests'] )
        tempdata = eval(strdata)
        # print(tempdata)

        if item['url'] in url_requests_inall :
            url_requests_inall[item['url']] += item['requests']
        else :
            url_requests_inall.update(tempdata)
    print (url_requests_inall)
##############################################################################

###############################################################################
    nonalldata = []
    hascalc = False
    for firstkey,firstvalue in rawdata.items() :
        if hascalc == True : break
        hascalc = True
        for secondkey,secondvalue in firstvalue.items() :
            if secondkey == 'all' : continue
            nonalldata.extend(secondvalue)
            # print(nonalldata)


    for item in nonalldata :
        satisfied = 0
        tolerating = 0
        frustrated = 0
        strdata =  '{"%s":%d}' % (item['url'] ,item['requests'] )
        tempdata = {}
        tempdata = eval(strdata)


        if item['latency'] <= interval * item['requests'] :
            if item['url'] in url_satisfied :
                url_satisfied[item['url']] += item['requests']
            else :
                url_satisfied.update(tempdata)
        elif item['latency'] >  4 * interval * item['requests'] :
            if item['url'] in url_frustrated :
                url_frustrated[item['url']] += item['requests']
            else :
                url_frustrated.update(tempdata)
        else :
            if item['url'] in url_tolerating :
                url_tolerating[item['url']] += item['requests']
            else :
                url_tolerating.update(tempdata)

    # print (url_frustrated)
##############################################################################


###############################################################################
    # print (alldata)
    satisfied = 0
    tolerating = 0
    frustrated = 0

    for item in alldata :
        if item['url'] in url_satisfied :
            satisfied += url_satisfied[item['url']]
        elif item['url'] in url_tolerating :
            tolerating += url_tolerating[item['url']]
        elif item['url'] in url_frustrated :
            frustrated += url_frustrated[item['url']]

        total_number = satisfied + tolerating + frustrated
        if total_number == 0 : continue
        # if total_number != item['requests'] :



        apdex = (satisfied + tolerating / 2) / total_number

        tempdata = {}
        strdata =  '{"%s":%f}' % (item['url'] ,apdex )
        tempdata = eval(strdata)
        url_apdex.update(tempdata)

        # if item['url'] in url_apdex :
        #     url_apdex[item['url']] += url_apdex
        # else :
        #     url_apdex.update(tempdata)
    print (url_apdex)
##############################################################################


    # for item in alldata :
    #     latency = item['latency']
    #     requests = item['requests']
    #     avglatency = latency / requests
    #     if latency <= interval : apdex = 0
    #     item.update({'apdex' : apdex})




    # for firstkey,firstvalue in rawdata.items() :
    #     # print (firstkey)
    #     # print (firstvalue)
    #     for secondkey,secondvalue in firstvalue.items() :
    #         if secondkey != 'all' : continue
    #         # print (secondkey)
    #         # print (secondvalue)
    #         for item in secondvalue :
    #             # print (item)
    #             for thirdkey,thirdvalue in item.items() :
    #                 # if thirdkey != 'url' :
    #                 #     continue
    #                 # print (thirdkey)
    #                 # print (thirdvalue)
    #                 # print (thirdkey, thirdvalue)
    #
    #                 if thirdkey == 'requests' :
    #                     totalrequest += thirdvalue
    #                     print ('totalrequest', totalrequest)

    # resultdata.update({"juyun":"www.clearclouds.com"})
    # print (resultdata)

    return url_apdex




def get_json_data_apdex(prefix):
    print(get_data_filename(prefix))
    rawdata = eval ( file_get_contents(get_data_filename(prefix)) )
    # print (rawdata)

    interval = 500000
    resultdata = {}
    firstdata = {}
    seconddata = {}
    thirddata = {}
    alldata = []
    nonalldata = []
    resultdata = {}
    url_requests_inall = {}
    url_apdex = {}
    url_errorrate = {}

    url_satisfied = {}
    url_tolerating = {}
    url_frustrated = {}

    totalrequest = 0
###############################################################################
    hascalc = False
    for firstkey,firstvalue in rawdata.items() :
        if hascalc == True : break
        hascalc = True
        for secondkey,secondvalue in firstvalue.items() :
            if secondkey != 'all' : continue
            alldata.extend(secondvalue)

    for item in alldata :
        tempdata = {}
        strdata =  '{"%s":%d}' % (item['url'] ,item['requests'] )
        tempdata = eval(strdata)
        # print(tempdata)

        if item['url'] in url_requests_inall :
            url_requests_inall[item['url']] += item['requests']
        else :
            url_requests_inall.update(tempdata)
    # print (url_requests_inall)
##############################################################################

###############################################################################
    nonalldata = []
    hascalc = False
    for firstkey,firstvalue in rawdata.items() :
        if hascalc == True : break
        hascalc = True
        for secondkey,secondvalue in firstvalue.items() :
            if secondkey == 'all' : continue
            nonalldata.extend(secondvalue)

    for item in nonalldata :
        satisfied = 0
        tolerating = 0
        frustrated = 0
        strdata =  '{"%s":%d}' % (item['url'] ,item['requests'] )
        tempdata = {}
        tempdata = eval(strdata)


        if item['latency'] <= interval * item['requests'] :
            if item['url'] in url_satisfied :
                url_satisfied[item['url']] += item['requests']
            else :
                url_satisfied.update(tempdata)
        elif item['latency'] >  4 * interval * item['requests'] :
            if item['url'] in url_frustrated :
                url_frustrated[item['url']] += item['requests']
            else :
                url_frustrated.update(tempdata)
        else :
            if item['url'] in url_tolerating :
                url_tolerating[item['url']] += item['requests']
            else :
                url_tolerating.update(tempdata)

    # print (url_frustrated)
##############################################################################


###############################################################################
    # print (alldata)
    satisfied = 0
    tolerating = 0
    frustrated = 0

    for item in alldata :
        if item['url'] in url_satisfied :
            satisfied += url_satisfied[item['url']]
        elif item['url'] in url_tolerating :
            tolerating += url_tolerating[item['url']]
        elif item['url'] in url_frustrated :
            frustrated += url_frustrated[item['url']]

        total_number = satisfied + tolerating + frustrated
        if total_number == 0 : continue
        # if total_number != item['requests'] :
        #     print('not equal ')
        #     print(total_number)
        #     print(item['requests'])

        apdex = (satisfied + tolerating / 2) / total_number

        tempdata = {}
        strdata =  '{"Component/Apdex/%s":%f}' % (item['url'] ,apdex )
        tempdata = eval(strdata)
        url_apdex.update(tempdata)

        # if item['url'] in url_apdex :
        #     url_apdex[item['url']] += url_apdex
        # else :
        #     url_apdex.update(tempdata)
    print (url_apdex)
##############################################################################


    # for item in alldata :
    #     latency = item['latency']
    #     requests = item['requests']
    #     avglatency = latency / requests
    #     if latency <= interval : apdex = 0
    #     item.update({'apdex' : apdex})




    # for firstkey,firstvalue in rawdata.items() :
    #     # print (firstkey)
    #     # print (firstvalue)
    #     for secondkey,secondvalue in firstvalue.items() :
    #         if secondkey != 'all' : continue
    #         # print (secondkey)
    #         # print (secondvalue)
    #         for item in secondvalue :
    #             # print (item)
    #             for thirdkey,thirdvalue in item.items() :
    #                 # if thirdkey != 'url' :
    #                 #     continue
    #                 # print (thirdkey)
    #                 # print (thirdvalue)
    #                 # print (thirdkey, thirdvalue)
    #
    #                 if thirdkey == 'requests' :
    #                     totalrequest += thirdvalue
    #                     print ('totalrequest', totalrequest)

    # resultdata.update({"juyun":"www.clearclouds.com"})
    # print (resultdata)

    return url_apdex


#######################################################################################################
#######################################################################################################
#######################################################################################################


def get_json_data_apdex2(rawdata):

    interval = 500000
    resultdata = {}
    firstdata = {}
    seconddata = {}
    thirddata = {}
    alldata = []
    nonalldata = []
    resultdata = {}
    url_requests_inall = {}
    url_apdex = {}
    url_errorrate = {}

    url_satisfied = {}
    url_tolerating = {}
    url_frustrated = {}

    totalrequest = 0
###############################################################################
    hascalc = False
    for firstkey,firstvalue in rawdata.items() :

        if firstkey != 'requests' : continue

        if hascalc == True : break
        hascalc = True

        for secondkey,secondvalue in firstvalue.items() :
            if secondkey != 'all' : continue
            alldata.extend(secondvalue)


    for item in alldata :
        tempdata = {}
        strdata =  '{"%s":%d}' % (item['url'] ,item['requests'] )
        tempdata = eval(strdata)
        # print(tempdata)

        if item['url'] in url_requests_inall :
            url_requests_inall[item['url']] += item['requests']
        else :
            url_requests_inall.update(tempdata)
    # print (url_requests_inall)
##############################################################################

###############################################################################
    nonalldata = []
    hascalc = False
    for firstkey,firstvalue in rawdata.items() :

        if firstkey != 'requests' : continue

        if hascalc == True : break
        hascalc = True
        for secondkey,secondvalue in firstvalue.items() :
            if secondkey == 'all' : continue
            nonalldata.extend(secondvalue)

    for item in nonalldata :
        satisfied = 0
        tolerating = 0
        frustrated = 0
        strdata =  '{"%s":%d}' % (item['url'] ,item['requests'] )
        tempdata = {}
        tempdata = eval(strdata)


        if item['latency'] <= interval * item['requests'] :
            if item['url'] in url_satisfied :
                url_satisfied[item['url']] += item['requests']
            else :
                url_satisfied.update(tempdata)
        elif item['latency'] >  4 * interval * item['requests'] :
            if item['url'] in url_frustrated :
                url_frustrated[item['url']] += item['requests']
            else :
                url_frustrated.update(tempdata)
        else :
            if item['url'] in url_tolerating :
                url_tolerating[item['url']] += item['requests']
            else :
                url_tolerating.update(tempdata)

    # print (url_frustrated)
##############################################################################


###############################################################################
    # print (alldata)
    satisfied = 0
    tolerating = 0
    frustrated = 0

    for item in alldata :

        if re.match(".*.php$",item['url']) == None : continue

        if item['url'] in url_satisfied :
            satisfied += url_satisfied[item['url']]
        elif item['url'] in url_tolerating :
            tolerating += url_tolerating[item['url']]
        elif item['url'] in url_frustrated :
            frustrated += url_frustrated[item['url']]

        total_number = satisfied + tolerating + frustrated

        if total_number == 0 : continue
        

        apdex = (satisfied + tolerating / 2) * 100 / total_number

        tempdata = {}
        strdata =  '{"Component/Apdex/%s":%f}' % (item['url'] ,apdex )
        tempdata = eval(strdata)
        url_apdex.update(tempdata)


        

        # print(tempdata)


    return url_apdex






# def main():

#     # url_apdex = get_json_data_errorate('http_url_5s')


#     url_apdex = get_json_data_apdex('http_url_5s')

#     print(url_apdex)



#     return 0


# exit(main())


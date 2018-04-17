#!/usr/bin/env python

"""
falls.py: Test Framework for running Niagara CI and regression
__copyright__ = "Copyright 2017, Western Digital Corporation"
__author__ = "Sazid Mahammad"
"""

import subprocess
import sys
import os
import platform
import logging
import random
from optparse import OptionParser, OptionGroup

sys.path.append("Falls_Utils")
from Falls_Utils import falls_socket
from Falls_Utils import falls_logging
from Falls_Utils import falls_mail

#Global Constants
FALLS_VERSION = "0.2.1"
USE_SOCKET = True
SUITE_ALDERAAN = "Alderaan"
SUITE_VULCAN = "Vulcan"

LOG_LEVEL_NORMAL = "Normal"
LOG_LEVEL_DEBUG  = "Debug"
COMMAND_TIMEOUT_DEFAULT = -1
UIL_LIST = {'wincil','winahci','sg','linsata','nvme','serial3','test','test2'}

# Find log/nsocket path location Windows/Linux
#todo: check if enviroment variable defined
log_path = os.getenv('FALLS_LOG_DIR', "")
nsocket = os.getenv('NIAGARA_PATH', "")
if platform.system() == 'Windows':
    log_path = "..\\"
    nsocket = "..\\nsocket.exe"
    srcErrFile = "..\\getSourceErr.txt"
else:
    log_path = "../"
    nsocket = "../nsocket"
    srcErrFile = "../getSourceErr.txt"

logger = logging.getLogger(falls_logging.FALLS_LOGGER)

def openshell(command):
    """Issue a command to the shell/console"""
    with subprocess.Popen(command, stdout=subprocess.PIPE, bufsize=0, universal_newlines=True) as p:
        for line in p.stdout:
            print(line, end='')  # print to console

def issue_cmd(command, timeout=COMMAND_TIMEOUT_DEFAULT, show=False, is_testcase=False):
    """Wrapper around issuing commands to log and stub out for testing"""
    logger.debug("Command: %s" % command)
    # todo : Add just test option .. No call to the system
    if(USE_SOCKET == True):
        alderaan_socket = falls_socket.FSocket()
        if False == alderaan_socket.connect():
            logger.error("Error: Failed to connect to Niagara socket")
            print("ERROR: Failed to connect to Niagara socket.\n\t Check if Niagara is running. Pass -l or --launch to launch niagara.")
            exit()
        arg = "-v  " + command
        alderaan_socket.send(arg)
        alderaan_socket.recv(timeout, show, is_testcase)
    else:
        arg = " -v \"" + command + "\""
        openshell(nsocket + arg)

def alderaan(bucket, testcase, codebin, replayfile, randomize=False, log_level=2):
    """Run Alderaan suite
     @bucket: Name of the bucket, None if not applied
     @testcase: Testcases(s), comma separated
     @codebin: Codebin directory path
     @replayfile: Replayfile location
     @randomize: True/False
     @log_level: 2-debug, 1-normal"""
    test_result = {}
    test_cases = []

    if testcase and bucket:
        print("ERROR: Both testcase and bucket not allowed")
        logger.error("ERROR: Both testcase and bucket not allowed")
        return test_result

    # Source falls alderaan
    arg = "source Falls//Alderaan//Falls_Alderaan.tcl"
    issue_cmd(arg)

    #Initialize Alderaan log/replay file etc.
    arg = "::fallsAlderaan::Init 0 "+ str(log_level)
    issue_cmd(arg)

    if codebin:
        #replace all foward slash to back slash
        codebin = codebin.replace('\\' , '/')

        logger.info("Setting codebin path :%s" % codebin)
        cmd = "::fallsAlderaan::SetCodebinPath " + str(codebin)
        issue_cmd(cmd)

    if replayfile:
        if not os.path.isfile(replayfile):
            logger.error("Replay file not found")
            print("\nERROR: Replay file not found.")
            return test_result

        with open(replayfile) as fp:
            for line in fp:
                test_cases.append(line.split("/")[-1][:-1])
                if not testcase:
                    testcase += line.split("/")[-1][:-1]
                else:
                    testcase += "," + line.split("/")[-1][:-1]

    # todo: Only alderaan suite supported (as of now)
    suite = "0"

    suite_bucket = SUITE_ALDERAAN + "_"
    if not testcase:
        suite_bucket += bucket
        bucket_file = ".//Alderaan//Buckets//" + bucket + "_tests.txt"
        with open(bucket_file) as fp:
            for line in fp:
                if "_" in line:
                    test_cases.append(line[:-1])
                else:
                    tests_dir = ".//Alderaan//Tests//" + line[:-1]
                    for test in os.listdir(tests_dir):
                        test_cases.append(test)
    else:
        test_cases = testcase.split(",")

    #Randomize if requested
    if (randomize):
        random.shuffle(test_cases)

    string_testcases = str(test_cases)
    logger.debug("TEST CASES: %s" % string_testcases)

    test_count = 1
    for test in test_cases:
        bucket = "0"
        print("----------------------\nRunning test", test_count," of ", len(test_cases), "\n----------------------")
        arg = "::fallsAlderaan::ExecuteTest 0 " + bucket + " " + suite + " " + test
        issue_cmd(arg, timeout=COMMAND_TIMEOUT_DEFAULT, show=True, is_testcase=True)

        if (USE_SOCKET == True):
            alderaan_socket = falls_socket.FSocket()
            last_result = alderaan_socket.get_last_result()
            test_result[test] = last_result
        test_count += 1

    string_result = str(test_result)
    logger.debug("TEST Result:\n %s" % string_result)
    print("TEST Result:\n", string_result)

    # Close Alderaan log/replay file etc.
    arg = "::fallsAlderaan::CleanupExit"
    issue_cmd(arg)
    return test_result

def clean_exit(status=0):
    """ Exit Niagara after Clean(Socket)"""
    if (USE_SOCKET == True):
        alderaan_socket = falls_socket.FSocket()
        alderaan_socket.disconnect()
    exit(status)

def upload_report(test_result, testlink_ip, testlink_key):
    """ Upload the result to the testlink"""
    build_name = "Build_Bench"
    sys.path.append("Falls_Utils")
    from Falls_Utils import falls_testlink

    #@todo:Handle exception
    testlink_obj = falls_testlink.TestlinkUpdate()
    testlink_obj.connect_testlink(testlink_ip, testlink_key)
    build_name = testlink_obj.createbuild_updateresult(test_result)
    logger.debug("Test Link Build Name: %s" % build_name)
    return build_name

def upload_logs(logfile_name, upload_logs_link, upload_logs_credential):
    """Compress log files and upload the compressed file to artifactory"""
    # @todo:Handle exception
    cmd = "7z  a -ssw " + logfile_name + " .\\Alderaan\Logs\*.log .\\Alderaan\Replays\*.rply .\\Logs\\Niagara_falls.log"
    openshell(cmd)

    log_link =  upload_logs_link + "/Alderaan_logs/" + logfile_name + ".7z"
    cmd = "curl -u"+ upload_logs_credential + " -T .\\" + logfile_name + ".7z " + log_link
    openshell(cmd)
    return log_link

def close_niagara(all_instances=True):
    """Close niagara running instance(s)"""
    ports = []
    logger.info("Close Niagara...")
    alderaan_socket = falls_socket.FSocket()
    ports = alderaan_socket.find_port(True)

    if ports is not None:
        if all_instances:
            for port in ports:
                logger.info("Exiting Niagara...")
                issue_cmd("exit")
                alderaan_socket.disconnect()
                import time
                time.sleep(5)
        else:
            logger.info("Exiting Niagara...")
            issue_cmd("exit")
            alderaan_socket.disconnect()
    else:
        logger.warning("No Niagara instance found.")

def arg_optional(default_val):
    """Callback function for option parser. Handles default string value scenario"""
    def callback_func(option, arg_str, value, parser):
        if parser.rargs and len(parser.rargs[0]) > 2:
            arg_val = parser.rargs[0]
            parser.rargs.pop(0)
        else:
            arg_val = default_val
        setattr(parser.values, option.dest, arg_val)

    return callback_func

def main(args):
    """Options parsing"""
    falls_logging.init_falls_log()
    logger.info("---Niagara Falls(Version:%s)---" % FALLS_VERSION)
    parser = OptionParser(add_help_option=False)

    parser.add_option("-c", "--close", action="store_true",
                      help="Close Niagara(all running instances)")

    parser.add_option("-h", "--help", action="store_true",
                      help="show this help message and exit")

    parser.add_option("-l", "--launch", dest="launch", action='callback', callback=arg_optional('-l 0 -x 64'),
                      help="Launch Niagara. Additional launch parameter can be passed within quote")

    parser.add_option("-q", "--quiet", action="store_true",
                      help="Run in quiet mode. Do not display output")

    parser.add_option("-r", "--random", action="store_true",
                      help="Randomize testcases")

    parser.add_option("-v", "--version", action="store_true",
                      help="Display version information")

    #Options with Value
    argument_opts = OptionGroup(parser, 'Argument options', 'These options need a value', )

    # todo: Add all the supported bucket name in help
    argument_opts.add_option("-b", "--bucket", dest="bucket", type="string",
                      help="Bucket name")

    argument_opts.add_option("-d", "--debuglog", dest="debuglog", type="string",
                      help="Test debug level. Possible values(normal|debug), default log level is debug")

    argument_opts.add_option("-e", "--email", dest="email", type="string",
                      help="User emailId to receive test report")

    argument_opts.add_option("-n", "--codebin", dest="codebin", type="string",
                      help="Path to product codebin directory")

    argument_opts.add_option("-s", "--suite", dest="suite", type="string",
                      help="Suite name")

    argument_opts.add_option("-t", "--testcase", dest="testcase", type="string",
                      help="Testcase name")

    argument_opts.add_option("-y", "--replayfile", dest="replayfile", type="string",
                      help="Replay file location, path with name")

    parser.add_option_group(argument_opts)

    # automation/Jenkins Options
    automation_opts = OptionGroup(parser, 'Automation options','These options are used by Jenkins',)

    automation_opts.add_option("-i", "--testlinkip", dest="testlinkip", type="string",
                      help="Testlink Server IP, used by Jenkins")

    automation_opts.add_option("-k", "--testlinkkey", dest="testlinkkey", type="string",
                      help="Testlink API key, used by Jenkins")

    automation_opts.add_option("-p", "--uploadcredential", dest="uploadcredential", type="string",
                      help="Artifactory credentials, used by Jenkins")

    automation_opts.add_option("-u", "--uploadlink", dest="uploadlink", type="string",
                      help="Artifactory Server details, used by Jenkins")

    parser.add_option_group(automation_opts)

    options = parser.parse_args(args)[0]

    if options.help:
        print("\n")
        parser.print_help()
        exit()

    if options.quiet:
        f = open(os.devnull, 'w')
        sys.stdout = f

        #  No parameter Passed
    if len(sys.argv) < 2:
        print("Error: No Parameter passed.\n")
        parser.print_help()
        exit(1)

        # Help Parameter
    count = 0
    while (count < len(sys.argv)):
        if sys.argv[count] == "help" or sys.argv[count] == "h":
            parser.print_help()
            exit(0)
        count = count + 1

    # Version Parameter
    if options.version:
        print("Niagara Falls Version: ", FALLS_VERSION)
        exit(0)

    if options.close:
        close_niagara()

    uil = "Unknown"
    if options.launch:
        print("Launching Niagara...")
        logger.debug("Launching Niagara...")

        srcErrFileHandle = open(srcErrFile, 'w')
        srcErrFileHandle.close()

        alderaan_socket = falls_socket.FSocket()
        ports = alderaan_socket.find_port(True)
        logger.debug("Existing Niagara ports: %s" % ports)
        if ports is None:
            len_ports = 0
        else:
            len_ports = len(ports)

        if platform.system() == 'Windows':
            #todo: handle exception/check if niagara.exe exists
            from subprocess import Popen
            script = "..\\niagara.exe " +  options.launch
            DETACHED_PROCESS = 0x00000008
            CREATE_NEW_PROCESS_GROUP = 0x00000200
            pid = Popen(script, shell=True, stdin=None, stdout=None, stderr=None,
                        creationflags=DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP)
        elif platform.system() == 'Linux':
            from subprocess import Popen
            # todo: handle exception/check if Niagara.sh exists
            script = "..//Niagara.sh " + options.launch
            pid = Popen(script, shell=True, stdin=None, stdout=None, stderr=None)
        else:
            print("ERROR: OS not supported\n")
            logger.error("OS not supported")
            exit(1)

        #Check for 5 mins
        loop_time = 5*60/15 #5 mins*60sec/sleeptime
        for counter in range(0, int(loop_time+1)):
            import time
            time.sleep(15)

            #Check if the $::env(NiagaraPath)/getSourceErr.txt has any errors populated
            if (os.path.isfile(srcErrFile)) and (os.path.getsize(srcErrFile) > 0) :
                with open(srcErrFile) as srcErrfileobj:
                    # Display all of the errors that were found while sourcing.
                    for x in srcErrfileobj.read().split(";") :
                        print (x)
                        logger.error(x)
                    exit(1)
            elif not os.path.isfile(srcErrFile):
                print("Error getSourceErr.txt failed to be created during startup")
                logger.error("Error getSourceErr.txt failed to be created during startup")
                exit(1)
            else :
               logger.debug("No sourcing errors until this point ...")

            temp_ports = alderaan_socket.find_port(True)
            logger.debug("Niagara ports after 15sec: %s" % temp_ports)
            if temp_ports == None:
                continue
            if len_ports < len(temp_ports):
                issue_cmd("uil name")
                uil = alderaan_socket.last_response.decode('us-ascii')[:-3]
                if str(uil) in UIL_LIST:
                    logger.debug("Niagara launched with driver: %s" % str(uil))
                    break
                else:
                    print("\nERROR: Unknown Niagara driver detected\n")
                    logger.error("Unknown Niagara driver detected: %s" % str(uil) )
                    exit(1)
            elif len_ports > len(temp_ports):
                print("\nERROR: Unexpected behaviour. Existing Niagara instance closed\n")
                logger.error("Existing Niagara instance closed. Niagara ports after 15sec: %s" % temp_ports)
                exit(1)

        if counter >= int(loop_time):
            print("\nERROR: Niagara instance didn't launch within the time\n")
            logger.error("Niagara instance didn't launch within the time")
            exit(1)

    # Parameter Validation
    if options.bucket and options.testcase:
        print("\nERROR: bucket and testcase are not allowed together\n")
        logger.error("bucket and testcase are not allowed together")
        exit(1)

    if options.suite and (options.testcase is None and options.bucket is None and options.replayfile is None):
        print("\nERROR: Bucket, testcase or replay file missing\n")
        logger.error("Bucket, testcase or replay file missing")
        exit(1)

    if options.suite is None and (options.testcase or options.bucket or options.replayfile):
        print("\nERROR: Suite name missing\n")
        logger.error("Suite name missing")
        exit(1)

    if options.suite:
        bucket = ""
        testcase = ""
        email = ""
        if options.bucket:
            bucket = options.bucket
            bucket_file = ".//Alderaan//Buckets//" + bucket + "_tests.txt"
            if not os.path.isfile(bucket_file):
                logger.error("Bucket not found")
                print("\nERROR: Bucket not found.")
                exit(1)
        if options.testcase:
            testcase = options.testcase
        if options.email:
            email = options.email
        randomize = False
        if options.random:
            randomize = True

        build_name = "Build_Bench"
        log_link = ""
        send_mail = False
        #todo: Check if the bucket file exists

        alderaan_socket = falls_socket.FSocket()
        ports = alderaan_socket.find_port(True)

        if ports is None:
            logger.error("No Nigara running instance found")
            print("\nERROR: No Nigara running instance found.\n\tUse -l/--launch to launch Niagara before test run.")
            exit(1)
        else:
            if len(ports) > 1:
                logger.warning("More than one Niagara instance running. The last launched instance will be used for all the operations.")
                print("\nWARNING: More than one Niagara instance running. \n\t The last launched instance will be used for all the operations.")

        log_level = 2 #default log level is debug(2)
        if options.debuglog and options.debuglog.lower() == LOG_LEVEL_NORMAL.lower():
            log_level = 1

        fail_count = 0
        if options.suite.lower() == SUITE_ALDERAAN.lower():
            test_result = alderaan(bucket, testcase, options.codebin, options.replayfile, randomize, log_level)
            issue_cmd("::identify")
            product = alderaan_socket.last_response.decode('us-ascii')[:-3]

            if options.launch:
                close_niagara(False)

            testdesc_dict = {}
            test_result_blocked = test_result.copy()
            # @todo: fix wrorkaround blocked testcase for testlink tool
            for test_name, test_res in test_result_blocked.items():
                if test_res == "SKIPPED":
                    test_result_blocked[test_name] = "BLOCKED"

            if options.testlinkip and options.testlinkkey:
                build_name = upload_report(test_result_blocked, options.testlinkip, options.testlinkkey)
                sys.path.append("Falls_Utils")
                from Falls_Utils import falls_testlink
                testlink_obj = falls_testlink.TestlinkUpdate()
                testlink_obj.connect_testlink(options.testlinkip, options.testlinkkey)
                for test in test_result:
                    testdesc_dict[test]=testlink_obj.gettestcase_summary(test)

            if options.uploadlink and options.uploadcredential:
                log_link = upload_logs(build_name, options.uploadlink, options.uploadcredential)

            if options.email:
                send_mail = True

            if str(uil) not in UIL_LIST:
                issue_cmd("uil name")
                uil = alderaan_socket.last_response.decode('us-ascii')[:-3]

            logger.info("Drive ProductID:%s" % product )
            logger.info("Generating report...")
            falls_mail.send_email(test_result, options.email, SUITE_ALDERAAN, bucket, build_name,
                            uil, product, testdesc_dict, send_mail, log_link)

            fail_count = len([x for x in test_result if test_result[x] == 'FAIL'])
        else:
            print("\nERROR: Invalid Parameter passed. Suite not supported.")
            logger.error("Invalid Parameter passed. Suite not supported.")
            fail_count = 1

        exit(fail_count)

    if options.suite is None and options.launch is None and options.close is None and options.codebin is None:
        print("\nERROR: Invalid Parameter passed.\n")
        parser.print_help()

if __name__ == "__main__":
    sys.exit(main(sys.argv))

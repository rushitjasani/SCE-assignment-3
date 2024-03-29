import sys
import os
import re

cur_dir = os.getcwd()

def cd(args=[]):
    try:
        global cur_dir
        if len(args) >  1:
            print "INVALID ARGUMENTS :("
            return
        elif len(args) == 0 :
            os.chdir(os.path.expanduser("~"))
        else:
            os.chdir(args[0])
        cur_dir = os.getcwd()
    except :
        print "Error :( "

def ls(args=[]):
    try:
        global cur_dir
        if len(args) >  1:
            print "INVALID ARGUMENTS :("
            return
        elif len(args) == 0 :
            path = cur_dir
        else:
            path = args[0]
            if path == "~":
                path = os.path.expanduser("~")
        files = os.listdir(path)
        for f_name in files:
            if(f_name[0] == "."):
                continue
            print f_name
    except:
        print "Error :( "

def pwd(args = []):
    try:
        if len(args) > 0:
            print "INVALID ARGUMENTS :("
            return
        else:
            print os.getcwd()
    except:
        print "Error :( "

def touch( args = [] ):
    try:
        if( len(args) == 0 ):
            print "INVALID ARGUMENTS :("
            return
        else:
            for i in args:
                try:
                    if os.path.isfile(i) :
                        os.utime(i,None)
                    else:
                        with open( i, "a" ):
                            pass
                except:
                    print "Error in touch : " + cur_dir + "/" + i
    except:
        print "Error :( "

def head(args = []):
    try:
        if( len(args) == 0 ):
            print "INVALID ARGUMENTS :("
            return
        else:
            for i in args:
                print "==>" + i + "<=="
                try:
                    with open( i, "r" ) as my_file :
                        for x in xrange(10):
                            try:
                                print next(my_file),
                            except StopIteration:
                                break
                    print 
                except:
                    print "Error in head : " + cur_dir + "/" + i
    except:
        print "Error :( "

def tail(args=[]):
    try:
        if( len(args) == 0 ):
            print "INVALID ARGUMENTS :("
            return
        else:
            for i in args:
                print "==>" + i + "<=="
                line_list = []
                count = 10
                try:
                    for line in reversed(open(i).readlines()):
                        count = count-1
                        line_list.append(line.rstrip())
                        if count == 0:
                            break
                    line_list = reversed(line_list)
                    for i in line_list:
                        print i
                    print
                except:
                    print "Error in head : " + cur_dir + "/" + i
    except:
        print "Error :( "

def tr(args=[]):
    try:
        if(len(args) == 0 or len(args) > 2 ):
            print "INVALID ARGUMENTS :("
            return
        else:
            str1 = args[0]
            str2 = args[1]
            diff =  len(str1) - len( str2 )
            if diff > 0:
                ap = str2[-1]*diff
                str2 = str2 + ap
            l1 = [ x for x in str1 ]
            l2 = [ x for x in str2 ]
            mymap = dict(zip( l1, l2 ))
            while(1):
                str = raw_input()
                ans = ""
                if str == "ctrld":
                    break
                for i in str:
                    if i in mymap:
                        ans = ans + mymap[i]
                    else:
                        ans = ans + i
                print ans
            return    
    except:
        print "Error :( "
     
def grep(args=[]):
    try:
        string_args = ' '.join(args)
        string_args.strip
        first_list = string_args.split('"')
        pattern = first_list[1]
        first_list = first_list[3:]
        mystring = first_list[:-1][0]
        indexes = [ x.start() for x in re.finditer(pattern, mystring)]
        if(len(indexes)) == 0:
            return
        pat_len = len(pattern)
        str_len = len(mystring)
        for i in xrange(str_len):
            if i in indexes:
                sys.stdout.write('\033[91m')    
            sys.stdout.write(mystring[i])
            d = i - pat_len + 1 
            if d in indexes:
                sys.stdout.write('\033[0m')
        print 
        return
    except :
        print "Error :("

def sed(args=[]):
    try:
        string_args = ' '.join(args)
        string_args.strip
        first_list = string_args.split('"')
        pattern1 = first_list[1]
        pattern2 = first_list[3]
        first_list = first_list[5:]
        mystring = first_list[:-1][0]
        ls1 = mystring.split(pattern1)
        final_ans = pattern2.join(ls1)
        print final_ans
        return
    except :
        print "Error :("

def diff(args=[]):
    try:
        if len(args) != 2 :
            print "INVALID ARGUMENTS :("
            return
        else:
            f1 = args[0]
            f2 = args[1]
            s1 = []
            s2 = []
            try:
                with open(f1,"rb") as file1:
                    s1 = file1.readlines()
            except :
                print "File 1 not found"
                return
            try:
                with open(f2,"rb") as file2:
                    s2 = file2.readlines()
            except :
                print "File 2 not found"
                return
            print "--"
            c = 0
            for i in s1:
                if i not in s2:
                    print str(c), i,
                c += 1
            print "++"
            c = 0
            for i in s2:
                if i not in s1:
                    print str(c), i,
                c += 1

    except:
        print "Error :( "

def terminal():
    inp = raw_input()
    cmdlist = inp.split()
    if(len(cmdlist) == 0):
        return
    cmd = cmdlist[0]
    if cmd == "exit":
        sys.exit()
    elif cmd == "cd":
        cd(cmdlist[1:])
    elif cmd == "ls":
        ls(cmdlist[1:])
    elif cmd == "pwd":
        pwd(cmdlist[1:])
    elif cmd == "touch":
        touch(cmdlist[1:])
    elif cmd == "grep":
        grep(cmdlist[1:])
    elif cmd == "head":
        head(cmdlist[1:])
    elif cmd == "tail":
        tail(cmdlist[1:])
    elif cmd == "tr":
        tr(cmdlist[1:])
    elif cmd == "sed":
        sed(cmdlist[1:])
    elif cmd == "diff":
        diff(cmdlist[1:])
    else:
        print "Command not valid\n"
    return

while(1):
    try:
        sys.stdout.write("\033[94;1m" + cur_dir + "\033[0m$")  
        terminal()
    except:
        print
        exit()
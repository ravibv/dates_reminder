def foo():
    print "in foo"
    print "now, returning back000000000000000000000"


def main():
    print "in main"
    print "now, about to call one more function"
    foo()
    
if __name__=="__main__":
    main()
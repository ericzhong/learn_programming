#!/usr/bin/python3


global_a='10'
global_b='20'
special_attributes=['doc','name','module','defaults','code','globals','dict','closure','annotations','kwdefaults']


def test(a,b,c=3,*args,d=4,e=5,**kwargs) -> "just for test":
    '''docstring.'''
    test.m = 'variable of function'
    n = 'local variable'
    print("args: {}".format(args))
    print("kwargs: {}".format(kwargs))
    return


def foo():
    x = "I am used"
    y = "I am free"
    z = "I am free too"

    def bar(x):
        return x, y, z

    return bar


if __name__=='__main__':
    test(1,2,3,4,x=5,y=6)
    for n in special_attributes:
        attr = "__%s__" % n
        print("%s: %s" % (attr,getattr(test,attr)))
    print("bar.__closure__: {}".format([i.cell_contents for i in foo().__closure__]))


# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_osm4routing_xml')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_osm4routing_xml')
    _osm4routing_xml = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_osm4routing_xml', [dirname(__file__)])
        except ImportError:
            import _osm4routing_xml
            return _osm4routing_xml
        try:
            _mod = imp.load_module('_osm4routing_xml', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _osm4routing_xml = swig_import_helper()
    del swig_import_helper
else:
    import _osm4routing_xml
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _osm4routing_xml.delete_SwigPyIterator
    __del__ = lambda self: None

    def value(self):
        return _osm4routing_xml.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _osm4routing_xml.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _osm4routing_xml.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _osm4routing_xml.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _osm4routing_xml.SwigPyIterator_equal(self, x)

    def copy(self):
        return _osm4routing_xml.SwigPyIterator_copy(self)

    def next(self):
        return _osm4routing_xml.SwigPyIterator_next(self)

    def __next__(self):
        return _osm4routing_xml.SwigPyIterator___next__(self)

    def previous(self):
        return _osm4routing_xml.SwigPyIterator_previous(self)

    def advance(self, n):
        return _osm4routing_xml.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _osm4routing_xml.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _osm4routing_xml.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _osm4routing_xml.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _osm4routing_xml.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _osm4routing_xml.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _osm4routing_xml.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self
SwigPyIterator_swigregister = _osm4routing_xml.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class Nodes(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Nodes, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Nodes, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _osm4routing_xml.Nodes_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _osm4routing_xml.Nodes___nonzero__(self)

    def __bool__(self):
        return _osm4routing_xml.Nodes___bool__(self)

    def __len__(self):
        return _osm4routing_xml.Nodes___len__(self)

    def __getslice__(self, i, j):
        return _osm4routing_xml.Nodes___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _osm4routing_xml.Nodes___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _osm4routing_xml.Nodes___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _osm4routing_xml.Nodes___delitem__(self, *args)

    def __getitem__(self, *args):
        return _osm4routing_xml.Nodes___getitem__(self, *args)

    def __setitem__(self, *args):
        return _osm4routing_xml.Nodes___setitem__(self, *args)

    def pop(self):
        return _osm4routing_xml.Nodes_pop(self)

    def append(self, x):
        return _osm4routing_xml.Nodes_append(self, x)

    def empty(self):
        return _osm4routing_xml.Nodes_empty(self)

    def size(self):
        return _osm4routing_xml.Nodes_size(self)

    def swap(self, v):
        return _osm4routing_xml.Nodes_swap(self, v)

    def begin(self):
        return _osm4routing_xml.Nodes_begin(self)

    def end(self):
        return _osm4routing_xml.Nodes_end(self)

    def rbegin(self):
        return _osm4routing_xml.Nodes_rbegin(self)

    def rend(self):
        return _osm4routing_xml.Nodes_rend(self)

    def clear(self):
        return _osm4routing_xml.Nodes_clear(self)

    def get_allocator(self):
        return _osm4routing_xml.Nodes_get_allocator(self)

    def pop_back(self):
        return _osm4routing_xml.Nodes_pop_back(self)

    def erase(self, *args):
        return _osm4routing_xml.Nodes_erase(self, *args)

    def __init__(self, *args):
        this = _osm4routing_xml.new_Nodes(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def push_back(self, x):
        return _osm4routing_xml.Nodes_push_back(self, x)

    def front(self):
        return _osm4routing_xml.Nodes_front(self)

    def back(self):
        return _osm4routing_xml.Nodes_back(self)

    def assign(self, n, x):
        return _osm4routing_xml.Nodes_assign(self, n, x)

    def resize(self, *args):
        return _osm4routing_xml.Nodes_resize(self, *args)

    def insert(self, *args):
        return _osm4routing_xml.Nodes_insert(self, *args)

    def reserve(self, n):
        return _osm4routing_xml.Nodes_reserve(self, n)

    def capacity(self):
        return _osm4routing_xml.Nodes_capacity(self)
    __swig_destroy__ = _osm4routing_xml.delete_Nodes
    __del__ = lambda self: None
Nodes_swigregister = _osm4routing_xml.Nodes_swigregister
Nodes_swigregister(Nodes)

class Edges(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Edges, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Edges, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _osm4routing_xml.Edges_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _osm4routing_xml.Edges___nonzero__(self)

    def __bool__(self):
        return _osm4routing_xml.Edges___bool__(self)

    def __len__(self):
        return _osm4routing_xml.Edges___len__(self)

    def __getslice__(self, i, j):
        return _osm4routing_xml.Edges___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _osm4routing_xml.Edges___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _osm4routing_xml.Edges___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _osm4routing_xml.Edges___delitem__(self, *args)

    def __getitem__(self, *args):
        return _osm4routing_xml.Edges___getitem__(self, *args)

    def __setitem__(self, *args):
        return _osm4routing_xml.Edges___setitem__(self, *args)

    def pop(self):
        return _osm4routing_xml.Edges_pop(self)

    def append(self, x):
        return _osm4routing_xml.Edges_append(self, x)

    def empty(self):
        return _osm4routing_xml.Edges_empty(self)

    def size(self):
        return _osm4routing_xml.Edges_size(self)

    def swap(self, v):
        return _osm4routing_xml.Edges_swap(self, v)

    def begin(self):
        return _osm4routing_xml.Edges_begin(self)

    def end(self):
        return _osm4routing_xml.Edges_end(self)

    def rbegin(self):
        return _osm4routing_xml.Edges_rbegin(self)

    def rend(self):
        return _osm4routing_xml.Edges_rend(self)

    def clear(self):
        return _osm4routing_xml.Edges_clear(self)

    def get_allocator(self):
        return _osm4routing_xml.Edges_get_allocator(self)

    def pop_back(self):
        return _osm4routing_xml.Edges_pop_back(self)

    def erase(self, *args):
        return _osm4routing_xml.Edges_erase(self, *args)

    def __init__(self, *args):
        this = _osm4routing_xml.new_Edges(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def push_back(self, x):
        return _osm4routing_xml.Edges_push_back(self, x)

    def front(self):
        return _osm4routing_xml.Edges_front(self)

    def back(self):
        return _osm4routing_xml.Edges_back(self)

    def assign(self, n, x):
        return _osm4routing_xml.Edges_assign(self, n, x)

    def resize(self, *args):
        return _osm4routing_xml.Edges_resize(self, *args)

    def insert(self, *args):
        return _osm4routing_xml.Edges_insert(self, *args)

    def reserve(self, n):
        return _osm4routing_xml.Edges_reserve(self, n)

    def capacity(self):
        return _osm4routing_xml.Edges_capacity(self)
    __swig_destroy__ = _osm4routing_xml.delete_Edges
    __del__ = lambda self: None
Edges_swigregister = _osm4routing_xml.Edges_swigregister
Edges_swigregister(Edges)

class Edge_property(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Edge_property, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Edge_property, name)
    __repr__ = _swig_repr
    __swig_setmethods__["car_direct"] = _osm4routing_xml.Edge_property_car_direct_set
    __swig_getmethods__["car_direct"] = _osm4routing_xml.Edge_property_car_direct_get
    if _newclass:
        car_direct = _swig_property(_osm4routing_xml.Edge_property_car_direct_get, _osm4routing_xml.Edge_property_car_direct_set)
    __swig_setmethods__["car_reverse"] = _osm4routing_xml.Edge_property_car_reverse_set
    __swig_getmethods__["car_reverse"] = _osm4routing_xml.Edge_property_car_reverse_get
    if _newclass:
        car_reverse = _swig_property(_osm4routing_xml.Edge_property_car_reverse_get, _osm4routing_xml.Edge_property_car_reverse_set)
    __swig_setmethods__["bike_direct"] = _osm4routing_xml.Edge_property_bike_direct_set
    __swig_getmethods__["bike_direct"] = _osm4routing_xml.Edge_property_bike_direct_get
    if _newclass:
        bike_direct = _swig_property(_osm4routing_xml.Edge_property_bike_direct_get, _osm4routing_xml.Edge_property_bike_direct_set)
    __swig_setmethods__["bike_reverse"] = _osm4routing_xml.Edge_property_bike_reverse_set
    __swig_getmethods__["bike_reverse"] = _osm4routing_xml.Edge_property_bike_reverse_get
    if _newclass:
        bike_reverse = _swig_property(_osm4routing_xml.Edge_property_bike_reverse_get, _osm4routing_xml.Edge_property_bike_reverse_set)
    __swig_setmethods__["foot"] = _osm4routing_xml.Edge_property_foot_set
    __swig_getmethods__["foot"] = _osm4routing_xml.Edge_property_foot_get
    if _newclass:
        foot = _swig_property(_osm4routing_xml.Edge_property_foot_get, _osm4routing_xml.Edge_property_foot_set)

    def __init__(self):
        this = _osm4routing_xml.new_Edge_property()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def accessible(self):
        return _osm4routing_xml.Edge_property_accessible(self)

    def direct_accessible(self):
        return _osm4routing_xml.Edge_property_direct_accessible(self)

    def reverse_accessible(self):
        return _osm4routing_xml.Edge_property_reverse_accessible(self)

    def update(self, tag, val):
        return _osm4routing_xml.Edge_property_update(self, tag, val)

    def normalize(self):
        return _osm4routing_xml.Edge_property_normalize(self)

    def reset(self):
        return _osm4routing_xml.Edge_property_reset(self)
    __swig_destroy__ = _osm4routing_xml.delete_Edge_property
    __del__ = lambda self: None
Edge_property_swigregister = _osm4routing_xml.Edge_property_swigregister
Edge_property_swigregister(Edge_property)

class Edge(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Edge, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Edge, name)
    __repr__ = _swig_repr
    __swig_setmethods__["edge_id"] = _osm4routing_xml.Edge_edge_id_set
    __swig_getmethods__["edge_id"] = _osm4routing_xml.Edge_edge_id_get
    if _newclass:
        edge_id = _swig_property(_osm4routing_xml.Edge_edge_id_get, _osm4routing_xml.Edge_edge_id_set)
    __swig_setmethods__["source"] = _osm4routing_xml.Edge_source_set
    __swig_getmethods__["source"] = _osm4routing_xml.Edge_source_get
    if _newclass:
        source = _swig_property(_osm4routing_xml.Edge_source_get, _osm4routing_xml.Edge_source_set)
    __swig_setmethods__["target"] = _osm4routing_xml.Edge_target_set
    __swig_getmethods__["target"] = _osm4routing_xml.Edge_target_get
    if _newclass:
        target = _swig_property(_osm4routing_xml.Edge_target_get, _osm4routing_xml.Edge_target_set)
    __swig_setmethods__["length"] = _osm4routing_xml.Edge_length_set
    __swig_getmethods__["length"] = _osm4routing_xml.Edge_length_get
    if _newclass:
        length = _swig_property(_osm4routing_xml.Edge_length_get, _osm4routing_xml.Edge_length_set)
    __swig_setmethods__["car"] = _osm4routing_xml.Edge_car_set
    __swig_getmethods__["car"] = _osm4routing_xml.Edge_car_get
    if _newclass:
        car = _swig_property(_osm4routing_xml.Edge_car_get, _osm4routing_xml.Edge_car_set)
    __swig_setmethods__["car_d"] = _osm4routing_xml.Edge_car_d_set
    __swig_getmethods__["car_d"] = _osm4routing_xml.Edge_car_d_get
    if _newclass:
        car_d = _swig_property(_osm4routing_xml.Edge_car_d_get, _osm4routing_xml.Edge_car_d_set)
    __swig_setmethods__["bike"] = _osm4routing_xml.Edge_bike_set
    __swig_getmethods__["bike"] = _osm4routing_xml.Edge_bike_get
    if _newclass:
        bike = _swig_property(_osm4routing_xml.Edge_bike_get, _osm4routing_xml.Edge_bike_set)
    __swig_setmethods__["bike_d"] = _osm4routing_xml.Edge_bike_d_set
    __swig_getmethods__["bike_d"] = _osm4routing_xml.Edge_bike_d_get
    if _newclass:
        bike_d = _swig_property(_osm4routing_xml.Edge_bike_d_get, _osm4routing_xml.Edge_bike_d_set)
    __swig_setmethods__["foot"] = _osm4routing_xml.Edge_foot_set
    __swig_getmethods__["foot"] = _osm4routing_xml.Edge_foot_get
    if _newclass:
        foot = _swig_property(_osm4routing_xml.Edge_foot_get, _osm4routing_xml.Edge_foot_set)
    __swig_setmethods__["geom"] = _osm4routing_xml.Edge_geom_set
    __swig_getmethods__["geom"] = _osm4routing_xml.Edge_geom_get
    if _newclass:
        geom = _swig_property(_osm4routing_xml.Edge_geom_get, _osm4routing_xml.Edge_geom_set)

    def __init__(self):
        this = _osm4routing_xml.new_Edge()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _osm4routing_xml.delete_Edge
    __del__ = lambda self: None
Edge_swigregister = _osm4routing_xml.Edge_swigregister
Edge_swigregister(Edge)

class Node(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Node, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Node, name)
    __repr__ = _swig_repr
    __swig_setmethods__["id"] = _osm4routing_xml.Node_id_set
    __swig_getmethods__["id"] = _osm4routing_xml.Node_id_get
    if _newclass:
        id = _swig_property(_osm4routing_xml.Node_id_get, _osm4routing_xml.Node_id_set)
    __swig_setmethods__["lon"] = _osm4routing_xml.Node_lon_set
    __swig_getmethods__["lon"] = _osm4routing_xml.Node_lon_get
    if _newclass:
        lon = _swig_property(_osm4routing_xml.Node_lon_get, _osm4routing_xml.Node_lon_set)
    __swig_setmethods__["lat"] = _osm4routing_xml.Node_lat_set
    __swig_getmethods__["lat"] = _osm4routing_xml.Node_lat_get
    if _newclass:
        lat = _swig_property(_osm4routing_xml.Node_lat_get, _osm4routing_xml.Node_lat_set)
    __swig_setmethods__["uses"] = _osm4routing_xml.Node_uses_set
    __swig_getmethods__["uses"] = _osm4routing_xml.Node_uses_get
    if _newclass:
        uses = _swig_property(_osm4routing_xml.Node_uses_get, _osm4routing_xml.Node_uses_set)

    def __init__(self):
        this = _osm4routing_xml.new_Node()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _osm4routing_xml.delete_Node
    __del__ = lambda self: None
Node_swigregister = _osm4routing_xml.Node_swigregister
Node_swigregister(Node)

class Parser(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Parser, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Parser, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _osm4routing_xml.new_Parser()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def read(self, arg2, arg3, arg4):
        return _osm4routing_xml.Parser_read(self, arg2, arg3, arg4)

    def get_nodes(self):
        return _osm4routing_xml.Parser_get_nodes(self)

    def get_edges(self):
        return _osm4routing_xml.Parser_get_edges(self)

    def get_osm_nodes(self):
        return _osm4routing_xml.Parser_get_osm_nodes(self)

    def get_osm_ways(self):
        return _osm4routing_xml.Parser_get_osm_ways(self)
    __swig_destroy__ = _osm4routing_xml.delete_Parser
    __del__ = lambda self: None
Parser_swigregister = _osm4routing_xml.Parser_swigregister
Parser_swigregister(Parser)

# This file is compatible with both classic and new-style classes.



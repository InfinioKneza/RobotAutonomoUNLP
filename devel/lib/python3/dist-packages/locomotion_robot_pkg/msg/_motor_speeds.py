# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from locomotion_robot_pkg/motor_speeds.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import std_msgs.msg

class motor_speeds(genpy.Message):
  _md5sum = "a93b21787a0d53fc674e601163010b45"
  _type = "locomotion_robot_pkg/motor_speeds"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """std_msgs/Float32 vel_a
std_msgs/Float32 vel_b
================================================================================
MSG: std_msgs/Float32
float32 data"""
  __slots__ = ['vel_a','vel_b']
  _slot_types = ['std_msgs/Float32','std_msgs/Float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       vel_a,vel_b

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(motor_speeds, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.vel_a is None:
        self.vel_a = std_msgs.msg.Float32()
      if self.vel_b is None:
        self.vel_b = std_msgs.msg.Float32()
    else:
      self.vel_a = std_msgs.msg.Float32()
      self.vel_b = std_msgs.msg.Float32()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_2f().pack(_x.vel_a.data, _x.vel_b.data))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.vel_a is None:
        self.vel_a = std_msgs.msg.Float32()
      if self.vel_b is None:
        self.vel_b = std_msgs.msg.Float32()
      end = 0
      _x = self
      start = end
      end += 8
      (_x.vel_a.data, _x.vel_b.data,) = _get_struct_2f().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_2f().pack(_x.vel_a.data, _x.vel_b.data))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.vel_a is None:
        self.vel_a = std_msgs.msg.Float32()
      if self.vel_b is None:
        self.vel_b = std_msgs.msg.Float32()
      end = 0
      _x = self
      start = end
      end += 8
      (_x.vel_a.data, _x.vel_b.data,) = _get_struct_2f().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2f = None
def _get_struct_2f():
    global _struct_2f
    if _struct_2f is None:
        _struct_2f = struct.Struct("<2f")
    return _struct_2f

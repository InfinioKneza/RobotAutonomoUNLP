// Auto-generated. Do not edit!

// (in-package locomotion_robot_pkg.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class sub_move {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.primitive = null;
      this.distance = null;
      this.angle = null;
    }
    else {
      if (initObj.hasOwnProperty('primitive')) {
        this.primitive = initObj.primitive
      }
      else {
        this.primitive = new std_msgs.msg.String();
      }
      if (initObj.hasOwnProperty('distance')) {
        this.distance = initObj.distance
      }
      else {
        this.distance = new std_msgs.msg.Int32();
      }
      if (initObj.hasOwnProperty('angle')) {
        this.angle = initObj.angle
      }
      else {
        this.angle = new std_msgs.msg.Int32();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type sub_move
    // Serialize message field [primitive]
    bufferOffset = std_msgs.msg.String.serialize(obj.primitive, buffer, bufferOffset);
    // Serialize message field [distance]
    bufferOffset = std_msgs.msg.Int32.serialize(obj.distance, buffer, bufferOffset);
    // Serialize message field [angle]
    bufferOffset = std_msgs.msg.Int32.serialize(obj.angle, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type sub_move
    let len;
    let data = new sub_move(null);
    // Deserialize message field [primitive]
    data.primitive = std_msgs.msg.String.deserialize(buffer, bufferOffset);
    // Deserialize message field [distance]
    data.distance = std_msgs.msg.Int32.deserialize(buffer, bufferOffset);
    // Deserialize message field [angle]
    data.angle = std_msgs.msg.Int32.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.String.getMessageSize(object.primitive);
    return length + 8;
  }

  static datatype() {
    // Returns string type for a message object
    return 'locomotion_robot_pkg/sub_move';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '1167768357c0e474a6f4a552c72b1fa2';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    std_msgs/String primitive
    std_msgs/Int32 distance
    std_msgs/Int32 angle
    ================================================================================
    MSG: std_msgs/String
    string data
    
    ================================================================================
    MSG: std_msgs/Int32
    int32 data
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new sub_move(null);
    if (msg.primitive !== undefined) {
      resolved.primitive = std_msgs.msg.String.Resolve(msg.primitive)
    }
    else {
      resolved.primitive = new std_msgs.msg.String()
    }

    if (msg.distance !== undefined) {
      resolved.distance = std_msgs.msg.Int32.Resolve(msg.distance)
    }
    else {
      resolved.distance = new std_msgs.msg.Int32()
    }

    if (msg.angle !== undefined) {
      resolved.angle = std_msgs.msg.Int32.Resolve(msg.angle)
    }
    else {
      resolved.angle = new std_msgs.msg.Int32()
    }

    return resolved;
    }
};

module.exports = sub_move;

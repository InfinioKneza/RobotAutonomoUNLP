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

class sync_type {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.sync_type = null;
      this.factor = null;
      this.dominant_motor = null;
    }
    else {
      if (initObj.hasOwnProperty('sync_type')) {
        this.sync_type = initObj.sync_type
      }
      else {
        this.sync_type = new std_msgs.msg.UInt8();
      }
      if (initObj.hasOwnProperty('factor')) {
        this.factor = initObj.factor
      }
      else {
        this.factor = new std_msgs.msg.Float32();
      }
      if (initObj.hasOwnProperty('dominant_motor')) {
        this.dominant_motor = initObj.dominant_motor
      }
      else {
        this.dominant_motor = new std_msgs.msg.UInt8();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type sync_type
    // Serialize message field [sync_type]
    bufferOffset = std_msgs.msg.UInt8.serialize(obj.sync_type, buffer, bufferOffset);
    // Serialize message field [factor]
    bufferOffset = std_msgs.msg.Float32.serialize(obj.factor, buffer, bufferOffset);
    // Serialize message field [dominant_motor]
    bufferOffset = std_msgs.msg.UInt8.serialize(obj.dominant_motor, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type sync_type
    let len;
    let data = new sync_type(null);
    // Deserialize message field [sync_type]
    data.sync_type = std_msgs.msg.UInt8.deserialize(buffer, bufferOffset);
    // Deserialize message field [factor]
    data.factor = std_msgs.msg.Float32.deserialize(buffer, bufferOffset);
    // Deserialize message field [dominant_motor]
    data.dominant_motor = std_msgs.msg.UInt8.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 6;
  }

  static datatype() {
    // Returns string type for a message object
    return 'locomotion_robot_pkg/sync_type';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '2ed07a61fe23e1a973a3f61ff858d59f';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    std_msgs/UInt8 sync_type
    std_msgs/Float32 factor
    std_msgs/UInt8 dominant_motor
    ================================================================================
    MSG: std_msgs/UInt8
    uint8 data
    
    ================================================================================
    MSG: std_msgs/Float32
    float32 data
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new sync_type(null);
    if (msg.sync_type !== undefined) {
      resolved.sync_type = std_msgs.msg.UInt8.Resolve(msg.sync_type)
    }
    else {
      resolved.sync_type = new std_msgs.msg.UInt8()
    }

    if (msg.factor !== undefined) {
      resolved.factor = std_msgs.msg.Float32.Resolve(msg.factor)
    }
    else {
      resolved.factor = new std_msgs.msg.Float32()
    }

    if (msg.dominant_motor !== undefined) {
      resolved.dominant_motor = std_msgs.msg.UInt8.Resolve(msg.dominant_motor)
    }
    else {
      resolved.dominant_motor = new std_msgs.msg.UInt8()
    }

    return resolved;
    }
};

module.exports = sync_type;

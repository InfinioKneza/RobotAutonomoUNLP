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

class motor_speeds {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.vel_a = null;
      this.vel_b = null;
    }
    else {
      if (initObj.hasOwnProperty('vel_a')) {
        this.vel_a = initObj.vel_a
      }
      else {
        this.vel_a = new std_msgs.msg.Float32();
      }
      if (initObj.hasOwnProperty('vel_b')) {
        this.vel_b = initObj.vel_b
      }
      else {
        this.vel_b = new std_msgs.msg.Float32();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type motor_speeds
    // Serialize message field [vel_a]
    bufferOffset = std_msgs.msg.Float32.serialize(obj.vel_a, buffer, bufferOffset);
    // Serialize message field [vel_b]
    bufferOffset = std_msgs.msg.Float32.serialize(obj.vel_b, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type motor_speeds
    let len;
    let data = new motor_speeds(null);
    // Deserialize message field [vel_a]
    data.vel_a = std_msgs.msg.Float32.deserialize(buffer, bufferOffset);
    // Deserialize message field [vel_b]
    data.vel_b = std_msgs.msg.Float32.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 8;
  }

  static datatype() {
    // Returns string type for a message object
    return 'locomotion_robot_pkg/motor_speeds';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'a93b21787a0d53fc674e601163010b45';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    std_msgs/Float32 vel_a
    std_msgs/Float32 vel_b
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
    const resolved = new motor_speeds(null);
    if (msg.vel_a !== undefined) {
      resolved.vel_a = std_msgs.msg.Float32.Resolve(msg.vel_a)
    }
    else {
      resolved.vel_a = new std_msgs.msg.Float32()
    }

    if (msg.vel_b !== undefined) {
      resolved.vel_b = std_msgs.msg.Float32.Resolve(msg.vel_b)
    }
    else {
      resolved.vel_b = new std_msgs.msg.Float32()
    }

    return resolved;
    }
};

module.exports = motor_speeds;

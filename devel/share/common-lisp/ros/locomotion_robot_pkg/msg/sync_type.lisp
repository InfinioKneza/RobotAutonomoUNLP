; Auto-generated. Do not edit!


(cl:in-package locomotion_robot_pkg-msg)


;//! \htmlinclude sync_type.msg.html

(cl:defclass <sync_type> (roslisp-msg-protocol:ros-message)
  ((sync_type
    :reader sync_type
    :initarg :sync_type
    :type std_msgs-msg:UInt8
    :initform (cl:make-instance 'std_msgs-msg:UInt8))
   (factor
    :reader factor
    :initarg :factor
    :type std_msgs-msg:Float32
    :initform (cl:make-instance 'std_msgs-msg:Float32))
   (dominant_motor
    :reader dominant_motor
    :initarg :dominant_motor
    :type std_msgs-msg:UInt8
    :initform (cl:make-instance 'std_msgs-msg:UInt8)))
)

(cl:defclass sync_type (<sync_type>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <sync_type>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'sync_type)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name locomotion_robot_pkg-msg:<sync_type> is deprecated: use locomotion_robot_pkg-msg:sync_type instead.")))

(cl:ensure-generic-function 'sync_type-val :lambda-list '(m))
(cl:defmethod sync_type-val ((m <sync_type>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader locomotion_robot_pkg-msg:sync_type-val is deprecated.  Use locomotion_robot_pkg-msg:sync_type instead.")
  (sync_type m))

(cl:ensure-generic-function 'factor-val :lambda-list '(m))
(cl:defmethod factor-val ((m <sync_type>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader locomotion_robot_pkg-msg:factor-val is deprecated.  Use locomotion_robot_pkg-msg:factor instead.")
  (factor m))

(cl:ensure-generic-function 'dominant_motor-val :lambda-list '(m))
(cl:defmethod dominant_motor-val ((m <sync_type>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader locomotion_robot_pkg-msg:dominant_motor-val is deprecated.  Use locomotion_robot_pkg-msg:dominant_motor instead.")
  (dominant_motor m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <sync_type>) ostream)
  "Serializes a message object of type '<sync_type>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'sync_type) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'factor) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'dominant_motor) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <sync_type>) istream)
  "Deserializes a message object of type '<sync_type>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'sync_type) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'factor) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'dominant_motor) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<sync_type>)))
  "Returns string type for a message object of type '<sync_type>"
  "locomotion_robot_pkg/sync_type")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'sync_type)))
  "Returns string type for a message object of type 'sync_type"
  "locomotion_robot_pkg/sync_type")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<sync_type>)))
  "Returns md5sum for a message object of type '<sync_type>"
  "2ed07a61fe23e1a973a3f61ff858d59f")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'sync_type)))
  "Returns md5sum for a message object of type 'sync_type"
  "2ed07a61fe23e1a973a3f61ff858d59f")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<sync_type>)))
  "Returns full string definition for message of type '<sync_type>"
  (cl:format cl:nil "std_msgs/UInt8 sync_type~%std_msgs/Float32 factor~%std_msgs/UInt8 dominant_motor~%================================================================================~%MSG: std_msgs/UInt8~%uint8 data~%~%================================================================================~%MSG: std_msgs/Float32~%float32 data~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'sync_type)))
  "Returns full string definition for message of type 'sync_type"
  (cl:format cl:nil "std_msgs/UInt8 sync_type~%std_msgs/Float32 factor~%std_msgs/UInt8 dominant_motor~%================================================================================~%MSG: std_msgs/UInt8~%uint8 data~%~%================================================================================~%MSG: std_msgs/Float32~%float32 data~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <sync_type>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'sync_type))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'factor))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'dominant_motor))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <sync_type>))
  "Converts a ROS message object to a list"
  (cl:list 'sync_type
    (cl:cons ':sync_type (sync_type msg))
    (cl:cons ':factor (factor msg))
    (cl:cons ':dominant_motor (dominant_motor msg))
))

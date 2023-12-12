; Auto-generated. Do not edit!


(cl:in-package locomotion_robot_pkg-msg)


;//! \htmlinclude motor_speeds.msg.html

(cl:defclass <motor_speeds> (roslisp-msg-protocol:ros-message)
  ((vel_a
    :reader vel_a
    :initarg :vel_a
    :type std_msgs-msg:Float32
    :initform (cl:make-instance 'std_msgs-msg:Float32))
   (vel_b
    :reader vel_b
    :initarg :vel_b
    :type std_msgs-msg:Float32
    :initform (cl:make-instance 'std_msgs-msg:Float32)))
)

(cl:defclass motor_speeds (<motor_speeds>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <motor_speeds>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'motor_speeds)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name locomotion_robot_pkg-msg:<motor_speeds> is deprecated: use locomotion_robot_pkg-msg:motor_speeds instead.")))

(cl:ensure-generic-function 'vel_a-val :lambda-list '(m))
(cl:defmethod vel_a-val ((m <motor_speeds>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader locomotion_robot_pkg-msg:vel_a-val is deprecated.  Use locomotion_robot_pkg-msg:vel_a instead.")
  (vel_a m))

(cl:ensure-generic-function 'vel_b-val :lambda-list '(m))
(cl:defmethod vel_b-val ((m <motor_speeds>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader locomotion_robot_pkg-msg:vel_b-val is deprecated.  Use locomotion_robot_pkg-msg:vel_b instead.")
  (vel_b m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <motor_speeds>) ostream)
  "Serializes a message object of type '<motor_speeds>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'vel_a) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'vel_b) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <motor_speeds>) istream)
  "Deserializes a message object of type '<motor_speeds>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'vel_a) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'vel_b) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<motor_speeds>)))
  "Returns string type for a message object of type '<motor_speeds>"
  "locomotion_robot_pkg/motor_speeds")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'motor_speeds)))
  "Returns string type for a message object of type 'motor_speeds"
  "locomotion_robot_pkg/motor_speeds")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<motor_speeds>)))
  "Returns md5sum for a message object of type '<motor_speeds>"
  "a93b21787a0d53fc674e601163010b45")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'motor_speeds)))
  "Returns md5sum for a message object of type 'motor_speeds"
  "a93b21787a0d53fc674e601163010b45")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<motor_speeds>)))
  "Returns full string definition for message of type '<motor_speeds>"
  (cl:format cl:nil "std_msgs/Float32 vel_a~%std_msgs/Float32 vel_b~%================================================================================~%MSG: std_msgs/Float32~%float32 data~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'motor_speeds)))
  "Returns full string definition for message of type 'motor_speeds"
  (cl:format cl:nil "std_msgs/Float32 vel_a~%std_msgs/Float32 vel_b~%================================================================================~%MSG: std_msgs/Float32~%float32 data~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <motor_speeds>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'vel_a))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'vel_b))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <motor_speeds>))
  "Converts a ROS message object to a list"
  (cl:list 'motor_speeds
    (cl:cons ':vel_a (vel_a msg))
    (cl:cons ':vel_b (vel_b msg))
))

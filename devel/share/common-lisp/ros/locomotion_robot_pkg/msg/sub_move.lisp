; Auto-generated. Do not edit!


(cl:in-package locomotion_robot_pkg-msg)


;//! \htmlinclude sub_move.msg.html

(cl:defclass <sub_move> (roslisp-msg-protocol:ros-message)
  ((primitive
    :reader primitive
    :initarg :primitive
    :type std_msgs-msg:String
    :initform (cl:make-instance 'std_msgs-msg:String))
   (distance
    :reader distance
    :initarg :distance
    :type std_msgs-msg:Int32
    :initform (cl:make-instance 'std_msgs-msg:Int32))
   (angle
    :reader angle
    :initarg :angle
    :type std_msgs-msg:Int32
    :initform (cl:make-instance 'std_msgs-msg:Int32)))
)

(cl:defclass sub_move (<sub_move>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <sub_move>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'sub_move)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name locomotion_robot_pkg-msg:<sub_move> is deprecated: use locomotion_robot_pkg-msg:sub_move instead.")))

(cl:ensure-generic-function 'primitive-val :lambda-list '(m))
(cl:defmethod primitive-val ((m <sub_move>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader locomotion_robot_pkg-msg:primitive-val is deprecated.  Use locomotion_robot_pkg-msg:primitive instead.")
  (primitive m))

(cl:ensure-generic-function 'distance-val :lambda-list '(m))
(cl:defmethod distance-val ((m <sub_move>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader locomotion_robot_pkg-msg:distance-val is deprecated.  Use locomotion_robot_pkg-msg:distance instead.")
  (distance m))

(cl:ensure-generic-function 'angle-val :lambda-list '(m))
(cl:defmethod angle-val ((m <sub_move>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader locomotion_robot_pkg-msg:angle-val is deprecated.  Use locomotion_robot_pkg-msg:angle instead.")
  (angle m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <sub_move>) ostream)
  "Serializes a message object of type '<sub_move>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'primitive) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'distance) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'angle) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <sub_move>) istream)
  "Deserializes a message object of type '<sub_move>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'primitive) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'distance) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'angle) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<sub_move>)))
  "Returns string type for a message object of type '<sub_move>"
  "locomotion_robot_pkg/sub_move")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'sub_move)))
  "Returns string type for a message object of type 'sub_move"
  "locomotion_robot_pkg/sub_move")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<sub_move>)))
  "Returns md5sum for a message object of type '<sub_move>"
  "1167768357c0e474a6f4a552c72b1fa2")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'sub_move)))
  "Returns md5sum for a message object of type 'sub_move"
  "1167768357c0e474a6f4a552c72b1fa2")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<sub_move>)))
  "Returns full string definition for message of type '<sub_move>"
  (cl:format cl:nil "std_msgs/String primitive~%std_msgs/Int32 distance~%std_msgs/Int32 angle~%================================================================================~%MSG: std_msgs/String~%string data~%~%================================================================================~%MSG: std_msgs/Int32~%int32 data~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'sub_move)))
  "Returns full string definition for message of type 'sub_move"
  (cl:format cl:nil "std_msgs/String primitive~%std_msgs/Int32 distance~%std_msgs/Int32 angle~%================================================================================~%MSG: std_msgs/String~%string data~%~%================================================================================~%MSG: std_msgs/Int32~%int32 data~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <sub_move>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'primitive))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'distance))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'angle))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <sub_move>))
  "Converts a ROS message object to a list"
  (cl:list 'sub_move
    (cl:cons ':primitive (primitive msg))
    (cl:cons ':distance (distance msg))
    (cl:cons ':angle (angle msg))
))

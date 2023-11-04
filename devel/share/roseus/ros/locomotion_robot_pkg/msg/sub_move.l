;; Auto-generated. Do not edit!


(when (boundp 'locomotion_robot_pkg::sub_move)
  (if (not (find-package "LOCOMOTION_ROBOT_PKG"))
    (make-package "LOCOMOTION_ROBOT_PKG"))
  (shadow 'sub_move (find-package "LOCOMOTION_ROBOT_PKG")))
(unless (find-package "LOCOMOTION_ROBOT_PKG::SUB_MOVE")
  (make-package "LOCOMOTION_ROBOT_PKG::SUB_MOVE"))

(in-package "ROS")
;;//! \htmlinclude sub_move.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass locomotion_robot_pkg::sub_move
  :super ros::object
  :slots (_primitive _distance _angle ))

(defmethod locomotion_robot_pkg::sub_move
  (:init
   (&key
    ((:primitive __primitive) (instance std_msgs::String :init))
    ((:distance __distance) (instance std_msgs::Int32 :init))
    ((:angle __angle) (instance std_msgs::Int32 :init))
    )
   (send-super :init)
   (setq _primitive __primitive)
   (setq _distance __distance)
   (setq _angle __angle)
   self)
  (:primitive
   (&rest __primitive)
   (if (keywordp (car __primitive))
       (send* _primitive __primitive)
     (progn
       (if __primitive (setq _primitive (car __primitive)))
       _primitive)))
  (:distance
   (&rest __distance)
   (if (keywordp (car __distance))
       (send* _distance __distance)
     (progn
       (if __distance (setq _distance (car __distance)))
       _distance)))
  (:angle
   (&rest __angle)
   (if (keywordp (car __angle))
       (send* _angle __angle)
     (progn
       (if __angle (setq _angle (car __angle)))
       _angle)))
  (:serialization-length
   ()
   (+
    ;; std_msgs/String _primitive
    (send _primitive :serialization-length)
    ;; std_msgs/Int32 _distance
    (send _distance :serialization-length)
    ;; std_msgs/Int32 _angle
    (send _angle :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/String _primitive
       (send _primitive :serialize s)
     ;; std_msgs/Int32 _distance
       (send _distance :serialize s)
     ;; std_msgs/Int32 _angle
       (send _angle :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/String _primitive
     (send _primitive :deserialize buf ptr-) (incf ptr- (send _primitive :serialization-length))
   ;; std_msgs/Int32 _distance
     (send _distance :deserialize buf ptr-) (incf ptr- (send _distance :serialization-length))
   ;; std_msgs/Int32 _angle
     (send _angle :deserialize buf ptr-) (incf ptr- (send _angle :serialization-length))
   ;;
   self)
  )

(setf (get locomotion_robot_pkg::sub_move :md5sum-) "1167768357c0e474a6f4a552c72b1fa2")
(setf (get locomotion_robot_pkg::sub_move :datatype-) "locomotion_robot_pkg/sub_move")
(setf (get locomotion_robot_pkg::sub_move :definition-)
      "std_msgs/String primitive
std_msgs/Int32 distance
std_msgs/Int32 angle
================================================================================
MSG: std_msgs/String
string data

================================================================================
MSG: std_msgs/Int32
int32 data
")



(provide :locomotion_robot_pkg/sub_move "1167768357c0e474a6f4a552c72b1fa2")



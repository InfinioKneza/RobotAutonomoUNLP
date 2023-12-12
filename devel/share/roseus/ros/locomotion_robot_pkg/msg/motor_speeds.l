;; Auto-generated. Do not edit!


(when (boundp 'locomotion_robot_pkg::motor_speeds)
  (if (not (find-package "LOCOMOTION_ROBOT_PKG"))
    (make-package "LOCOMOTION_ROBOT_PKG"))
  (shadow 'motor_speeds (find-package "LOCOMOTION_ROBOT_PKG")))
(unless (find-package "LOCOMOTION_ROBOT_PKG::MOTOR_SPEEDS")
  (make-package "LOCOMOTION_ROBOT_PKG::MOTOR_SPEEDS"))

(in-package "ROS")
;;//! \htmlinclude motor_speeds.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass locomotion_robot_pkg::motor_speeds
  :super ros::object
  :slots (_vel_a _vel_b ))

(defmethod locomotion_robot_pkg::motor_speeds
  (:init
   (&key
    ((:vel_a __vel_a) (instance std_msgs::Float32 :init))
    ((:vel_b __vel_b) (instance std_msgs::Float32 :init))
    )
   (send-super :init)
   (setq _vel_a __vel_a)
   (setq _vel_b __vel_b)
   self)
  (:vel_a
   (&rest __vel_a)
   (if (keywordp (car __vel_a))
       (send* _vel_a __vel_a)
     (progn
       (if __vel_a (setq _vel_a (car __vel_a)))
       _vel_a)))
  (:vel_b
   (&rest __vel_b)
   (if (keywordp (car __vel_b))
       (send* _vel_b __vel_b)
     (progn
       (if __vel_b (setq _vel_b (car __vel_b)))
       _vel_b)))
  (:serialization-length
   ()
   (+
    ;; std_msgs/Float32 _vel_a
    (send _vel_a :serialization-length)
    ;; std_msgs/Float32 _vel_b
    (send _vel_b :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Float32 _vel_a
       (send _vel_a :serialize s)
     ;; std_msgs/Float32 _vel_b
       (send _vel_b :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Float32 _vel_a
     (send _vel_a :deserialize buf ptr-) (incf ptr- (send _vel_a :serialization-length))
   ;; std_msgs/Float32 _vel_b
     (send _vel_b :deserialize buf ptr-) (incf ptr- (send _vel_b :serialization-length))
   ;;
   self)
  )

(setf (get locomotion_robot_pkg::motor_speeds :md5sum-) "a93b21787a0d53fc674e601163010b45")
(setf (get locomotion_robot_pkg::motor_speeds :datatype-) "locomotion_robot_pkg/motor_speeds")
(setf (get locomotion_robot_pkg::motor_speeds :definition-)
      "std_msgs/Float32 vel_a
std_msgs/Float32 vel_b
================================================================================
MSG: std_msgs/Float32
float32 data
")



(provide :locomotion_robot_pkg/motor_speeds "a93b21787a0d53fc674e601163010b45")



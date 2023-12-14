;; Auto-generated. Do not edit!


(when (boundp 'locomotion_robot_pkg::sync_type)
  (if (not (find-package "LOCOMOTION_ROBOT_PKG"))
    (make-package "LOCOMOTION_ROBOT_PKG"))
  (shadow 'sync_type (find-package "LOCOMOTION_ROBOT_PKG")))
(unless (find-package "LOCOMOTION_ROBOT_PKG::SYNC_TYPE")
  (make-package "LOCOMOTION_ROBOT_PKG::SYNC_TYPE"))

(in-package "ROS")
;;//! \htmlinclude sync_type.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass locomotion_robot_pkg::sync_type
  :super ros::object
  :slots (_sync_type _factor _dominant_motor ))

(defmethod locomotion_robot_pkg::sync_type
  (:init
   (&key
    ((:sync_type __sync_type) (instance std_msgs::UInt8 :init))
    ((:factor __factor) (instance std_msgs::Float32 :init))
    ((:dominant_motor __dominant_motor) (instance std_msgs::UInt8 :init))
    )
   (send-super :init)
   (setq _sync_type __sync_type)
   (setq _factor __factor)
   (setq _dominant_motor __dominant_motor)
   self)
  (:sync_type
   (&rest __sync_type)
   (if (keywordp (car __sync_type))
       (send* _sync_type __sync_type)
     (progn
       (if __sync_type (setq _sync_type (car __sync_type)))
       _sync_type)))
  (:factor
   (&rest __factor)
   (if (keywordp (car __factor))
       (send* _factor __factor)
     (progn
       (if __factor (setq _factor (car __factor)))
       _factor)))
  (:dominant_motor
   (&rest __dominant_motor)
   (if (keywordp (car __dominant_motor))
       (send* _dominant_motor __dominant_motor)
     (progn
       (if __dominant_motor (setq _dominant_motor (car __dominant_motor)))
       _dominant_motor)))
  (:serialization-length
   ()
   (+
    ;; std_msgs/UInt8 _sync_type
    (send _sync_type :serialization-length)
    ;; std_msgs/Float32 _factor
    (send _factor :serialization-length)
    ;; std_msgs/UInt8 _dominant_motor
    (send _dominant_motor :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/UInt8 _sync_type
       (send _sync_type :serialize s)
     ;; std_msgs/Float32 _factor
       (send _factor :serialize s)
     ;; std_msgs/UInt8 _dominant_motor
       (send _dominant_motor :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/UInt8 _sync_type
     (send _sync_type :deserialize buf ptr-) (incf ptr- (send _sync_type :serialization-length))
   ;; std_msgs/Float32 _factor
     (send _factor :deserialize buf ptr-) (incf ptr- (send _factor :serialization-length))
   ;; std_msgs/UInt8 _dominant_motor
     (send _dominant_motor :deserialize buf ptr-) (incf ptr- (send _dominant_motor :serialization-length))
   ;;
   self)
  )

(setf (get locomotion_robot_pkg::sync_type :md5sum-) "2ed07a61fe23e1a973a3f61ff858d59f")
(setf (get locomotion_robot_pkg::sync_type :datatype-) "locomotion_robot_pkg/sync_type")
(setf (get locomotion_robot_pkg::sync_type :definition-)
      "std_msgs/UInt8 sync_type
std_msgs/Float32 factor
std_msgs/UInt8 dominant_motor
================================================================================
MSG: std_msgs/UInt8
uint8 data

================================================================================
MSG: std_msgs/Float32
float32 data
")



(provide :locomotion_robot_pkg/sync_type "2ed07a61fe23e1a973a3f61ff858d59f")



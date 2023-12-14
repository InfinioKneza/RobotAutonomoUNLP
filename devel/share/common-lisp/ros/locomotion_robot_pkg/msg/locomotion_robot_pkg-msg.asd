
(cl:in-package :asdf)

(defsystem "locomotion_robot_pkg-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "motor_speeds" :depends-on ("_package_motor_speeds"))
    (:file "_package_motor_speeds" :depends-on ("_package"))
    (:file "sub_move" :depends-on ("_package_sub_move"))
    (:file "_package_sub_move" :depends-on ("_package"))
    (:file "sync_type" :depends-on ("_package_sync_type"))
    (:file "_package_sync_type" :depends-on ("_package"))
  ))
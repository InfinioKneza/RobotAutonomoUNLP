
(cl:in-package :asdf)

(defsystem "locomotion_robot_pkg-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "sub_move" :depends-on ("_package_sub_move"))
    (:file "_package_sub_move" :depends-on ("_package"))
  ))
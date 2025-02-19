#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

def callback(data):
    rospy.loginfo(f"Received command: {data.data}")
    
    # Membuat publisher untuk mengontrol TurtleSim
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    twist = Twist()
    
    # Menentukan perintah berdasarkan input string
    if data.data.lower() == "maju":
        twist.linear.x = 2.0
        twist.angular.z = 0.0
    elif data.data.lower() == "mundur":
        twist.linear.x = -2.0
        twist.angular.z = 0.0
    elif data.data.lower() == "kiri":
        twist.linear.x = 0.0
        twist.angular.z = 2.0
    elif data.data.lower() == "kanan":
        twist.linear.x = 0.0
        twist.angular.z = -2.0
    else:
        rospy.loginfo("Perintah tidak dikenali. Gunakan: maju, mundur, kiri, kanan")
        return  # Tidak mengirim perintah jika input salah

    # Publikasi perintah ke TurtleSim
    pub.publish(twist)

def listener():
    rospy.init_node('turtle_controller', anonymous=True)
    rospy.Subscriber("/turtle_commands", String, callback)  # Subscriber untuk topik '/turtle_commands'
    rospy.spin()  # Menjaga node tetap berjalan

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass

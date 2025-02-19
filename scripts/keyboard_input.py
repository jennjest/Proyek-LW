#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def main():
    # Inisialisasi node ROS
    rospy.init_node('keyboard_input', anonymous=True)
    
    # Membuat publisher untuk topik '/turtle_commands'
    pub = rospy.Publisher('/turtle_commands', String, queue_size=10)
    
    # Feedback untuk pengguna
    rospy.loginfo("Node keyboard_input aktif. Masukkan perintah: maju, mundur, kiri, kanan. Tekan Ctrl+C untuk keluar.")
    
    # Loop untuk meminta input pengguna
    while not rospy.is_shutdown():
        try:
            # Menerima input dari keyboard
            command = input("Masukkan perintah (maju/mundur/kiri/kanan): ").strip().lower()
            
            # Validasi input
            if command in ["maju", "mundur", "kiri", "kanan"]:
                # Publikasi perintah ke topik '/turtle_commands'
                pub.publish(command)
                rospy.loginfo(f"Perintah '{command}' telah dikirim ke /turtle_commands")
            else:
                rospy.loginfo("Perintah tidak valid. Gunakan: maju, mundur, kiri, kanan.")
        except KeyboardInterrupt:
            rospy.loginfo("Node keyboard_input dihentikan.")
            break

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass

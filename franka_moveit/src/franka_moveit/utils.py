
import geometry_msgs.msg
import quaternion

def create_pose_stamped_msg(position, orientation):
    """
        Create Pose message using the provided position and orientation

        :return: Pose message for the give end-effector position and orientation
        :rtype: geometry_msgs.msg.Pose
        :param position: End-effector position in base frame of the robot
        :type position: [float]*3
        :param orientation: orientation quaternion of end-effector in base frame
        :type orientation: quaternion.quaternion / [float]*4: (w,x,y,z)
    """
    pose = geometry_msgs.msg.Pose()

    pose.position.x = position[0]
    pose.position.y = position[1]
    pose.position.z = position[2]

    if isinstance(orientation,quaternion.quaternion):
        pose.orientation.x = orientation.x
        pose.orientation.y = orientation.y
        pose.orientation.z = orientation.z
        pose.orientation.w = orientation.w
    else:
        pose.orientation.x = orientation[1]
        pose.orientation.y = orientation[2]
        pose.orientation.z = orientation[3]
        pose.orientation.w = orientation[0]

    return pose
    
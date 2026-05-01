# Status message for the arm subsystem
std_msgs/Header header
bool is_moving
float32[] joint_angles  # radians
string state            # e.g. "idle", "moving", "error"

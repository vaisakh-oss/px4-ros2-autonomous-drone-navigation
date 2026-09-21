#include <chrono>
#include <functional>
#include <memory>
#include <string>

#include "rclcpp/rclcpp.hpp"
#include "geometry_msgs/msg/pose_stamped.hpp"

class DroneNavigationNode : public rclcpp::Node
{
public:
    DroneNavigationNode() : Node("drone_nav_node")
    {
        RCLCPP_INFO(this->get_logger(), "Autonomous Drone Navigation Node Initialized.");
        RCLCPP_INFO(this->get_logger(), "Developer: Vaisakh TV | System: Offboard Simulation Mode");
    }
};

int main(int argc, char * argv[])
{
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<DroneNavigationNode>());
    rclcpp::shutdown();
    return 0;
}

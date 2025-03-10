import rclpy
from rclpy.node import Node
from std_msgs.msg import String 

class SimpleSubscriber(Node):
    def __init__(self):
        
        # name of the node
        super().__init__("simple_subscriber")

        # name of the topic
        self.sub_ = self.create_subscription(String, 'chatter', self.msgCallback, 10 )

    def msgCallback(self, msg):
        self.get_logger().info(f"I heard: {msg.data}")

def main():
    # initialise ros2
    rclpy.init()

    simple_subscriber = SimpleSubscriber()

    rclpy.spin(simple_subscriber)

    simple_subscriber.destroy_node()

    rclpy.shutdown()

if __name__ == "__main__":
    main()
# 🤖 FALCON – Color Sorting Robot

<p align="center">
  <img src="https://user-images.githubusercontent.com/your_image_here.gif" width="300" alt="FALCON Robot">
</p>

Welcome to **FALCON** – a smart and fully functional color-sorting robot equipped with a robotic arm and autonomous movement. It detects colored objects using OpenCV and sorts them precisely using inverse kinematics and servo motors. Built with Raspberry Pi, 3D-printed components, and a passion for automation!

---

## 📦 Features

- 🎯 **Color-Based Object Detection** using OpenCV (HSV model)
- 🚗 **Autonomous Navigation** powered by Raspberry Pi
- 🦾 **Robotic Arm Control** with Inverse Kinematics (TinyIK)
- 🔊 **Voice Feedback** with Text-to-Speech
- 🔋 **Battery Monitoring** with LiPo Indicator
- 💡 **LED Signaling** and Safety Indicators
- 🧠 Modular Python Codebase with GPIO, PCA9685, and more

---

## 📸 Project Demo

Falcon

---

## 🛠 Hardware Used

| Component | Description |
|----------|-------------|
| Raspberry Pi 4 Model B | Brain of the robot |
| Pi Camera v2 | For real-time color detection |
| MG996R & MG90S Servos | Arm actuation |
| PCA9685 | 16-channel PWM controller |
| L298N Driver | DC motor control |
| LiPo Battery | Portable power supply |
| Ultrasonic Sensor | Obstacle detection |

---

## 🧠 Software Stack

- **Python 3** for all logic
- **OpenCV** for image processing
- **TinyIK** for inverse kinematics
- **Adafruit PCA9685** for servo control
- **GPIOZero / RPi.GPIO** for motor commands
- **SolidWorks** for mechanical CAD design
- **3D Printing** with Creality Ender 3 V2

---

## 🔄 System Architecture

[ Camera ] ---> [ Color Detection ] ---> [ Raspberry Pi ]
|--> [ Arm IK + Motor Control ]
|--> [ LEDs + Voice ]
|--> [ Movement Logic ]


---

## 🧠 How It Works

1. The camera detects the object’s color using the HSV color model.
2. If color matches, robot navigates towards the object.
3. Inverse Kinematics calculates joint angles.
4. The robotic arm picks and places the object in the correct colored bin.
5. The robot announces its action with voice feedback.


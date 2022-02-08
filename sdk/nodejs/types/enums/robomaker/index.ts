// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***


export const RobotApplicationRobotSoftwareSuiteName = {
    Ros: "ROS",
    Ros2: "ROS2",
    General: "General",
} as const;

/**
 * The name of robot software suite.
 */
export type RobotApplicationRobotSoftwareSuiteName = (typeof RobotApplicationRobotSoftwareSuiteName)[keyof typeof RobotApplicationRobotSoftwareSuiteName];

export const RobotApplicationRobotSoftwareSuiteVersion = {
    Kinetic: "Kinetic",
    Melodic: "Melodic",
    Dashing: "Dashing",
} as const;

/**
 * The version of robot software suite.
 */
export type RobotApplicationRobotSoftwareSuiteVersion = (typeof RobotApplicationRobotSoftwareSuiteVersion)[keyof typeof RobotApplicationRobotSoftwareSuiteVersion];

export const RobotApplicationSourceConfigArchitecture = {
    X8664: "X86_64",
    Arm64: "ARM64",
    Armhf: "ARMHF",
} as const;

/**
 * The architecture of robot application.
 */
export type RobotApplicationSourceConfigArchitecture = (typeof RobotApplicationSourceConfigArchitecture)[keyof typeof RobotApplicationSourceConfigArchitecture];

export const RobotArchitecture = {
    X8664: "X86_64",
    Arm64: "ARM64",
    Armhf: "ARMHF",
} as const;

/**
 * The target architecture of the robot.
 */
export type RobotArchitecture = (typeof RobotArchitecture)[keyof typeof RobotArchitecture];

export const SimulationApplicationRenderingEngineName = {
    Ogre: "OGRE",
} as const;

/**
 * The name of the rendering engine.
 */
export type SimulationApplicationRenderingEngineName = (typeof SimulationApplicationRenderingEngineName)[keyof typeof SimulationApplicationRenderingEngineName];

export const SimulationApplicationRobotSoftwareSuiteName = {
    Ros: "ROS",
    Ros2: "ROS2",
    General: "General",
} as const;

/**
 * The name of the robot software suite.
 */
export type SimulationApplicationRobotSoftwareSuiteName = (typeof SimulationApplicationRobotSoftwareSuiteName)[keyof typeof SimulationApplicationRobotSoftwareSuiteName];

export const SimulationApplicationRobotSoftwareSuiteVersion = {
    Kinetic: "Kinetic",
    Melodic: "Melodic",
    Dashing: "Dashing",
    Foxy: "Foxy",
} as const;

/**
 * The version of the robot software suite.
 */
export type SimulationApplicationRobotSoftwareSuiteVersion = (typeof SimulationApplicationRobotSoftwareSuiteVersion)[keyof typeof SimulationApplicationRobotSoftwareSuiteVersion];

export const SimulationApplicationSimulationSoftwareSuiteName = {
    Gazebo: "Gazebo",
    RosbagPlay: "RosbagPlay",
    SimulationRuntime: "SimulationRuntime",
} as const;

/**
 * The name of the simulation software suite.
 */
export type SimulationApplicationSimulationSoftwareSuiteName = (typeof SimulationApplicationSimulationSoftwareSuiteName)[keyof typeof SimulationApplicationSimulationSoftwareSuiteName];

export const SimulationApplicationSimulationSoftwareSuiteVersion = {
    Seven: "7",
    Nine: "9",
    SimulationApplicationSimulationSoftwareSuiteVersion_11: "11",
    Kinetic: "Kinetic",
    Melodic: "Melodic",
    Dashing: "Dashing",
    Foxy: "Foxy",
} as const;

/**
 * The version of the simulation software suite.
 */
export type SimulationApplicationSimulationSoftwareSuiteVersion = (typeof SimulationApplicationSimulationSoftwareSuiteVersion)[keyof typeof SimulationApplicationSimulationSoftwareSuiteVersion];

export const SimulationApplicationSourceConfigArchitecture = {
    X8664: "X86_64",
    Arm64: "ARM64",
    Armhf: "ARMHF",
} as const;

/**
 * The target processor architecture for the application.
 */
export type SimulationApplicationSourceConfigArchitecture = (typeof SimulationApplicationSourceConfigArchitecture)[keyof typeof SimulationApplicationSourceConfigArchitecture];

// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * The AWS::GameLift::Fleet resource creates an Amazon GameLift (GameLift) fleet to host game servers. A fleet is a set of EC2 or Anywhere instances, each of which can host multiple game sessions.
 */
export class Fleet extends pulumi.CustomResource {
    /**
     * Get an existing Fleet resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Fleet {
        return new Fleet(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:gamelift:Fleet';

    /**
     * Returns true if the given object is an instance of Fleet.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Fleet {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Fleet.__pulumiType;
    }

    /**
     * Configuration for Anywhere fleet.
     */
    public readonly anywhereConfiguration!: pulumi.Output<outputs.gamelift.FleetAnywhereConfiguration | undefined>;
    /**
     * A unique identifier for a build to be deployed on the new fleet. If you are deploying the fleet with a custom game build, you must specify this property. The build must have been successfully uploaded to Amazon GameLift and be in a READY status. This fleet setting cannot be changed once the fleet is created.
     */
    public readonly buildId!: pulumi.Output<string | undefined>;
    /**
     * Indicates whether to generate a TLS/SSL certificate for the new fleet. TLS certificates are used for encrypting traffic between game clients and game servers running on GameLift. If this parameter is not set, certificate generation is disabled. This fleet setting cannot be changed once the fleet is created.
     */
    public readonly certificateConfiguration!: pulumi.Output<outputs.gamelift.FleetCertificateConfiguration | undefined>;
    /**
     * ComputeType to differentiate EC2 hardware managed by GameLift and Anywhere hardware managed by the customer.
     */
    public readonly computeType!: pulumi.Output<enums.gamelift.FleetComputeType | undefined>;
    /**
     * A human-readable description of a fleet.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * [DEPRECATED] The number of EC2 instances that you want this fleet to host. When creating a new fleet, GameLift automatically sets this value to "1" and initiates a single instance. Once the fleet is active, update this value to trigger GameLift to add or remove instances from the fleet.
     */
    public readonly desiredEc2Instances!: pulumi.Output<number | undefined>;
    /**
     * A range of IP addresses and port settings that allow inbound traffic to connect to server processes on an Amazon GameLift server.
     */
    public readonly ec2InboundPermissions!: pulumi.Output<outputs.gamelift.FleetIpPermission[] | undefined>;
    /**
     * The name of an EC2 instance type that is supported in Amazon GameLift. A fleet instance type determines the computing resources of each instance in the fleet, including CPU, memory, storage, and networking capacity. Amazon GameLift supports the following EC2 instance types. See Amazon EC2 Instance Types for detailed descriptions.
     */
    public readonly ec2InstanceType!: pulumi.Output<string | undefined>;
    /**
     * Unique fleet ID
     */
    public /*out*/ readonly fleetId!: pulumi.Output<string>;
    /**
     * Indicates whether to use On-Demand instances or Spot instances for this fleet. If empty, the default is ON_DEMAND. Both categories of instances use identical hardware and configurations based on the instance type selected for this fleet.
     */
    public readonly fleetType!: pulumi.Output<enums.gamelift.FleetType | undefined>;
    /**
     * A unique identifier for an AWS IAM role that manages access to your AWS services. With an instance role ARN set, any application that runs on an instance in this fleet can assume the role, including install scripts, server processes, and daemons (background processes). Create a role or look up a role's ARN from the IAM dashboard in the AWS Management Console.
     */
    public readonly instanceRoleArn!: pulumi.Output<string | undefined>;
    public readonly locations!: pulumi.Output<outputs.gamelift.FleetLocationConfiguration[] | undefined>;
    /**
     * This parameter is no longer used. When hosting a custom game build, specify where Amazon GameLift should store log files using the Amazon GameLift server API call ProcessReady()
     */
    public readonly logPaths!: pulumi.Output<string[] | undefined>;
    /**
     * [DEPRECATED] The maximum value that is allowed for the fleet's instance count. When creating a new fleet, GameLift automatically sets this value to "1". Once the fleet is active, you can change this value.
     */
    public readonly maxSize!: pulumi.Output<number | undefined>;
    /**
     * The name of an Amazon CloudWatch metric group. A metric group aggregates the metrics for all fleets in the group. Specify a string containing the metric group name. You can use an existing name or use a new name to create a new metric group. Currently, this parameter can have only one string.
     */
    public readonly metricGroups!: pulumi.Output<string[] | undefined>;
    /**
     * [DEPRECATED] The minimum value allowed for the fleet's instance count. When creating a new fleet, GameLift automatically sets this value to "0". After the fleet is active, you can change this value.
     */
    public readonly minSize!: pulumi.Output<number | undefined>;
    /**
     * A descriptive label that is associated with a fleet. Fleet names do not need to be unique.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * A game session protection policy to apply to all game sessions hosted on instances in this fleet. When protected, active game sessions cannot be terminated during a scale-down event. If this parameter is not set, instances in this fleet default to no protection. You can change a fleet's protection policy to affect future game sessions on the fleet. You can also set protection for individual game sessions.
     */
    public readonly newGameSessionProtectionPolicy!: pulumi.Output<enums.gamelift.FleetNewGameSessionProtectionPolicy | undefined>;
    /**
     * A unique identifier for the AWS account with the VPC that you want to peer your Amazon GameLift fleet with. You can find your account ID in the AWS Management Console under account settings.
     */
    public readonly peerVpcAwsAccountId!: pulumi.Output<string | undefined>;
    /**
     * A unique identifier for a VPC with resources to be accessed by your Amazon GameLift fleet. The VPC must be in the same Region as your fleet. To look up a VPC ID, use the VPC Dashboard in the AWS Management Console.
     */
    public readonly peerVpcId!: pulumi.Output<string | undefined>;
    /**
     * A policy that limits the number of game sessions an individual player can create over a span of time for this fleet.
     */
    public readonly resourceCreationLimitPolicy!: pulumi.Output<outputs.gamelift.FleetResourceCreationLimitPolicy | undefined>;
    /**
     * Instructions for launching server processes on each instance in the fleet. Server processes run either a custom game build executable or a Realtime script. The runtime configuration defines the server executables or launch script file, launch parameters, and the number of processes to run concurrently on each instance. When creating a fleet, the runtime configuration must have at least one server process configuration; otherwise the request fails with an invalid request exception.
     *
     * This parameter is required unless the parameters ServerLaunchPath and ServerLaunchParameters are defined. Runtime configuration has replaced these parameters, but fleets that use them will continue to work.
     */
    public readonly runtimeConfiguration!: pulumi.Output<outputs.gamelift.FleetRuntimeConfiguration | undefined>;
    /**
     * A unique identifier for a Realtime script to be deployed on a new Realtime Servers fleet. The script must have been successfully uploaded to Amazon GameLift. This fleet setting cannot be changed once the fleet is created.
     *
     * Note: It is not currently possible to use the !Ref command to reference a script created with a CloudFormation template for the fleet property ScriptId. Instead, use Fn::GetAtt Script.Arn or Fn::GetAtt Script.Id to retrieve either of these properties as input for ScriptId. Alternatively, enter a ScriptId string manually.
     */
    public readonly scriptId!: pulumi.Output<string | undefined>;
    /**
     * This parameter is no longer used but is retained for backward compatibility. Instead, specify server launch parameters in the RuntimeConfiguration parameter. A request must specify either a runtime configuration or values for both ServerLaunchParameters and ServerLaunchPath.
     */
    public readonly serverLaunchParameters!: pulumi.Output<string | undefined>;
    /**
     * This parameter is no longer used. Instead, specify a server launch path using the RuntimeConfiguration parameter. Requests that specify a server launch path and launch parameters instead of a runtime configuration will continue to work.
     */
    public readonly serverLaunchPath!: pulumi.Output<string | undefined>;

    /**
     * Create a Fleet resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: FleetArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            resourceInputs["anywhereConfiguration"] = args ? args.anywhereConfiguration : undefined;
            resourceInputs["buildId"] = args ? args.buildId : undefined;
            resourceInputs["certificateConfiguration"] = args ? args.certificateConfiguration : undefined;
            resourceInputs["computeType"] = args ? args.computeType : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["desiredEc2Instances"] = args ? args.desiredEc2Instances : undefined;
            resourceInputs["ec2InboundPermissions"] = args ? args.ec2InboundPermissions : undefined;
            resourceInputs["ec2InstanceType"] = args ? args.ec2InstanceType : undefined;
            resourceInputs["fleetType"] = args ? args.fleetType : undefined;
            resourceInputs["instanceRoleArn"] = args ? args.instanceRoleArn : undefined;
            resourceInputs["locations"] = args ? args.locations : undefined;
            resourceInputs["logPaths"] = args ? args.logPaths : undefined;
            resourceInputs["maxSize"] = args ? args.maxSize : undefined;
            resourceInputs["metricGroups"] = args ? args.metricGroups : undefined;
            resourceInputs["minSize"] = args ? args.minSize : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["newGameSessionProtectionPolicy"] = args ? args.newGameSessionProtectionPolicy : undefined;
            resourceInputs["peerVpcAwsAccountId"] = args ? args.peerVpcAwsAccountId : undefined;
            resourceInputs["peerVpcId"] = args ? args.peerVpcId : undefined;
            resourceInputs["resourceCreationLimitPolicy"] = args ? args.resourceCreationLimitPolicy : undefined;
            resourceInputs["runtimeConfiguration"] = args ? args.runtimeConfiguration : undefined;
            resourceInputs["scriptId"] = args ? args.scriptId : undefined;
            resourceInputs["serverLaunchParameters"] = args ? args.serverLaunchParameters : undefined;
            resourceInputs["serverLaunchPath"] = args ? args.serverLaunchPath : undefined;
            resourceInputs["fleetId"] = undefined /*out*/;
        } else {
            resourceInputs["anywhereConfiguration"] = undefined /*out*/;
            resourceInputs["buildId"] = undefined /*out*/;
            resourceInputs["certificateConfiguration"] = undefined /*out*/;
            resourceInputs["computeType"] = undefined /*out*/;
            resourceInputs["description"] = undefined /*out*/;
            resourceInputs["desiredEc2Instances"] = undefined /*out*/;
            resourceInputs["ec2InboundPermissions"] = undefined /*out*/;
            resourceInputs["ec2InstanceType"] = undefined /*out*/;
            resourceInputs["fleetId"] = undefined /*out*/;
            resourceInputs["fleetType"] = undefined /*out*/;
            resourceInputs["instanceRoleArn"] = undefined /*out*/;
            resourceInputs["locations"] = undefined /*out*/;
            resourceInputs["logPaths"] = undefined /*out*/;
            resourceInputs["maxSize"] = undefined /*out*/;
            resourceInputs["metricGroups"] = undefined /*out*/;
            resourceInputs["minSize"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["newGameSessionProtectionPolicy"] = undefined /*out*/;
            resourceInputs["peerVpcAwsAccountId"] = undefined /*out*/;
            resourceInputs["peerVpcId"] = undefined /*out*/;
            resourceInputs["resourceCreationLimitPolicy"] = undefined /*out*/;
            resourceInputs["runtimeConfiguration"] = undefined /*out*/;
            resourceInputs["scriptId"] = undefined /*out*/;
            resourceInputs["serverLaunchParameters"] = undefined /*out*/;
            resourceInputs["serverLaunchPath"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Fleet.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Fleet resource.
 */
export interface FleetArgs {
    /**
     * Configuration for Anywhere fleet.
     */
    anywhereConfiguration?: pulumi.Input<inputs.gamelift.FleetAnywhereConfigurationArgs>;
    /**
     * A unique identifier for a build to be deployed on the new fleet. If you are deploying the fleet with a custom game build, you must specify this property. The build must have been successfully uploaded to Amazon GameLift and be in a READY status. This fleet setting cannot be changed once the fleet is created.
     */
    buildId?: pulumi.Input<string>;
    /**
     * Indicates whether to generate a TLS/SSL certificate for the new fleet. TLS certificates are used for encrypting traffic between game clients and game servers running on GameLift. If this parameter is not set, certificate generation is disabled. This fleet setting cannot be changed once the fleet is created.
     */
    certificateConfiguration?: pulumi.Input<inputs.gamelift.FleetCertificateConfigurationArgs>;
    /**
     * ComputeType to differentiate EC2 hardware managed by GameLift and Anywhere hardware managed by the customer.
     */
    computeType?: pulumi.Input<enums.gamelift.FleetComputeType>;
    /**
     * A human-readable description of a fleet.
     */
    description?: pulumi.Input<string>;
    /**
     * [DEPRECATED] The number of EC2 instances that you want this fleet to host. When creating a new fleet, GameLift automatically sets this value to "1" and initiates a single instance. Once the fleet is active, update this value to trigger GameLift to add or remove instances from the fleet.
     */
    desiredEc2Instances?: pulumi.Input<number>;
    /**
     * A range of IP addresses and port settings that allow inbound traffic to connect to server processes on an Amazon GameLift server.
     */
    ec2InboundPermissions?: pulumi.Input<pulumi.Input<inputs.gamelift.FleetIpPermissionArgs>[]>;
    /**
     * The name of an EC2 instance type that is supported in Amazon GameLift. A fleet instance type determines the computing resources of each instance in the fleet, including CPU, memory, storage, and networking capacity. Amazon GameLift supports the following EC2 instance types. See Amazon EC2 Instance Types for detailed descriptions.
     */
    ec2InstanceType?: pulumi.Input<string>;
    /**
     * Indicates whether to use On-Demand instances or Spot instances for this fleet. If empty, the default is ON_DEMAND. Both categories of instances use identical hardware and configurations based on the instance type selected for this fleet.
     */
    fleetType?: pulumi.Input<enums.gamelift.FleetType>;
    /**
     * A unique identifier for an AWS IAM role that manages access to your AWS services. With an instance role ARN set, any application that runs on an instance in this fleet can assume the role, including install scripts, server processes, and daemons (background processes). Create a role or look up a role's ARN from the IAM dashboard in the AWS Management Console.
     */
    instanceRoleArn?: pulumi.Input<string>;
    locations?: pulumi.Input<pulumi.Input<inputs.gamelift.FleetLocationConfigurationArgs>[]>;
    /**
     * This parameter is no longer used. When hosting a custom game build, specify where Amazon GameLift should store log files using the Amazon GameLift server API call ProcessReady()
     */
    logPaths?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * [DEPRECATED] The maximum value that is allowed for the fleet's instance count. When creating a new fleet, GameLift automatically sets this value to "1". Once the fleet is active, you can change this value.
     */
    maxSize?: pulumi.Input<number>;
    /**
     * The name of an Amazon CloudWatch metric group. A metric group aggregates the metrics for all fleets in the group. Specify a string containing the metric group name. You can use an existing name or use a new name to create a new metric group. Currently, this parameter can have only one string.
     */
    metricGroups?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * [DEPRECATED] The minimum value allowed for the fleet's instance count. When creating a new fleet, GameLift automatically sets this value to "0". After the fleet is active, you can change this value.
     */
    minSize?: pulumi.Input<number>;
    /**
     * A descriptive label that is associated with a fleet. Fleet names do not need to be unique.
     */
    name?: pulumi.Input<string>;
    /**
     * A game session protection policy to apply to all game sessions hosted on instances in this fleet. When protected, active game sessions cannot be terminated during a scale-down event. If this parameter is not set, instances in this fleet default to no protection. You can change a fleet's protection policy to affect future game sessions on the fleet. You can also set protection for individual game sessions.
     */
    newGameSessionProtectionPolicy?: pulumi.Input<enums.gamelift.FleetNewGameSessionProtectionPolicy>;
    /**
     * A unique identifier for the AWS account with the VPC that you want to peer your Amazon GameLift fleet with. You can find your account ID in the AWS Management Console under account settings.
     */
    peerVpcAwsAccountId?: pulumi.Input<string>;
    /**
     * A unique identifier for a VPC with resources to be accessed by your Amazon GameLift fleet. The VPC must be in the same Region as your fleet. To look up a VPC ID, use the VPC Dashboard in the AWS Management Console.
     */
    peerVpcId?: pulumi.Input<string>;
    /**
     * A policy that limits the number of game sessions an individual player can create over a span of time for this fleet.
     */
    resourceCreationLimitPolicy?: pulumi.Input<inputs.gamelift.FleetResourceCreationLimitPolicyArgs>;
    /**
     * Instructions for launching server processes on each instance in the fleet. Server processes run either a custom game build executable or a Realtime script. The runtime configuration defines the server executables or launch script file, launch parameters, and the number of processes to run concurrently on each instance. When creating a fleet, the runtime configuration must have at least one server process configuration; otherwise the request fails with an invalid request exception.
     *
     * This parameter is required unless the parameters ServerLaunchPath and ServerLaunchParameters are defined. Runtime configuration has replaced these parameters, but fleets that use them will continue to work.
     */
    runtimeConfiguration?: pulumi.Input<inputs.gamelift.FleetRuntimeConfigurationArgs>;
    /**
     * A unique identifier for a Realtime script to be deployed on a new Realtime Servers fleet. The script must have been successfully uploaded to Amazon GameLift. This fleet setting cannot be changed once the fleet is created.
     *
     * Note: It is not currently possible to use the !Ref command to reference a script created with a CloudFormation template for the fleet property ScriptId. Instead, use Fn::GetAtt Script.Arn or Fn::GetAtt Script.Id to retrieve either of these properties as input for ScriptId. Alternatively, enter a ScriptId string manually.
     */
    scriptId?: pulumi.Input<string>;
    /**
     * This parameter is no longer used but is retained for backward compatibility. Instead, specify server launch parameters in the RuntimeConfiguration parameter. A request must specify either a runtime configuration or values for both ServerLaunchParameters and ServerLaunchPath.
     */
    serverLaunchParameters?: pulumi.Input<string>;
    /**
     * This parameter is no longer used. Instead, specify a server launch path using the RuntimeConfiguration parameter. Requests that specify a server launch path and launch parameters instead of a runtime configuration will continue to work.
     */
    serverLaunchPath?: pulumi.Input<string>;
}

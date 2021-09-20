// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package gamelift

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The AWS::GameLift::Fleet resource creates an Amazon GameLift (GameLift) fleet to host game servers.  A fleet is a set of EC2 instances, each of which can host multiple game sessions.
type Fleet struct {
	pulumi.CustomResourceState

	// A unique identifier for a build to be deployed on the new fleet. If you are deploying the fleet with a custom game build, you must specify this property. The build must have been successfully uploaded to Amazon GameLift and be in a READY status. This fleet setting cannot be changed once the fleet is created.
	BuildId pulumi.StringPtrOutput `pulumi:"buildId"`
	// Indicates whether to generate a TLS/SSL certificate for the new fleet. TLS certificates are used for encrypting traffic between game clients and game servers running on GameLift. If this parameter is not set, certificate generation is disabled. This fleet setting cannot be changed once the fleet is created.
	CertificateConfiguration FleetCertificateConfigurationPtrOutput `pulumi:"certificateConfiguration"`
	// A human-readable description of a fleet.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// [DEPRECATED] The number of EC2 instances that you want this fleet to host. When creating a new fleet, GameLift automatically sets this value to "1" and initiates a single instance. Once the fleet is active, update this value to trigger GameLift to add or remove instances from the fleet.
	DesiredEC2Instances pulumi.IntPtrOutput `pulumi:"desiredEC2Instances"`
	// A range of IP addresses and port settings that allow inbound traffic to connect to server processes on an Amazon GameLift server.
	EC2InboundPermissions FleetIpPermissionArrayOutput `pulumi:"eC2InboundPermissions"`
	// The name of an EC2 instance type that is supported in Amazon GameLift. A fleet instance type determines the computing resources of each instance in the fleet, including CPU, memory, storage, and networking capacity. Amazon GameLift supports the following EC2 instance types. See Amazon EC2 Instance Types for detailed descriptions.
	EC2InstanceType pulumi.StringPtrOutput `pulumi:"eC2InstanceType"`
	// Unique fleet ID
	FleetId pulumi.StringOutput `pulumi:"fleetId"`
	// Indicates whether to use On-Demand instances or Spot instances for this fleet. If empty, the default is ON_DEMAND. Both categories of instances use identical hardware and configurations based on the instance type selected for this fleet.
	FleetType FleetFleetTypePtrOutput `pulumi:"fleetType"`
	// A unique identifier for an AWS IAM role that manages access to your AWS services. With an instance role ARN set, any application that runs on an instance in this fleet can assume the role, including install scripts, server processes, and daemons (background processes). Create a role or look up a role's ARN from the IAM dashboard in the AWS Management Console.
	InstanceRoleARN pulumi.StringPtrOutput                `pulumi:"instanceRoleARN"`
	Locations       FleetLocationConfigurationArrayOutput `pulumi:"locations"`
	// This parameter is no longer used. When hosting a custom game build, specify where Amazon GameLift should store log files using the Amazon GameLift server API call ProcessReady()
	LogPaths pulumi.StringArrayOutput `pulumi:"logPaths"`
	// [DEPRECATED] The maximum value that is allowed for the fleet's instance count. When creating a new fleet, GameLift automatically sets this value to "1". Once the fleet is active, you can change this value.
	MaxSize pulumi.IntPtrOutput `pulumi:"maxSize"`
	// The name of an Amazon CloudWatch metric group. A metric group aggregates the metrics for all fleets in the group. Specify a string containing the metric group name. You can use an existing name or use a new name to create a new metric group. Currently, this parameter can have only one string.
	MetricGroups pulumi.StringArrayOutput `pulumi:"metricGroups"`
	// [DEPRECATED] The minimum value allowed for the fleet's instance count. When creating a new fleet, GameLift automatically sets this value to "0". After the fleet is active, you can change this value.
	MinSize pulumi.IntPtrOutput `pulumi:"minSize"`
	// A descriptive label that is associated with a fleet. Fleet names do not need to be unique.
	Name pulumi.StringPtrOutput `pulumi:"name"`
	// A game session protection policy to apply to all game sessions hosted on instances in this fleet. When protected, active game sessions cannot be terminated during a scale-down event. If this parameter is not set, instances in this fleet default to no protection. You can change a fleet's protection policy to affect future game sessions on the fleet. You can also set protection for individual game sessions.
	NewGameSessionProtectionPolicy FleetNewGameSessionProtectionPolicyPtrOutput `pulumi:"newGameSessionProtectionPolicy"`
	// A unique identifier for the AWS account with the VPC that you want to peer your Amazon GameLift fleet with. You can find your account ID in the AWS Management Console under account settings.
	PeerVpcAwsAccountId pulumi.StringPtrOutput `pulumi:"peerVpcAwsAccountId"`
	// A unique identifier for a VPC with resources to be accessed by your Amazon GameLift fleet. The VPC must be in the same Region as your fleet. To look up a VPC ID, use the VPC Dashboard in the AWS Management Console.
	PeerVpcId pulumi.StringPtrOutput `pulumi:"peerVpcId"`
	// A policy that limits the number of game sessions an individual player can create over a span of time for this fleet.
	ResourceCreationLimitPolicy FleetResourceCreationLimitPolicyPtrOutput `pulumi:"resourceCreationLimitPolicy"`
	// Instructions for launching server processes on each instance in the fleet. Server processes run either a custom game build executable or a Realtime script. The runtime configuration defines the server executables or launch script file, launch parameters, and the number of processes to run concurrently on each instance. When creating a fleet, the runtime configuration must have at least one server process configuration; otherwise the request fails with an invalid request exception.
	//
	// This parameter is required unless the parameters ServerLaunchPath and ServerLaunchParameters are defined. Runtime configuration has replaced these parameters, but fleets that use them will continue to work.
	RuntimeConfiguration FleetRuntimeConfigurationPtrOutput `pulumi:"runtimeConfiguration"`
	// A unique identifier for a Realtime script to be deployed on a new Realtime Servers fleet. The script must have been successfully uploaded to Amazon GameLift. This fleet setting cannot be changed once the fleet is created.
	//
	// Note: It is not currently possible to use the !Ref command to reference a script created with a CloudFormation template for the fleet property ScriptId. Instead, use Fn::GetAtt Script.Arn or Fn::GetAtt Script.Id to retrieve either of these properties as input for ScriptId. Alternatively, enter a ScriptId string manually.
	ScriptId pulumi.StringPtrOutput `pulumi:"scriptId"`
	// This parameter is no longer used but is retained for backward compatibility. Instead, specify server launch parameters in the RuntimeConfiguration parameter. A request must specify either a runtime configuration or values for both ServerLaunchParameters and ServerLaunchPath.
	ServerLaunchParameters pulumi.StringPtrOutput `pulumi:"serverLaunchParameters"`
	// This parameter is no longer used. Instead, specify a server launch path using the RuntimeConfiguration parameter. Requests that specify a server launch path and launch parameters instead of a runtime configuration will continue to work.
	ServerLaunchPath pulumi.StringPtrOutput `pulumi:"serverLaunchPath"`
}

// NewFleet registers a new resource with the given unique name, arguments, and options.
func NewFleet(ctx *pulumi.Context,
	name string, args *FleetArgs, opts ...pulumi.ResourceOption) (*Fleet, error) {
	if args == nil {
		args = &FleetArgs{}
	}

	var resource Fleet
	err := ctx.RegisterResource("aws-native:gamelift:Fleet", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetFleet gets an existing Fleet resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetFleet(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *FleetState, opts ...pulumi.ResourceOption) (*Fleet, error) {
	var resource Fleet
	err := ctx.ReadResource("aws-native:gamelift:Fleet", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Fleet resources.
type fleetState struct {
}

type FleetState struct {
}

func (FleetState) ElementType() reflect.Type {
	return reflect.TypeOf((*fleetState)(nil)).Elem()
}

type fleetArgs struct {
	// A unique identifier for a build to be deployed on the new fleet. If you are deploying the fleet with a custom game build, you must specify this property. The build must have been successfully uploaded to Amazon GameLift and be in a READY status. This fleet setting cannot be changed once the fleet is created.
	BuildId *string `pulumi:"buildId"`
	// Indicates whether to generate a TLS/SSL certificate for the new fleet. TLS certificates are used for encrypting traffic between game clients and game servers running on GameLift. If this parameter is not set, certificate generation is disabled. This fleet setting cannot be changed once the fleet is created.
	CertificateConfiguration *FleetCertificateConfiguration `pulumi:"certificateConfiguration"`
	// A human-readable description of a fleet.
	Description *string `pulumi:"description"`
	// [DEPRECATED] The number of EC2 instances that you want this fleet to host. When creating a new fleet, GameLift automatically sets this value to "1" and initiates a single instance. Once the fleet is active, update this value to trigger GameLift to add or remove instances from the fleet.
	DesiredEC2Instances *int `pulumi:"desiredEC2Instances"`
	// A range of IP addresses and port settings that allow inbound traffic to connect to server processes on an Amazon GameLift server.
	EC2InboundPermissions []FleetIpPermission `pulumi:"eC2InboundPermissions"`
	// The name of an EC2 instance type that is supported in Amazon GameLift. A fleet instance type determines the computing resources of each instance in the fleet, including CPU, memory, storage, and networking capacity. Amazon GameLift supports the following EC2 instance types. See Amazon EC2 Instance Types for detailed descriptions.
	EC2InstanceType *string `pulumi:"eC2InstanceType"`
	// Indicates whether to use On-Demand instances or Spot instances for this fleet. If empty, the default is ON_DEMAND. Both categories of instances use identical hardware and configurations based on the instance type selected for this fleet.
	FleetType *FleetFleetType `pulumi:"fleetType"`
	// A unique identifier for an AWS IAM role that manages access to your AWS services. With an instance role ARN set, any application that runs on an instance in this fleet can assume the role, including install scripts, server processes, and daemons (background processes). Create a role or look up a role's ARN from the IAM dashboard in the AWS Management Console.
	InstanceRoleARN *string                      `pulumi:"instanceRoleARN"`
	Locations       []FleetLocationConfiguration `pulumi:"locations"`
	// This parameter is no longer used. When hosting a custom game build, specify where Amazon GameLift should store log files using the Amazon GameLift server API call ProcessReady()
	LogPaths []string `pulumi:"logPaths"`
	// [DEPRECATED] The maximum value that is allowed for the fleet's instance count. When creating a new fleet, GameLift automatically sets this value to "1". Once the fleet is active, you can change this value.
	MaxSize *int `pulumi:"maxSize"`
	// The name of an Amazon CloudWatch metric group. A metric group aggregates the metrics for all fleets in the group. Specify a string containing the metric group name. You can use an existing name or use a new name to create a new metric group. Currently, this parameter can have only one string.
	MetricGroups []string `pulumi:"metricGroups"`
	// [DEPRECATED] The minimum value allowed for the fleet's instance count. When creating a new fleet, GameLift automatically sets this value to "0". After the fleet is active, you can change this value.
	MinSize *int `pulumi:"minSize"`
	// A descriptive label that is associated with a fleet. Fleet names do not need to be unique.
	Name *string `pulumi:"name"`
	// A game session protection policy to apply to all game sessions hosted on instances in this fleet. When protected, active game sessions cannot be terminated during a scale-down event. If this parameter is not set, instances in this fleet default to no protection. You can change a fleet's protection policy to affect future game sessions on the fleet. You can also set protection for individual game sessions.
	NewGameSessionProtectionPolicy *FleetNewGameSessionProtectionPolicy `pulumi:"newGameSessionProtectionPolicy"`
	// A unique identifier for the AWS account with the VPC that you want to peer your Amazon GameLift fleet with. You can find your account ID in the AWS Management Console under account settings.
	PeerVpcAwsAccountId *string `pulumi:"peerVpcAwsAccountId"`
	// A unique identifier for a VPC with resources to be accessed by your Amazon GameLift fleet. The VPC must be in the same Region as your fleet. To look up a VPC ID, use the VPC Dashboard in the AWS Management Console.
	PeerVpcId *string `pulumi:"peerVpcId"`
	// A policy that limits the number of game sessions an individual player can create over a span of time for this fleet.
	ResourceCreationLimitPolicy *FleetResourceCreationLimitPolicy `pulumi:"resourceCreationLimitPolicy"`
	// Instructions for launching server processes on each instance in the fleet. Server processes run either a custom game build executable or a Realtime script. The runtime configuration defines the server executables or launch script file, launch parameters, and the number of processes to run concurrently on each instance. When creating a fleet, the runtime configuration must have at least one server process configuration; otherwise the request fails with an invalid request exception.
	//
	// This parameter is required unless the parameters ServerLaunchPath and ServerLaunchParameters are defined. Runtime configuration has replaced these parameters, but fleets that use them will continue to work.
	RuntimeConfiguration *FleetRuntimeConfiguration `pulumi:"runtimeConfiguration"`
	// A unique identifier for a Realtime script to be deployed on a new Realtime Servers fleet. The script must have been successfully uploaded to Amazon GameLift. This fleet setting cannot be changed once the fleet is created.
	//
	// Note: It is not currently possible to use the !Ref command to reference a script created with a CloudFormation template for the fleet property ScriptId. Instead, use Fn::GetAtt Script.Arn or Fn::GetAtt Script.Id to retrieve either of these properties as input for ScriptId. Alternatively, enter a ScriptId string manually.
	ScriptId *string `pulumi:"scriptId"`
	// This parameter is no longer used but is retained for backward compatibility. Instead, specify server launch parameters in the RuntimeConfiguration parameter. A request must specify either a runtime configuration or values for both ServerLaunchParameters and ServerLaunchPath.
	ServerLaunchParameters *string `pulumi:"serverLaunchParameters"`
	// This parameter is no longer used. Instead, specify a server launch path using the RuntimeConfiguration parameter. Requests that specify a server launch path and launch parameters instead of a runtime configuration will continue to work.
	ServerLaunchPath *string `pulumi:"serverLaunchPath"`
}

// The set of arguments for constructing a Fleet resource.
type FleetArgs struct {
	// A unique identifier for a build to be deployed on the new fleet. If you are deploying the fleet with a custom game build, you must specify this property. The build must have been successfully uploaded to Amazon GameLift and be in a READY status. This fleet setting cannot be changed once the fleet is created.
	BuildId pulumi.StringPtrInput
	// Indicates whether to generate a TLS/SSL certificate for the new fleet. TLS certificates are used for encrypting traffic between game clients and game servers running on GameLift. If this parameter is not set, certificate generation is disabled. This fleet setting cannot be changed once the fleet is created.
	CertificateConfiguration FleetCertificateConfigurationPtrInput
	// A human-readable description of a fleet.
	Description pulumi.StringPtrInput
	// [DEPRECATED] The number of EC2 instances that you want this fleet to host. When creating a new fleet, GameLift automatically sets this value to "1" and initiates a single instance. Once the fleet is active, update this value to trigger GameLift to add or remove instances from the fleet.
	DesiredEC2Instances pulumi.IntPtrInput
	// A range of IP addresses and port settings that allow inbound traffic to connect to server processes on an Amazon GameLift server.
	EC2InboundPermissions FleetIpPermissionArrayInput
	// The name of an EC2 instance type that is supported in Amazon GameLift. A fleet instance type determines the computing resources of each instance in the fleet, including CPU, memory, storage, and networking capacity. Amazon GameLift supports the following EC2 instance types. See Amazon EC2 Instance Types for detailed descriptions.
	EC2InstanceType pulumi.StringPtrInput
	// Indicates whether to use On-Demand instances or Spot instances for this fleet. If empty, the default is ON_DEMAND. Both categories of instances use identical hardware and configurations based on the instance type selected for this fleet.
	FleetType FleetFleetTypePtrInput
	// A unique identifier for an AWS IAM role that manages access to your AWS services. With an instance role ARN set, any application that runs on an instance in this fleet can assume the role, including install scripts, server processes, and daemons (background processes). Create a role or look up a role's ARN from the IAM dashboard in the AWS Management Console.
	InstanceRoleARN pulumi.StringPtrInput
	Locations       FleetLocationConfigurationArrayInput
	// This parameter is no longer used. When hosting a custom game build, specify where Amazon GameLift should store log files using the Amazon GameLift server API call ProcessReady()
	LogPaths pulumi.StringArrayInput
	// [DEPRECATED] The maximum value that is allowed for the fleet's instance count. When creating a new fleet, GameLift automatically sets this value to "1". Once the fleet is active, you can change this value.
	MaxSize pulumi.IntPtrInput
	// The name of an Amazon CloudWatch metric group. A metric group aggregates the metrics for all fleets in the group. Specify a string containing the metric group name. You can use an existing name or use a new name to create a new metric group. Currently, this parameter can have only one string.
	MetricGroups pulumi.StringArrayInput
	// [DEPRECATED] The minimum value allowed for the fleet's instance count. When creating a new fleet, GameLift automatically sets this value to "0". After the fleet is active, you can change this value.
	MinSize pulumi.IntPtrInput
	// A descriptive label that is associated with a fleet. Fleet names do not need to be unique.
	Name pulumi.StringPtrInput
	// A game session protection policy to apply to all game sessions hosted on instances in this fleet. When protected, active game sessions cannot be terminated during a scale-down event. If this parameter is not set, instances in this fleet default to no protection. You can change a fleet's protection policy to affect future game sessions on the fleet. You can also set protection for individual game sessions.
	NewGameSessionProtectionPolicy FleetNewGameSessionProtectionPolicyPtrInput
	// A unique identifier for the AWS account with the VPC that you want to peer your Amazon GameLift fleet with. You can find your account ID in the AWS Management Console under account settings.
	PeerVpcAwsAccountId pulumi.StringPtrInput
	// A unique identifier for a VPC with resources to be accessed by your Amazon GameLift fleet. The VPC must be in the same Region as your fleet. To look up a VPC ID, use the VPC Dashboard in the AWS Management Console.
	PeerVpcId pulumi.StringPtrInput
	// A policy that limits the number of game sessions an individual player can create over a span of time for this fleet.
	ResourceCreationLimitPolicy FleetResourceCreationLimitPolicyPtrInput
	// Instructions for launching server processes on each instance in the fleet. Server processes run either a custom game build executable or a Realtime script. The runtime configuration defines the server executables or launch script file, launch parameters, and the number of processes to run concurrently on each instance. When creating a fleet, the runtime configuration must have at least one server process configuration; otherwise the request fails with an invalid request exception.
	//
	// This parameter is required unless the parameters ServerLaunchPath and ServerLaunchParameters are defined. Runtime configuration has replaced these parameters, but fleets that use them will continue to work.
	RuntimeConfiguration FleetRuntimeConfigurationPtrInput
	// A unique identifier for a Realtime script to be deployed on a new Realtime Servers fleet. The script must have been successfully uploaded to Amazon GameLift. This fleet setting cannot be changed once the fleet is created.
	//
	// Note: It is not currently possible to use the !Ref command to reference a script created with a CloudFormation template for the fleet property ScriptId. Instead, use Fn::GetAtt Script.Arn or Fn::GetAtt Script.Id to retrieve either of these properties as input for ScriptId. Alternatively, enter a ScriptId string manually.
	ScriptId pulumi.StringPtrInput
	// This parameter is no longer used but is retained for backward compatibility. Instead, specify server launch parameters in the RuntimeConfiguration parameter. A request must specify either a runtime configuration or values for both ServerLaunchParameters and ServerLaunchPath.
	ServerLaunchParameters pulumi.StringPtrInput
	// This parameter is no longer used. Instead, specify a server launch path using the RuntimeConfiguration parameter. Requests that specify a server launch path and launch parameters instead of a runtime configuration will continue to work.
	ServerLaunchPath pulumi.StringPtrInput
}

func (FleetArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*fleetArgs)(nil)).Elem()
}

type FleetInput interface {
	pulumi.Input

	ToFleetOutput() FleetOutput
	ToFleetOutputWithContext(ctx context.Context) FleetOutput
}

func (*Fleet) ElementType() reflect.Type {
	return reflect.TypeOf((*Fleet)(nil))
}

func (i *Fleet) ToFleetOutput() FleetOutput {
	return i.ToFleetOutputWithContext(context.Background())
}

func (i *Fleet) ToFleetOutputWithContext(ctx context.Context) FleetOutput {
	return pulumi.ToOutputWithContext(ctx, i).(FleetOutput)
}

type FleetOutput struct{ *pulumi.OutputState }

func (FleetOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*Fleet)(nil))
}

func (o FleetOutput) ToFleetOutput() FleetOutput {
	return o
}

func (o FleetOutput) ToFleetOutputWithContext(ctx context.Context) FleetOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(FleetOutput{})
}

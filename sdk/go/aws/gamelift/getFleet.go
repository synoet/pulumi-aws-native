// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package gamelift

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The AWS::GameLift::Fleet resource creates an Amazon GameLift (GameLift) fleet to host game servers. A fleet is a set of EC2 or Anywhere instances, each of which can host multiple game sessions.
func LookupFleet(ctx *pulumi.Context, args *LookupFleetArgs, opts ...pulumi.InvokeOption) (*LookupFleetResult, error) {
	var rv LookupFleetResult
	err := ctx.Invoke("aws-native:gamelift:getFleet", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupFleetArgs struct {
	// Unique fleet ID
	FleetId string `pulumi:"fleetId"`
}

type LookupFleetResult struct {
	// Configuration for Anywhere fleet.
	AnywhereConfiguration *FleetAnywhereConfiguration `pulumi:"anywhereConfiguration"`
	// A human-readable description of a fleet.
	Description *string `pulumi:"description"`
	// [DEPRECATED] The number of EC2 instances that you want this fleet to host. When creating a new fleet, GameLift automatically sets this value to "1" and initiates a single instance. Once the fleet is active, update this value to trigger GameLift to add or remove instances from the fleet.
	DesiredEC2Instances *int `pulumi:"desiredEC2Instances"`
	// A range of IP addresses and port settings that allow inbound traffic to connect to server processes on an Amazon GameLift server.
	EC2InboundPermissions []FleetIpPermission `pulumi:"eC2InboundPermissions"`
	// Unique fleet ID
	FleetId   *string                      `pulumi:"fleetId"`
	Locations []FleetLocationConfiguration `pulumi:"locations"`
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
	// A policy that limits the number of game sessions an individual player can create over a span of time for this fleet.
	ResourceCreationLimitPolicy *FleetResourceCreationLimitPolicy `pulumi:"resourceCreationLimitPolicy"`
	// Instructions for launching server processes on each instance in the fleet. Server processes run either a custom game build executable or a Realtime script. The runtime configuration defines the server executables or launch script file, launch parameters, and the number of processes to run concurrently on each instance. When creating a fleet, the runtime configuration must have at least one server process configuration; otherwise the request fails with an invalid request exception.
	//
	// This parameter is required unless the parameters ServerLaunchPath and ServerLaunchParameters are defined. Runtime configuration has replaced these parameters, but fleets that use them will continue to work.
	RuntimeConfiguration *FleetRuntimeConfiguration `pulumi:"runtimeConfiguration"`
}

func LookupFleetOutput(ctx *pulumi.Context, args LookupFleetOutputArgs, opts ...pulumi.InvokeOption) LookupFleetResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupFleetResult, error) {
			args := v.(LookupFleetArgs)
			r, err := LookupFleet(ctx, &args, opts...)
			var s LookupFleetResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupFleetResultOutput)
}

type LookupFleetOutputArgs struct {
	// Unique fleet ID
	FleetId pulumi.StringInput `pulumi:"fleetId"`
}

func (LookupFleetOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupFleetArgs)(nil)).Elem()
}

type LookupFleetResultOutput struct{ *pulumi.OutputState }

func (LookupFleetResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupFleetResult)(nil)).Elem()
}

func (o LookupFleetResultOutput) ToLookupFleetResultOutput() LookupFleetResultOutput {
	return o
}

func (o LookupFleetResultOutput) ToLookupFleetResultOutputWithContext(ctx context.Context) LookupFleetResultOutput {
	return o
}

// Configuration for Anywhere fleet.
func (o LookupFleetResultOutput) AnywhereConfiguration() FleetAnywhereConfigurationPtrOutput {
	return o.ApplyT(func(v LookupFleetResult) *FleetAnywhereConfiguration { return v.AnywhereConfiguration }).(FleetAnywhereConfigurationPtrOutput)
}

// A human-readable description of a fleet.
func (o LookupFleetResultOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupFleetResult) *string { return v.Description }).(pulumi.StringPtrOutput)
}

// [DEPRECATED] The number of EC2 instances that you want this fleet to host. When creating a new fleet, GameLift automatically sets this value to "1" and initiates a single instance. Once the fleet is active, update this value to trigger GameLift to add or remove instances from the fleet.
func (o LookupFleetResultOutput) DesiredEC2Instances() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupFleetResult) *int { return v.DesiredEC2Instances }).(pulumi.IntPtrOutput)
}

// A range of IP addresses and port settings that allow inbound traffic to connect to server processes on an Amazon GameLift server.
func (o LookupFleetResultOutput) EC2InboundPermissions() FleetIpPermissionArrayOutput {
	return o.ApplyT(func(v LookupFleetResult) []FleetIpPermission { return v.EC2InboundPermissions }).(FleetIpPermissionArrayOutput)
}

// Unique fleet ID
func (o LookupFleetResultOutput) FleetId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupFleetResult) *string { return v.FleetId }).(pulumi.StringPtrOutput)
}

func (o LookupFleetResultOutput) Locations() FleetLocationConfigurationArrayOutput {
	return o.ApplyT(func(v LookupFleetResult) []FleetLocationConfiguration { return v.Locations }).(FleetLocationConfigurationArrayOutput)
}

// [DEPRECATED] The maximum value that is allowed for the fleet's instance count. When creating a new fleet, GameLift automatically sets this value to "1". Once the fleet is active, you can change this value.
func (o LookupFleetResultOutput) MaxSize() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupFleetResult) *int { return v.MaxSize }).(pulumi.IntPtrOutput)
}

// The name of an Amazon CloudWatch metric group. A metric group aggregates the metrics for all fleets in the group. Specify a string containing the metric group name. You can use an existing name or use a new name to create a new metric group. Currently, this parameter can have only one string.
func (o LookupFleetResultOutput) MetricGroups() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupFleetResult) []string { return v.MetricGroups }).(pulumi.StringArrayOutput)
}

// [DEPRECATED] The minimum value allowed for the fleet's instance count. When creating a new fleet, GameLift automatically sets this value to "0". After the fleet is active, you can change this value.
func (o LookupFleetResultOutput) MinSize() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupFleetResult) *int { return v.MinSize }).(pulumi.IntPtrOutput)
}

// A descriptive label that is associated with a fleet. Fleet names do not need to be unique.
func (o LookupFleetResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupFleetResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

// A game session protection policy to apply to all game sessions hosted on instances in this fleet. When protected, active game sessions cannot be terminated during a scale-down event. If this parameter is not set, instances in this fleet default to no protection. You can change a fleet's protection policy to affect future game sessions on the fleet. You can also set protection for individual game sessions.
func (o LookupFleetResultOutput) NewGameSessionProtectionPolicy() FleetNewGameSessionProtectionPolicyPtrOutput {
	return o.ApplyT(func(v LookupFleetResult) *FleetNewGameSessionProtectionPolicy {
		return v.NewGameSessionProtectionPolicy
	}).(FleetNewGameSessionProtectionPolicyPtrOutput)
}

// A policy that limits the number of game sessions an individual player can create over a span of time for this fleet.
func (o LookupFleetResultOutput) ResourceCreationLimitPolicy() FleetResourceCreationLimitPolicyPtrOutput {
	return o.ApplyT(func(v LookupFleetResult) *FleetResourceCreationLimitPolicy { return v.ResourceCreationLimitPolicy }).(FleetResourceCreationLimitPolicyPtrOutput)
}

// Instructions for launching server processes on each instance in the fleet. Server processes run either a custom game build executable or a Realtime script. The runtime configuration defines the server executables or launch script file, launch parameters, and the number of processes to run concurrently on each instance. When creating a fleet, the runtime configuration must have at least one server process configuration; otherwise the request fails with an invalid request exception.
//
// This parameter is required unless the parameters ServerLaunchPath and ServerLaunchParameters are defined. Runtime configuration has replaced these parameters, but fleets that use them will continue to work.
func (o LookupFleetResultOutput) RuntimeConfiguration() FleetRuntimeConfigurationPtrOutput {
	return o.ApplyT(func(v LookupFleetResult) *FleetRuntimeConfiguration { return v.RuntimeConfiguration }).(FleetRuntimeConfigurationPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupFleetResultOutput{})
}

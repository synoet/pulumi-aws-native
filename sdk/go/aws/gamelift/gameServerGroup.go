// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package gamelift

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The AWS::GameLift::GameServerGroup resource creates an Amazon GameLift (GameLift) GameServerGroup.
type GameServerGroup struct {
	pulumi.CustomResourceState

	// A generated unique ID for the EC2 Auto Scaling group that is associated with this game server group.
	AutoScalingGroupArn pulumi.StringOutput `pulumi:"autoScalingGroupArn"`
	// Configuration settings to define a scaling policy for the Auto Scaling group that is optimized for game hosting
	AutoScalingPolicy GameServerGroupAutoScalingPolicyPtrOutput `pulumi:"autoScalingPolicy"`
	// The fallback balancing method to use for the game server group when Spot Instances in a Region become unavailable or are not viable for game hosting.
	BalancingStrategy GameServerGroupBalancingStrategyPtrOutput `pulumi:"balancingStrategy"`
	// The type of delete to perform.
	DeleteOption GameServerGroupDeleteOptionPtrOutput `pulumi:"deleteOption"`
	// A generated unique ID for the game server group.
	GameServerGroupArn pulumi.StringOutput `pulumi:"gameServerGroupArn"`
	// An identifier for the new game server group.
	GameServerGroupName pulumi.StringOutput `pulumi:"gameServerGroupName"`
	// A flag that indicates whether instances in the game server group are protected from early termination.
	GameServerProtectionPolicy GameServerGroupGameServerProtectionPolicyPtrOutput `pulumi:"gameServerProtectionPolicy"`
	// A set of EC2 instance types to use when creating instances in the group.
	InstanceDefinitions GameServerGroupInstanceDefinitionArrayOutput `pulumi:"instanceDefinitions"`
	// The EC2 launch template that contains configuration settings and game server code to be deployed to all instances in the game server group.
	LaunchTemplate GameServerGroupLaunchTemplatePtrOutput `pulumi:"launchTemplate"`
	// The maximum number of instances allowed in the EC2 Auto Scaling group.
	MaxSize pulumi.Float64PtrOutput `pulumi:"maxSize"`
	// The minimum number of instances allowed in the EC2 Auto Scaling group.
	MinSize pulumi.Float64PtrOutput `pulumi:"minSize"`
	// The Amazon Resource Name (ARN) for an IAM role that allows Amazon GameLift to access your EC2 Auto Scaling groups.
	RoleArn pulumi.StringOutput `pulumi:"roleArn"`
	// A list of labels to assign to the new game server group resource.
	Tags GameServerGroupTagArrayOutput `pulumi:"tags"`
	// A list of virtual private cloud (VPC) subnets to use with instances in the game server group.
	VpcSubnets pulumi.StringArrayOutput `pulumi:"vpcSubnets"`
}

// NewGameServerGroup registers a new resource with the given unique name, arguments, and options.
func NewGameServerGroup(ctx *pulumi.Context,
	name string, args *GameServerGroupArgs, opts ...pulumi.ResourceOption) (*GameServerGroup, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.InstanceDefinitions == nil {
		return nil, errors.New("invalid value for required argument 'InstanceDefinitions'")
	}
	if args.RoleArn == nil {
		return nil, errors.New("invalid value for required argument 'RoleArn'")
	}
	var resource GameServerGroup
	err := ctx.RegisterResource("aws-native:gamelift:GameServerGroup", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetGameServerGroup gets an existing GameServerGroup resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetGameServerGroup(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *GameServerGroupState, opts ...pulumi.ResourceOption) (*GameServerGroup, error) {
	var resource GameServerGroup
	err := ctx.ReadResource("aws-native:gamelift:GameServerGroup", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering GameServerGroup resources.
type gameServerGroupState struct {
}

type GameServerGroupState struct {
}

func (GameServerGroupState) ElementType() reflect.Type {
	return reflect.TypeOf((*gameServerGroupState)(nil)).Elem()
}

type gameServerGroupArgs struct {
	// Configuration settings to define a scaling policy for the Auto Scaling group that is optimized for game hosting
	AutoScalingPolicy *GameServerGroupAutoScalingPolicy `pulumi:"autoScalingPolicy"`
	// The fallback balancing method to use for the game server group when Spot Instances in a Region become unavailable or are not viable for game hosting.
	BalancingStrategy *GameServerGroupBalancingStrategy `pulumi:"balancingStrategy"`
	// The type of delete to perform.
	DeleteOption *GameServerGroupDeleteOption `pulumi:"deleteOption"`
	// An identifier for the new game server group.
	GameServerGroupName *string `pulumi:"gameServerGroupName"`
	// A flag that indicates whether instances in the game server group are protected from early termination.
	GameServerProtectionPolicy *GameServerGroupGameServerProtectionPolicy `pulumi:"gameServerProtectionPolicy"`
	// A set of EC2 instance types to use when creating instances in the group.
	InstanceDefinitions []GameServerGroupInstanceDefinition `pulumi:"instanceDefinitions"`
	// The EC2 launch template that contains configuration settings and game server code to be deployed to all instances in the game server group.
	LaunchTemplate *GameServerGroupLaunchTemplate `pulumi:"launchTemplate"`
	// The maximum number of instances allowed in the EC2 Auto Scaling group.
	MaxSize *float64 `pulumi:"maxSize"`
	// The minimum number of instances allowed in the EC2 Auto Scaling group.
	MinSize *float64 `pulumi:"minSize"`
	// The Amazon Resource Name (ARN) for an IAM role that allows Amazon GameLift to access your EC2 Auto Scaling groups.
	RoleArn string `pulumi:"roleArn"`
	// A list of labels to assign to the new game server group resource.
	Tags []GameServerGroupTag `pulumi:"tags"`
	// A list of virtual private cloud (VPC) subnets to use with instances in the game server group.
	VpcSubnets []string `pulumi:"vpcSubnets"`
}

// The set of arguments for constructing a GameServerGroup resource.
type GameServerGroupArgs struct {
	// Configuration settings to define a scaling policy for the Auto Scaling group that is optimized for game hosting
	AutoScalingPolicy GameServerGroupAutoScalingPolicyPtrInput
	// The fallback balancing method to use for the game server group when Spot Instances in a Region become unavailable or are not viable for game hosting.
	BalancingStrategy GameServerGroupBalancingStrategyPtrInput
	// The type of delete to perform.
	DeleteOption GameServerGroupDeleteOptionPtrInput
	// An identifier for the new game server group.
	GameServerGroupName pulumi.StringPtrInput
	// A flag that indicates whether instances in the game server group are protected from early termination.
	GameServerProtectionPolicy GameServerGroupGameServerProtectionPolicyPtrInput
	// A set of EC2 instance types to use when creating instances in the group.
	InstanceDefinitions GameServerGroupInstanceDefinitionArrayInput
	// The EC2 launch template that contains configuration settings and game server code to be deployed to all instances in the game server group.
	LaunchTemplate GameServerGroupLaunchTemplatePtrInput
	// The maximum number of instances allowed in the EC2 Auto Scaling group.
	MaxSize pulumi.Float64PtrInput
	// The minimum number of instances allowed in the EC2 Auto Scaling group.
	MinSize pulumi.Float64PtrInput
	// The Amazon Resource Name (ARN) for an IAM role that allows Amazon GameLift to access your EC2 Auto Scaling groups.
	RoleArn pulumi.StringInput
	// A list of labels to assign to the new game server group resource.
	Tags GameServerGroupTagArrayInput
	// A list of virtual private cloud (VPC) subnets to use with instances in the game server group.
	VpcSubnets pulumi.StringArrayInput
}

func (GameServerGroupArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*gameServerGroupArgs)(nil)).Elem()
}

type GameServerGroupInput interface {
	pulumi.Input

	ToGameServerGroupOutput() GameServerGroupOutput
	ToGameServerGroupOutputWithContext(ctx context.Context) GameServerGroupOutput
}

func (*GameServerGroup) ElementType() reflect.Type {
	return reflect.TypeOf((**GameServerGroup)(nil)).Elem()
}

func (i *GameServerGroup) ToGameServerGroupOutput() GameServerGroupOutput {
	return i.ToGameServerGroupOutputWithContext(context.Background())
}

func (i *GameServerGroup) ToGameServerGroupOutputWithContext(ctx context.Context) GameServerGroupOutput {
	return pulumi.ToOutputWithContext(ctx, i).(GameServerGroupOutput)
}

type GameServerGroupOutput struct{ *pulumi.OutputState }

func (GameServerGroupOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**GameServerGroup)(nil)).Elem()
}

func (o GameServerGroupOutput) ToGameServerGroupOutput() GameServerGroupOutput {
	return o
}

func (o GameServerGroupOutput) ToGameServerGroupOutputWithContext(ctx context.Context) GameServerGroupOutput {
	return o
}

// A generated unique ID for the EC2 Auto Scaling group that is associated with this game server group.
func (o GameServerGroupOutput) AutoScalingGroupArn() pulumi.StringOutput {
	return o.ApplyT(func(v *GameServerGroup) pulumi.StringOutput { return v.AutoScalingGroupArn }).(pulumi.StringOutput)
}

// Configuration settings to define a scaling policy for the Auto Scaling group that is optimized for game hosting
func (o GameServerGroupOutput) AutoScalingPolicy() GameServerGroupAutoScalingPolicyPtrOutput {
	return o.ApplyT(func(v *GameServerGroup) GameServerGroupAutoScalingPolicyPtrOutput { return v.AutoScalingPolicy }).(GameServerGroupAutoScalingPolicyPtrOutput)
}

// The fallback balancing method to use for the game server group when Spot Instances in a Region become unavailable or are not viable for game hosting.
func (o GameServerGroupOutput) BalancingStrategy() GameServerGroupBalancingStrategyPtrOutput {
	return o.ApplyT(func(v *GameServerGroup) GameServerGroupBalancingStrategyPtrOutput { return v.BalancingStrategy }).(GameServerGroupBalancingStrategyPtrOutput)
}

// The type of delete to perform.
func (o GameServerGroupOutput) DeleteOption() GameServerGroupDeleteOptionPtrOutput {
	return o.ApplyT(func(v *GameServerGroup) GameServerGroupDeleteOptionPtrOutput { return v.DeleteOption }).(GameServerGroupDeleteOptionPtrOutput)
}

// A generated unique ID for the game server group.
func (o GameServerGroupOutput) GameServerGroupArn() pulumi.StringOutput {
	return o.ApplyT(func(v *GameServerGroup) pulumi.StringOutput { return v.GameServerGroupArn }).(pulumi.StringOutput)
}

// An identifier for the new game server group.
func (o GameServerGroupOutput) GameServerGroupName() pulumi.StringOutput {
	return o.ApplyT(func(v *GameServerGroup) pulumi.StringOutput { return v.GameServerGroupName }).(pulumi.StringOutput)
}

// A flag that indicates whether instances in the game server group are protected from early termination.
func (o GameServerGroupOutput) GameServerProtectionPolicy() GameServerGroupGameServerProtectionPolicyPtrOutput {
	return o.ApplyT(func(v *GameServerGroup) GameServerGroupGameServerProtectionPolicyPtrOutput {
		return v.GameServerProtectionPolicy
	}).(GameServerGroupGameServerProtectionPolicyPtrOutput)
}

// A set of EC2 instance types to use when creating instances in the group.
func (o GameServerGroupOutput) InstanceDefinitions() GameServerGroupInstanceDefinitionArrayOutput {
	return o.ApplyT(func(v *GameServerGroup) GameServerGroupInstanceDefinitionArrayOutput { return v.InstanceDefinitions }).(GameServerGroupInstanceDefinitionArrayOutput)
}

// The EC2 launch template that contains configuration settings and game server code to be deployed to all instances in the game server group.
func (o GameServerGroupOutput) LaunchTemplate() GameServerGroupLaunchTemplatePtrOutput {
	return o.ApplyT(func(v *GameServerGroup) GameServerGroupLaunchTemplatePtrOutput { return v.LaunchTemplate }).(GameServerGroupLaunchTemplatePtrOutput)
}

// The maximum number of instances allowed in the EC2 Auto Scaling group.
func (o GameServerGroupOutput) MaxSize() pulumi.Float64PtrOutput {
	return o.ApplyT(func(v *GameServerGroup) pulumi.Float64PtrOutput { return v.MaxSize }).(pulumi.Float64PtrOutput)
}

// The minimum number of instances allowed in the EC2 Auto Scaling group.
func (o GameServerGroupOutput) MinSize() pulumi.Float64PtrOutput {
	return o.ApplyT(func(v *GameServerGroup) pulumi.Float64PtrOutput { return v.MinSize }).(pulumi.Float64PtrOutput)
}

// The Amazon Resource Name (ARN) for an IAM role that allows Amazon GameLift to access your EC2 Auto Scaling groups.
func (o GameServerGroupOutput) RoleArn() pulumi.StringOutput {
	return o.ApplyT(func(v *GameServerGroup) pulumi.StringOutput { return v.RoleArn }).(pulumi.StringOutput)
}

// A list of labels to assign to the new game server group resource.
func (o GameServerGroupOutput) Tags() GameServerGroupTagArrayOutput {
	return o.ApplyT(func(v *GameServerGroup) GameServerGroupTagArrayOutput { return v.Tags }).(GameServerGroupTagArrayOutput)
}

// A list of virtual private cloud (VPC) subnets to use with instances in the game server group.
func (o GameServerGroupOutput) VpcSubnets() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *GameServerGroup) pulumi.StringArrayOutput { return v.VpcSubnets }).(pulumi.StringArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*GameServerGroupInput)(nil)).Elem(), &GameServerGroup{})
	pulumi.RegisterOutputType(GameServerGroupOutput{})
}

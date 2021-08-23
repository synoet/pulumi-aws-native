// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package networkfirewall

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html
type Firewall struct {
	pulumi.CustomResourceState

	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-deleteprotection
	DeleteProtection pulumi.BoolPtrOutput `pulumi:"deleteProtection"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-description
	Description pulumi.StringPtrOutput   `pulumi:"description"`
	EndpointIds pulumi.StringArrayOutput `pulumi:"endpointIds"`
	FirewallArn pulumi.StringOutput      `pulumi:"firewallArn"`
	FirewallId  pulumi.StringOutput      `pulumi:"firewallId"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-firewallname
	FirewallName pulumi.StringOutput `pulumi:"firewallName"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-firewallpolicyarn
	FirewallPolicyArn pulumi.StringOutput `pulumi:"firewallPolicyArn"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-firewallpolicychangeprotection
	FirewallPolicyChangeProtection pulumi.BoolPtrOutput `pulumi:"firewallPolicyChangeProtection"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-subnetchangeprotection
	SubnetChangeProtection pulumi.BoolPtrOutput `pulumi:"subnetChangeProtection"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-subnetmappings
	SubnetMappings FirewallSubnetMappingArrayOutput `pulumi:"subnetMappings"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-tags
	Tags aws.TagArrayOutput `pulumi:"tags"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-vpcid
	VpcId pulumi.StringOutput `pulumi:"vpcId"`
}

// NewFirewall registers a new resource with the given unique name, arguments, and options.
func NewFirewall(ctx *pulumi.Context,
	name string, args *FirewallArgs, opts ...pulumi.ResourceOption) (*Firewall, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.FirewallName == nil {
		return nil, errors.New("invalid value for required argument 'FirewallName'")
	}
	if args.FirewallPolicyArn == nil {
		return nil, errors.New("invalid value for required argument 'FirewallPolicyArn'")
	}
	if args.SubnetMappings == nil {
		return nil, errors.New("invalid value for required argument 'SubnetMappings'")
	}
	if args.VpcId == nil {
		return nil, errors.New("invalid value for required argument 'VpcId'")
	}
	var resource Firewall
	err := ctx.RegisterResource("aws-native:networkfirewall:Firewall", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetFirewall gets an existing Firewall resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetFirewall(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *FirewallState, opts ...pulumi.ResourceOption) (*Firewall, error) {
	var resource Firewall
	err := ctx.ReadResource("aws-native:networkfirewall:Firewall", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Firewall resources.
type firewallState struct {
}

type FirewallState struct {
}

func (FirewallState) ElementType() reflect.Type {
	return reflect.TypeOf((*firewallState)(nil)).Elem()
}

type firewallArgs struct {
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-deleteprotection
	DeleteProtection *bool `pulumi:"deleteProtection"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-description
	Description *string `pulumi:"description"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-firewallname
	FirewallName string `pulumi:"firewallName"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-firewallpolicyarn
	FirewallPolicyArn string `pulumi:"firewallPolicyArn"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-firewallpolicychangeprotection
	FirewallPolicyChangeProtection *bool `pulumi:"firewallPolicyChangeProtection"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-subnetchangeprotection
	SubnetChangeProtection *bool `pulumi:"subnetChangeProtection"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-subnetmappings
	SubnetMappings []FirewallSubnetMapping `pulumi:"subnetMappings"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-tags
	Tags []aws.Tag `pulumi:"tags"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-vpcid
	VpcId string `pulumi:"vpcId"`
}

// The set of arguments for constructing a Firewall resource.
type FirewallArgs struct {
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-deleteprotection
	DeleteProtection pulumi.BoolPtrInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-description
	Description pulumi.StringPtrInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-firewallname
	FirewallName pulumi.StringInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-firewallpolicyarn
	FirewallPolicyArn pulumi.StringInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-firewallpolicychangeprotection
	FirewallPolicyChangeProtection pulumi.BoolPtrInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-subnetchangeprotection
	SubnetChangeProtection pulumi.BoolPtrInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-subnetmappings
	SubnetMappings FirewallSubnetMappingArrayInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-tags
	Tags aws.TagArrayInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-vpcid
	VpcId pulumi.StringInput
}

func (FirewallArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*firewallArgs)(nil)).Elem()
}

type FirewallInput interface {
	pulumi.Input

	ToFirewallOutput() FirewallOutput
	ToFirewallOutputWithContext(ctx context.Context) FirewallOutput
}

func (*Firewall) ElementType() reflect.Type {
	return reflect.TypeOf((*Firewall)(nil))
}

func (i *Firewall) ToFirewallOutput() FirewallOutput {
	return i.ToFirewallOutputWithContext(context.Background())
}

func (i *Firewall) ToFirewallOutputWithContext(ctx context.Context) FirewallOutput {
	return pulumi.ToOutputWithContext(ctx, i).(FirewallOutput)
}

type FirewallOutput struct{ *pulumi.OutputState }

func (FirewallOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*Firewall)(nil))
}

func (o FirewallOutput) ToFirewallOutput() FirewallOutput {
	return o
}

func (o FirewallOutput) ToFirewallOutputWithContext(ctx context.Context) FirewallOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(FirewallOutput{})
}

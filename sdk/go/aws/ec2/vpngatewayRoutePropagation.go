// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package ec2

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::EC2::VPNGatewayRoutePropagation
//
// Deprecated: VPNGatewayRoutePropagation is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.
type VPNGatewayRoutePropagation struct {
	pulumi.CustomResourceState

	RouteTableIds pulumi.StringArrayOutput `pulumi:"routeTableIds"`
	VpnGatewayId  pulumi.StringOutput      `pulumi:"vpnGatewayId"`
}

// NewVPNGatewayRoutePropagation registers a new resource with the given unique name, arguments, and options.
func NewVPNGatewayRoutePropagation(ctx *pulumi.Context,
	name string, args *VPNGatewayRoutePropagationArgs, opts ...pulumi.ResourceOption) (*VPNGatewayRoutePropagation, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.RouteTableIds == nil {
		return nil, errors.New("invalid value for required argument 'RouteTableIds'")
	}
	if args.VpnGatewayId == nil {
		return nil, errors.New("invalid value for required argument 'VpnGatewayId'")
	}
	var resource VPNGatewayRoutePropagation
	err := ctx.RegisterResource("aws-native:ec2:VPNGatewayRoutePropagation", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetVPNGatewayRoutePropagation gets an existing VPNGatewayRoutePropagation resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetVPNGatewayRoutePropagation(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *VPNGatewayRoutePropagationState, opts ...pulumi.ResourceOption) (*VPNGatewayRoutePropagation, error) {
	var resource VPNGatewayRoutePropagation
	err := ctx.ReadResource("aws-native:ec2:VPNGatewayRoutePropagation", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering VPNGatewayRoutePropagation resources.
type vpngatewayRoutePropagationState struct {
}

type VPNGatewayRoutePropagationState struct {
}

func (VPNGatewayRoutePropagationState) ElementType() reflect.Type {
	return reflect.TypeOf((*vpngatewayRoutePropagationState)(nil)).Elem()
}

type vpngatewayRoutePropagationArgs struct {
	RouteTableIds []string `pulumi:"routeTableIds"`
	VpnGatewayId  string   `pulumi:"vpnGatewayId"`
}

// The set of arguments for constructing a VPNGatewayRoutePropagation resource.
type VPNGatewayRoutePropagationArgs struct {
	RouteTableIds pulumi.StringArrayInput
	VpnGatewayId  pulumi.StringInput
}

func (VPNGatewayRoutePropagationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*vpngatewayRoutePropagationArgs)(nil)).Elem()
}

type VPNGatewayRoutePropagationInput interface {
	pulumi.Input

	ToVPNGatewayRoutePropagationOutput() VPNGatewayRoutePropagationOutput
	ToVPNGatewayRoutePropagationOutputWithContext(ctx context.Context) VPNGatewayRoutePropagationOutput
}

func (*VPNGatewayRoutePropagation) ElementType() reflect.Type {
	return reflect.TypeOf((*VPNGatewayRoutePropagation)(nil))
}

func (i *VPNGatewayRoutePropagation) ToVPNGatewayRoutePropagationOutput() VPNGatewayRoutePropagationOutput {
	return i.ToVPNGatewayRoutePropagationOutputWithContext(context.Background())
}

func (i *VPNGatewayRoutePropagation) ToVPNGatewayRoutePropagationOutputWithContext(ctx context.Context) VPNGatewayRoutePropagationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(VPNGatewayRoutePropagationOutput)
}

type VPNGatewayRoutePropagationOutput struct{ *pulumi.OutputState }

func (VPNGatewayRoutePropagationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*VPNGatewayRoutePropagation)(nil))
}

func (o VPNGatewayRoutePropagationOutput) ToVPNGatewayRoutePropagationOutput() VPNGatewayRoutePropagationOutput {
	return o
}

func (o VPNGatewayRoutePropagationOutput) ToVPNGatewayRoutePropagationOutputWithContext(ctx context.Context) VPNGatewayRoutePropagationOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(VPNGatewayRoutePropagationOutput{})
}

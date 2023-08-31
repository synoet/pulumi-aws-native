// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ec2

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::EC2::EgressOnlyInternetGateway
type EgressOnlyInternetGateway struct {
	pulumi.CustomResourceState

	// The ID of the VPC for which to create the egress-only internet gateway.
	VpcId pulumi.StringOutput `pulumi:"vpcId"`
}

// NewEgressOnlyInternetGateway registers a new resource with the given unique name, arguments, and options.
func NewEgressOnlyInternetGateway(ctx *pulumi.Context,
	name string, args *EgressOnlyInternetGatewayArgs, opts ...pulumi.ResourceOption) (*EgressOnlyInternetGateway, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.VpcId == nil {
		return nil, errors.New("invalid value for required argument 'VpcId'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"vpcId",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource EgressOnlyInternetGateway
	err := ctx.RegisterResource("aws-native:ec2:EgressOnlyInternetGateway", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetEgressOnlyInternetGateway gets an existing EgressOnlyInternetGateway resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetEgressOnlyInternetGateway(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *EgressOnlyInternetGatewayState, opts ...pulumi.ResourceOption) (*EgressOnlyInternetGateway, error) {
	var resource EgressOnlyInternetGateway
	err := ctx.ReadResource("aws-native:ec2:EgressOnlyInternetGateway", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering EgressOnlyInternetGateway resources.
type egressOnlyInternetGatewayState struct {
}

type EgressOnlyInternetGatewayState struct {
}

func (EgressOnlyInternetGatewayState) ElementType() reflect.Type {
	return reflect.TypeOf((*egressOnlyInternetGatewayState)(nil)).Elem()
}

type egressOnlyInternetGatewayArgs struct {
	// The ID of the VPC for which to create the egress-only internet gateway.
	VpcId string `pulumi:"vpcId"`
}

// The set of arguments for constructing a EgressOnlyInternetGateway resource.
type EgressOnlyInternetGatewayArgs struct {
	// The ID of the VPC for which to create the egress-only internet gateway.
	VpcId pulumi.StringInput
}

func (EgressOnlyInternetGatewayArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*egressOnlyInternetGatewayArgs)(nil)).Elem()
}

type EgressOnlyInternetGatewayInput interface {
	pulumi.Input

	ToEgressOnlyInternetGatewayOutput() EgressOnlyInternetGatewayOutput
	ToEgressOnlyInternetGatewayOutputWithContext(ctx context.Context) EgressOnlyInternetGatewayOutput
}

func (*EgressOnlyInternetGateway) ElementType() reflect.Type {
	return reflect.TypeOf((**EgressOnlyInternetGateway)(nil)).Elem()
}

func (i *EgressOnlyInternetGateway) ToEgressOnlyInternetGatewayOutput() EgressOnlyInternetGatewayOutput {
	return i.ToEgressOnlyInternetGatewayOutputWithContext(context.Background())
}

func (i *EgressOnlyInternetGateway) ToEgressOnlyInternetGatewayOutputWithContext(ctx context.Context) EgressOnlyInternetGatewayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(EgressOnlyInternetGatewayOutput)
}

type EgressOnlyInternetGatewayOutput struct{ *pulumi.OutputState }

func (EgressOnlyInternetGatewayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**EgressOnlyInternetGateway)(nil)).Elem()
}

func (o EgressOnlyInternetGatewayOutput) ToEgressOnlyInternetGatewayOutput() EgressOnlyInternetGatewayOutput {
	return o
}

func (o EgressOnlyInternetGatewayOutput) ToEgressOnlyInternetGatewayOutputWithContext(ctx context.Context) EgressOnlyInternetGatewayOutput {
	return o
}

// The ID of the VPC for which to create the egress-only internet gateway.
func (o EgressOnlyInternetGatewayOutput) VpcId() pulumi.StringOutput {
	return o.ApplyT(func(v *EgressOnlyInternetGateway) pulumi.StringOutput { return v.VpcId }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*EgressOnlyInternetGatewayInput)(nil)).Elem(), &EgressOnlyInternetGateway{})
	pulumi.RegisterOutputType(EgressOnlyInternetGatewayOutput{})
}

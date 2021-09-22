// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package ec2

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::EC2::EIP
//
// Deprecated: EIP is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.
type EIP struct {
	pulumi.CustomResourceState

	AllocationId   pulumi.StringOutput    `pulumi:"allocationId"`
	Domain         pulumi.StringPtrOutput `pulumi:"domain"`
	InstanceId     pulumi.StringPtrOutput `pulumi:"instanceId"`
	PublicIpv4Pool pulumi.StringPtrOutput `pulumi:"publicIpv4Pool"`
	Tags           EIPTagArrayOutput      `pulumi:"tags"`
}

// NewEIP registers a new resource with the given unique name, arguments, and options.
func NewEIP(ctx *pulumi.Context,
	name string, args *EIPArgs, opts ...pulumi.ResourceOption) (*EIP, error) {
	if args == nil {
		args = &EIPArgs{}
	}

	var resource EIP
	err := ctx.RegisterResource("aws-native:ec2:EIP", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetEIP gets an existing EIP resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetEIP(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *EIPState, opts ...pulumi.ResourceOption) (*EIP, error) {
	var resource EIP
	err := ctx.ReadResource("aws-native:ec2:EIP", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering EIP resources.
type eipState struct {
}

type EIPState struct {
}

func (EIPState) ElementType() reflect.Type {
	return reflect.TypeOf((*eipState)(nil)).Elem()
}

type eipArgs struct {
	Domain         *string  `pulumi:"domain"`
	InstanceId     *string  `pulumi:"instanceId"`
	PublicIpv4Pool *string  `pulumi:"publicIpv4Pool"`
	Tags           []EIPTag `pulumi:"tags"`
}

// The set of arguments for constructing a EIP resource.
type EIPArgs struct {
	Domain         pulumi.StringPtrInput
	InstanceId     pulumi.StringPtrInput
	PublicIpv4Pool pulumi.StringPtrInput
	Tags           EIPTagArrayInput
}

func (EIPArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*eipArgs)(nil)).Elem()
}

type EIPInput interface {
	pulumi.Input

	ToEIPOutput() EIPOutput
	ToEIPOutputWithContext(ctx context.Context) EIPOutput
}

func (*EIP) ElementType() reflect.Type {
	return reflect.TypeOf((*EIP)(nil))
}

func (i *EIP) ToEIPOutput() EIPOutput {
	return i.ToEIPOutputWithContext(context.Background())
}

func (i *EIP) ToEIPOutputWithContext(ctx context.Context) EIPOutput {
	return pulumi.ToOutputWithContext(ctx, i).(EIPOutput)
}

type EIPOutput struct{ *pulumi.OutputState }

func (EIPOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*EIP)(nil))
}

func (o EIPOutput) ToEIPOutput() EIPOutput {
	return o
}

func (o EIPOutput) ToEIPOutputWithContext(ctx context.Context) EIPOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(EIPOutput{})
}

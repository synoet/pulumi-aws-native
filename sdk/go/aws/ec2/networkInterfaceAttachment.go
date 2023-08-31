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

// Resource Type definition for AWS::EC2::NetworkInterfaceAttachment
type NetworkInterfaceAttachment struct {
	pulumi.CustomResourceState

	// The ID of the network interface attachment.
	AttachmentId pulumi.StringOutput `pulumi:"attachmentId"`
	// Whether to delete the network interface when the instance terminates. By default, this value is set to true.
	DeleteOnTermination pulumi.BoolPtrOutput `pulumi:"deleteOnTermination"`
	// The network interface's position in the attachment order. For example, the first attached network interface has a DeviceIndex of 0.
	DeviceIndex pulumi.StringOutput `pulumi:"deviceIndex"`
	// The ID of the instance to which you will attach the ENI.
	InstanceId pulumi.StringOutput `pulumi:"instanceId"`
	// The ID of the ENI that you want to attach.
	NetworkInterfaceId pulumi.StringOutput `pulumi:"networkInterfaceId"`
}

// NewNetworkInterfaceAttachment registers a new resource with the given unique name, arguments, and options.
func NewNetworkInterfaceAttachment(ctx *pulumi.Context,
	name string, args *NetworkInterfaceAttachmentArgs, opts ...pulumi.ResourceOption) (*NetworkInterfaceAttachment, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.DeviceIndex == nil {
		return nil, errors.New("invalid value for required argument 'DeviceIndex'")
	}
	if args.InstanceId == nil {
		return nil, errors.New("invalid value for required argument 'InstanceId'")
	}
	if args.NetworkInterfaceId == nil {
		return nil, errors.New("invalid value for required argument 'NetworkInterfaceId'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"deviceIndex",
		"instanceId",
		"networkInterfaceId",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource NetworkInterfaceAttachment
	err := ctx.RegisterResource("aws-native:ec2:NetworkInterfaceAttachment", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetNetworkInterfaceAttachment gets an existing NetworkInterfaceAttachment resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetNetworkInterfaceAttachment(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *NetworkInterfaceAttachmentState, opts ...pulumi.ResourceOption) (*NetworkInterfaceAttachment, error) {
	var resource NetworkInterfaceAttachment
	err := ctx.ReadResource("aws-native:ec2:NetworkInterfaceAttachment", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering NetworkInterfaceAttachment resources.
type networkInterfaceAttachmentState struct {
}

type NetworkInterfaceAttachmentState struct {
}

func (NetworkInterfaceAttachmentState) ElementType() reflect.Type {
	return reflect.TypeOf((*networkInterfaceAttachmentState)(nil)).Elem()
}

type networkInterfaceAttachmentArgs struct {
	// Whether to delete the network interface when the instance terminates. By default, this value is set to true.
	DeleteOnTermination *bool `pulumi:"deleteOnTermination"`
	// The network interface's position in the attachment order. For example, the first attached network interface has a DeviceIndex of 0.
	DeviceIndex string `pulumi:"deviceIndex"`
	// The ID of the instance to which you will attach the ENI.
	InstanceId string `pulumi:"instanceId"`
	// The ID of the ENI that you want to attach.
	NetworkInterfaceId string `pulumi:"networkInterfaceId"`
}

// The set of arguments for constructing a NetworkInterfaceAttachment resource.
type NetworkInterfaceAttachmentArgs struct {
	// Whether to delete the network interface when the instance terminates. By default, this value is set to true.
	DeleteOnTermination pulumi.BoolPtrInput
	// The network interface's position in the attachment order. For example, the first attached network interface has a DeviceIndex of 0.
	DeviceIndex pulumi.StringInput
	// The ID of the instance to which you will attach the ENI.
	InstanceId pulumi.StringInput
	// The ID of the ENI that you want to attach.
	NetworkInterfaceId pulumi.StringInput
}

func (NetworkInterfaceAttachmentArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*networkInterfaceAttachmentArgs)(nil)).Elem()
}

type NetworkInterfaceAttachmentInput interface {
	pulumi.Input

	ToNetworkInterfaceAttachmentOutput() NetworkInterfaceAttachmentOutput
	ToNetworkInterfaceAttachmentOutputWithContext(ctx context.Context) NetworkInterfaceAttachmentOutput
}

func (*NetworkInterfaceAttachment) ElementType() reflect.Type {
	return reflect.TypeOf((**NetworkInterfaceAttachment)(nil)).Elem()
}

func (i *NetworkInterfaceAttachment) ToNetworkInterfaceAttachmentOutput() NetworkInterfaceAttachmentOutput {
	return i.ToNetworkInterfaceAttachmentOutputWithContext(context.Background())
}

func (i *NetworkInterfaceAttachment) ToNetworkInterfaceAttachmentOutputWithContext(ctx context.Context) NetworkInterfaceAttachmentOutput {
	return pulumi.ToOutputWithContext(ctx, i).(NetworkInterfaceAttachmentOutput)
}

type NetworkInterfaceAttachmentOutput struct{ *pulumi.OutputState }

func (NetworkInterfaceAttachmentOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**NetworkInterfaceAttachment)(nil)).Elem()
}

func (o NetworkInterfaceAttachmentOutput) ToNetworkInterfaceAttachmentOutput() NetworkInterfaceAttachmentOutput {
	return o
}

func (o NetworkInterfaceAttachmentOutput) ToNetworkInterfaceAttachmentOutputWithContext(ctx context.Context) NetworkInterfaceAttachmentOutput {
	return o
}

// The ID of the network interface attachment.
func (o NetworkInterfaceAttachmentOutput) AttachmentId() pulumi.StringOutput {
	return o.ApplyT(func(v *NetworkInterfaceAttachment) pulumi.StringOutput { return v.AttachmentId }).(pulumi.StringOutput)
}

// Whether to delete the network interface when the instance terminates. By default, this value is set to true.
func (o NetworkInterfaceAttachmentOutput) DeleteOnTermination() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *NetworkInterfaceAttachment) pulumi.BoolPtrOutput { return v.DeleteOnTermination }).(pulumi.BoolPtrOutput)
}

// The network interface's position in the attachment order. For example, the first attached network interface has a DeviceIndex of 0.
func (o NetworkInterfaceAttachmentOutput) DeviceIndex() pulumi.StringOutput {
	return o.ApplyT(func(v *NetworkInterfaceAttachment) pulumi.StringOutput { return v.DeviceIndex }).(pulumi.StringOutput)
}

// The ID of the instance to which you will attach the ENI.
func (o NetworkInterfaceAttachmentOutput) InstanceId() pulumi.StringOutput {
	return o.ApplyT(func(v *NetworkInterfaceAttachment) pulumi.StringOutput { return v.InstanceId }).(pulumi.StringOutput)
}

// The ID of the ENI that you want to attach.
func (o NetworkInterfaceAttachmentOutput) NetworkInterfaceId() pulumi.StringOutput {
	return o.ApplyT(func(v *NetworkInterfaceAttachment) pulumi.StringOutput { return v.NetworkInterfaceId }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*NetworkInterfaceAttachmentInput)(nil)).Elem(), &NetworkInterfaceAttachment{})
	pulumi.RegisterOutputType(NetworkInterfaceAttachmentOutput{})
}

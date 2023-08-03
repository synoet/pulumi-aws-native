// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package iam

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::IAM::VirtualMFADevice
type VirtualMfaDevice struct {
	pulumi.CustomResourceState

	Path                 pulumi.StringPtrOutput         `pulumi:"path"`
	SerialNumber         pulumi.StringOutput            `pulumi:"serialNumber"`
	Tags                 VirtualMfaDeviceTagArrayOutput `pulumi:"tags"`
	Users                pulumi.StringArrayOutput       `pulumi:"users"`
	VirtualMfaDeviceName pulumi.StringPtrOutput         `pulumi:"virtualMfaDeviceName"`
}

// NewVirtualMfaDevice registers a new resource with the given unique name, arguments, and options.
func NewVirtualMfaDevice(ctx *pulumi.Context,
	name string, args *VirtualMfaDeviceArgs, opts ...pulumi.ResourceOption) (*VirtualMfaDevice, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Users == nil {
		return nil, errors.New("invalid value for required argument 'Users'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource VirtualMfaDevice
	err := ctx.RegisterResource("aws-native:iam:VirtualMfaDevice", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetVirtualMfaDevice gets an existing VirtualMfaDevice resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetVirtualMfaDevice(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *VirtualMfaDeviceState, opts ...pulumi.ResourceOption) (*VirtualMfaDevice, error) {
	var resource VirtualMfaDevice
	err := ctx.ReadResource("aws-native:iam:VirtualMfaDevice", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering VirtualMfaDevice resources.
type virtualMfaDeviceState struct {
}

type VirtualMfaDeviceState struct {
}

func (VirtualMfaDeviceState) ElementType() reflect.Type {
	return reflect.TypeOf((*virtualMfaDeviceState)(nil)).Elem()
}

type virtualMfaDeviceArgs struct {
	Path                 *string               `pulumi:"path"`
	Tags                 []VirtualMfaDeviceTag `pulumi:"tags"`
	Users                []string              `pulumi:"users"`
	VirtualMfaDeviceName *string               `pulumi:"virtualMfaDeviceName"`
}

// The set of arguments for constructing a VirtualMfaDevice resource.
type VirtualMfaDeviceArgs struct {
	Path                 pulumi.StringPtrInput
	Tags                 VirtualMfaDeviceTagArrayInput
	Users                pulumi.StringArrayInput
	VirtualMfaDeviceName pulumi.StringPtrInput
}

func (VirtualMfaDeviceArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*virtualMfaDeviceArgs)(nil)).Elem()
}

type VirtualMfaDeviceInput interface {
	pulumi.Input

	ToVirtualMfaDeviceOutput() VirtualMfaDeviceOutput
	ToVirtualMfaDeviceOutputWithContext(ctx context.Context) VirtualMfaDeviceOutput
}

func (*VirtualMfaDevice) ElementType() reflect.Type {
	return reflect.TypeOf((**VirtualMfaDevice)(nil)).Elem()
}

func (i *VirtualMfaDevice) ToVirtualMfaDeviceOutput() VirtualMfaDeviceOutput {
	return i.ToVirtualMfaDeviceOutputWithContext(context.Background())
}

func (i *VirtualMfaDevice) ToVirtualMfaDeviceOutputWithContext(ctx context.Context) VirtualMfaDeviceOutput {
	return pulumi.ToOutputWithContext(ctx, i).(VirtualMfaDeviceOutput)
}

type VirtualMfaDeviceOutput struct{ *pulumi.OutputState }

func (VirtualMfaDeviceOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**VirtualMfaDevice)(nil)).Elem()
}

func (o VirtualMfaDeviceOutput) ToVirtualMfaDeviceOutput() VirtualMfaDeviceOutput {
	return o
}

func (o VirtualMfaDeviceOutput) ToVirtualMfaDeviceOutputWithContext(ctx context.Context) VirtualMfaDeviceOutput {
	return o
}

func (o VirtualMfaDeviceOutput) Path() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *VirtualMfaDevice) pulumi.StringPtrOutput { return v.Path }).(pulumi.StringPtrOutput)
}

func (o VirtualMfaDeviceOutput) SerialNumber() pulumi.StringOutput {
	return o.ApplyT(func(v *VirtualMfaDevice) pulumi.StringOutput { return v.SerialNumber }).(pulumi.StringOutput)
}

func (o VirtualMfaDeviceOutput) Tags() VirtualMfaDeviceTagArrayOutput {
	return o.ApplyT(func(v *VirtualMfaDevice) VirtualMfaDeviceTagArrayOutput { return v.Tags }).(VirtualMfaDeviceTagArrayOutput)
}

func (o VirtualMfaDeviceOutput) Users() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *VirtualMfaDevice) pulumi.StringArrayOutput { return v.Users }).(pulumi.StringArrayOutput)
}

func (o VirtualMfaDeviceOutput) VirtualMfaDeviceName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *VirtualMfaDevice) pulumi.StringPtrOutput { return v.VirtualMfaDeviceName }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*VirtualMfaDeviceInput)(nil)).Elem(), &VirtualMfaDevice{})
	pulumi.RegisterOutputType(VirtualMfaDeviceOutput{})
}

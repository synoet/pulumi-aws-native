// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package appstream

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::AppStream::Fleet
//
// Deprecated: Fleet is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
type Fleet struct {
	pulumi.CustomResourceState

	ComputeCapacity                FleetComputeCapacityPtrOutput `pulumi:"computeCapacity"`
	Description                    pulumi.StringPtrOutput        `pulumi:"description"`
	DisconnectTimeoutInSeconds     pulumi.IntPtrOutput           `pulumi:"disconnectTimeoutInSeconds"`
	DisplayName                    pulumi.StringPtrOutput        `pulumi:"displayName"`
	DomainJoinInfo                 FleetDomainJoinInfoPtrOutput  `pulumi:"domainJoinInfo"`
	EnableDefaultInternetAccess    pulumi.BoolPtrOutput          `pulumi:"enableDefaultInternetAccess"`
	FleetType                      pulumi.StringPtrOutput        `pulumi:"fleetType"`
	IamRoleArn                     pulumi.StringPtrOutput        `pulumi:"iamRoleArn"`
	IdleDisconnectTimeoutInSeconds pulumi.IntPtrOutput           `pulumi:"idleDisconnectTimeoutInSeconds"`
	ImageArn                       pulumi.StringPtrOutput        `pulumi:"imageArn"`
	ImageName                      pulumi.StringPtrOutput        `pulumi:"imageName"`
	InstanceType                   pulumi.StringOutput           `pulumi:"instanceType"`
	MaxConcurrentSessions          pulumi.IntPtrOutput           `pulumi:"maxConcurrentSessions"`
	MaxSessionsPerInstance         pulumi.IntPtrOutput           `pulumi:"maxSessionsPerInstance"`
	MaxUserDurationInSeconds       pulumi.IntPtrOutput           `pulumi:"maxUserDurationInSeconds"`
	Name                           pulumi.StringOutput           `pulumi:"name"`
	Platform                       pulumi.StringPtrOutput        `pulumi:"platform"`
	SessionScriptS3Location        FleetS3LocationPtrOutput      `pulumi:"sessionScriptS3Location"`
	StreamView                     pulumi.StringPtrOutput        `pulumi:"streamView"`
	Tags                           FleetTagArrayOutput           `pulumi:"tags"`
	UsbDeviceFilterStrings         pulumi.StringArrayOutput      `pulumi:"usbDeviceFilterStrings"`
	VpcConfig                      FleetVpcConfigPtrOutput       `pulumi:"vpcConfig"`
}

// NewFleet registers a new resource with the given unique name, arguments, and options.
func NewFleet(ctx *pulumi.Context,
	name string, args *FleetArgs, opts ...pulumi.ResourceOption) (*Fleet, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.InstanceType == nil {
		return nil, errors.New("invalid value for required argument 'InstanceType'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"fleetType",
		"name",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Fleet
	err := ctx.RegisterResource("aws-native:appstream:Fleet", name, args, &resource, opts...)
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
	err := ctx.ReadResource("aws-native:appstream:Fleet", name, id, state, &resource, opts...)
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
	ComputeCapacity                *FleetComputeCapacity `pulumi:"computeCapacity"`
	Description                    *string               `pulumi:"description"`
	DisconnectTimeoutInSeconds     *int                  `pulumi:"disconnectTimeoutInSeconds"`
	DisplayName                    *string               `pulumi:"displayName"`
	DomainJoinInfo                 *FleetDomainJoinInfo  `pulumi:"domainJoinInfo"`
	EnableDefaultInternetAccess    *bool                 `pulumi:"enableDefaultInternetAccess"`
	FleetType                      *string               `pulumi:"fleetType"`
	IamRoleArn                     *string               `pulumi:"iamRoleArn"`
	IdleDisconnectTimeoutInSeconds *int                  `pulumi:"idleDisconnectTimeoutInSeconds"`
	ImageArn                       *string               `pulumi:"imageArn"`
	ImageName                      *string               `pulumi:"imageName"`
	InstanceType                   string                `pulumi:"instanceType"`
	MaxConcurrentSessions          *int                  `pulumi:"maxConcurrentSessions"`
	MaxSessionsPerInstance         *int                  `pulumi:"maxSessionsPerInstance"`
	MaxUserDurationInSeconds       *int                  `pulumi:"maxUserDurationInSeconds"`
	Name                           *string               `pulumi:"name"`
	Platform                       *string               `pulumi:"platform"`
	SessionScriptS3Location        *FleetS3Location      `pulumi:"sessionScriptS3Location"`
	StreamView                     *string               `pulumi:"streamView"`
	Tags                           []FleetTag            `pulumi:"tags"`
	UsbDeviceFilterStrings         []string              `pulumi:"usbDeviceFilterStrings"`
	VpcConfig                      *FleetVpcConfig       `pulumi:"vpcConfig"`
}

// The set of arguments for constructing a Fleet resource.
type FleetArgs struct {
	ComputeCapacity                FleetComputeCapacityPtrInput
	Description                    pulumi.StringPtrInput
	DisconnectTimeoutInSeconds     pulumi.IntPtrInput
	DisplayName                    pulumi.StringPtrInput
	DomainJoinInfo                 FleetDomainJoinInfoPtrInput
	EnableDefaultInternetAccess    pulumi.BoolPtrInput
	FleetType                      pulumi.StringPtrInput
	IamRoleArn                     pulumi.StringPtrInput
	IdleDisconnectTimeoutInSeconds pulumi.IntPtrInput
	ImageArn                       pulumi.StringPtrInput
	ImageName                      pulumi.StringPtrInput
	InstanceType                   pulumi.StringInput
	MaxConcurrentSessions          pulumi.IntPtrInput
	MaxSessionsPerInstance         pulumi.IntPtrInput
	MaxUserDurationInSeconds       pulumi.IntPtrInput
	Name                           pulumi.StringPtrInput
	Platform                       pulumi.StringPtrInput
	SessionScriptS3Location        FleetS3LocationPtrInput
	StreamView                     pulumi.StringPtrInput
	Tags                           FleetTagArrayInput
	UsbDeviceFilterStrings         pulumi.StringArrayInput
	VpcConfig                      FleetVpcConfigPtrInput
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
	return reflect.TypeOf((**Fleet)(nil)).Elem()
}

func (i *Fleet) ToFleetOutput() FleetOutput {
	return i.ToFleetOutputWithContext(context.Background())
}

func (i *Fleet) ToFleetOutputWithContext(ctx context.Context) FleetOutput {
	return pulumi.ToOutputWithContext(ctx, i).(FleetOutput)
}

type FleetOutput struct{ *pulumi.OutputState }

func (FleetOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Fleet)(nil)).Elem()
}

func (o FleetOutput) ToFleetOutput() FleetOutput {
	return o
}

func (o FleetOutput) ToFleetOutputWithContext(ctx context.Context) FleetOutput {
	return o
}

func (o FleetOutput) ComputeCapacity() FleetComputeCapacityPtrOutput {
	return o.ApplyT(func(v *Fleet) FleetComputeCapacityPtrOutput { return v.ComputeCapacity }).(FleetComputeCapacityPtrOutput)
}

func (o FleetOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Fleet) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

func (o FleetOutput) DisconnectTimeoutInSeconds() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *Fleet) pulumi.IntPtrOutput { return v.DisconnectTimeoutInSeconds }).(pulumi.IntPtrOutput)
}

func (o FleetOutput) DisplayName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Fleet) pulumi.StringPtrOutput { return v.DisplayName }).(pulumi.StringPtrOutput)
}

func (o FleetOutput) DomainJoinInfo() FleetDomainJoinInfoPtrOutput {
	return o.ApplyT(func(v *Fleet) FleetDomainJoinInfoPtrOutput { return v.DomainJoinInfo }).(FleetDomainJoinInfoPtrOutput)
}

func (o FleetOutput) EnableDefaultInternetAccess() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *Fleet) pulumi.BoolPtrOutput { return v.EnableDefaultInternetAccess }).(pulumi.BoolPtrOutput)
}

func (o FleetOutput) FleetType() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Fleet) pulumi.StringPtrOutput { return v.FleetType }).(pulumi.StringPtrOutput)
}

func (o FleetOutput) IamRoleArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Fleet) pulumi.StringPtrOutput { return v.IamRoleArn }).(pulumi.StringPtrOutput)
}

func (o FleetOutput) IdleDisconnectTimeoutInSeconds() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *Fleet) pulumi.IntPtrOutput { return v.IdleDisconnectTimeoutInSeconds }).(pulumi.IntPtrOutput)
}

func (o FleetOutput) ImageArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Fleet) pulumi.StringPtrOutput { return v.ImageArn }).(pulumi.StringPtrOutput)
}

func (o FleetOutput) ImageName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Fleet) pulumi.StringPtrOutput { return v.ImageName }).(pulumi.StringPtrOutput)
}

func (o FleetOutput) InstanceType() pulumi.StringOutput {
	return o.ApplyT(func(v *Fleet) pulumi.StringOutput { return v.InstanceType }).(pulumi.StringOutput)
}

func (o FleetOutput) MaxConcurrentSessions() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *Fleet) pulumi.IntPtrOutput { return v.MaxConcurrentSessions }).(pulumi.IntPtrOutput)
}

func (o FleetOutput) MaxSessionsPerInstance() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *Fleet) pulumi.IntPtrOutput { return v.MaxSessionsPerInstance }).(pulumi.IntPtrOutput)
}

func (o FleetOutput) MaxUserDurationInSeconds() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *Fleet) pulumi.IntPtrOutput { return v.MaxUserDurationInSeconds }).(pulumi.IntPtrOutput)
}

func (o FleetOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *Fleet) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

func (o FleetOutput) Platform() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Fleet) pulumi.StringPtrOutput { return v.Platform }).(pulumi.StringPtrOutput)
}

func (o FleetOutput) SessionScriptS3Location() FleetS3LocationPtrOutput {
	return o.ApplyT(func(v *Fleet) FleetS3LocationPtrOutput { return v.SessionScriptS3Location }).(FleetS3LocationPtrOutput)
}

func (o FleetOutput) StreamView() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Fleet) pulumi.StringPtrOutput { return v.StreamView }).(pulumi.StringPtrOutput)
}

func (o FleetOutput) Tags() FleetTagArrayOutput {
	return o.ApplyT(func(v *Fleet) FleetTagArrayOutput { return v.Tags }).(FleetTagArrayOutput)
}

func (o FleetOutput) UsbDeviceFilterStrings() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *Fleet) pulumi.StringArrayOutput { return v.UsbDeviceFilterStrings }).(pulumi.StringArrayOutput)
}

func (o FleetOutput) VpcConfig() FleetVpcConfigPtrOutput {
	return o.ApplyT(func(v *Fleet) FleetVpcConfigPtrOutput { return v.VpcConfig }).(FleetVpcConfigPtrOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*FleetInput)(nil)).Elem(), &Fleet{})
	pulumi.RegisterOutputType(FleetOutput{})
}

// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package devicefarm

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// AWS::DeviceFarm::VPCEConfiguration creates a new Device Farm VPCE Configuration
type VPCEConfiguration struct {
	pulumi.CustomResourceState

	Arn                          pulumi.StringOutput             `pulumi:"arn"`
	ServiceDnsName               pulumi.StringOutput             `pulumi:"serviceDnsName"`
	Tags                         VPCEConfigurationTagArrayOutput `pulumi:"tags"`
	VpceConfigurationDescription pulumi.StringPtrOutput          `pulumi:"vpceConfigurationDescription"`
	VpceConfigurationName        pulumi.StringOutput             `pulumi:"vpceConfigurationName"`
	VpceServiceName              pulumi.StringOutput             `pulumi:"vpceServiceName"`
}

// NewVPCEConfiguration registers a new resource with the given unique name, arguments, and options.
func NewVPCEConfiguration(ctx *pulumi.Context,
	name string, args *VPCEConfigurationArgs, opts ...pulumi.ResourceOption) (*VPCEConfiguration, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ServiceDnsName == nil {
		return nil, errors.New("invalid value for required argument 'ServiceDnsName'")
	}
	if args.VpceConfigurationName == nil {
		return nil, errors.New("invalid value for required argument 'VpceConfigurationName'")
	}
	if args.VpceServiceName == nil {
		return nil, errors.New("invalid value for required argument 'VpceServiceName'")
	}
	var resource VPCEConfiguration
	err := ctx.RegisterResource("aws-native:devicefarm:VPCEConfiguration", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetVPCEConfiguration gets an existing VPCEConfiguration resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetVPCEConfiguration(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *VPCEConfigurationState, opts ...pulumi.ResourceOption) (*VPCEConfiguration, error) {
	var resource VPCEConfiguration
	err := ctx.ReadResource("aws-native:devicefarm:VPCEConfiguration", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering VPCEConfiguration resources.
type vpceconfigurationState struct {
}

type VPCEConfigurationState struct {
}

func (VPCEConfigurationState) ElementType() reflect.Type {
	return reflect.TypeOf((*vpceconfigurationState)(nil)).Elem()
}

type vpceconfigurationArgs struct {
	ServiceDnsName               string                 `pulumi:"serviceDnsName"`
	Tags                         []VPCEConfigurationTag `pulumi:"tags"`
	VpceConfigurationDescription *string                `pulumi:"vpceConfigurationDescription"`
	VpceConfigurationName        string                 `pulumi:"vpceConfigurationName"`
	VpceServiceName              string                 `pulumi:"vpceServiceName"`
}

// The set of arguments for constructing a VPCEConfiguration resource.
type VPCEConfigurationArgs struct {
	ServiceDnsName               pulumi.StringInput
	Tags                         VPCEConfigurationTagArrayInput
	VpceConfigurationDescription pulumi.StringPtrInput
	VpceConfigurationName        pulumi.StringInput
	VpceServiceName              pulumi.StringInput
}

func (VPCEConfigurationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*vpceconfigurationArgs)(nil)).Elem()
}

type VPCEConfigurationInput interface {
	pulumi.Input

	ToVPCEConfigurationOutput() VPCEConfigurationOutput
	ToVPCEConfigurationOutputWithContext(ctx context.Context) VPCEConfigurationOutput
}

func (*VPCEConfiguration) ElementType() reflect.Type {
	return reflect.TypeOf((**VPCEConfiguration)(nil)).Elem()
}

func (i *VPCEConfiguration) ToVPCEConfigurationOutput() VPCEConfigurationOutput {
	return i.ToVPCEConfigurationOutputWithContext(context.Background())
}

func (i *VPCEConfiguration) ToVPCEConfigurationOutputWithContext(ctx context.Context) VPCEConfigurationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(VPCEConfigurationOutput)
}

type VPCEConfigurationOutput struct{ *pulumi.OutputState }

func (VPCEConfigurationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**VPCEConfiguration)(nil)).Elem()
}

func (o VPCEConfigurationOutput) ToVPCEConfigurationOutput() VPCEConfigurationOutput {
	return o
}

func (o VPCEConfigurationOutput) ToVPCEConfigurationOutputWithContext(ctx context.Context) VPCEConfigurationOutput {
	return o
}

func (o VPCEConfigurationOutput) Arn() pulumi.StringOutput {
	return o.ApplyT(func(v *VPCEConfiguration) pulumi.StringOutput { return v.Arn }).(pulumi.StringOutput)
}

func (o VPCEConfigurationOutput) ServiceDnsName() pulumi.StringOutput {
	return o.ApplyT(func(v *VPCEConfiguration) pulumi.StringOutput { return v.ServiceDnsName }).(pulumi.StringOutput)
}

func (o VPCEConfigurationOutput) Tags() VPCEConfigurationTagArrayOutput {
	return o.ApplyT(func(v *VPCEConfiguration) VPCEConfigurationTagArrayOutput { return v.Tags }).(VPCEConfigurationTagArrayOutput)
}

func (o VPCEConfigurationOutput) VpceConfigurationDescription() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *VPCEConfiguration) pulumi.StringPtrOutput { return v.VpceConfigurationDescription }).(pulumi.StringPtrOutput)
}

func (o VPCEConfigurationOutput) VpceConfigurationName() pulumi.StringOutput {
	return o.ApplyT(func(v *VPCEConfiguration) pulumi.StringOutput { return v.VpceConfigurationName }).(pulumi.StringOutput)
}

func (o VPCEConfigurationOutput) VpceServiceName() pulumi.StringOutput {
	return o.ApplyT(func(v *VPCEConfiguration) pulumi.StringOutput { return v.VpceServiceName }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*VPCEConfigurationInput)(nil)).Elem(), &VPCEConfiguration{})
	pulumi.RegisterOutputType(VPCEConfigurationOutput{})
}

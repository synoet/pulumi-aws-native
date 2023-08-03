// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package route53

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource schema for AWS::Route53::HostedZone.
type HostedZone struct {
	pulumi.CustomResourceState

	HostedZoneConfig HostedZoneConfigPtrOutput `pulumi:"hostedZoneConfig"`
	// Adds, edits, or deletes tags for a health check or a hosted zone.
	//
	// For information about using tags for cost allocation, see Using Cost Allocation Tags in the AWS Billing and Cost Management User Guide.
	HostedZoneTags HostedZoneTagArrayOutput `pulumi:"hostedZoneTags"`
	// The name of the domain. Specify a fully qualified domain name, for example, www.example.com. The trailing dot is optional; Amazon Route 53 assumes that the domain name is fully qualified. This means that Route 53 treats www.example.com (without a trailing dot) and www.example.com. (with a trailing dot) as identical.
	//
	// If you're creating a public hosted zone, this is the name you have registered with your DNS registrar. If your domain name is registered with a registrar other than Route 53, change the name servers for your domain to the set of NameServers that are returned by the Fn::GetAtt intrinsic function.
	Name               pulumi.StringPtrOutput                `pulumi:"name"`
	NameServers        pulumi.StringArrayOutput              `pulumi:"nameServers"`
	QueryLoggingConfig HostedZoneQueryLoggingConfigPtrOutput `pulumi:"queryLoggingConfig"`
	// A complex type that contains information about the VPCs that are associated with the specified hosted zone.
	Vpcs HostedZoneVpcArrayOutput `pulumi:"vpcs"`
}

// NewHostedZone registers a new resource with the given unique name, arguments, and options.
func NewHostedZone(ctx *pulumi.Context,
	name string, args *HostedZoneArgs, opts ...pulumi.ResourceOption) (*HostedZone, error) {
	if args == nil {
		args = &HostedZoneArgs{}
	}

	opts = internal.PkgResourceDefaultOpts(opts)
	var resource HostedZone
	err := ctx.RegisterResource("aws-native:route53:HostedZone", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetHostedZone gets an existing HostedZone resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetHostedZone(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *HostedZoneState, opts ...pulumi.ResourceOption) (*HostedZone, error) {
	var resource HostedZone
	err := ctx.ReadResource("aws-native:route53:HostedZone", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering HostedZone resources.
type hostedZoneState struct {
}

type HostedZoneState struct {
}

func (HostedZoneState) ElementType() reflect.Type {
	return reflect.TypeOf((*hostedZoneState)(nil)).Elem()
}

type hostedZoneArgs struct {
	HostedZoneConfig *HostedZoneConfig `pulumi:"hostedZoneConfig"`
	// Adds, edits, or deletes tags for a health check or a hosted zone.
	//
	// For information about using tags for cost allocation, see Using Cost Allocation Tags in the AWS Billing and Cost Management User Guide.
	HostedZoneTags []HostedZoneTag `pulumi:"hostedZoneTags"`
	// The name of the domain. Specify a fully qualified domain name, for example, www.example.com. The trailing dot is optional; Amazon Route 53 assumes that the domain name is fully qualified. This means that Route 53 treats www.example.com (without a trailing dot) and www.example.com. (with a trailing dot) as identical.
	//
	// If you're creating a public hosted zone, this is the name you have registered with your DNS registrar. If your domain name is registered with a registrar other than Route 53, change the name servers for your domain to the set of NameServers that are returned by the Fn::GetAtt intrinsic function.
	Name               *string                       `pulumi:"name"`
	QueryLoggingConfig *HostedZoneQueryLoggingConfig `pulumi:"queryLoggingConfig"`
	// A complex type that contains information about the VPCs that are associated with the specified hosted zone.
	Vpcs []HostedZoneVpc `pulumi:"vpcs"`
}

// The set of arguments for constructing a HostedZone resource.
type HostedZoneArgs struct {
	HostedZoneConfig HostedZoneConfigPtrInput
	// Adds, edits, or deletes tags for a health check or a hosted zone.
	//
	// For information about using tags for cost allocation, see Using Cost Allocation Tags in the AWS Billing and Cost Management User Guide.
	HostedZoneTags HostedZoneTagArrayInput
	// The name of the domain. Specify a fully qualified domain name, for example, www.example.com. The trailing dot is optional; Amazon Route 53 assumes that the domain name is fully qualified. This means that Route 53 treats www.example.com (without a trailing dot) and www.example.com. (with a trailing dot) as identical.
	//
	// If you're creating a public hosted zone, this is the name you have registered with your DNS registrar. If your domain name is registered with a registrar other than Route 53, change the name servers for your domain to the set of NameServers that are returned by the Fn::GetAtt intrinsic function.
	Name               pulumi.StringPtrInput
	QueryLoggingConfig HostedZoneQueryLoggingConfigPtrInput
	// A complex type that contains information about the VPCs that are associated with the specified hosted zone.
	Vpcs HostedZoneVpcArrayInput
}

func (HostedZoneArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*hostedZoneArgs)(nil)).Elem()
}

type HostedZoneInput interface {
	pulumi.Input

	ToHostedZoneOutput() HostedZoneOutput
	ToHostedZoneOutputWithContext(ctx context.Context) HostedZoneOutput
}

func (*HostedZone) ElementType() reflect.Type {
	return reflect.TypeOf((**HostedZone)(nil)).Elem()
}

func (i *HostedZone) ToHostedZoneOutput() HostedZoneOutput {
	return i.ToHostedZoneOutputWithContext(context.Background())
}

func (i *HostedZone) ToHostedZoneOutputWithContext(ctx context.Context) HostedZoneOutput {
	return pulumi.ToOutputWithContext(ctx, i).(HostedZoneOutput)
}

type HostedZoneOutput struct{ *pulumi.OutputState }

func (HostedZoneOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**HostedZone)(nil)).Elem()
}

func (o HostedZoneOutput) ToHostedZoneOutput() HostedZoneOutput {
	return o
}

func (o HostedZoneOutput) ToHostedZoneOutputWithContext(ctx context.Context) HostedZoneOutput {
	return o
}

func (o HostedZoneOutput) HostedZoneConfig() HostedZoneConfigPtrOutput {
	return o.ApplyT(func(v *HostedZone) HostedZoneConfigPtrOutput { return v.HostedZoneConfig }).(HostedZoneConfigPtrOutput)
}

// Adds, edits, or deletes tags for a health check or a hosted zone.
//
// For information about using tags for cost allocation, see Using Cost Allocation Tags in the AWS Billing and Cost Management User Guide.
func (o HostedZoneOutput) HostedZoneTags() HostedZoneTagArrayOutput {
	return o.ApplyT(func(v *HostedZone) HostedZoneTagArrayOutput { return v.HostedZoneTags }).(HostedZoneTagArrayOutput)
}

// The name of the domain. Specify a fully qualified domain name, for example, www.example.com. The trailing dot is optional; Amazon Route 53 assumes that the domain name is fully qualified. This means that Route 53 treats www.example.com (without a trailing dot) and www.example.com. (with a trailing dot) as identical.
//
// If you're creating a public hosted zone, this is the name you have registered with your DNS registrar. If your domain name is registered with a registrar other than Route 53, change the name servers for your domain to the set of NameServers that are returned by the Fn::GetAtt intrinsic function.
func (o HostedZoneOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *HostedZone) pulumi.StringPtrOutput { return v.Name }).(pulumi.StringPtrOutput)
}

func (o HostedZoneOutput) NameServers() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *HostedZone) pulumi.StringArrayOutput { return v.NameServers }).(pulumi.StringArrayOutput)
}

func (o HostedZoneOutput) QueryLoggingConfig() HostedZoneQueryLoggingConfigPtrOutput {
	return o.ApplyT(func(v *HostedZone) HostedZoneQueryLoggingConfigPtrOutput { return v.QueryLoggingConfig }).(HostedZoneQueryLoggingConfigPtrOutput)
}

// A complex type that contains information about the VPCs that are associated with the specified hosted zone.
func (o HostedZoneOutput) Vpcs() HostedZoneVpcArrayOutput {
	return o.ApplyT(func(v *HostedZone) HostedZoneVpcArrayOutput { return v.Vpcs }).(HostedZoneVpcArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*HostedZoneInput)(nil)).Elem(), &HostedZone{})
	pulumi.RegisterOutputType(HostedZoneOutput{})
}

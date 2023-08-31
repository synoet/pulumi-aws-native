// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package servicediscovery

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::ServiceDiscovery::Service
//
// Deprecated: Service is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
type Service struct {
	pulumi.CustomResourceState

	Arn                     pulumi.StringOutput                     `pulumi:"arn"`
	Description             pulumi.StringPtrOutput                  `pulumi:"description"`
	DnsConfig               ServiceDnsConfigPtrOutput               `pulumi:"dnsConfig"`
	HealthCheckConfig       ServiceHealthCheckConfigPtrOutput       `pulumi:"healthCheckConfig"`
	HealthCheckCustomConfig ServiceHealthCheckCustomConfigPtrOutput `pulumi:"healthCheckCustomConfig"`
	Name                    pulumi.StringPtrOutput                  `pulumi:"name"`
	NamespaceId             pulumi.StringPtrOutput                  `pulumi:"namespaceId"`
	Tags                    ServiceTagArrayOutput                   `pulumi:"tags"`
	Type                    pulumi.StringPtrOutput                  `pulumi:"type"`
}

// NewService registers a new resource with the given unique name, arguments, and options.
func NewService(ctx *pulumi.Context,
	name string, args *ServiceArgs, opts ...pulumi.ResourceOption) (*Service, error) {
	if args == nil {
		args = &ServiceArgs{}
	}

	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"healthCheckCustomConfig",
		"name",
		"namespaceId",
		"type",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Service
	err := ctx.RegisterResource("aws-native:servicediscovery:Service", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetService gets an existing Service resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetService(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ServiceState, opts ...pulumi.ResourceOption) (*Service, error) {
	var resource Service
	err := ctx.ReadResource("aws-native:servicediscovery:Service", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Service resources.
type serviceState struct {
}

type ServiceState struct {
}

func (ServiceState) ElementType() reflect.Type {
	return reflect.TypeOf((*serviceState)(nil)).Elem()
}

type serviceArgs struct {
	Description             *string                         `pulumi:"description"`
	DnsConfig               *ServiceDnsConfig               `pulumi:"dnsConfig"`
	HealthCheckConfig       *ServiceHealthCheckConfig       `pulumi:"healthCheckConfig"`
	HealthCheckCustomConfig *ServiceHealthCheckCustomConfig `pulumi:"healthCheckCustomConfig"`
	Name                    *string                         `pulumi:"name"`
	NamespaceId             *string                         `pulumi:"namespaceId"`
	Tags                    []ServiceTag                    `pulumi:"tags"`
	Type                    *string                         `pulumi:"type"`
}

// The set of arguments for constructing a Service resource.
type ServiceArgs struct {
	Description             pulumi.StringPtrInput
	DnsConfig               ServiceDnsConfigPtrInput
	HealthCheckConfig       ServiceHealthCheckConfigPtrInput
	HealthCheckCustomConfig ServiceHealthCheckCustomConfigPtrInput
	Name                    pulumi.StringPtrInput
	NamespaceId             pulumi.StringPtrInput
	Tags                    ServiceTagArrayInput
	Type                    pulumi.StringPtrInput
}

func (ServiceArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*serviceArgs)(nil)).Elem()
}

type ServiceInput interface {
	pulumi.Input

	ToServiceOutput() ServiceOutput
	ToServiceOutputWithContext(ctx context.Context) ServiceOutput
}

func (*Service) ElementType() reflect.Type {
	return reflect.TypeOf((**Service)(nil)).Elem()
}

func (i *Service) ToServiceOutput() ServiceOutput {
	return i.ToServiceOutputWithContext(context.Background())
}

func (i *Service) ToServiceOutputWithContext(ctx context.Context) ServiceOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ServiceOutput)
}

type ServiceOutput struct{ *pulumi.OutputState }

func (ServiceOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Service)(nil)).Elem()
}

func (o ServiceOutput) ToServiceOutput() ServiceOutput {
	return o
}

func (o ServiceOutput) ToServiceOutputWithContext(ctx context.Context) ServiceOutput {
	return o
}

func (o ServiceOutput) Arn() pulumi.StringOutput {
	return o.ApplyT(func(v *Service) pulumi.StringOutput { return v.Arn }).(pulumi.StringOutput)
}

func (o ServiceOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Service) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

func (o ServiceOutput) DnsConfig() ServiceDnsConfigPtrOutput {
	return o.ApplyT(func(v *Service) ServiceDnsConfigPtrOutput { return v.DnsConfig }).(ServiceDnsConfigPtrOutput)
}

func (o ServiceOutput) HealthCheckConfig() ServiceHealthCheckConfigPtrOutput {
	return o.ApplyT(func(v *Service) ServiceHealthCheckConfigPtrOutput { return v.HealthCheckConfig }).(ServiceHealthCheckConfigPtrOutput)
}

func (o ServiceOutput) HealthCheckCustomConfig() ServiceHealthCheckCustomConfigPtrOutput {
	return o.ApplyT(func(v *Service) ServiceHealthCheckCustomConfigPtrOutput { return v.HealthCheckCustomConfig }).(ServiceHealthCheckCustomConfigPtrOutput)
}

func (o ServiceOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Service) pulumi.StringPtrOutput { return v.Name }).(pulumi.StringPtrOutput)
}

func (o ServiceOutput) NamespaceId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Service) pulumi.StringPtrOutput { return v.NamespaceId }).(pulumi.StringPtrOutput)
}

func (o ServiceOutput) Tags() ServiceTagArrayOutput {
	return o.ApplyT(func(v *Service) ServiceTagArrayOutput { return v.Tags }).(ServiceTagArrayOutput)
}

func (o ServiceOutput) Type() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Service) pulumi.StringPtrOutput { return v.Type }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ServiceInput)(nil)).Elem(), &Service{})
	pulumi.RegisterOutputType(ServiceOutput{})
}

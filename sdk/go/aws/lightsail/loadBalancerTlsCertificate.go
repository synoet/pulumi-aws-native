// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package lightsail

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::Lightsail::LoadBalancerTlsCertificate
type LoadBalancerTlsCertificate struct {
	pulumi.CustomResourceState

	// An array of strings listing alternative domains and subdomains for your SSL/TLS certificate.
	CertificateAlternativeNames pulumi.StringArrayOutput `pulumi:"certificateAlternativeNames"`
	// The domain name (e.g., example.com ) for your SSL/TLS certificate.
	CertificateDomainName pulumi.StringOutput `pulumi:"certificateDomainName"`
	// The SSL/TLS certificate name.
	CertificateName pulumi.StringOutput `pulumi:"certificateName"`
	// A Boolean value that indicates whether HTTPS redirection is enabled for the load balancer.
	HttpsRedirectionEnabled pulumi.BoolPtrOutput `pulumi:"httpsRedirectionEnabled"`
	// When true, the SSL/TLS certificate is attached to the Lightsail load balancer.
	IsAttached pulumi.BoolPtrOutput `pulumi:"isAttached"`
	// The name of your load balancer.
	LoadBalancerName              pulumi.StringOutput `pulumi:"loadBalancerName"`
	LoadBalancerTlsCertificateArn pulumi.StringOutput `pulumi:"loadBalancerTlsCertificateArn"`
	// The validation status of the SSL/TLS certificate.
	Status pulumi.StringOutput `pulumi:"status"`
}

// NewLoadBalancerTlsCertificate registers a new resource with the given unique name, arguments, and options.
func NewLoadBalancerTlsCertificate(ctx *pulumi.Context,
	name string, args *LoadBalancerTlsCertificateArgs, opts ...pulumi.ResourceOption) (*LoadBalancerTlsCertificate, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.CertificateDomainName == nil {
		return nil, errors.New("invalid value for required argument 'CertificateDomainName'")
	}
	if args.CertificateName == nil {
		return nil, errors.New("invalid value for required argument 'CertificateName'")
	}
	if args.LoadBalancerName == nil {
		return nil, errors.New("invalid value for required argument 'LoadBalancerName'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"certificateAlternativeNames[*]",
		"certificateDomainName",
		"certificateName",
		"loadBalancerName",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource LoadBalancerTlsCertificate
	err := ctx.RegisterResource("aws-native:lightsail:LoadBalancerTlsCertificate", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetLoadBalancerTlsCertificate gets an existing LoadBalancerTlsCertificate resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetLoadBalancerTlsCertificate(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *LoadBalancerTlsCertificateState, opts ...pulumi.ResourceOption) (*LoadBalancerTlsCertificate, error) {
	var resource LoadBalancerTlsCertificate
	err := ctx.ReadResource("aws-native:lightsail:LoadBalancerTlsCertificate", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering LoadBalancerTlsCertificate resources.
type loadBalancerTlsCertificateState struct {
}

type LoadBalancerTlsCertificateState struct {
}

func (LoadBalancerTlsCertificateState) ElementType() reflect.Type {
	return reflect.TypeOf((*loadBalancerTlsCertificateState)(nil)).Elem()
}

type loadBalancerTlsCertificateArgs struct {
	// An array of strings listing alternative domains and subdomains for your SSL/TLS certificate.
	CertificateAlternativeNames []string `pulumi:"certificateAlternativeNames"`
	// The domain name (e.g., example.com ) for your SSL/TLS certificate.
	CertificateDomainName string `pulumi:"certificateDomainName"`
	// The SSL/TLS certificate name.
	CertificateName string `pulumi:"certificateName"`
	// A Boolean value that indicates whether HTTPS redirection is enabled for the load balancer.
	HttpsRedirectionEnabled *bool `pulumi:"httpsRedirectionEnabled"`
	// When true, the SSL/TLS certificate is attached to the Lightsail load balancer.
	IsAttached *bool `pulumi:"isAttached"`
	// The name of your load balancer.
	LoadBalancerName string `pulumi:"loadBalancerName"`
}

// The set of arguments for constructing a LoadBalancerTlsCertificate resource.
type LoadBalancerTlsCertificateArgs struct {
	// An array of strings listing alternative domains and subdomains for your SSL/TLS certificate.
	CertificateAlternativeNames pulumi.StringArrayInput
	// The domain name (e.g., example.com ) for your SSL/TLS certificate.
	CertificateDomainName pulumi.StringInput
	// The SSL/TLS certificate name.
	CertificateName pulumi.StringInput
	// A Boolean value that indicates whether HTTPS redirection is enabled for the load balancer.
	HttpsRedirectionEnabled pulumi.BoolPtrInput
	// When true, the SSL/TLS certificate is attached to the Lightsail load balancer.
	IsAttached pulumi.BoolPtrInput
	// The name of your load balancer.
	LoadBalancerName pulumi.StringInput
}

func (LoadBalancerTlsCertificateArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*loadBalancerTlsCertificateArgs)(nil)).Elem()
}

type LoadBalancerTlsCertificateInput interface {
	pulumi.Input

	ToLoadBalancerTlsCertificateOutput() LoadBalancerTlsCertificateOutput
	ToLoadBalancerTlsCertificateOutputWithContext(ctx context.Context) LoadBalancerTlsCertificateOutput
}

func (*LoadBalancerTlsCertificate) ElementType() reflect.Type {
	return reflect.TypeOf((**LoadBalancerTlsCertificate)(nil)).Elem()
}

func (i *LoadBalancerTlsCertificate) ToLoadBalancerTlsCertificateOutput() LoadBalancerTlsCertificateOutput {
	return i.ToLoadBalancerTlsCertificateOutputWithContext(context.Background())
}

func (i *LoadBalancerTlsCertificate) ToLoadBalancerTlsCertificateOutputWithContext(ctx context.Context) LoadBalancerTlsCertificateOutput {
	return pulumi.ToOutputWithContext(ctx, i).(LoadBalancerTlsCertificateOutput)
}

type LoadBalancerTlsCertificateOutput struct{ *pulumi.OutputState }

func (LoadBalancerTlsCertificateOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**LoadBalancerTlsCertificate)(nil)).Elem()
}

func (o LoadBalancerTlsCertificateOutput) ToLoadBalancerTlsCertificateOutput() LoadBalancerTlsCertificateOutput {
	return o
}

func (o LoadBalancerTlsCertificateOutput) ToLoadBalancerTlsCertificateOutputWithContext(ctx context.Context) LoadBalancerTlsCertificateOutput {
	return o
}

// An array of strings listing alternative domains and subdomains for your SSL/TLS certificate.
func (o LoadBalancerTlsCertificateOutput) CertificateAlternativeNames() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *LoadBalancerTlsCertificate) pulumi.StringArrayOutput { return v.CertificateAlternativeNames }).(pulumi.StringArrayOutput)
}

// The domain name (e.g., example.com ) for your SSL/TLS certificate.
func (o LoadBalancerTlsCertificateOutput) CertificateDomainName() pulumi.StringOutput {
	return o.ApplyT(func(v *LoadBalancerTlsCertificate) pulumi.StringOutput { return v.CertificateDomainName }).(pulumi.StringOutput)
}

// The SSL/TLS certificate name.
func (o LoadBalancerTlsCertificateOutput) CertificateName() pulumi.StringOutput {
	return o.ApplyT(func(v *LoadBalancerTlsCertificate) pulumi.StringOutput { return v.CertificateName }).(pulumi.StringOutput)
}

// A Boolean value that indicates whether HTTPS redirection is enabled for the load balancer.
func (o LoadBalancerTlsCertificateOutput) HttpsRedirectionEnabled() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *LoadBalancerTlsCertificate) pulumi.BoolPtrOutput { return v.HttpsRedirectionEnabled }).(pulumi.BoolPtrOutput)
}

// When true, the SSL/TLS certificate is attached to the Lightsail load balancer.
func (o LoadBalancerTlsCertificateOutput) IsAttached() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *LoadBalancerTlsCertificate) pulumi.BoolPtrOutput { return v.IsAttached }).(pulumi.BoolPtrOutput)
}

// The name of your load balancer.
func (o LoadBalancerTlsCertificateOutput) LoadBalancerName() pulumi.StringOutput {
	return o.ApplyT(func(v *LoadBalancerTlsCertificate) pulumi.StringOutput { return v.LoadBalancerName }).(pulumi.StringOutput)
}

func (o LoadBalancerTlsCertificateOutput) LoadBalancerTlsCertificateArn() pulumi.StringOutput {
	return o.ApplyT(func(v *LoadBalancerTlsCertificate) pulumi.StringOutput { return v.LoadBalancerTlsCertificateArn }).(pulumi.StringOutput)
}

// The validation status of the SSL/TLS certificate.
func (o LoadBalancerTlsCertificateOutput) Status() pulumi.StringOutput {
	return o.ApplyT(func(v *LoadBalancerTlsCertificate) pulumi.StringOutput { return v.Status }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*LoadBalancerTlsCertificateInput)(nil)).Elem(), &LoadBalancerTlsCertificate{})
	pulumi.RegisterOutputType(LoadBalancerTlsCertificateOutput{})
}

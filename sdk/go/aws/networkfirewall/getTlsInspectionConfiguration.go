// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package networkfirewall

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource type definition for AWS::NetworkFirewall::TLSInspectionConfiguration
func LookupTlsInspectionConfiguration(ctx *pulumi.Context, args *LookupTlsInspectionConfigurationArgs, opts ...pulumi.InvokeOption) (*LookupTlsInspectionConfigurationResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupTlsInspectionConfigurationResult
	err := ctx.Invoke("aws-native:networkfirewall:getTlsInspectionConfiguration", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupTlsInspectionConfigurationArgs struct {
	TlsInspectionConfigurationArn string `pulumi:"tlsInspectionConfigurationArn"`
}

type LookupTlsInspectionConfigurationResult struct {
	Description                   *string                                               `pulumi:"description"`
	Tags                          []TlsInspectionConfigurationTag                       `pulumi:"tags"`
	TlsInspectionConfiguration    *TlsInspectionConfigurationTlsInspectionConfiguration `pulumi:"tlsInspectionConfiguration"`
	TlsInspectionConfigurationArn *string                                               `pulumi:"tlsInspectionConfigurationArn"`
	TlsInspectionConfigurationId  *string                                               `pulumi:"tlsInspectionConfigurationId"`
}

func LookupTlsInspectionConfigurationOutput(ctx *pulumi.Context, args LookupTlsInspectionConfigurationOutputArgs, opts ...pulumi.InvokeOption) LookupTlsInspectionConfigurationResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupTlsInspectionConfigurationResult, error) {
			args := v.(LookupTlsInspectionConfigurationArgs)
			r, err := LookupTlsInspectionConfiguration(ctx, &args, opts...)
			var s LookupTlsInspectionConfigurationResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupTlsInspectionConfigurationResultOutput)
}

type LookupTlsInspectionConfigurationOutputArgs struct {
	TlsInspectionConfigurationArn pulumi.StringInput `pulumi:"tlsInspectionConfigurationArn"`
}

func (LookupTlsInspectionConfigurationOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupTlsInspectionConfigurationArgs)(nil)).Elem()
}

type LookupTlsInspectionConfigurationResultOutput struct{ *pulumi.OutputState }

func (LookupTlsInspectionConfigurationResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupTlsInspectionConfigurationResult)(nil)).Elem()
}

func (o LookupTlsInspectionConfigurationResultOutput) ToLookupTlsInspectionConfigurationResultOutput() LookupTlsInspectionConfigurationResultOutput {
	return o
}

func (o LookupTlsInspectionConfigurationResultOutput) ToLookupTlsInspectionConfigurationResultOutputWithContext(ctx context.Context) LookupTlsInspectionConfigurationResultOutput {
	return o
}

func (o LookupTlsInspectionConfigurationResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupTlsInspectionConfigurationResult] {
	return pulumix.Output[LookupTlsInspectionConfigurationResult]{
		OutputState: o.OutputState,
	}
}

func (o LookupTlsInspectionConfigurationResultOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupTlsInspectionConfigurationResult) *string { return v.Description }).(pulumi.StringPtrOutput)
}

func (o LookupTlsInspectionConfigurationResultOutput) Tags() TlsInspectionConfigurationTagArrayOutput {
	return o.ApplyT(func(v LookupTlsInspectionConfigurationResult) []TlsInspectionConfigurationTag { return v.Tags }).(TlsInspectionConfigurationTagArrayOutput)
}

func (o LookupTlsInspectionConfigurationResultOutput) TlsInspectionConfiguration() TlsInspectionConfigurationTlsInspectionConfigurationPtrOutput {
	return o.ApplyT(func(v LookupTlsInspectionConfigurationResult) *TlsInspectionConfigurationTlsInspectionConfiguration {
		return v.TlsInspectionConfiguration
	}).(TlsInspectionConfigurationTlsInspectionConfigurationPtrOutput)
}

func (o LookupTlsInspectionConfigurationResultOutput) TlsInspectionConfigurationArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupTlsInspectionConfigurationResult) *string { return v.TlsInspectionConfigurationArn }).(pulumi.StringPtrOutput)
}

func (o LookupTlsInspectionConfigurationResultOutput) TlsInspectionConfigurationId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupTlsInspectionConfigurationResult) *string { return v.TlsInspectionConfigurationId }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupTlsInspectionConfigurationResultOutput{})
}

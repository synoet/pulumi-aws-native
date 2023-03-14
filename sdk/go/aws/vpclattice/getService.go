// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package vpclattice

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// A logical unit that is exposed to one or more Mercury networks containing a unique FQDN, a set of routing names, TLS certificates, and routing policies
func LookupService(ctx *pulumi.Context, args *LookupServiceArgs, opts ...pulumi.InvokeOption) (*LookupServiceResult, error) {
	var rv LookupServiceResult
	err := ctx.Invoke("aws-native:vpclattice:getService", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupServiceArgs struct {
	Arn string `pulumi:"arn"`
}

type LookupServiceResult struct {
	Arn            *string          `pulumi:"arn"`
	AuthType       *ServiceAuthType `pulumi:"authType"`
	CertificateArn *string          `pulumi:"certificateArn"`
	CreatedAt      *string          `pulumi:"createdAt"`
	DnsEntry       *ServiceDnsEntry `pulumi:"dnsEntry"`
	Id             *string          `pulumi:"id"`
	LastUpdatedAt  *string          `pulumi:"lastUpdatedAt"`
	Status         *ServiceStatus   `pulumi:"status"`
	Tags           []ServiceTag     `pulumi:"tags"`
}

func LookupServiceOutput(ctx *pulumi.Context, args LookupServiceOutputArgs, opts ...pulumi.InvokeOption) LookupServiceResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupServiceResult, error) {
			args := v.(LookupServiceArgs)
			r, err := LookupService(ctx, &args, opts...)
			var s LookupServiceResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupServiceResultOutput)
}

type LookupServiceOutputArgs struct {
	Arn pulumi.StringInput `pulumi:"arn"`
}

func (LookupServiceOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupServiceArgs)(nil)).Elem()
}

type LookupServiceResultOutput struct{ *pulumi.OutputState }

func (LookupServiceResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupServiceResult)(nil)).Elem()
}

func (o LookupServiceResultOutput) ToLookupServiceResultOutput() LookupServiceResultOutput {
	return o
}

func (o LookupServiceResultOutput) ToLookupServiceResultOutputWithContext(ctx context.Context) LookupServiceResultOutput {
	return o
}

func (o LookupServiceResultOutput) Arn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupServiceResult) *string { return v.Arn }).(pulumi.StringPtrOutput)
}

func (o LookupServiceResultOutput) AuthType() ServiceAuthTypePtrOutput {
	return o.ApplyT(func(v LookupServiceResult) *ServiceAuthType { return v.AuthType }).(ServiceAuthTypePtrOutput)
}

func (o LookupServiceResultOutput) CertificateArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupServiceResult) *string { return v.CertificateArn }).(pulumi.StringPtrOutput)
}

func (o LookupServiceResultOutput) CreatedAt() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupServiceResult) *string { return v.CreatedAt }).(pulumi.StringPtrOutput)
}

func (o LookupServiceResultOutput) DnsEntry() ServiceDnsEntryPtrOutput {
	return o.ApplyT(func(v LookupServiceResult) *ServiceDnsEntry { return v.DnsEntry }).(ServiceDnsEntryPtrOutput)
}

func (o LookupServiceResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupServiceResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

func (o LookupServiceResultOutput) LastUpdatedAt() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupServiceResult) *string { return v.LastUpdatedAt }).(pulumi.StringPtrOutput)
}

func (o LookupServiceResultOutput) Status() ServiceStatusPtrOutput {
	return o.ApplyT(func(v LookupServiceResult) *ServiceStatus { return v.Status }).(ServiceStatusPtrOutput)
}

func (o LookupServiceResultOutput) Tags() ServiceTagArrayOutput {
	return o.ApplyT(func(v LookupServiceResult) []ServiceTag { return v.Tags }).(ServiceTagArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupServiceResultOutput{})
}

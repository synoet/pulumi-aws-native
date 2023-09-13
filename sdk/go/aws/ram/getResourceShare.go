// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ram

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::RAM::ResourceShare
func LookupResourceShare(ctx *pulumi.Context, args *LookupResourceShareArgs, opts ...pulumi.InvokeOption) (*LookupResourceShareResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupResourceShareResult
	err := ctx.Invoke("aws-native:ram:getResourceShare", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupResourceShareArgs struct {
	Id string `pulumi:"id"`
}

type LookupResourceShareResult struct {
	AllowExternalPrincipals *bool              `pulumi:"allowExternalPrincipals"`
	Arn                     *string            `pulumi:"arn"`
	Id                      *string            `pulumi:"id"`
	Name                    *string            `pulumi:"name"`
	PermissionArns          []string           `pulumi:"permissionArns"`
	Principals              []string           `pulumi:"principals"`
	ResourceArns            []string           `pulumi:"resourceArns"`
	Sources                 []string           `pulumi:"sources"`
	Tags                    []ResourceShareTag `pulumi:"tags"`
}

func LookupResourceShareOutput(ctx *pulumi.Context, args LookupResourceShareOutputArgs, opts ...pulumi.InvokeOption) LookupResourceShareResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupResourceShareResult, error) {
			args := v.(LookupResourceShareArgs)
			r, err := LookupResourceShare(ctx, &args, opts...)
			var s LookupResourceShareResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupResourceShareResultOutput)
}

type LookupResourceShareOutputArgs struct {
	Id pulumi.StringInput `pulumi:"id"`
}

func (LookupResourceShareOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupResourceShareArgs)(nil)).Elem()
}

type LookupResourceShareResultOutput struct{ *pulumi.OutputState }

func (LookupResourceShareResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupResourceShareResult)(nil)).Elem()
}

func (o LookupResourceShareResultOutput) ToLookupResourceShareResultOutput() LookupResourceShareResultOutput {
	return o
}

func (o LookupResourceShareResultOutput) ToLookupResourceShareResultOutputWithContext(ctx context.Context) LookupResourceShareResultOutput {
	return o
}

func (o LookupResourceShareResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupResourceShareResult] {
	return pulumix.Output[LookupResourceShareResult]{
		OutputState: o.OutputState,
	}
}

func (o LookupResourceShareResultOutput) AllowExternalPrincipals() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupResourceShareResult) *bool { return v.AllowExternalPrincipals }).(pulumi.BoolPtrOutput)
}

func (o LookupResourceShareResultOutput) Arn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupResourceShareResult) *string { return v.Arn }).(pulumi.StringPtrOutput)
}

func (o LookupResourceShareResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupResourceShareResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

func (o LookupResourceShareResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupResourceShareResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

func (o LookupResourceShareResultOutput) PermissionArns() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupResourceShareResult) []string { return v.PermissionArns }).(pulumi.StringArrayOutput)
}

func (o LookupResourceShareResultOutput) Principals() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupResourceShareResult) []string { return v.Principals }).(pulumi.StringArrayOutput)
}

func (o LookupResourceShareResultOutput) ResourceArns() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupResourceShareResult) []string { return v.ResourceArns }).(pulumi.StringArrayOutput)
}

func (o LookupResourceShareResultOutput) Sources() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupResourceShareResult) []string { return v.Sources }).(pulumi.StringArrayOutput)
}

func (o LookupResourceShareResultOutput) Tags() ResourceShareTagArrayOutput {
	return o.ApplyT(func(v LookupResourceShareResult) []ResourceShareTag { return v.Tags }).(ResourceShareTagArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupResourceShareResultOutput{})
}

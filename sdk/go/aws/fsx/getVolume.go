// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package fsx

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::FSx::Volume
func LookupVolume(ctx *pulumi.Context, args *LookupVolumeArgs, opts ...pulumi.InvokeOption) (*LookupVolumeResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupVolumeResult
	err := ctx.Invoke("aws-native:fsx:getVolume", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupVolumeArgs struct {
	VolumeId string `pulumi:"volumeId"`
}

type LookupVolumeResult struct {
	Name                 *string                     `pulumi:"name"`
	OntapConfiguration   *VolumeOntapConfiguration   `pulumi:"ontapConfiguration"`
	OpenZfsConfiguration *VolumeOpenZFSConfiguration `pulumi:"openZfsConfiguration"`
	ResourceArn          *string                     `pulumi:"resourceArn"`
	Tags                 []VolumeTag                 `pulumi:"tags"`
	Uuid                 *string                     `pulumi:"uuid"`
	VolumeId             *string                     `pulumi:"volumeId"`
}

func LookupVolumeOutput(ctx *pulumi.Context, args LookupVolumeOutputArgs, opts ...pulumi.InvokeOption) LookupVolumeResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupVolumeResult, error) {
			args := v.(LookupVolumeArgs)
			r, err := LookupVolume(ctx, &args, opts...)
			var s LookupVolumeResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupVolumeResultOutput)
}

type LookupVolumeOutputArgs struct {
	VolumeId pulumi.StringInput `pulumi:"volumeId"`
}

func (LookupVolumeOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupVolumeArgs)(nil)).Elem()
}

type LookupVolumeResultOutput struct{ *pulumi.OutputState }

func (LookupVolumeResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupVolumeResult)(nil)).Elem()
}

func (o LookupVolumeResultOutput) ToLookupVolumeResultOutput() LookupVolumeResultOutput {
	return o
}

func (o LookupVolumeResultOutput) ToLookupVolumeResultOutputWithContext(ctx context.Context) LookupVolumeResultOutput {
	return o
}

func (o LookupVolumeResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupVolumeResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

func (o LookupVolumeResultOutput) OntapConfiguration() VolumeOntapConfigurationPtrOutput {
	return o.ApplyT(func(v LookupVolumeResult) *VolumeOntapConfiguration { return v.OntapConfiguration }).(VolumeOntapConfigurationPtrOutput)
}

func (o LookupVolumeResultOutput) OpenZfsConfiguration() VolumeOpenZFSConfigurationPtrOutput {
	return o.ApplyT(func(v LookupVolumeResult) *VolumeOpenZFSConfiguration { return v.OpenZfsConfiguration }).(VolumeOpenZFSConfigurationPtrOutput)
}

func (o LookupVolumeResultOutput) ResourceArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupVolumeResult) *string { return v.ResourceArn }).(pulumi.StringPtrOutput)
}

func (o LookupVolumeResultOutput) Tags() VolumeTagArrayOutput {
	return o.ApplyT(func(v LookupVolumeResult) []VolumeTag { return v.Tags }).(VolumeTagArrayOutput)
}

func (o LookupVolumeResultOutput) Uuid() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupVolumeResult) *string { return v.Uuid }).(pulumi.StringPtrOutput)
}

func (o LookupVolumeResultOutput) VolumeId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupVolumeResult) *string { return v.VolumeId }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupVolumeResultOutput{})
}

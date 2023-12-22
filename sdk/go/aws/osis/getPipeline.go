// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package osis

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// An OpenSearch Ingestion Service Data Prepper pipeline running Data Prepper.
func LookupPipeline(ctx *pulumi.Context, args *LookupPipelineArgs, opts ...pulumi.InvokeOption) (*LookupPipelineResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupPipelineResult
	err := ctx.Invoke("aws-native:osis:getPipeline", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupPipelineArgs struct {
	// The Amazon Resource Name (ARN) of the pipeline.
	PipelineArn string `pulumi:"pipelineArn"`
}

type LookupPipelineResult struct {
	BufferOptions           *PipelineBufferOptions           `pulumi:"bufferOptions"`
	EncryptionAtRestOptions *PipelineEncryptionAtRestOptions `pulumi:"encryptionAtRestOptions"`
	// A list of endpoints that can be used for ingesting data into a pipeline
	IngestEndpointUrls   []string                      `pulumi:"ingestEndpointUrls"`
	LogPublishingOptions *PipelineLogPublishingOptions `pulumi:"logPublishingOptions"`
	// The maximum pipeline capacity, in Ingestion Compute Units (ICUs).
	MaxUnits *int `pulumi:"maxUnits"`
	// The minimum pipeline capacity, in Ingestion Compute Units (ICUs).
	MinUnits *int `pulumi:"minUnits"`
	// The Amazon Resource Name (ARN) of the pipeline.
	PipelineArn *string `pulumi:"pipelineArn"`
	// The Data Prepper pipeline configuration in YAML format.
	PipelineConfigurationBody *string `pulumi:"pipelineConfigurationBody"`
	// An array of key-value pairs to apply to this resource.
	Tags []PipelineTag `pulumi:"tags"`
	// The VPC interface endpoints that have access to the pipeline.
	VpcEndpoints []PipelineVpcEndpoint `pulumi:"vpcEndpoints"`
}

func LookupPipelineOutput(ctx *pulumi.Context, args LookupPipelineOutputArgs, opts ...pulumi.InvokeOption) LookupPipelineResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupPipelineResult, error) {
			args := v.(LookupPipelineArgs)
			r, err := LookupPipeline(ctx, &args, opts...)
			var s LookupPipelineResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupPipelineResultOutput)
}

type LookupPipelineOutputArgs struct {
	// The Amazon Resource Name (ARN) of the pipeline.
	PipelineArn pulumi.StringInput `pulumi:"pipelineArn"`
}

func (LookupPipelineOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupPipelineArgs)(nil)).Elem()
}

type LookupPipelineResultOutput struct{ *pulumi.OutputState }

func (LookupPipelineResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupPipelineResult)(nil)).Elem()
}

func (o LookupPipelineResultOutput) ToLookupPipelineResultOutput() LookupPipelineResultOutput {
	return o
}

func (o LookupPipelineResultOutput) ToLookupPipelineResultOutputWithContext(ctx context.Context) LookupPipelineResultOutput {
	return o
}

func (o LookupPipelineResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupPipelineResult] {
	return pulumix.Output[LookupPipelineResult]{
		OutputState: o.OutputState,
	}
}

func (o LookupPipelineResultOutput) BufferOptions() PipelineBufferOptionsPtrOutput {
	return o.ApplyT(func(v LookupPipelineResult) *PipelineBufferOptions { return v.BufferOptions }).(PipelineBufferOptionsPtrOutput)
}

func (o LookupPipelineResultOutput) EncryptionAtRestOptions() PipelineEncryptionAtRestOptionsPtrOutput {
	return o.ApplyT(func(v LookupPipelineResult) *PipelineEncryptionAtRestOptions { return v.EncryptionAtRestOptions }).(PipelineEncryptionAtRestOptionsPtrOutput)
}

// A list of endpoints that can be used for ingesting data into a pipeline
func (o LookupPipelineResultOutput) IngestEndpointUrls() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupPipelineResult) []string { return v.IngestEndpointUrls }).(pulumi.StringArrayOutput)
}

func (o LookupPipelineResultOutput) LogPublishingOptions() PipelineLogPublishingOptionsPtrOutput {
	return o.ApplyT(func(v LookupPipelineResult) *PipelineLogPublishingOptions { return v.LogPublishingOptions }).(PipelineLogPublishingOptionsPtrOutput)
}

// The maximum pipeline capacity, in Ingestion Compute Units (ICUs).
func (o LookupPipelineResultOutput) MaxUnits() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupPipelineResult) *int { return v.MaxUnits }).(pulumi.IntPtrOutput)
}

// The minimum pipeline capacity, in Ingestion Compute Units (ICUs).
func (o LookupPipelineResultOutput) MinUnits() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupPipelineResult) *int { return v.MinUnits }).(pulumi.IntPtrOutput)
}

// The Amazon Resource Name (ARN) of the pipeline.
func (o LookupPipelineResultOutput) PipelineArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupPipelineResult) *string { return v.PipelineArn }).(pulumi.StringPtrOutput)
}

// The Data Prepper pipeline configuration in YAML format.
func (o LookupPipelineResultOutput) PipelineConfigurationBody() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupPipelineResult) *string { return v.PipelineConfigurationBody }).(pulumi.StringPtrOutput)
}

// An array of key-value pairs to apply to this resource.
func (o LookupPipelineResultOutput) Tags() PipelineTagArrayOutput {
	return o.ApplyT(func(v LookupPipelineResult) []PipelineTag { return v.Tags }).(PipelineTagArrayOutput)
}

// The VPC interface endpoints that have access to the pipeline.
func (o LookupPipelineResultOutput) VpcEndpoints() PipelineVpcEndpointArrayOutput {
	return o.ApplyT(func(v LookupPipelineResult) []PipelineVpcEndpoint { return v.VpcEndpoints }).(PipelineVpcEndpointArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupPipelineResultOutput{})
}

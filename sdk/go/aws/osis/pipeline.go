// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package osis

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// An OpenSearch Ingestion Service Data Prepper pipeline running Data Prepper.
type Pipeline struct {
	pulumi.CustomResourceState

	BufferOptions           PipelineBufferOptionsPtrOutput           `pulumi:"bufferOptions"`
	EncryptionAtRestOptions PipelineEncryptionAtRestOptionsPtrOutput `pulumi:"encryptionAtRestOptions"`
	// A list of endpoints that can be used for ingesting data into a pipeline
	IngestEndpointUrls   pulumi.StringArrayOutput              `pulumi:"ingestEndpointUrls"`
	LogPublishingOptions PipelineLogPublishingOptionsPtrOutput `pulumi:"logPublishingOptions"`
	// The maximum pipeline capacity, in Ingestion Compute Units (ICUs).
	MaxUnits pulumi.IntOutput `pulumi:"maxUnits"`
	// The minimum pipeline capacity, in Ingestion Compute Units (ICUs).
	MinUnits pulumi.IntOutput `pulumi:"minUnits"`
	// The Amazon Resource Name (ARN) of the pipeline.
	PipelineArn pulumi.StringOutput `pulumi:"pipelineArn"`
	// The Data Prepper pipeline configuration in YAML format.
	PipelineConfigurationBody pulumi.StringOutput `pulumi:"pipelineConfigurationBody"`
	// Name of the OpenSearch Ingestion Service pipeline to create. Pipeline names are unique across the pipelines owned by an account within an AWS Region.
	PipelineName pulumi.StringOutput `pulumi:"pipelineName"`
	// An array of key-value pairs to apply to this resource.
	Tags PipelineTagArrayOutput `pulumi:"tags"`
	// The VPC interface endpoints that have access to the pipeline.
	VpcEndpoints PipelineVpcEndpointArrayOutput `pulumi:"vpcEndpoints"`
	VpcOptions   PipelineVpcOptionsPtrOutput    `pulumi:"vpcOptions"`
}

// NewPipeline registers a new resource with the given unique name, arguments, and options.
func NewPipeline(ctx *pulumi.Context,
	name string, args *PipelineArgs, opts ...pulumi.ResourceOption) (*Pipeline, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.MaxUnits == nil {
		return nil, errors.New("invalid value for required argument 'MaxUnits'")
	}
	if args.MinUnits == nil {
		return nil, errors.New("invalid value for required argument 'MinUnits'")
	}
	if args.PipelineConfigurationBody == nil {
		return nil, errors.New("invalid value for required argument 'PipelineConfigurationBody'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"pipelineName",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Pipeline
	err := ctx.RegisterResource("aws-native:osis:Pipeline", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetPipeline gets an existing Pipeline resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetPipeline(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *PipelineState, opts ...pulumi.ResourceOption) (*Pipeline, error) {
	var resource Pipeline
	err := ctx.ReadResource("aws-native:osis:Pipeline", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Pipeline resources.
type pipelineState struct {
}

type PipelineState struct {
}

func (PipelineState) ElementType() reflect.Type {
	return reflect.TypeOf((*pipelineState)(nil)).Elem()
}

type pipelineArgs struct {
	BufferOptions           *PipelineBufferOptions           `pulumi:"bufferOptions"`
	EncryptionAtRestOptions *PipelineEncryptionAtRestOptions `pulumi:"encryptionAtRestOptions"`
	LogPublishingOptions    *PipelineLogPublishingOptions    `pulumi:"logPublishingOptions"`
	// The maximum pipeline capacity, in Ingestion Compute Units (ICUs).
	MaxUnits int `pulumi:"maxUnits"`
	// The minimum pipeline capacity, in Ingestion Compute Units (ICUs).
	MinUnits int `pulumi:"minUnits"`
	// The Data Prepper pipeline configuration in YAML format.
	PipelineConfigurationBody string `pulumi:"pipelineConfigurationBody"`
	// Name of the OpenSearch Ingestion Service pipeline to create. Pipeline names are unique across the pipelines owned by an account within an AWS Region.
	PipelineName *string `pulumi:"pipelineName"`
	// An array of key-value pairs to apply to this resource.
	Tags       []PipelineTag       `pulumi:"tags"`
	VpcOptions *PipelineVpcOptions `pulumi:"vpcOptions"`
}

// The set of arguments for constructing a Pipeline resource.
type PipelineArgs struct {
	BufferOptions           PipelineBufferOptionsPtrInput
	EncryptionAtRestOptions PipelineEncryptionAtRestOptionsPtrInput
	LogPublishingOptions    PipelineLogPublishingOptionsPtrInput
	// The maximum pipeline capacity, in Ingestion Compute Units (ICUs).
	MaxUnits pulumi.IntInput
	// The minimum pipeline capacity, in Ingestion Compute Units (ICUs).
	MinUnits pulumi.IntInput
	// The Data Prepper pipeline configuration in YAML format.
	PipelineConfigurationBody pulumi.StringInput
	// Name of the OpenSearch Ingestion Service pipeline to create. Pipeline names are unique across the pipelines owned by an account within an AWS Region.
	PipelineName pulumi.StringPtrInput
	// An array of key-value pairs to apply to this resource.
	Tags       PipelineTagArrayInput
	VpcOptions PipelineVpcOptionsPtrInput
}

func (PipelineArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*pipelineArgs)(nil)).Elem()
}

type PipelineInput interface {
	pulumi.Input

	ToPipelineOutput() PipelineOutput
	ToPipelineOutputWithContext(ctx context.Context) PipelineOutput
}

func (*Pipeline) ElementType() reflect.Type {
	return reflect.TypeOf((**Pipeline)(nil)).Elem()
}

func (i *Pipeline) ToPipelineOutput() PipelineOutput {
	return i.ToPipelineOutputWithContext(context.Background())
}

func (i *Pipeline) ToPipelineOutputWithContext(ctx context.Context) PipelineOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PipelineOutput)
}

func (i *Pipeline) ToOutput(ctx context.Context) pulumix.Output[*Pipeline] {
	return pulumix.Output[*Pipeline]{
		OutputState: i.ToPipelineOutputWithContext(ctx).OutputState,
	}
}

type PipelineOutput struct{ *pulumi.OutputState }

func (PipelineOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Pipeline)(nil)).Elem()
}

func (o PipelineOutput) ToPipelineOutput() PipelineOutput {
	return o
}

func (o PipelineOutput) ToPipelineOutputWithContext(ctx context.Context) PipelineOutput {
	return o
}

func (o PipelineOutput) ToOutput(ctx context.Context) pulumix.Output[*Pipeline] {
	return pulumix.Output[*Pipeline]{
		OutputState: o.OutputState,
	}
}

func (o PipelineOutput) BufferOptions() PipelineBufferOptionsPtrOutput {
	return o.ApplyT(func(v *Pipeline) PipelineBufferOptionsPtrOutput { return v.BufferOptions }).(PipelineBufferOptionsPtrOutput)
}

func (o PipelineOutput) EncryptionAtRestOptions() PipelineEncryptionAtRestOptionsPtrOutput {
	return o.ApplyT(func(v *Pipeline) PipelineEncryptionAtRestOptionsPtrOutput { return v.EncryptionAtRestOptions }).(PipelineEncryptionAtRestOptionsPtrOutput)
}

// A list of endpoints that can be used for ingesting data into a pipeline
func (o PipelineOutput) IngestEndpointUrls() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *Pipeline) pulumi.StringArrayOutput { return v.IngestEndpointUrls }).(pulumi.StringArrayOutput)
}

func (o PipelineOutput) LogPublishingOptions() PipelineLogPublishingOptionsPtrOutput {
	return o.ApplyT(func(v *Pipeline) PipelineLogPublishingOptionsPtrOutput { return v.LogPublishingOptions }).(PipelineLogPublishingOptionsPtrOutput)
}

// The maximum pipeline capacity, in Ingestion Compute Units (ICUs).
func (o PipelineOutput) MaxUnits() pulumi.IntOutput {
	return o.ApplyT(func(v *Pipeline) pulumi.IntOutput { return v.MaxUnits }).(pulumi.IntOutput)
}

// The minimum pipeline capacity, in Ingestion Compute Units (ICUs).
func (o PipelineOutput) MinUnits() pulumi.IntOutput {
	return o.ApplyT(func(v *Pipeline) pulumi.IntOutput { return v.MinUnits }).(pulumi.IntOutput)
}

// The Amazon Resource Name (ARN) of the pipeline.
func (o PipelineOutput) PipelineArn() pulumi.StringOutput {
	return o.ApplyT(func(v *Pipeline) pulumi.StringOutput { return v.PipelineArn }).(pulumi.StringOutput)
}

// The Data Prepper pipeline configuration in YAML format.
func (o PipelineOutput) PipelineConfigurationBody() pulumi.StringOutput {
	return o.ApplyT(func(v *Pipeline) pulumi.StringOutput { return v.PipelineConfigurationBody }).(pulumi.StringOutput)
}

// Name of the OpenSearch Ingestion Service pipeline to create. Pipeline names are unique across the pipelines owned by an account within an AWS Region.
func (o PipelineOutput) PipelineName() pulumi.StringOutput {
	return o.ApplyT(func(v *Pipeline) pulumi.StringOutput { return v.PipelineName }).(pulumi.StringOutput)
}

// An array of key-value pairs to apply to this resource.
func (o PipelineOutput) Tags() PipelineTagArrayOutput {
	return o.ApplyT(func(v *Pipeline) PipelineTagArrayOutput { return v.Tags }).(PipelineTagArrayOutput)
}

// The VPC interface endpoints that have access to the pipeline.
func (o PipelineOutput) VpcEndpoints() PipelineVpcEndpointArrayOutput {
	return o.ApplyT(func(v *Pipeline) PipelineVpcEndpointArrayOutput { return v.VpcEndpoints }).(PipelineVpcEndpointArrayOutput)
}

func (o PipelineOutput) VpcOptions() PipelineVpcOptionsPtrOutput {
	return o.ApplyT(func(v *Pipeline) PipelineVpcOptionsPtrOutput { return v.VpcOptions }).(PipelineVpcOptionsPtrOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*PipelineInput)(nil)).Elem(), &Pipeline{})
	pulumi.RegisterOutputType(PipelineOutput{})
}

// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ec2

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::EC2::TrafficMirrorFilter
//
// Deprecated: TrafficMirrorFilter is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
type TrafficMirrorFilter struct {
	pulumi.CustomResourceState

	Description     pulumi.StringPtrOutput            `pulumi:"description"`
	NetworkServices pulumi.StringArrayOutput          `pulumi:"networkServices"`
	Tags            TrafficMirrorFilterTagArrayOutput `pulumi:"tags"`
}

// NewTrafficMirrorFilter registers a new resource with the given unique name, arguments, and options.
func NewTrafficMirrorFilter(ctx *pulumi.Context,
	name string, args *TrafficMirrorFilterArgs, opts ...pulumi.ResourceOption) (*TrafficMirrorFilter, error) {
	if args == nil {
		args = &TrafficMirrorFilterArgs{}
	}

	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"description",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource TrafficMirrorFilter
	err := ctx.RegisterResource("aws-native:ec2:TrafficMirrorFilter", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetTrafficMirrorFilter gets an existing TrafficMirrorFilter resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetTrafficMirrorFilter(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *TrafficMirrorFilterState, opts ...pulumi.ResourceOption) (*TrafficMirrorFilter, error) {
	var resource TrafficMirrorFilter
	err := ctx.ReadResource("aws-native:ec2:TrafficMirrorFilter", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering TrafficMirrorFilter resources.
type trafficMirrorFilterState struct {
}

type TrafficMirrorFilterState struct {
}

func (TrafficMirrorFilterState) ElementType() reflect.Type {
	return reflect.TypeOf((*trafficMirrorFilterState)(nil)).Elem()
}

type trafficMirrorFilterArgs struct {
	Description     *string                  `pulumi:"description"`
	NetworkServices []string                 `pulumi:"networkServices"`
	Tags            []TrafficMirrorFilterTag `pulumi:"tags"`
}

// The set of arguments for constructing a TrafficMirrorFilter resource.
type TrafficMirrorFilterArgs struct {
	Description     pulumi.StringPtrInput
	NetworkServices pulumi.StringArrayInput
	Tags            TrafficMirrorFilterTagArrayInput
}

func (TrafficMirrorFilterArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*trafficMirrorFilterArgs)(nil)).Elem()
}

type TrafficMirrorFilterInput interface {
	pulumi.Input

	ToTrafficMirrorFilterOutput() TrafficMirrorFilterOutput
	ToTrafficMirrorFilterOutputWithContext(ctx context.Context) TrafficMirrorFilterOutput
}

func (*TrafficMirrorFilter) ElementType() reflect.Type {
	return reflect.TypeOf((**TrafficMirrorFilter)(nil)).Elem()
}

func (i *TrafficMirrorFilter) ToTrafficMirrorFilterOutput() TrafficMirrorFilterOutput {
	return i.ToTrafficMirrorFilterOutputWithContext(context.Background())
}

func (i *TrafficMirrorFilter) ToTrafficMirrorFilterOutputWithContext(ctx context.Context) TrafficMirrorFilterOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TrafficMirrorFilterOutput)
}

type TrafficMirrorFilterOutput struct{ *pulumi.OutputState }

func (TrafficMirrorFilterOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**TrafficMirrorFilter)(nil)).Elem()
}

func (o TrafficMirrorFilterOutput) ToTrafficMirrorFilterOutput() TrafficMirrorFilterOutput {
	return o
}

func (o TrafficMirrorFilterOutput) ToTrafficMirrorFilterOutputWithContext(ctx context.Context) TrafficMirrorFilterOutput {
	return o
}

func (o TrafficMirrorFilterOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *TrafficMirrorFilter) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

func (o TrafficMirrorFilterOutput) NetworkServices() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *TrafficMirrorFilter) pulumi.StringArrayOutput { return v.NetworkServices }).(pulumi.StringArrayOutput)
}

func (o TrafficMirrorFilterOutput) Tags() TrafficMirrorFilterTagArrayOutput {
	return o.ApplyT(func(v *TrafficMirrorFilter) TrafficMirrorFilterTagArrayOutput { return v.Tags }).(TrafficMirrorFilterTagArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*TrafficMirrorFilterInput)(nil)).Elem(), &TrafficMirrorFilter{})
	pulumi.RegisterOutputType(TrafficMirrorFilterOutput{})
}

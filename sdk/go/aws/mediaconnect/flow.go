// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package mediaconnect

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource schema for AWS::MediaConnect::Flow
type Flow struct {
	pulumi.CustomResourceState

	// The Availability Zone that you want to create the flow in. These options are limited to the Availability Zones within the current AWS.
	AvailabilityZone pulumi.StringPtrOutput `pulumi:"availabilityZone"`
	// The Amazon Resource Name (ARN), a unique identifier for any AWS resource, of the flow.
	FlowArn pulumi.StringOutput `pulumi:"flowArn"`
	// The Availability Zone that you want to create the flow in. These options are limited to the Availability Zones within the current AWS.(ReadOnly)
	FlowAvailabilityZone pulumi.StringOutput `pulumi:"flowAvailabilityZone"`
	// The name of the flow.
	Name pulumi.StringOutput `pulumi:"name"`
	// The source of the flow.
	Source FlowSourceTypeOutput `pulumi:"source"`
	// The source failover config of the flow.
	SourceFailoverConfig FlowFailoverConfigPtrOutput `pulumi:"sourceFailoverConfig"`
}

// NewFlow registers a new resource with the given unique name, arguments, and options.
func NewFlow(ctx *pulumi.Context,
	name string, args *FlowArgs, opts ...pulumi.ResourceOption) (*Flow, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Source == nil {
		return nil, errors.New("invalid value for required argument 'Source'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"availabilityZone",
		"name",
		"source.name",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Flow
	err := ctx.RegisterResource("aws-native:mediaconnect:Flow", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetFlow gets an existing Flow resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetFlow(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *FlowState, opts ...pulumi.ResourceOption) (*Flow, error) {
	var resource Flow
	err := ctx.ReadResource("aws-native:mediaconnect:Flow", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Flow resources.
type flowState struct {
}

type FlowState struct {
}

func (FlowState) ElementType() reflect.Type {
	return reflect.TypeOf((*flowState)(nil)).Elem()
}

type flowArgs struct {
	// The Availability Zone that you want to create the flow in. These options are limited to the Availability Zones within the current AWS.
	AvailabilityZone *string `pulumi:"availabilityZone"`
	// The name of the flow.
	Name *string `pulumi:"name"`
	// The source of the flow.
	Source FlowSourceType `pulumi:"source"`
	// The source failover config of the flow.
	SourceFailoverConfig *FlowFailoverConfig `pulumi:"sourceFailoverConfig"`
}

// The set of arguments for constructing a Flow resource.
type FlowArgs struct {
	// The Availability Zone that you want to create the flow in. These options are limited to the Availability Zones within the current AWS.
	AvailabilityZone pulumi.StringPtrInput
	// The name of the flow.
	Name pulumi.StringPtrInput
	// The source of the flow.
	Source FlowSourceTypeInput
	// The source failover config of the flow.
	SourceFailoverConfig FlowFailoverConfigPtrInput
}

func (FlowArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*flowArgs)(nil)).Elem()
}

type FlowInput interface {
	pulumi.Input

	ToFlowOutput() FlowOutput
	ToFlowOutputWithContext(ctx context.Context) FlowOutput
}

func (*Flow) ElementType() reflect.Type {
	return reflect.TypeOf((**Flow)(nil)).Elem()
}

func (i *Flow) ToFlowOutput() FlowOutput {
	return i.ToFlowOutputWithContext(context.Background())
}

func (i *Flow) ToFlowOutputWithContext(ctx context.Context) FlowOutput {
	return pulumi.ToOutputWithContext(ctx, i).(FlowOutput)
}

type FlowOutput struct{ *pulumi.OutputState }

func (FlowOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Flow)(nil)).Elem()
}

func (o FlowOutput) ToFlowOutput() FlowOutput {
	return o
}

func (o FlowOutput) ToFlowOutputWithContext(ctx context.Context) FlowOutput {
	return o
}

// The Availability Zone that you want to create the flow in. These options are limited to the Availability Zones within the current AWS.
func (o FlowOutput) AvailabilityZone() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Flow) pulumi.StringPtrOutput { return v.AvailabilityZone }).(pulumi.StringPtrOutput)
}

// The Amazon Resource Name (ARN), a unique identifier for any AWS resource, of the flow.
func (o FlowOutput) FlowArn() pulumi.StringOutput {
	return o.ApplyT(func(v *Flow) pulumi.StringOutput { return v.FlowArn }).(pulumi.StringOutput)
}

// The Availability Zone that you want to create the flow in. These options are limited to the Availability Zones within the current AWS.(ReadOnly)
func (o FlowOutput) FlowAvailabilityZone() pulumi.StringOutput {
	return o.ApplyT(func(v *Flow) pulumi.StringOutput { return v.FlowAvailabilityZone }).(pulumi.StringOutput)
}

// The name of the flow.
func (o FlowOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *Flow) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// The source of the flow.
func (o FlowOutput) Source() FlowSourceTypeOutput {
	return o.ApplyT(func(v *Flow) FlowSourceTypeOutput { return v.Source }).(FlowSourceTypeOutput)
}

// The source failover config of the flow.
func (o FlowOutput) SourceFailoverConfig() FlowFailoverConfigPtrOutput {
	return o.ApplyT(func(v *Flow) FlowFailoverConfigPtrOutput { return v.SourceFailoverConfig }).(FlowFailoverConfigPtrOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*FlowInput)(nil)).Elem(), &Flow{})
	pulumi.RegisterOutputType(FlowOutput{})
}

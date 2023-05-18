// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package frauddetector

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// An label for fraud detector.
type Label struct {
	pulumi.CustomResourceState

	// The label ARN.
	Arn pulumi.StringOutput `pulumi:"arn"`
	// The timestamp when the label was created.
	CreatedTime pulumi.StringOutput `pulumi:"createdTime"`
	// The label description.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// The timestamp when the label was last updated.
	LastUpdatedTime pulumi.StringOutput `pulumi:"lastUpdatedTime"`
	// The name of the label.
	Name pulumi.StringOutput `pulumi:"name"`
	// Tags associated with this label.
	Tags LabelTagArrayOutput `pulumi:"tags"`
}

// NewLabel registers a new resource with the given unique name, arguments, and options.
func NewLabel(ctx *pulumi.Context,
	name string, args *LabelArgs, opts ...pulumi.ResourceOption) (*Label, error) {
	if args == nil {
		args = &LabelArgs{}
	}

	var resource Label
	err := ctx.RegisterResource("aws-native:frauddetector:Label", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetLabel gets an existing Label resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetLabel(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *LabelState, opts ...pulumi.ResourceOption) (*Label, error) {
	var resource Label
	err := ctx.ReadResource("aws-native:frauddetector:Label", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Label resources.
type labelState struct {
}

type LabelState struct {
}

func (LabelState) ElementType() reflect.Type {
	return reflect.TypeOf((*labelState)(nil)).Elem()
}

type labelArgs struct {
	// The label description.
	Description *string `pulumi:"description"`
	// The name of the label.
	Name *string `pulumi:"name"`
	// Tags associated with this label.
	Tags []LabelTag `pulumi:"tags"`
}

// The set of arguments for constructing a Label resource.
type LabelArgs struct {
	// The label description.
	Description pulumi.StringPtrInput
	// The name of the label.
	Name pulumi.StringPtrInput
	// Tags associated with this label.
	Tags LabelTagArrayInput
}

func (LabelArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*labelArgs)(nil)).Elem()
}

type LabelInput interface {
	pulumi.Input

	ToLabelOutput() LabelOutput
	ToLabelOutputWithContext(ctx context.Context) LabelOutput
}

func (*Label) ElementType() reflect.Type {
	return reflect.TypeOf((**Label)(nil)).Elem()
}

func (i *Label) ToLabelOutput() LabelOutput {
	return i.ToLabelOutputWithContext(context.Background())
}

func (i *Label) ToLabelOutputWithContext(ctx context.Context) LabelOutput {
	return pulumi.ToOutputWithContext(ctx, i).(LabelOutput)
}

type LabelOutput struct{ *pulumi.OutputState }

func (LabelOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Label)(nil)).Elem()
}

func (o LabelOutput) ToLabelOutput() LabelOutput {
	return o
}

func (o LabelOutput) ToLabelOutputWithContext(ctx context.Context) LabelOutput {
	return o
}

// The label ARN.
func (o LabelOutput) Arn() pulumi.StringOutput {
	return o.ApplyT(func(v *Label) pulumi.StringOutput { return v.Arn }).(pulumi.StringOutput)
}

// The timestamp when the label was created.
func (o LabelOutput) CreatedTime() pulumi.StringOutput {
	return o.ApplyT(func(v *Label) pulumi.StringOutput { return v.CreatedTime }).(pulumi.StringOutput)
}

// The label description.
func (o LabelOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Label) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

// The timestamp when the label was last updated.
func (o LabelOutput) LastUpdatedTime() pulumi.StringOutput {
	return o.ApplyT(func(v *Label) pulumi.StringOutput { return v.LastUpdatedTime }).(pulumi.StringOutput)
}

// The name of the label.
func (o LabelOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *Label) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// Tags associated with this label.
func (o LabelOutput) Tags() LabelTagArrayOutput {
	return o.ApplyT(func(v *Label) LabelTagArrayOutput { return v.Tags }).(LabelTagArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*LabelInput)(nil)).Elem(), &Label{})
	pulumi.RegisterOutputType(LabelOutput{})
}

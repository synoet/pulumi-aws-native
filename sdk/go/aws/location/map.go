// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package location

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Definition of AWS::Location::Map Resource Type
type Map struct {
	pulumi.CustomResourceState

	Arn           pulumi.StringOutput     `pulumi:"arn"`
	Configuration MapConfigurationOutput  `pulumi:"configuration"`
	CreateTime    pulumi.StringOutput     `pulumi:"createTime"`
	Description   pulumi.StringPtrOutput  `pulumi:"description"`
	MapArn        pulumi.StringOutput     `pulumi:"mapArn"`
	MapName       pulumi.StringOutput     `pulumi:"mapName"`
	PricingPlan   MapPricingPlanPtrOutput `pulumi:"pricingPlan"`
	// An array of key-value pairs to apply to this resource.
	Tags       MapTagArrayOutput   `pulumi:"tags"`
	UpdateTime pulumi.StringOutput `pulumi:"updateTime"`
}

// NewMap registers a new resource with the given unique name, arguments, and options.
func NewMap(ctx *pulumi.Context,
	name string, args *MapArgs, opts ...pulumi.ResourceOption) (*Map, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Configuration == nil {
		return nil, errors.New("invalid value for required argument 'Configuration'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"configuration",
		"mapName",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Map
	err := ctx.RegisterResource("aws-native:location:Map", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetMap gets an existing Map resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetMap(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *MapState, opts ...pulumi.ResourceOption) (*Map, error) {
	var resource Map
	err := ctx.ReadResource("aws-native:location:Map", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Map resources.
type mapState struct {
}

type MapState struct {
}

func (MapState) ElementType() reflect.Type {
	return reflect.TypeOf((*mapState)(nil)).Elem()
}

type mapArgs struct {
	Configuration MapConfiguration `pulumi:"configuration"`
	Description   *string          `pulumi:"description"`
	MapName       *string          `pulumi:"mapName"`
	PricingPlan   *MapPricingPlan  `pulumi:"pricingPlan"`
	// An array of key-value pairs to apply to this resource.
	Tags []MapTag `pulumi:"tags"`
}

// The set of arguments for constructing a Map resource.
type MapArgs struct {
	Configuration MapConfigurationInput
	Description   pulumi.StringPtrInput
	MapName       pulumi.StringPtrInput
	PricingPlan   MapPricingPlanPtrInput
	// An array of key-value pairs to apply to this resource.
	Tags MapTagArrayInput
}

func (MapArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*mapArgs)(nil)).Elem()
}

type MapInput interface {
	pulumi.Input

	ToMapOutput() MapOutput
	ToMapOutputWithContext(ctx context.Context) MapOutput
}

func (*Map) ElementType() reflect.Type {
	return reflect.TypeOf((**Map)(nil)).Elem()
}

func (i *Map) ToMapOutput() MapOutput {
	return i.ToMapOutputWithContext(context.Background())
}

func (i *Map) ToMapOutputWithContext(ctx context.Context) MapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(MapOutput)
}

func (i *Map) ToOutput(ctx context.Context) pulumix.Output[*Map] {
	return pulumix.Output[*Map]{
		OutputState: i.ToMapOutputWithContext(ctx).OutputState,
	}
}

type MapOutput struct{ *pulumi.OutputState }

func (MapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Map)(nil)).Elem()
}

func (o MapOutput) ToMapOutput() MapOutput {
	return o
}

func (o MapOutput) ToMapOutputWithContext(ctx context.Context) MapOutput {
	return o
}

func (o MapOutput) ToOutput(ctx context.Context) pulumix.Output[*Map] {
	return pulumix.Output[*Map]{
		OutputState: o.OutputState,
	}
}

func (o MapOutput) Arn() pulumi.StringOutput {
	return o.ApplyT(func(v *Map) pulumi.StringOutput { return v.Arn }).(pulumi.StringOutput)
}

func (o MapOutput) Configuration() MapConfigurationOutput {
	return o.ApplyT(func(v *Map) MapConfigurationOutput { return v.Configuration }).(MapConfigurationOutput)
}

func (o MapOutput) CreateTime() pulumi.StringOutput {
	return o.ApplyT(func(v *Map) pulumi.StringOutput { return v.CreateTime }).(pulumi.StringOutput)
}

func (o MapOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Map) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

func (o MapOutput) MapArn() pulumi.StringOutput {
	return o.ApplyT(func(v *Map) pulumi.StringOutput { return v.MapArn }).(pulumi.StringOutput)
}

func (o MapOutput) MapName() pulumi.StringOutput {
	return o.ApplyT(func(v *Map) pulumi.StringOutput { return v.MapName }).(pulumi.StringOutput)
}

func (o MapOutput) PricingPlan() MapPricingPlanPtrOutput {
	return o.ApplyT(func(v *Map) MapPricingPlanPtrOutput { return v.PricingPlan }).(MapPricingPlanPtrOutput)
}

// An array of key-value pairs to apply to this resource.
func (o MapOutput) Tags() MapTagArrayOutput {
	return o.ApplyT(func(v *Map) MapTagArrayOutput { return v.Tags }).(MapTagArrayOutput)
}

func (o MapOutput) UpdateTime() pulumi.StringOutput {
	return o.ApplyT(func(v *Map) pulumi.StringOutput { return v.UpdateTime }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*MapInput)(nil)).Elem(), &Map{})
	pulumi.RegisterOutputType(MapOutput{})
}

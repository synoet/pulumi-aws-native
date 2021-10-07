// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package location

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Definition of AWS::Location::Map Resource Type
type Map struct {
	pulumi.CustomResourceState

	Arn           pulumi.StringOutput    `pulumi:"arn"`
	Configuration MapConfigurationOutput `pulumi:"configuration"`
	CreateTime    pulumi.StringOutput    `pulumi:"createTime"`
	DataSource    pulumi.StringOutput    `pulumi:"dataSource"`
	Description   pulumi.StringPtrOutput `pulumi:"description"`
	MapArn        pulumi.StringOutput    `pulumi:"mapArn"`
	MapName       pulumi.StringOutput    `pulumi:"mapName"`
	PricingPlan   MapPricingPlanOutput   `pulumi:"pricingPlan"`
	UpdateTime    pulumi.StringOutput    `pulumi:"updateTime"`
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
	if args.MapName == nil {
		return nil, errors.New("invalid value for required argument 'MapName'")
	}
	if args.PricingPlan == nil {
		return nil, errors.New("invalid value for required argument 'PricingPlan'")
	}
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
	MapName       string           `pulumi:"mapName"`
	PricingPlan   MapPricingPlan   `pulumi:"pricingPlan"`
}

// The set of arguments for constructing a Map resource.
type MapArgs struct {
	Configuration MapConfigurationInput
	Description   pulumi.StringPtrInput
	MapName       pulumi.StringInput
	PricingPlan   MapPricingPlanInput
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
	return reflect.TypeOf((*Map)(nil))
}

func (i *Map) ToMapOutput() MapOutput {
	return i.ToMapOutputWithContext(context.Background())
}

func (i *Map) ToMapOutputWithContext(ctx context.Context) MapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(MapOutput)
}

type MapOutput struct{ *pulumi.OutputState }

func (MapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*Map)(nil))
}

func (o MapOutput) ToMapOutput() MapOutput {
	return o
}

func (o MapOutput) ToMapOutputWithContext(ctx context.Context) MapOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(MapOutput{})
}

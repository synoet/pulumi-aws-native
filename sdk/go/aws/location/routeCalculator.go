// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package location

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Definition of AWS::Location::RouteCalculator Resource Type
type RouteCalculator struct {
	pulumi.CustomResourceState

	Arn            pulumi.StringOutput              `pulumi:"arn"`
	CalculatorArn  pulumi.StringOutput              `pulumi:"calculatorArn"`
	CalculatorName pulumi.StringOutput              `pulumi:"calculatorName"`
	CreateTime     pulumi.StringOutput              `pulumi:"createTime"`
	DataSource     pulumi.StringOutput              `pulumi:"dataSource"`
	Description    pulumi.StringPtrOutput           `pulumi:"description"`
	PricingPlan    RouteCalculatorPricingPlanOutput `pulumi:"pricingPlan"`
	UpdateTime     pulumi.StringOutput              `pulumi:"updateTime"`
}

// NewRouteCalculator registers a new resource with the given unique name, arguments, and options.
func NewRouteCalculator(ctx *pulumi.Context,
	name string, args *RouteCalculatorArgs, opts ...pulumi.ResourceOption) (*RouteCalculator, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.CalculatorName == nil {
		return nil, errors.New("invalid value for required argument 'CalculatorName'")
	}
	if args.DataSource == nil {
		return nil, errors.New("invalid value for required argument 'DataSource'")
	}
	if args.PricingPlan == nil {
		return nil, errors.New("invalid value for required argument 'PricingPlan'")
	}
	var resource RouteCalculator
	err := ctx.RegisterResource("aws-native:location:RouteCalculator", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetRouteCalculator gets an existing RouteCalculator resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetRouteCalculator(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *RouteCalculatorState, opts ...pulumi.ResourceOption) (*RouteCalculator, error) {
	var resource RouteCalculator
	err := ctx.ReadResource("aws-native:location:RouteCalculator", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering RouteCalculator resources.
type routeCalculatorState struct {
}

type RouteCalculatorState struct {
}

func (RouteCalculatorState) ElementType() reflect.Type {
	return reflect.TypeOf((*routeCalculatorState)(nil)).Elem()
}

type routeCalculatorArgs struct {
	CalculatorName string                     `pulumi:"calculatorName"`
	DataSource     string                     `pulumi:"dataSource"`
	Description    *string                    `pulumi:"description"`
	PricingPlan    RouteCalculatorPricingPlan `pulumi:"pricingPlan"`
}

// The set of arguments for constructing a RouteCalculator resource.
type RouteCalculatorArgs struct {
	CalculatorName pulumi.StringInput
	DataSource     pulumi.StringInput
	Description    pulumi.StringPtrInput
	PricingPlan    RouteCalculatorPricingPlanInput
}

func (RouteCalculatorArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*routeCalculatorArgs)(nil)).Elem()
}

type RouteCalculatorInput interface {
	pulumi.Input

	ToRouteCalculatorOutput() RouteCalculatorOutput
	ToRouteCalculatorOutputWithContext(ctx context.Context) RouteCalculatorOutput
}

func (*RouteCalculator) ElementType() reflect.Type {
	return reflect.TypeOf((*RouteCalculator)(nil))
}

func (i *RouteCalculator) ToRouteCalculatorOutput() RouteCalculatorOutput {
	return i.ToRouteCalculatorOutputWithContext(context.Background())
}

func (i *RouteCalculator) ToRouteCalculatorOutputWithContext(ctx context.Context) RouteCalculatorOutput {
	return pulumi.ToOutputWithContext(ctx, i).(RouteCalculatorOutput)
}

type RouteCalculatorOutput struct{ *pulumi.OutputState }

func (RouteCalculatorOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*RouteCalculator)(nil))
}

func (o RouteCalculatorOutput) ToRouteCalculatorOutput() RouteCalculatorOutput {
	return o
}

func (o RouteCalculatorOutput) ToRouteCalculatorOutputWithContext(ctx context.Context) RouteCalculatorOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(RouteCalculatorOutput{})
}

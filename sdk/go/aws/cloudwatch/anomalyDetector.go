// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package cloudwatch

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::CloudWatch::AnomalyDetector
//
// Deprecated: AnomalyDetector is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
type AnomalyDetector struct {
	pulumi.CustomResourceState

	Configuration               AnomalyDetectorConfigurationPtrOutput               `pulumi:"configuration"`
	Dimensions                  AnomalyDetectorDimensionArrayOutput                 `pulumi:"dimensions"`
	MetricMathAnomalyDetector   AnomalyDetectorMetricMathAnomalyDetectorPtrOutput   `pulumi:"metricMathAnomalyDetector"`
	MetricName                  pulumi.StringPtrOutput                              `pulumi:"metricName"`
	Namespace                   pulumi.StringPtrOutput                              `pulumi:"namespace"`
	SingleMetricAnomalyDetector AnomalyDetectorSingleMetricAnomalyDetectorPtrOutput `pulumi:"singleMetricAnomalyDetector"`
	Stat                        pulumi.StringPtrOutput                              `pulumi:"stat"`
}

// NewAnomalyDetector registers a new resource with the given unique name, arguments, and options.
func NewAnomalyDetector(ctx *pulumi.Context,
	name string, args *AnomalyDetectorArgs, opts ...pulumi.ResourceOption) (*AnomalyDetector, error) {
	if args == nil {
		args = &AnomalyDetectorArgs{}
	}

	var resource AnomalyDetector
	err := ctx.RegisterResource("aws-native:cloudwatch:AnomalyDetector", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetAnomalyDetector gets an existing AnomalyDetector resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetAnomalyDetector(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *AnomalyDetectorState, opts ...pulumi.ResourceOption) (*AnomalyDetector, error) {
	var resource AnomalyDetector
	err := ctx.ReadResource("aws-native:cloudwatch:AnomalyDetector", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering AnomalyDetector resources.
type anomalyDetectorState struct {
}

type AnomalyDetectorState struct {
}

func (AnomalyDetectorState) ElementType() reflect.Type {
	return reflect.TypeOf((*anomalyDetectorState)(nil)).Elem()
}

type anomalyDetectorArgs struct {
	Configuration               *AnomalyDetectorConfiguration               `pulumi:"configuration"`
	Dimensions                  []AnomalyDetectorDimension                  `pulumi:"dimensions"`
	MetricMathAnomalyDetector   *AnomalyDetectorMetricMathAnomalyDetector   `pulumi:"metricMathAnomalyDetector"`
	MetricName                  *string                                     `pulumi:"metricName"`
	Namespace                   *string                                     `pulumi:"namespace"`
	SingleMetricAnomalyDetector *AnomalyDetectorSingleMetricAnomalyDetector `pulumi:"singleMetricAnomalyDetector"`
	Stat                        *string                                     `pulumi:"stat"`
}

// The set of arguments for constructing a AnomalyDetector resource.
type AnomalyDetectorArgs struct {
	Configuration               AnomalyDetectorConfigurationPtrInput
	Dimensions                  AnomalyDetectorDimensionArrayInput
	MetricMathAnomalyDetector   AnomalyDetectorMetricMathAnomalyDetectorPtrInput
	MetricName                  pulumi.StringPtrInput
	Namespace                   pulumi.StringPtrInput
	SingleMetricAnomalyDetector AnomalyDetectorSingleMetricAnomalyDetectorPtrInput
	Stat                        pulumi.StringPtrInput
}

func (AnomalyDetectorArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*anomalyDetectorArgs)(nil)).Elem()
}

type AnomalyDetectorInput interface {
	pulumi.Input

	ToAnomalyDetectorOutput() AnomalyDetectorOutput
	ToAnomalyDetectorOutputWithContext(ctx context.Context) AnomalyDetectorOutput
}

func (*AnomalyDetector) ElementType() reflect.Type {
	return reflect.TypeOf((**AnomalyDetector)(nil)).Elem()
}

func (i *AnomalyDetector) ToAnomalyDetectorOutput() AnomalyDetectorOutput {
	return i.ToAnomalyDetectorOutputWithContext(context.Background())
}

func (i *AnomalyDetector) ToAnomalyDetectorOutputWithContext(ctx context.Context) AnomalyDetectorOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AnomalyDetectorOutput)
}

type AnomalyDetectorOutput struct{ *pulumi.OutputState }

func (AnomalyDetectorOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**AnomalyDetector)(nil)).Elem()
}

func (o AnomalyDetectorOutput) ToAnomalyDetectorOutput() AnomalyDetectorOutput {
	return o
}

func (o AnomalyDetectorOutput) ToAnomalyDetectorOutputWithContext(ctx context.Context) AnomalyDetectorOutput {
	return o
}

func (o AnomalyDetectorOutput) Configuration() AnomalyDetectorConfigurationPtrOutput {
	return o.ApplyT(func(v *AnomalyDetector) AnomalyDetectorConfigurationPtrOutput { return v.Configuration }).(AnomalyDetectorConfigurationPtrOutput)
}

func (o AnomalyDetectorOutput) Dimensions() AnomalyDetectorDimensionArrayOutput {
	return o.ApplyT(func(v *AnomalyDetector) AnomalyDetectorDimensionArrayOutput { return v.Dimensions }).(AnomalyDetectorDimensionArrayOutput)
}

func (o AnomalyDetectorOutput) MetricMathAnomalyDetector() AnomalyDetectorMetricMathAnomalyDetectorPtrOutput {
	return o.ApplyT(func(v *AnomalyDetector) AnomalyDetectorMetricMathAnomalyDetectorPtrOutput {
		return v.MetricMathAnomalyDetector
	}).(AnomalyDetectorMetricMathAnomalyDetectorPtrOutput)
}

func (o AnomalyDetectorOutput) MetricName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *AnomalyDetector) pulumi.StringPtrOutput { return v.MetricName }).(pulumi.StringPtrOutput)
}

func (o AnomalyDetectorOutput) Namespace() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *AnomalyDetector) pulumi.StringPtrOutput { return v.Namespace }).(pulumi.StringPtrOutput)
}

func (o AnomalyDetectorOutput) SingleMetricAnomalyDetector() AnomalyDetectorSingleMetricAnomalyDetectorPtrOutput {
	return o.ApplyT(func(v *AnomalyDetector) AnomalyDetectorSingleMetricAnomalyDetectorPtrOutput {
		return v.SingleMetricAnomalyDetector
	}).(AnomalyDetectorSingleMetricAnomalyDetectorPtrOutput)
}

func (o AnomalyDetectorOutput) Stat() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *AnomalyDetector) pulumi.StringPtrOutput { return v.Stat }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*AnomalyDetectorInput)(nil)).Elem(), &AnomalyDetector{})
	pulumi.RegisterOutputType(AnomalyDetectorOutput{})
}

// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package iotevents

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The comparison operator.
type AlarmModelSimpleRuleComparisonOperator string

const (
	AlarmModelSimpleRuleComparisonOperatorGreater        = AlarmModelSimpleRuleComparisonOperator("GREATER")
	AlarmModelSimpleRuleComparisonOperatorGreaterOrEqual = AlarmModelSimpleRuleComparisonOperator("GREATER_OR_EQUAL")
	AlarmModelSimpleRuleComparisonOperatorLess           = AlarmModelSimpleRuleComparisonOperator("LESS")
	AlarmModelSimpleRuleComparisonOperatorLessOrEqual    = AlarmModelSimpleRuleComparisonOperator("LESS_OR_EQUAL")
	AlarmModelSimpleRuleComparisonOperatorEqual          = AlarmModelSimpleRuleComparisonOperator("EQUAL")
	AlarmModelSimpleRuleComparisonOperatorNotEqual       = AlarmModelSimpleRuleComparisonOperator("NOT_EQUAL")
)

func (AlarmModelSimpleRuleComparisonOperator) ElementType() reflect.Type {
	return reflect.TypeOf((*AlarmModelSimpleRuleComparisonOperator)(nil)).Elem()
}

func (e AlarmModelSimpleRuleComparisonOperator) ToAlarmModelSimpleRuleComparisonOperatorOutput() AlarmModelSimpleRuleComparisonOperatorOutput {
	return pulumi.ToOutput(e).(AlarmModelSimpleRuleComparisonOperatorOutput)
}

func (e AlarmModelSimpleRuleComparisonOperator) ToAlarmModelSimpleRuleComparisonOperatorOutputWithContext(ctx context.Context) AlarmModelSimpleRuleComparisonOperatorOutput {
	return pulumi.ToOutputWithContext(ctx, e).(AlarmModelSimpleRuleComparisonOperatorOutput)
}

func (e AlarmModelSimpleRuleComparisonOperator) ToAlarmModelSimpleRuleComparisonOperatorPtrOutput() AlarmModelSimpleRuleComparisonOperatorPtrOutput {
	return e.ToAlarmModelSimpleRuleComparisonOperatorPtrOutputWithContext(context.Background())
}

func (e AlarmModelSimpleRuleComparisonOperator) ToAlarmModelSimpleRuleComparisonOperatorPtrOutputWithContext(ctx context.Context) AlarmModelSimpleRuleComparisonOperatorPtrOutput {
	return AlarmModelSimpleRuleComparisonOperator(e).ToAlarmModelSimpleRuleComparisonOperatorOutputWithContext(ctx).ToAlarmModelSimpleRuleComparisonOperatorPtrOutputWithContext(ctx)
}

func (e AlarmModelSimpleRuleComparisonOperator) ToStringOutput() pulumi.StringOutput {
	return pulumi.ToOutput(pulumi.String(e)).(pulumi.StringOutput)
}

func (e AlarmModelSimpleRuleComparisonOperator) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return pulumi.ToOutputWithContext(ctx, pulumi.String(e)).(pulumi.StringOutput)
}

func (e AlarmModelSimpleRuleComparisonOperator) ToStringPtrOutput() pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringPtrOutputWithContext(context.Background())
}

func (e AlarmModelSimpleRuleComparisonOperator) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringOutputWithContext(ctx).ToStringPtrOutputWithContext(ctx)
}

type AlarmModelSimpleRuleComparisonOperatorOutput struct{ *pulumi.OutputState }

func (AlarmModelSimpleRuleComparisonOperatorOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*AlarmModelSimpleRuleComparisonOperator)(nil)).Elem()
}

func (o AlarmModelSimpleRuleComparisonOperatorOutput) ToAlarmModelSimpleRuleComparisonOperatorOutput() AlarmModelSimpleRuleComparisonOperatorOutput {
	return o
}

func (o AlarmModelSimpleRuleComparisonOperatorOutput) ToAlarmModelSimpleRuleComparisonOperatorOutputWithContext(ctx context.Context) AlarmModelSimpleRuleComparisonOperatorOutput {
	return o
}

func (o AlarmModelSimpleRuleComparisonOperatorOutput) ToAlarmModelSimpleRuleComparisonOperatorPtrOutput() AlarmModelSimpleRuleComparisonOperatorPtrOutput {
	return o.ToAlarmModelSimpleRuleComparisonOperatorPtrOutputWithContext(context.Background())
}

func (o AlarmModelSimpleRuleComparisonOperatorOutput) ToAlarmModelSimpleRuleComparisonOperatorPtrOutputWithContext(ctx context.Context) AlarmModelSimpleRuleComparisonOperatorPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v AlarmModelSimpleRuleComparisonOperator) *AlarmModelSimpleRuleComparisonOperator {
		return &v
	}).(AlarmModelSimpleRuleComparisonOperatorPtrOutput)
}

func (o AlarmModelSimpleRuleComparisonOperatorOutput) ToStringOutput() pulumi.StringOutput {
	return o.ToStringOutputWithContext(context.Background())
}

func (o AlarmModelSimpleRuleComparisonOperatorOutput) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e AlarmModelSimpleRuleComparisonOperator) string {
		return string(e)
	}).(pulumi.StringOutput)
}

func (o AlarmModelSimpleRuleComparisonOperatorOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o AlarmModelSimpleRuleComparisonOperatorOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e AlarmModelSimpleRuleComparisonOperator) *string {
		v := string(e)
		return &v
	}).(pulumi.StringPtrOutput)
}

type AlarmModelSimpleRuleComparisonOperatorPtrOutput struct{ *pulumi.OutputState }

func (AlarmModelSimpleRuleComparisonOperatorPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**AlarmModelSimpleRuleComparisonOperator)(nil)).Elem()
}

func (o AlarmModelSimpleRuleComparisonOperatorPtrOutput) ToAlarmModelSimpleRuleComparisonOperatorPtrOutput() AlarmModelSimpleRuleComparisonOperatorPtrOutput {
	return o
}

func (o AlarmModelSimpleRuleComparisonOperatorPtrOutput) ToAlarmModelSimpleRuleComparisonOperatorPtrOutputWithContext(ctx context.Context) AlarmModelSimpleRuleComparisonOperatorPtrOutput {
	return o
}

func (o AlarmModelSimpleRuleComparisonOperatorPtrOutput) Elem() AlarmModelSimpleRuleComparisonOperatorOutput {
	return o.ApplyT(func(v *AlarmModelSimpleRuleComparisonOperator) AlarmModelSimpleRuleComparisonOperator {
		if v != nil {
			return *v
		}
		var ret AlarmModelSimpleRuleComparisonOperator
		return ret
	}).(AlarmModelSimpleRuleComparisonOperatorOutput)
}

func (o AlarmModelSimpleRuleComparisonOperatorPtrOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o AlarmModelSimpleRuleComparisonOperatorPtrOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e *AlarmModelSimpleRuleComparisonOperator) *string {
		if e == nil {
			return nil
		}
		v := string(*e)
		return &v
	}).(pulumi.StringPtrOutput)
}

// AlarmModelSimpleRuleComparisonOperatorInput is an input type that accepts AlarmModelSimpleRuleComparisonOperatorArgs and AlarmModelSimpleRuleComparisonOperatorOutput values.
// You can construct a concrete instance of `AlarmModelSimpleRuleComparisonOperatorInput` via:
//
//          AlarmModelSimpleRuleComparisonOperatorArgs{...}
type AlarmModelSimpleRuleComparisonOperatorInput interface {
	pulumi.Input

	ToAlarmModelSimpleRuleComparisonOperatorOutput() AlarmModelSimpleRuleComparisonOperatorOutput
	ToAlarmModelSimpleRuleComparisonOperatorOutputWithContext(context.Context) AlarmModelSimpleRuleComparisonOperatorOutput
}

var alarmModelSimpleRuleComparisonOperatorPtrType = reflect.TypeOf((**AlarmModelSimpleRuleComparisonOperator)(nil)).Elem()

type AlarmModelSimpleRuleComparisonOperatorPtrInput interface {
	pulumi.Input

	ToAlarmModelSimpleRuleComparisonOperatorPtrOutput() AlarmModelSimpleRuleComparisonOperatorPtrOutput
	ToAlarmModelSimpleRuleComparisonOperatorPtrOutputWithContext(context.Context) AlarmModelSimpleRuleComparisonOperatorPtrOutput
}

type alarmModelSimpleRuleComparisonOperatorPtr string

func AlarmModelSimpleRuleComparisonOperatorPtr(v string) AlarmModelSimpleRuleComparisonOperatorPtrInput {
	return (*alarmModelSimpleRuleComparisonOperatorPtr)(&v)
}

func (*alarmModelSimpleRuleComparisonOperatorPtr) ElementType() reflect.Type {
	return alarmModelSimpleRuleComparisonOperatorPtrType
}

func (in *alarmModelSimpleRuleComparisonOperatorPtr) ToAlarmModelSimpleRuleComparisonOperatorPtrOutput() AlarmModelSimpleRuleComparisonOperatorPtrOutput {
	return pulumi.ToOutput(in).(AlarmModelSimpleRuleComparisonOperatorPtrOutput)
}

func (in *alarmModelSimpleRuleComparisonOperatorPtr) ToAlarmModelSimpleRuleComparisonOperatorPtrOutputWithContext(ctx context.Context) AlarmModelSimpleRuleComparisonOperatorPtrOutput {
	return pulumi.ToOutputWithContext(ctx, in).(AlarmModelSimpleRuleComparisonOperatorPtrOutput)
}

// Information about the order in which events are evaluated and how actions are executed.
type DetectorModelEvaluationMethod string

const (
	DetectorModelEvaluationMethodBatch  = DetectorModelEvaluationMethod("BATCH")
	DetectorModelEvaluationMethodSerial = DetectorModelEvaluationMethod("SERIAL")
)

func (DetectorModelEvaluationMethod) ElementType() reflect.Type {
	return reflect.TypeOf((*DetectorModelEvaluationMethod)(nil)).Elem()
}

func (e DetectorModelEvaluationMethod) ToDetectorModelEvaluationMethodOutput() DetectorModelEvaluationMethodOutput {
	return pulumi.ToOutput(e).(DetectorModelEvaluationMethodOutput)
}

func (e DetectorModelEvaluationMethod) ToDetectorModelEvaluationMethodOutputWithContext(ctx context.Context) DetectorModelEvaluationMethodOutput {
	return pulumi.ToOutputWithContext(ctx, e).(DetectorModelEvaluationMethodOutput)
}

func (e DetectorModelEvaluationMethod) ToDetectorModelEvaluationMethodPtrOutput() DetectorModelEvaluationMethodPtrOutput {
	return e.ToDetectorModelEvaluationMethodPtrOutputWithContext(context.Background())
}

func (e DetectorModelEvaluationMethod) ToDetectorModelEvaluationMethodPtrOutputWithContext(ctx context.Context) DetectorModelEvaluationMethodPtrOutput {
	return DetectorModelEvaluationMethod(e).ToDetectorModelEvaluationMethodOutputWithContext(ctx).ToDetectorModelEvaluationMethodPtrOutputWithContext(ctx)
}

func (e DetectorModelEvaluationMethod) ToStringOutput() pulumi.StringOutput {
	return pulumi.ToOutput(pulumi.String(e)).(pulumi.StringOutput)
}

func (e DetectorModelEvaluationMethod) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return pulumi.ToOutputWithContext(ctx, pulumi.String(e)).(pulumi.StringOutput)
}

func (e DetectorModelEvaluationMethod) ToStringPtrOutput() pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringPtrOutputWithContext(context.Background())
}

func (e DetectorModelEvaluationMethod) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringOutputWithContext(ctx).ToStringPtrOutputWithContext(ctx)
}

type DetectorModelEvaluationMethodOutput struct{ *pulumi.OutputState }

func (DetectorModelEvaluationMethodOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*DetectorModelEvaluationMethod)(nil)).Elem()
}

func (o DetectorModelEvaluationMethodOutput) ToDetectorModelEvaluationMethodOutput() DetectorModelEvaluationMethodOutput {
	return o
}

func (o DetectorModelEvaluationMethodOutput) ToDetectorModelEvaluationMethodOutputWithContext(ctx context.Context) DetectorModelEvaluationMethodOutput {
	return o
}

func (o DetectorModelEvaluationMethodOutput) ToDetectorModelEvaluationMethodPtrOutput() DetectorModelEvaluationMethodPtrOutput {
	return o.ToDetectorModelEvaluationMethodPtrOutputWithContext(context.Background())
}

func (o DetectorModelEvaluationMethodOutput) ToDetectorModelEvaluationMethodPtrOutputWithContext(ctx context.Context) DetectorModelEvaluationMethodPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v DetectorModelEvaluationMethod) *DetectorModelEvaluationMethod {
		return &v
	}).(DetectorModelEvaluationMethodPtrOutput)
}

func (o DetectorModelEvaluationMethodOutput) ToStringOutput() pulumi.StringOutput {
	return o.ToStringOutputWithContext(context.Background())
}

func (o DetectorModelEvaluationMethodOutput) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e DetectorModelEvaluationMethod) string {
		return string(e)
	}).(pulumi.StringOutput)
}

func (o DetectorModelEvaluationMethodOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o DetectorModelEvaluationMethodOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e DetectorModelEvaluationMethod) *string {
		v := string(e)
		return &v
	}).(pulumi.StringPtrOutput)
}

type DetectorModelEvaluationMethodPtrOutput struct{ *pulumi.OutputState }

func (DetectorModelEvaluationMethodPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**DetectorModelEvaluationMethod)(nil)).Elem()
}

func (o DetectorModelEvaluationMethodPtrOutput) ToDetectorModelEvaluationMethodPtrOutput() DetectorModelEvaluationMethodPtrOutput {
	return o
}

func (o DetectorModelEvaluationMethodPtrOutput) ToDetectorModelEvaluationMethodPtrOutputWithContext(ctx context.Context) DetectorModelEvaluationMethodPtrOutput {
	return o
}

func (o DetectorModelEvaluationMethodPtrOutput) Elem() DetectorModelEvaluationMethodOutput {
	return o.ApplyT(func(v *DetectorModelEvaluationMethod) DetectorModelEvaluationMethod {
		if v != nil {
			return *v
		}
		var ret DetectorModelEvaluationMethod
		return ret
	}).(DetectorModelEvaluationMethodOutput)
}

func (o DetectorModelEvaluationMethodPtrOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o DetectorModelEvaluationMethodPtrOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e *DetectorModelEvaluationMethod) *string {
		if e == nil {
			return nil
		}
		v := string(*e)
		return &v
	}).(pulumi.StringPtrOutput)
}

// DetectorModelEvaluationMethodInput is an input type that accepts DetectorModelEvaluationMethodArgs and DetectorModelEvaluationMethodOutput values.
// You can construct a concrete instance of `DetectorModelEvaluationMethodInput` via:
//
//          DetectorModelEvaluationMethodArgs{...}
type DetectorModelEvaluationMethodInput interface {
	pulumi.Input

	ToDetectorModelEvaluationMethodOutput() DetectorModelEvaluationMethodOutput
	ToDetectorModelEvaluationMethodOutputWithContext(context.Context) DetectorModelEvaluationMethodOutput
}

var detectorModelEvaluationMethodPtrType = reflect.TypeOf((**DetectorModelEvaluationMethod)(nil)).Elem()

type DetectorModelEvaluationMethodPtrInput interface {
	pulumi.Input

	ToDetectorModelEvaluationMethodPtrOutput() DetectorModelEvaluationMethodPtrOutput
	ToDetectorModelEvaluationMethodPtrOutputWithContext(context.Context) DetectorModelEvaluationMethodPtrOutput
}

type detectorModelEvaluationMethodPtr string

func DetectorModelEvaluationMethodPtr(v string) DetectorModelEvaluationMethodPtrInput {
	return (*detectorModelEvaluationMethodPtr)(&v)
}

func (*detectorModelEvaluationMethodPtr) ElementType() reflect.Type {
	return detectorModelEvaluationMethodPtrType
}

func (in *detectorModelEvaluationMethodPtr) ToDetectorModelEvaluationMethodPtrOutput() DetectorModelEvaluationMethodPtrOutput {
	return pulumi.ToOutput(in).(DetectorModelEvaluationMethodPtrOutput)
}

func (in *detectorModelEvaluationMethodPtr) ToDetectorModelEvaluationMethodPtrOutputWithContext(ctx context.Context) DetectorModelEvaluationMethodPtrOutput {
	return pulumi.ToOutputWithContext(ctx, in).(DetectorModelEvaluationMethodPtrOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*AlarmModelSimpleRuleComparisonOperatorInput)(nil)).Elem(), AlarmModelSimpleRuleComparisonOperator("GREATER"))
	pulumi.RegisterInputType(reflect.TypeOf((*AlarmModelSimpleRuleComparisonOperatorPtrInput)(nil)).Elem(), AlarmModelSimpleRuleComparisonOperator("GREATER"))
	pulumi.RegisterInputType(reflect.TypeOf((*DetectorModelEvaluationMethodInput)(nil)).Elem(), DetectorModelEvaluationMethod("BATCH"))
	pulumi.RegisterInputType(reflect.TypeOf((*DetectorModelEvaluationMethodPtrInput)(nil)).Elem(), DetectorModelEvaluationMethod("BATCH"))
	pulumi.RegisterOutputType(AlarmModelSimpleRuleComparisonOperatorOutput{})
	pulumi.RegisterOutputType(AlarmModelSimpleRuleComparisonOperatorPtrOutput{})
	pulumi.RegisterOutputType(DetectorModelEvaluationMethodOutput{})
	pulumi.RegisterOutputType(DetectorModelEvaluationMethodPtrOutput{})
}

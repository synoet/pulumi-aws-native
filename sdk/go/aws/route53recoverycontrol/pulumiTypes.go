// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package route53recoverycontrol

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type ClusterEndpoint struct {
	Endpoint *string `pulumi:"endpoint"`
	Region   *string `pulumi:"region"`
}

type ClusterEndpointOutput struct{ *pulumi.OutputState }

func (ClusterEndpointOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ClusterEndpoint)(nil)).Elem()
}

func (o ClusterEndpointOutput) ToClusterEndpointOutput() ClusterEndpointOutput {
	return o
}

func (o ClusterEndpointOutput) ToClusterEndpointOutputWithContext(ctx context.Context) ClusterEndpointOutput {
	return o
}

func (o ClusterEndpointOutput) Endpoint() pulumi.StringPtrOutput {
	return o.ApplyT(func(v ClusterEndpoint) *string { return v.Endpoint }).(pulumi.StringPtrOutput)
}

func (o ClusterEndpointOutput) Region() pulumi.StringPtrOutput {
	return o.ApplyT(func(v ClusterEndpoint) *string { return v.Region }).(pulumi.StringPtrOutput)
}

type ClusterEndpointArrayOutput struct{ *pulumi.OutputState }

func (ClusterEndpointArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]ClusterEndpoint)(nil)).Elem()
}

func (o ClusterEndpointArrayOutput) ToClusterEndpointArrayOutput() ClusterEndpointArrayOutput {
	return o
}

func (o ClusterEndpointArrayOutput) ToClusterEndpointArrayOutputWithContext(ctx context.Context) ClusterEndpointArrayOutput {
	return o
}

func (o ClusterEndpointArrayOutput) Index(i pulumi.IntInput) ClusterEndpointOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) ClusterEndpoint {
		return vs[0].([]ClusterEndpoint)[vs[1].(int)]
	}).(ClusterEndpointOutput)
}

type ClusterTag struct {
	Key   string `pulumi:"key"`
	Value string `pulumi:"value"`
}

// ClusterTagInput is an input type that accepts ClusterTagArgs and ClusterTagOutput values.
// You can construct a concrete instance of `ClusterTagInput` via:
//
//	ClusterTagArgs{...}
type ClusterTagInput interface {
	pulumi.Input

	ToClusterTagOutput() ClusterTagOutput
	ToClusterTagOutputWithContext(context.Context) ClusterTagOutput
}

type ClusterTagArgs struct {
	Key   pulumi.StringInput `pulumi:"key"`
	Value pulumi.StringInput `pulumi:"value"`
}

func (ClusterTagArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*ClusterTag)(nil)).Elem()
}

func (i ClusterTagArgs) ToClusterTagOutput() ClusterTagOutput {
	return i.ToClusterTagOutputWithContext(context.Background())
}

func (i ClusterTagArgs) ToClusterTagOutputWithContext(ctx context.Context) ClusterTagOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ClusterTagOutput)
}

// ClusterTagArrayInput is an input type that accepts ClusterTagArray and ClusterTagArrayOutput values.
// You can construct a concrete instance of `ClusterTagArrayInput` via:
//
//	ClusterTagArray{ ClusterTagArgs{...} }
type ClusterTagArrayInput interface {
	pulumi.Input

	ToClusterTagArrayOutput() ClusterTagArrayOutput
	ToClusterTagArrayOutputWithContext(context.Context) ClusterTagArrayOutput
}

type ClusterTagArray []ClusterTagInput

func (ClusterTagArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]ClusterTag)(nil)).Elem()
}

func (i ClusterTagArray) ToClusterTagArrayOutput() ClusterTagArrayOutput {
	return i.ToClusterTagArrayOutputWithContext(context.Background())
}

func (i ClusterTagArray) ToClusterTagArrayOutputWithContext(ctx context.Context) ClusterTagArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ClusterTagArrayOutput)
}

type ClusterTagOutput struct{ *pulumi.OutputState }

func (ClusterTagOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ClusterTag)(nil)).Elem()
}

func (o ClusterTagOutput) ToClusterTagOutput() ClusterTagOutput {
	return o
}

func (o ClusterTagOutput) ToClusterTagOutputWithContext(ctx context.Context) ClusterTagOutput {
	return o
}

func (o ClusterTagOutput) Key() pulumi.StringOutput {
	return o.ApplyT(func(v ClusterTag) string { return v.Key }).(pulumi.StringOutput)
}

func (o ClusterTagOutput) Value() pulumi.StringOutput {
	return o.ApplyT(func(v ClusterTag) string { return v.Value }).(pulumi.StringOutput)
}

type ClusterTagArrayOutput struct{ *pulumi.OutputState }

func (ClusterTagArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]ClusterTag)(nil)).Elem()
}

func (o ClusterTagArrayOutput) ToClusterTagArrayOutput() ClusterTagArrayOutput {
	return o
}

func (o ClusterTagArrayOutput) ToClusterTagArrayOutputWithContext(ctx context.Context) ClusterTagArrayOutput {
	return o
}

func (o ClusterTagArrayOutput) Index(i pulumi.IntInput) ClusterTagOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) ClusterTag {
		return vs[0].([]ClusterTag)[vs[1].(int)]
	}).(ClusterTagOutput)
}

type ControlPanelTag struct {
	Key   string `pulumi:"key"`
	Value string `pulumi:"value"`
}

// ControlPanelTagInput is an input type that accepts ControlPanelTagArgs and ControlPanelTagOutput values.
// You can construct a concrete instance of `ControlPanelTagInput` via:
//
//	ControlPanelTagArgs{...}
type ControlPanelTagInput interface {
	pulumi.Input

	ToControlPanelTagOutput() ControlPanelTagOutput
	ToControlPanelTagOutputWithContext(context.Context) ControlPanelTagOutput
}

type ControlPanelTagArgs struct {
	Key   pulumi.StringInput `pulumi:"key"`
	Value pulumi.StringInput `pulumi:"value"`
}

func (ControlPanelTagArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*ControlPanelTag)(nil)).Elem()
}

func (i ControlPanelTagArgs) ToControlPanelTagOutput() ControlPanelTagOutput {
	return i.ToControlPanelTagOutputWithContext(context.Background())
}

func (i ControlPanelTagArgs) ToControlPanelTagOutputWithContext(ctx context.Context) ControlPanelTagOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ControlPanelTagOutput)
}

// ControlPanelTagArrayInput is an input type that accepts ControlPanelTagArray and ControlPanelTagArrayOutput values.
// You can construct a concrete instance of `ControlPanelTagArrayInput` via:
//
//	ControlPanelTagArray{ ControlPanelTagArgs{...} }
type ControlPanelTagArrayInput interface {
	pulumi.Input

	ToControlPanelTagArrayOutput() ControlPanelTagArrayOutput
	ToControlPanelTagArrayOutputWithContext(context.Context) ControlPanelTagArrayOutput
}

type ControlPanelTagArray []ControlPanelTagInput

func (ControlPanelTagArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]ControlPanelTag)(nil)).Elem()
}

func (i ControlPanelTagArray) ToControlPanelTagArrayOutput() ControlPanelTagArrayOutput {
	return i.ToControlPanelTagArrayOutputWithContext(context.Background())
}

func (i ControlPanelTagArray) ToControlPanelTagArrayOutputWithContext(ctx context.Context) ControlPanelTagArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ControlPanelTagArrayOutput)
}

type ControlPanelTagOutput struct{ *pulumi.OutputState }

func (ControlPanelTagOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ControlPanelTag)(nil)).Elem()
}

func (o ControlPanelTagOutput) ToControlPanelTagOutput() ControlPanelTagOutput {
	return o
}

func (o ControlPanelTagOutput) ToControlPanelTagOutputWithContext(ctx context.Context) ControlPanelTagOutput {
	return o
}

func (o ControlPanelTagOutput) Key() pulumi.StringOutput {
	return o.ApplyT(func(v ControlPanelTag) string { return v.Key }).(pulumi.StringOutput)
}

func (o ControlPanelTagOutput) Value() pulumi.StringOutput {
	return o.ApplyT(func(v ControlPanelTag) string { return v.Value }).(pulumi.StringOutput)
}

type ControlPanelTagArrayOutput struct{ *pulumi.OutputState }

func (ControlPanelTagArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]ControlPanelTag)(nil)).Elem()
}

func (o ControlPanelTagArrayOutput) ToControlPanelTagArrayOutput() ControlPanelTagArrayOutput {
	return o
}

func (o ControlPanelTagArrayOutput) ToControlPanelTagArrayOutputWithContext(ctx context.Context) ControlPanelTagArrayOutput {
	return o
}

func (o ControlPanelTagArrayOutput) Index(i pulumi.IntInput) ControlPanelTagOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) ControlPanelTag {
		return vs[0].([]ControlPanelTag)[vs[1].(int)]
	}).(ControlPanelTagOutput)
}

// An assertion rule enforces that, when a routing control state is changed, that the criteria set by the rule configuration is met. Otherwise, the change to the routing control is not accepted.
type SafetyRuleAssertionRule struct {
	// The routing controls that are part of transactions that are evaluated to determine if a request to change a routing control state is allowed. For example, you might include three routing controls, one for each of three AWS Regions.
	AssertedControls []string `pulumi:"assertedControls"`
	// An evaluation period, in milliseconds (ms), during which any request against the target routing controls will fail. This helps prevent "flapping" of state. The wait period is 5000 ms by default, but you can choose a custom value.
	WaitPeriodMs int `pulumi:"waitPeriodMs"`
}

// SafetyRuleAssertionRuleInput is an input type that accepts SafetyRuleAssertionRuleArgs and SafetyRuleAssertionRuleOutput values.
// You can construct a concrete instance of `SafetyRuleAssertionRuleInput` via:
//
//	SafetyRuleAssertionRuleArgs{...}
type SafetyRuleAssertionRuleInput interface {
	pulumi.Input

	ToSafetyRuleAssertionRuleOutput() SafetyRuleAssertionRuleOutput
	ToSafetyRuleAssertionRuleOutputWithContext(context.Context) SafetyRuleAssertionRuleOutput
}

// An assertion rule enforces that, when a routing control state is changed, that the criteria set by the rule configuration is met. Otherwise, the change to the routing control is not accepted.
type SafetyRuleAssertionRuleArgs struct {
	// The routing controls that are part of transactions that are evaluated to determine if a request to change a routing control state is allowed. For example, you might include three routing controls, one for each of three AWS Regions.
	AssertedControls pulumi.StringArrayInput `pulumi:"assertedControls"`
	// An evaluation period, in milliseconds (ms), during which any request against the target routing controls will fail. This helps prevent "flapping" of state. The wait period is 5000 ms by default, but you can choose a custom value.
	WaitPeriodMs pulumi.IntInput `pulumi:"waitPeriodMs"`
}

func (SafetyRuleAssertionRuleArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*SafetyRuleAssertionRule)(nil)).Elem()
}

func (i SafetyRuleAssertionRuleArgs) ToSafetyRuleAssertionRuleOutput() SafetyRuleAssertionRuleOutput {
	return i.ToSafetyRuleAssertionRuleOutputWithContext(context.Background())
}

func (i SafetyRuleAssertionRuleArgs) ToSafetyRuleAssertionRuleOutputWithContext(ctx context.Context) SafetyRuleAssertionRuleOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SafetyRuleAssertionRuleOutput)
}

func (i SafetyRuleAssertionRuleArgs) ToSafetyRuleAssertionRulePtrOutput() SafetyRuleAssertionRulePtrOutput {
	return i.ToSafetyRuleAssertionRulePtrOutputWithContext(context.Background())
}

func (i SafetyRuleAssertionRuleArgs) ToSafetyRuleAssertionRulePtrOutputWithContext(ctx context.Context) SafetyRuleAssertionRulePtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SafetyRuleAssertionRuleOutput).ToSafetyRuleAssertionRulePtrOutputWithContext(ctx)
}

// SafetyRuleAssertionRulePtrInput is an input type that accepts SafetyRuleAssertionRuleArgs, SafetyRuleAssertionRulePtr and SafetyRuleAssertionRulePtrOutput values.
// You can construct a concrete instance of `SafetyRuleAssertionRulePtrInput` via:
//
//	        SafetyRuleAssertionRuleArgs{...}
//
//	or:
//
//	        nil
type SafetyRuleAssertionRulePtrInput interface {
	pulumi.Input

	ToSafetyRuleAssertionRulePtrOutput() SafetyRuleAssertionRulePtrOutput
	ToSafetyRuleAssertionRulePtrOutputWithContext(context.Context) SafetyRuleAssertionRulePtrOutput
}

type safetyRuleAssertionRulePtrType SafetyRuleAssertionRuleArgs

func SafetyRuleAssertionRulePtr(v *SafetyRuleAssertionRuleArgs) SafetyRuleAssertionRulePtrInput {
	return (*safetyRuleAssertionRulePtrType)(v)
}

func (*safetyRuleAssertionRulePtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**SafetyRuleAssertionRule)(nil)).Elem()
}

func (i *safetyRuleAssertionRulePtrType) ToSafetyRuleAssertionRulePtrOutput() SafetyRuleAssertionRulePtrOutput {
	return i.ToSafetyRuleAssertionRulePtrOutputWithContext(context.Background())
}

func (i *safetyRuleAssertionRulePtrType) ToSafetyRuleAssertionRulePtrOutputWithContext(ctx context.Context) SafetyRuleAssertionRulePtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SafetyRuleAssertionRulePtrOutput)
}

// An assertion rule enforces that, when a routing control state is changed, that the criteria set by the rule configuration is met. Otherwise, the change to the routing control is not accepted.
type SafetyRuleAssertionRuleOutput struct{ *pulumi.OutputState }

func (SafetyRuleAssertionRuleOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*SafetyRuleAssertionRule)(nil)).Elem()
}

func (o SafetyRuleAssertionRuleOutput) ToSafetyRuleAssertionRuleOutput() SafetyRuleAssertionRuleOutput {
	return o
}

func (o SafetyRuleAssertionRuleOutput) ToSafetyRuleAssertionRuleOutputWithContext(ctx context.Context) SafetyRuleAssertionRuleOutput {
	return o
}

func (o SafetyRuleAssertionRuleOutput) ToSafetyRuleAssertionRulePtrOutput() SafetyRuleAssertionRulePtrOutput {
	return o.ToSafetyRuleAssertionRulePtrOutputWithContext(context.Background())
}

func (o SafetyRuleAssertionRuleOutput) ToSafetyRuleAssertionRulePtrOutputWithContext(ctx context.Context) SafetyRuleAssertionRulePtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v SafetyRuleAssertionRule) *SafetyRuleAssertionRule {
		return &v
	}).(SafetyRuleAssertionRulePtrOutput)
}

// The routing controls that are part of transactions that are evaluated to determine if a request to change a routing control state is allowed. For example, you might include three routing controls, one for each of three AWS Regions.
func (o SafetyRuleAssertionRuleOutput) AssertedControls() pulumi.StringArrayOutput {
	return o.ApplyT(func(v SafetyRuleAssertionRule) []string { return v.AssertedControls }).(pulumi.StringArrayOutput)
}

// An evaluation period, in milliseconds (ms), during which any request against the target routing controls will fail. This helps prevent "flapping" of state. The wait period is 5000 ms by default, but you can choose a custom value.
func (o SafetyRuleAssertionRuleOutput) WaitPeriodMs() pulumi.IntOutput {
	return o.ApplyT(func(v SafetyRuleAssertionRule) int { return v.WaitPeriodMs }).(pulumi.IntOutput)
}

type SafetyRuleAssertionRulePtrOutput struct{ *pulumi.OutputState }

func (SafetyRuleAssertionRulePtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**SafetyRuleAssertionRule)(nil)).Elem()
}

func (o SafetyRuleAssertionRulePtrOutput) ToSafetyRuleAssertionRulePtrOutput() SafetyRuleAssertionRulePtrOutput {
	return o
}

func (o SafetyRuleAssertionRulePtrOutput) ToSafetyRuleAssertionRulePtrOutputWithContext(ctx context.Context) SafetyRuleAssertionRulePtrOutput {
	return o
}

func (o SafetyRuleAssertionRulePtrOutput) Elem() SafetyRuleAssertionRuleOutput {
	return o.ApplyT(func(v *SafetyRuleAssertionRule) SafetyRuleAssertionRule {
		if v != nil {
			return *v
		}
		var ret SafetyRuleAssertionRule
		return ret
	}).(SafetyRuleAssertionRuleOutput)
}

// The routing controls that are part of transactions that are evaluated to determine if a request to change a routing control state is allowed. For example, you might include three routing controls, one for each of three AWS Regions.
func (o SafetyRuleAssertionRulePtrOutput) AssertedControls() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *SafetyRuleAssertionRule) []string {
		if v == nil {
			return nil
		}
		return v.AssertedControls
	}).(pulumi.StringArrayOutput)
}

// An evaluation period, in milliseconds (ms), during which any request against the target routing controls will fail. This helps prevent "flapping" of state. The wait period is 5000 ms by default, but you can choose a custom value.
func (o SafetyRuleAssertionRulePtrOutput) WaitPeriodMs() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *SafetyRuleAssertionRule) *int {
		if v == nil {
			return nil
		}
		return &v.WaitPeriodMs
	}).(pulumi.IntPtrOutput)
}

// A gating rule verifies that a set of gating controls evaluates as true, based on a rule configuration that you specify. If the gating rule evaluates to true, Amazon Route 53 Application Recovery Controller allows a set of routing control state changes to run and complete against the set of target controls.
type SafetyRuleGatingRule struct {
	// The gating controls for the gating rule. That is, routing controls that are evaluated by the rule configuration that you specify.
	GatingControls []string `pulumi:"gatingControls"`
	// Routing controls that can only be set or unset if the specified RuleConfig evaluates to true for the specified GatingControls. For example, say you have three gating controls, one for each of three AWS Regions. Now you specify AtLeast 2 as your RuleConfig. With these settings, you can only change (set or unset) the routing controls that you have specified as TargetControls if that rule evaluates to true.
	// In other words, your ability to change the routing controls that you have specified as TargetControls is gated by the rule that you set for the routing controls in GatingControls.
	TargetControls []string `pulumi:"targetControls"`
	// An evaluation period, in milliseconds (ms), during which any request against the target routing controls will fail. This helps prevent "flapping" of state. The wait period is 5000 ms by default, but you can choose a custom value.
	WaitPeriodMs int `pulumi:"waitPeriodMs"`
}

// SafetyRuleGatingRuleInput is an input type that accepts SafetyRuleGatingRuleArgs and SafetyRuleGatingRuleOutput values.
// You can construct a concrete instance of `SafetyRuleGatingRuleInput` via:
//
//	SafetyRuleGatingRuleArgs{...}
type SafetyRuleGatingRuleInput interface {
	pulumi.Input

	ToSafetyRuleGatingRuleOutput() SafetyRuleGatingRuleOutput
	ToSafetyRuleGatingRuleOutputWithContext(context.Context) SafetyRuleGatingRuleOutput
}

// A gating rule verifies that a set of gating controls evaluates as true, based on a rule configuration that you specify. If the gating rule evaluates to true, Amazon Route 53 Application Recovery Controller allows a set of routing control state changes to run and complete against the set of target controls.
type SafetyRuleGatingRuleArgs struct {
	// The gating controls for the gating rule. That is, routing controls that are evaluated by the rule configuration that you specify.
	GatingControls pulumi.StringArrayInput `pulumi:"gatingControls"`
	// Routing controls that can only be set or unset if the specified RuleConfig evaluates to true for the specified GatingControls. For example, say you have three gating controls, one for each of three AWS Regions. Now you specify AtLeast 2 as your RuleConfig. With these settings, you can only change (set or unset) the routing controls that you have specified as TargetControls if that rule evaluates to true.
	// In other words, your ability to change the routing controls that you have specified as TargetControls is gated by the rule that you set for the routing controls in GatingControls.
	TargetControls pulumi.StringArrayInput `pulumi:"targetControls"`
	// An evaluation period, in milliseconds (ms), during which any request against the target routing controls will fail. This helps prevent "flapping" of state. The wait period is 5000 ms by default, but you can choose a custom value.
	WaitPeriodMs pulumi.IntInput `pulumi:"waitPeriodMs"`
}

func (SafetyRuleGatingRuleArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*SafetyRuleGatingRule)(nil)).Elem()
}

func (i SafetyRuleGatingRuleArgs) ToSafetyRuleGatingRuleOutput() SafetyRuleGatingRuleOutput {
	return i.ToSafetyRuleGatingRuleOutputWithContext(context.Background())
}

func (i SafetyRuleGatingRuleArgs) ToSafetyRuleGatingRuleOutputWithContext(ctx context.Context) SafetyRuleGatingRuleOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SafetyRuleGatingRuleOutput)
}

func (i SafetyRuleGatingRuleArgs) ToSafetyRuleGatingRulePtrOutput() SafetyRuleGatingRulePtrOutput {
	return i.ToSafetyRuleGatingRulePtrOutputWithContext(context.Background())
}

func (i SafetyRuleGatingRuleArgs) ToSafetyRuleGatingRulePtrOutputWithContext(ctx context.Context) SafetyRuleGatingRulePtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SafetyRuleGatingRuleOutput).ToSafetyRuleGatingRulePtrOutputWithContext(ctx)
}

// SafetyRuleGatingRulePtrInput is an input type that accepts SafetyRuleGatingRuleArgs, SafetyRuleGatingRulePtr and SafetyRuleGatingRulePtrOutput values.
// You can construct a concrete instance of `SafetyRuleGatingRulePtrInput` via:
//
//	        SafetyRuleGatingRuleArgs{...}
//
//	or:
//
//	        nil
type SafetyRuleGatingRulePtrInput interface {
	pulumi.Input

	ToSafetyRuleGatingRulePtrOutput() SafetyRuleGatingRulePtrOutput
	ToSafetyRuleGatingRulePtrOutputWithContext(context.Context) SafetyRuleGatingRulePtrOutput
}

type safetyRuleGatingRulePtrType SafetyRuleGatingRuleArgs

func SafetyRuleGatingRulePtr(v *SafetyRuleGatingRuleArgs) SafetyRuleGatingRulePtrInput {
	return (*safetyRuleGatingRulePtrType)(v)
}

func (*safetyRuleGatingRulePtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**SafetyRuleGatingRule)(nil)).Elem()
}

func (i *safetyRuleGatingRulePtrType) ToSafetyRuleGatingRulePtrOutput() SafetyRuleGatingRulePtrOutput {
	return i.ToSafetyRuleGatingRulePtrOutputWithContext(context.Background())
}

func (i *safetyRuleGatingRulePtrType) ToSafetyRuleGatingRulePtrOutputWithContext(ctx context.Context) SafetyRuleGatingRulePtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SafetyRuleGatingRulePtrOutput)
}

// A gating rule verifies that a set of gating controls evaluates as true, based on a rule configuration that you specify. If the gating rule evaluates to true, Amazon Route 53 Application Recovery Controller allows a set of routing control state changes to run and complete against the set of target controls.
type SafetyRuleGatingRuleOutput struct{ *pulumi.OutputState }

func (SafetyRuleGatingRuleOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*SafetyRuleGatingRule)(nil)).Elem()
}

func (o SafetyRuleGatingRuleOutput) ToSafetyRuleGatingRuleOutput() SafetyRuleGatingRuleOutput {
	return o
}

func (o SafetyRuleGatingRuleOutput) ToSafetyRuleGatingRuleOutputWithContext(ctx context.Context) SafetyRuleGatingRuleOutput {
	return o
}

func (o SafetyRuleGatingRuleOutput) ToSafetyRuleGatingRulePtrOutput() SafetyRuleGatingRulePtrOutput {
	return o.ToSafetyRuleGatingRulePtrOutputWithContext(context.Background())
}

func (o SafetyRuleGatingRuleOutput) ToSafetyRuleGatingRulePtrOutputWithContext(ctx context.Context) SafetyRuleGatingRulePtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v SafetyRuleGatingRule) *SafetyRuleGatingRule {
		return &v
	}).(SafetyRuleGatingRulePtrOutput)
}

// The gating controls for the gating rule. That is, routing controls that are evaluated by the rule configuration that you specify.
func (o SafetyRuleGatingRuleOutput) GatingControls() pulumi.StringArrayOutput {
	return o.ApplyT(func(v SafetyRuleGatingRule) []string { return v.GatingControls }).(pulumi.StringArrayOutput)
}

// Routing controls that can only be set or unset if the specified RuleConfig evaluates to true for the specified GatingControls. For example, say you have three gating controls, one for each of three AWS Regions. Now you specify AtLeast 2 as your RuleConfig. With these settings, you can only change (set or unset) the routing controls that you have specified as TargetControls if that rule evaluates to true.
// In other words, your ability to change the routing controls that you have specified as TargetControls is gated by the rule that you set for the routing controls in GatingControls.
func (o SafetyRuleGatingRuleOutput) TargetControls() pulumi.StringArrayOutput {
	return o.ApplyT(func(v SafetyRuleGatingRule) []string { return v.TargetControls }).(pulumi.StringArrayOutput)
}

// An evaluation period, in milliseconds (ms), during which any request against the target routing controls will fail. This helps prevent "flapping" of state. The wait period is 5000 ms by default, but you can choose a custom value.
func (o SafetyRuleGatingRuleOutput) WaitPeriodMs() pulumi.IntOutput {
	return o.ApplyT(func(v SafetyRuleGatingRule) int { return v.WaitPeriodMs }).(pulumi.IntOutput)
}

type SafetyRuleGatingRulePtrOutput struct{ *pulumi.OutputState }

func (SafetyRuleGatingRulePtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**SafetyRuleGatingRule)(nil)).Elem()
}

func (o SafetyRuleGatingRulePtrOutput) ToSafetyRuleGatingRulePtrOutput() SafetyRuleGatingRulePtrOutput {
	return o
}

func (o SafetyRuleGatingRulePtrOutput) ToSafetyRuleGatingRulePtrOutputWithContext(ctx context.Context) SafetyRuleGatingRulePtrOutput {
	return o
}

func (o SafetyRuleGatingRulePtrOutput) Elem() SafetyRuleGatingRuleOutput {
	return o.ApplyT(func(v *SafetyRuleGatingRule) SafetyRuleGatingRule {
		if v != nil {
			return *v
		}
		var ret SafetyRuleGatingRule
		return ret
	}).(SafetyRuleGatingRuleOutput)
}

// The gating controls for the gating rule. That is, routing controls that are evaluated by the rule configuration that you specify.
func (o SafetyRuleGatingRulePtrOutput) GatingControls() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *SafetyRuleGatingRule) []string {
		if v == nil {
			return nil
		}
		return v.GatingControls
	}).(pulumi.StringArrayOutput)
}

// Routing controls that can only be set or unset if the specified RuleConfig evaluates to true for the specified GatingControls. For example, say you have three gating controls, one for each of three AWS Regions. Now you specify AtLeast 2 as your RuleConfig. With these settings, you can only change (set or unset) the routing controls that you have specified as TargetControls if that rule evaluates to true.
// In other words, your ability to change the routing controls that you have specified as TargetControls is gated by the rule that you set for the routing controls in GatingControls.
func (o SafetyRuleGatingRulePtrOutput) TargetControls() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *SafetyRuleGatingRule) []string {
		if v == nil {
			return nil
		}
		return v.TargetControls
	}).(pulumi.StringArrayOutput)
}

// An evaluation period, in milliseconds (ms), during which any request against the target routing controls will fail. This helps prevent "flapping" of state. The wait period is 5000 ms by default, but you can choose a custom value.
func (o SafetyRuleGatingRulePtrOutput) WaitPeriodMs() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *SafetyRuleGatingRule) *int {
		if v == nil {
			return nil
		}
		return &v.WaitPeriodMs
	}).(pulumi.IntPtrOutput)
}

// The rule configuration for an assertion rule or gating rule. This is the criteria that you set for specific assertion controls (routing controls) or gating controls. This configuration specifies how many controls must be enabled after a transaction completes.
type SafetyRuleRuleConfig struct {
	// Logical negation of the rule. If the rule would usually evaluate true, it's evaluated as false, and vice versa.
	Inverted bool `pulumi:"inverted"`
	// The value of N, when you specify an ATLEAST rule type. That is, Threshold is the number of controls that must be set when you specify an ATLEAST type.
	Threshold int                `pulumi:"threshold"`
	Type      SafetyRuleRuleType `pulumi:"type"`
}

// SafetyRuleRuleConfigInput is an input type that accepts SafetyRuleRuleConfigArgs and SafetyRuleRuleConfigOutput values.
// You can construct a concrete instance of `SafetyRuleRuleConfigInput` via:
//
//	SafetyRuleRuleConfigArgs{...}
type SafetyRuleRuleConfigInput interface {
	pulumi.Input

	ToSafetyRuleRuleConfigOutput() SafetyRuleRuleConfigOutput
	ToSafetyRuleRuleConfigOutputWithContext(context.Context) SafetyRuleRuleConfigOutput
}

// The rule configuration for an assertion rule or gating rule. This is the criteria that you set for specific assertion controls (routing controls) or gating controls. This configuration specifies how many controls must be enabled after a transaction completes.
type SafetyRuleRuleConfigArgs struct {
	// Logical negation of the rule. If the rule would usually evaluate true, it's evaluated as false, and vice versa.
	Inverted pulumi.BoolInput `pulumi:"inverted"`
	// The value of N, when you specify an ATLEAST rule type. That is, Threshold is the number of controls that must be set when you specify an ATLEAST type.
	Threshold pulumi.IntInput         `pulumi:"threshold"`
	Type      SafetyRuleRuleTypeInput `pulumi:"type"`
}

func (SafetyRuleRuleConfigArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*SafetyRuleRuleConfig)(nil)).Elem()
}

func (i SafetyRuleRuleConfigArgs) ToSafetyRuleRuleConfigOutput() SafetyRuleRuleConfigOutput {
	return i.ToSafetyRuleRuleConfigOutputWithContext(context.Background())
}

func (i SafetyRuleRuleConfigArgs) ToSafetyRuleRuleConfigOutputWithContext(ctx context.Context) SafetyRuleRuleConfigOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SafetyRuleRuleConfigOutput)
}

func (i SafetyRuleRuleConfigArgs) ToSafetyRuleRuleConfigPtrOutput() SafetyRuleRuleConfigPtrOutput {
	return i.ToSafetyRuleRuleConfigPtrOutputWithContext(context.Background())
}

func (i SafetyRuleRuleConfigArgs) ToSafetyRuleRuleConfigPtrOutputWithContext(ctx context.Context) SafetyRuleRuleConfigPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SafetyRuleRuleConfigOutput).ToSafetyRuleRuleConfigPtrOutputWithContext(ctx)
}

// SafetyRuleRuleConfigPtrInput is an input type that accepts SafetyRuleRuleConfigArgs, SafetyRuleRuleConfigPtr and SafetyRuleRuleConfigPtrOutput values.
// You can construct a concrete instance of `SafetyRuleRuleConfigPtrInput` via:
//
//	        SafetyRuleRuleConfigArgs{...}
//
//	or:
//
//	        nil
type SafetyRuleRuleConfigPtrInput interface {
	pulumi.Input

	ToSafetyRuleRuleConfigPtrOutput() SafetyRuleRuleConfigPtrOutput
	ToSafetyRuleRuleConfigPtrOutputWithContext(context.Context) SafetyRuleRuleConfigPtrOutput
}

type safetyRuleRuleConfigPtrType SafetyRuleRuleConfigArgs

func SafetyRuleRuleConfigPtr(v *SafetyRuleRuleConfigArgs) SafetyRuleRuleConfigPtrInput {
	return (*safetyRuleRuleConfigPtrType)(v)
}

func (*safetyRuleRuleConfigPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**SafetyRuleRuleConfig)(nil)).Elem()
}

func (i *safetyRuleRuleConfigPtrType) ToSafetyRuleRuleConfigPtrOutput() SafetyRuleRuleConfigPtrOutput {
	return i.ToSafetyRuleRuleConfigPtrOutputWithContext(context.Background())
}

func (i *safetyRuleRuleConfigPtrType) ToSafetyRuleRuleConfigPtrOutputWithContext(ctx context.Context) SafetyRuleRuleConfigPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SafetyRuleRuleConfigPtrOutput)
}

// The rule configuration for an assertion rule or gating rule. This is the criteria that you set for specific assertion controls (routing controls) or gating controls. This configuration specifies how many controls must be enabled after a transaction completes.
type SafetyRuleRuleConfigOutput struct{ *pulumi.OutputState }

func (SafetyRuleRuleConfigOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*SafetyRuleRuleConfig)(nil)).Elem()
}

func (o SafetyRuleRuleConfigOutput) ToSafetyRuleRuleConfigOutput() SafetyRuleRuleConfigOutput {
	return o
}

func (o SafetyRuleRuleConfigOutput) ToSafetyRuleRuleConfigOutputWithContext(ctx context.Context) SafetyRuleRuleConfigOutput {
	return o
}

func (o SafetyRuleRuleConfigOutput) ToSafetyRuleRuleConfigPtrOutput() SafetyRuleRuleConfigPtrOutput {
	return o.ToSafetyRuleRuleConfigPtrOutputWithContext(context.Background())
}

func (o SafetyRuleRuleConfigOutput) ToSafetyRuleRuleConfigPtrOutputWithContext(ctx context.Context) SafetyRuleRuleConfigPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v SafetyRuleRuleConfig) *SafetyRuleRuleConfig {
		return &v
	}).(SafetyRuleRuleConfigPtrOutput)
}

// Logical negation of the rule. If the rule would usually evaluate true, it's evaluated as false, and vice versa.
func (o SafetyRuleRuleConfigOutput) Inverted() pulumi.BoolOutput {
	return o.ApplyT(func(v SafetyRuleRuleConfig) bool { return v.Inverted }).(pulumi.BoolOutput)
}

// The value of N, when you specify an ATLEAST rule type. That is, Threshold is the number of controls that must be set when you specify an ATLEAST type.
func (o SafetyRuleRuleConfigOutput) Threshold() pulumi.IntOutput {
	return o.ApplyT(func(v SafetyRuleRuleConfig) int { return v.Threshold }).(pulumi.IntOutput)
}

func (o SafetyRuleRuleConfigOutput) Type() SafetyRuleRuleTypeOutput {
	return o.ApplyT(func(v SafetyRuleRuleConfig) SafetyRuleRuleType { return v.Type }).(SafetyRuleRuleTypeOutput)
}

type SafetyRuleRuleConfigPtrOutput struct{ *pulumi.OutputState }

func (SafetyRuleRuleConfigPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**SafetyRuleRuleConfig)(nil)).Elem()
}

func (o SafetyRuleRuleConfigPtrOutput) ToSafetyRuleRuleConfigPtrOutput() SafetyRuleRuleConfigPtrOutput {
	return o
}

func (o SafetyRuleRuleConfigPtrOutput) ToSafetyRuleRuleConfigPtrOutputWithContext(ctx context.Context) SafetyRuleRuleConfigPtrOutput {
	return o
}

func (o SafetyRuleRuleConfigPtrOutput) Elem() SafetyRuleRuleConfigOutput {
	return o.ApplyT(func(v *SafetyRuleRuleConfig) SafetyRuleRuleConfig {
		if v != nil {
			return *v
		}
		var ret SafetyRuleRuleConfig
		return ret
	}).(SafetyRuleRuleConfigOutput)
}

// Logical negation of the rule. If the rule would usually evaluate true, it's evaluated as false, and vice versa.
func (o SafetyRuleRuleConfigPtrOutput) Inverted() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *SafetyRuleRuleConfig) *bool {
		if v == nil {
			return nil
		}
		return &v.Inverted
	}).(pulumi.BoolPtrOutput)
}

// The value of N, when you specify an ATLEAST rule type. That is, Threshold is the number of controls that must be set when you specify an ATLEAST type.
func (o SafetyRuleRuleConfigPtrOutput) Threshold() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *SafetyRuleRuleConfig) *int {
		if v == nil {
			return nil
		}
		return &v.Threshold
	}).(pulumi.IntPtrOutput)
}

func (o SafetyRuleRuleConfigPtrOutput) Type() SafetyRuleRuleTypePtrOutput {
	return o.ApplyT(func(v *SafetyRuleRuleConfig) *SafetyRuleRuleType {
		if v == nil {
			return nil
		}
		return &v.Type
	}).(SafetyRuleRuleTypePtrOutput)
}

type SafetyRuleTag struct {
	Key   string `pulumi:"key"`
	Value string `pulumi:"value"`
}

// SafetyRuleTagInput is an input type that accepts SafetyRuleTagArgs and SafetyRuleTagOutput values.
// You can construct a concrete instance of `SafetyRuleTagInput` via:
//
//	SafetyRuleTagArgs{...}
type SafetyRuleTagInput interface {
	pulumi.Input

	ToSafetyRuleTagOutput() SafetyRuleTagOutput
	ToSafetyRuleTagOutputWithContext(context.Context) SafetyRuleTagOutput
}

type SafetyRuleTagArgs struct {
	Key   pulumi.StringInput `pulumi:"key"`
	Value pulumi.StringInput `pulumi:"value"`
}

func (SafetyRuleTagArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*SafetyRuleTag)(nil)).Elem()
}

func (i SafetyRuleTagArgs) ToSafetyRuleTagOutput() SafetyRuleTagOutput {
	return i.ToSafetyRuleTagOutputWithContext(context.Background())
}

func (i SafetyRuleTagArgs) ToSafetyRuleTagOutputWithContext(ctx context.Context) SafetyRuleTagOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SafetyRuleTagOutput)
}

// SafetyRuleTagArrayInput is an input type that accepts SafetyRuleTagArray and SafetyRuleTagArrayOutput values.
// You can construct a concrete instance of `SafetyRuleTagArrayInput` via:
//
//	SafetyRuleTagArray{ SafetyRuleTagArgs{...} }
type SafetyRuleTagArrayInput interface {
	pulumi.Input

	ToSafetyRuleTagArrayOutput() SafetyRuleTagArrayOutput
	ToSafetyRuleTagArrayOutputWithContext(context.Context) SafetyRuleTagArrayOutput
}

type SafetyRuleTagArray []SafetyRuleTagInput

func (SafetyRuleTagArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]SafetyRuleTag)(nil)).Elem()
}

func (i SafetyRuleTagArray) ToSafetyRuleTagArrayOutput() SafetyRuleTagArrayOutput {
	return i.ToSafetyRuleTagArrayOutputWithContext(context.Background())
}

func (i SafetyRuleTagArray) ToSafetyRuleTagArrayOutputWithContext(ctx context.Context) SafetyRuleTagArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SafetyRuleTagArrayOutput)
}

type SafetyRuleTagOutput struct{ *pulumi.OutputState }

func (SafetyRuleTagOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*SafetyRuleTag)(nil)).Elem()
}

func (o SafetyRuleTagOutput) ToSafetyRuleTagOutput() SafetyRuleTagOutput {
	return o
}

func (o SafetyRuleTagOutput) ToSafetyRuleTagOutputWithContext(ctx context.Context) SafetyRuleTagOutput {
	return o
}

func (o SafetyRuleTagOutput) Key() pulumi.StringOutput {
	return o.ApplyT(func(v SafetyRuleTag) string { return v.Key }).(pulumi.StringOutput)
}

func (o SafetyRuleTagOutput) Value() pulumi.StringOutput {
	return o.ApplyT(func(v SafetyRuleTag) string { return v.Value }).(pulumi.StringOutput)
}

type SafetyRuleTagArrayOutput struct{ *pulumi.OutputState }

func (SafetyRuleTagArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]SafetyRuleTag)(nil)).Elem()
}

func (o SafetyRuleTagArrayOutput) ToSafetyRuleTagArrayOutput() SafetyRuleTagArrayOutput {
	return o
}

func (o SafetyRuleTagArrayOutput) ToSafetyRuleTagArrayOutputWithContext(ctx context.Context) SafetyRuleTagArrayOutput {
	return o
}

func (o SafetyRuleTagArrayOutput) Index(i pulumi.IntInput) SafetyRuleTagOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) SafetyRuleTag {
		return vs[0].([]SafetyRuleTag)[vs[1].(int)]
	}).(SafetyRuleTagOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ClusterTagInput)(nil)).Elem(), ClusterTagArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*ClusterTagArrayInput)(nil)).Elem(), ClusterTagArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*ControlPanelTagInput)(nil)).Elem(), ControlPanelTagArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*ControlPanelTagArrayInput)(nil)).Elem(), ControlPanelTagArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*SafetyRuleAssertionRuleInput)(nil)).Elem(), SafetyRuleAssertionRuleArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*SafetyRuleAssertionRulePtrInput)(nil)).Elem(), SafetyRuleAssertionRuleArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*SafetyRuleGatingRuleInput)(nil)).Elem(), SafetyRuleGatingRuleArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*SafetyRuleGatingRulePtrInput)(nil)).Elem(), SafetyRuleGatingRuleArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*SafetyRuleRuleConfigInput)(nil)).Elem(), SafetyRuleRuleConfigArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*SafetyRuleRuleConfigPtrInput)(nil)).Elem(), SafetyRuleRuleConfigArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*SafetyRuleTagInput)(nil)).Elem(), SafetyRuleTagArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*SafetyRuleTagArrayInput)(nil)).Elem(), SafetyRuleTagArray{})
	pulumi.RegisterOutputType(ClusterEndpointOutput{})
	pulumi.RegisterOutputType(ClusterEndpointArrayOutput{})
	pulumi.RegisterOutputType(ClusterTagOutput{})
	pulumi.RegisterOutputType(ClusterTagArrayOutput{})
	pulumi.RegisterOutputType(ControlPanelTagOutput{})
	pulumi.RegisterOutputType(ControlPanelTagArrayOutput{})
	pulumi.RegisterOutputType(SafetyRuleAssertionRuleOutput{})
	pulumi.RegisterOutputType(SafetyRuleAssertionRulePtrOutput{})
	pulumi.RegisterOutputType(SafetyRuleGatingRuleOutput{})
	pulumi.RegisterOutputType(SafetyRuleGatingRulePtrOutput{})
	pulumi.RegisterOutputType(SafetyRuleRuleConfigOutput{})
	pulumi.RegisterOutputType(SafetyRuleRuleConfigPtrOutput{})
	pulumi.RegisterOutputType(SafetyRuleTagOutput{})
	pulumi.RegisterOutputType(SafetyRuleTagArrayOutput{})
}

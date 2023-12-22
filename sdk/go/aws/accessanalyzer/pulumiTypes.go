// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package accessanalyzer

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

var _ = internal.GetEnvOrDefault

// An Access Analyzer archive rule. Archive rules automatically archive new findings that meet the criteria you define when you create the rule.
type AnalyzerArchiveRule struct {
	Filter []AnalyzerFilter `pulumi:"filter"`
	// The archive rule name
	RuleName string `pulumi:"ruleName"`
}

// AnalyzerArchiveRuleInput is an input type that accepts AnalyzerArchiveRuleArgs and AnalyzerArchiveRuleOutput values.
// You can construct a concrete instance of `AnalyzerArchiveRuleInput` via:
//
//	AnalyzerArchiveRuleArgs{...}
type AnalyzerArchiveRuleInput interface {
	pulumi.Input

	ToAnalyzerArchiveRuleOutput() AnalyzerArchiveRuleOutput
	ToAnalyzerArchiveRuleOutputWithContext(context.Context) AnalyzerArchiveRuleOutput
}

// An Access Analyzer archive rule. Archive rules automatically archive new findings that meet the criteria you define when you create the rule.
type AnalyzerArchiveRuleArgs struct {
	Filter AnalyzerFilterArrayInput `pulumi:"filter"`
	// The archive rule name
	RuleName pulumi.StringInput `pulumi:"ruleName"`
}

func (AnalyzerArchiveRuleArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*AnalyzerArchiveRule)(nil)).Elem()
}

func (i AnalyzerArchiveRuleArgs) ToAnalyzerArchiveRuleOutput() AnalyzerArchiveRuleOutput {
	return i.ToAnalyzerArchiveRuleOutputWithContext(context.Background())
}

func (i AnalyzerArchiveRuleArgs) ToAnalyzerArchiveRuleOutputWithContext(ctx context.Context) AnalyzerArchiveRuleOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AnalyzerArchiveRuleOutput)
}

func (i AnalyzerArchiveRuleArgs) ToOutput(ctx context.Context) pulumix.Output[AnalyzerArchiveRule] {
	return pulumix.Output[AnalyzerArchiveRule]{
		OutputState: i.ToAnalyzerArchiveRuleOutputWithContext(ctx).OutputState,
	}
}

// AnalyzerArchiveRuleArrayInput is an input type that accepts AnalyzerArchiveRuleArray and AnalyzerArchiveRuleArrayOutput values.
// You can construct a concrete instance of `AnalyzerArchiveRuleArrayInput` via:
//
//	AnalyzerArchiveRuleArray{ AnalyzerArchiveRuleArgs{...} }
type AnalyzerArchiveRuleArrayInput interface {
	pulumi.Input

	ToAnalyzerArchiveRuleArrayOutput() AnalyzerArchiveRuleArrayOutput
	ToAnalyzerArchiveRuleArrayOutputWithContext(context.Context) AnalyzerArchiveRuleArrayOutput
}

type AnalyzerArchiveRuleArray []AnalyzerArchiveRuleInput

func (AnalyzerArchiveRuleArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]AnalyzerArchiveRule)(nil)).Elem()
}

func (i AnalyzerArchiveRuleArray) ToAnalyzerArchiveRuleArrayOutput() AnalyzerArchiveRuleArrayOutput {
	return i.ToAnalyzerArchiveRuleArrayOutputWithContext(context.Background())
}

func (i AnalyzerArchiveRuleArray) ToAnalyzerArchiveRuleArrayOutputWithContext(ctx context.Context) AnalyzerArchiveRuleArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AnalyzerArchiveRuleArrayOutput)
}

func (i AnalyzerArchiveRuleArray) ToOutput(ctx context.Context) pulumix.Output[[]AnalyzerArchiveRule] {
	return pulumix.Output[[]AnalyzerArchiveRule]{
		OutputState: i.ToAnalyzerArchiveRuleArrayOutputWithContext(ctx).OutputState,
	}
}

// An Access Analyzer archive rule. Archive rules automatically archive new findings that meet the criteria you define when you create the rule.
type AnalyzerArchiveRuleOutput struct{ *pulumi.OutputState }

func (AnalyzerArchiveRuleOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*AnalyzerArchiveRule)(nil)).Elem()
}

func (o AnalyzerArchiveRuleOutput) ToAnalyzerArchiveRuleOutput() AnalyzerArchiveRuleOutput {
	return o
}

func (o AnalyzerArchiveRuleOutput) ToAnalyzerArchiveRuleOutputWithContext(ctx context.Context) AnalyzerArchiveRuleOutput {
	return o
}

func (o AnalyzerArchiveRuleOutput) ToOutput(ctx context.Context) pulumix.Output[AnalyzerArchiveRule] {
	return pulumix.Output[AnalyzerArchiveRule]{
		OutputState: o.OutputState,
	}
}

func (o AnalyzerArchiveRuleOutput) Filter() AnalyzerFilterArrayOutput {
	return o.ApplyT(func(v AnalyzerArchiveRule) []AnalyzerFilter { return v.Filter }).(AnalyzerFilterArrayOutput)
}

// The archive rule name
func (o AnalyzerArchiveRuleOutput) RuleName() pulumi.StringOutput {
	return o.ApplyT(func(v AnalyzerArchiveRule) string { return v.RuleName }).(pulumi.StringOutput)
}

type AnalyzerArchiveRuleArrayOutput struct{ *pulumi.OutputState }

func (AnalyzerArchiveRuleArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]AnalyzerArchiveRule)(nil)).Elem()
}

func (o AnalyzerArchiveRuleArrayOutput) ToAnalyzerArchiveRuleArrayOutput() AnalyzerArchiveRuleArrayOutput {
	return o
}

func (o AnalyzerArchiveRuleArrayOutput) ToAnalyzerArchiveRuleArrayOutputWithContext(ctx context.Context) AnalyzerArchiveRuleArrayOutput {
	return o
}

func (o AnalyzerArchiveRuleArrayOutput) ToOutput(ctx context.Context) pulumix.Output[[]AnalyzerArchiveRule] {
	return pulumix.Output[[]AnalyzerArchiveRule]{
		OutputState: o.OutputState,
	}
}

func (o AnalyzerArchiveRuleArrayOutput) Index(i pulumi.IntInput) AnalyzerArchiveRuleOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) AnalyzerArchiveRule {
		return vs[0].([]AnalyzerArchiveRule)[vs[1].(int)]
	}).(AnalyzerArchiveRuleOutput)
}

// The configuration for the analyzer
type AnalyzerConfigurationProperties struct {
	UnusedAccessConfiguration *AnalyzerUnusedAccessConfiguration `pulumi:"unusedAccessConfiguration"`
}

// AnalyzerConfigurationPropertiesInput is an input type that accepts AnalyzerConfigurationPropertiesArgs and AnalyzerConfigurationPropertiesOutput values.
// You can construct a concrete instance of `AnalyzerConfigurationPropertiesInput` via:
//
//	AnalyzerConfigurationPropertiesArgs{...}
type AnalyzerConfigurationPropertiesInput interface {
	pulumi.Input

	ToAnalyzerConfigurationPropertiesOutput() AnalyzerConfigurationPropertiesOutput
	ToAnalyzerConfigurationPropertiesOutputWithContext(context.Context) AnalyzerConfigurationPropertiesOutput
}

// The configuration for the analyzer
type AnalyzerConfigurationPropertiesArgs struct {
	UnusedAccessConfiguration AnalyzerUnusedAccessConfigurationPtrInput `pulumi:"unusedAccessConfiguration"`
}

func (AnalyzerConfigurationPropertiesArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*AnalyzerConfigurationProperties)(nil)).Elem()
}

func (i AnalyzerConfigurationPropertiesArgs) ToAnalyzerConfigurationPropertiesOutput() AnalyzerConfigurationPropertiesOutput {
	return i.ToAnalyzerConfigurationPropertiesOutputWithContext(context.Background())
}

func (i AnalyzerConfigurationPropertiesArgs) ToAnalyzerConfigurationPropertiesOutputWithContext(ctx context.Context) AnalyzerConfigurationPropertiesOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AnalyzerConfigurationPropertiesOutput)
}

func (i AnalyzerConfigurationPropertiesArgs) ToOutput(ctx context.Context) pulumix.Output[AnalyzerConfigurationProperties] {
	return pulumix.Output[AnalyzerConfigurationProperties]{
		OutputState: i.ToAnalyzerConfigurationPropertiesOutputWithContext(ctx).OutputState,
	}
}

func (i AnalyzerConfigurationPropertiesArgs) ToAnalyzerConfigurationPropertiesPtrOutput() AnalyzerConfigurationPropertiesPtrOutput {
	return i.ToAnalyzerConfigurationPropertiesPtrOutputWithContext(context.Background())
}

func (i AnalyzerConfigurationPropertiesArgs) ToAnalyzerConfigurationPropertiesPtrOutputWithContext(ctx context.Context) AnalyzerConfigurationPropertiesPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AnalyzerConfigurationPropertiesOutput).ToAnalyzerConfigurationPropertiesPtrOutputWithContext(ctx)
}

// AnalyzerConfigurationPropertiesPtrInput is an input type that accepts AnalyzerConfigurationPropertiesArgs, AnalyzerConfigurationPropertiesPtr and AnalyzerConfigurationPropertiesPtrOutput values.
// You can construct a concrete instance of `AnalyzerConfigurationPropertiesPtrInput` via:
//
//	        AnalyzerConfigurationPropertiesArgs{...}
//
//	or:
//
//	        nil
type AnalyzerConfigurationPropertiesPtrInput interface {
	pulumi.Input

	ToAnalyzerConfigurationPropertiesPtrOutput() AnalyzerConfigurationPropertiesPtrOutput
	ToAnalyzerConfigurationPropertiesPtrOutputWithContext(context.Context) AnalyzerConfigurationPropertiesPtrOutput
}

type analyzerConfigurationPropertiesPtrType AnalyzerConfigurationPropertiesArgs

func AnalyzerConfigurationPropertiesPtr(v *AnalyzerConfigurationPropertiesArgs) AnalyzerConfigurationPropertiesPtrInput {
	return (*analyzerConfigurationPropertiesPtrType)(v)
}

func (*analyzerConfigurationPropertiesPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**AnalyzerConfigurationProperties)(nil)).Elem()
}

func (i *analyzerConfigurationPropertiesPtrType) ToAnalyzerConfigurationPropertiesPtrOutput() AnalyzerConfigurationPropertiesPtrOutput {
	return i.ToAnalyzerConfigurationPropertiesPtrOutputWithContext(context.Background())
}

func (i *analyzerConfigurationPropertiesPtrType) ToAnalyzerConfigurationPropertiesPtrOutputWithContext(ctx context.Context) AnalyzerConfigurationPropertiesPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AnalyzerConfigurationPropertiesPtrOutput)
}

func (i *analyzerConfigurationPropertiesPtrType) ToOutput(ctx context.Context) pulumix.Output[*AnalyzerConfigurationProperties] {
	return pulumix.Output[*AnalyzerConfigurationProperties]{
		OutputState: i.ToAnalyzerConfigurationPropertiesPtrOutputWithContext(ctx).OutputState,
	}
}

// The configuration for the analyzer
type AnalyzerConfigurationPropertiesOutput struct{ *pulumi.OutputState }

func (AnalyzerConfigurationPropertiesOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*AnalyzerConfigurationProperties)(nil)).Elem()
}

func (o AnalyzerConfigurationPropertiesOutput) ToAnalyzerConfigurationPropertiesOutput() AnalyzerConfigurationPropertiesOutput {
	return o
}

func (o AnalyzerConfigurationPropertiesOutput) ToAnalyzerConfigurationPropertiesOutputWithContext(ctx context.Context) AnalyzerConfigurationPropertiesOutput {
	return o
}

func (o AnalyzerConfigurationPropertiesOutput) ToAnalyzerConfigurationPropertiesPtrOutput() AnalyzerConfigurationPropertiesPtrOutput {
	return o.ToAnalyzerConfigurationPropertiesPtrOutputWithContext(context.Background())
}

func (o AnalyzerConfigurationPropertiesOutput) ToAnalyzerConfigurationPropertiesPtrOutputWithContext(ctx context.Context) AnalyzerConfigurationPropertiesPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v AnalyzerConfigurationProperties) *AnalyzerConfigurationProperties {
		return &v
	}).(AnalyzerConfigurationPropertiesPtrOutput)
}

func (o AnalyzerConfigurationPropertiesOutput) ToOutput(ctx context.Context) pulumix.Output[AnalyzerConfigurationProperties] {
	return pulumix.Output[AnalyzerConfigurationProperties]{
		OutputState: o.OutputState,
	}
}

func (o AnalyzerConfigurationPropertiesOutput) UnusedAccessConfiguration() AnalyzerUnusedAccessConfigurationPtrOutput {
	return o.ApplyT(func(v AnalyzerConfigurationProperties) *AnalyzerUnusedAccessConfiguration {
		return v.UnusedAccessConfiguration
	}).(AnalyzerUnusedAccessConfigurationPtrOutput)
}

type AnalyzerConfigurationPropertiesPtrOutput struct{ *pulumi.OutputState }

func (AnalyzerConfigurationPropertiesPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**AnalyzerConfigurationProperties)(nil)).Elem()
}

func (o AnalyzerConfigurationPropertiesPtrOutput) ToAnalyzerConfigurationPropertiesPtrOutput() AnalyzerConfigurationPropertiesPtrOutput {
	return o
}

func (o AnalyzerConfigurationPropertiesPtrOutput) ToAnalyzerConfigurationPropertiesPtrOutputWithContext(ctx context.Context) AnalyzerConfigurationPropertiesPtrOutput {
	return o
}

func (o AnalyzerConfigurationPropertiesPtrOutput) ToOutput(ctx context.Context) pulumix.Output[*AnalyzerConfigurationProperties] {
	return pulumix.Output[*AnalyzerConfigurationProperties]{
		OutputState: o.OutputState,
	}
}

func (o AnalyzerConfigurationPropertiesPtrOutput) Elem() AnalyzerConfigurationPropertiesOutput {
	return o.ApplyT(func(v *AnalyzerConfigurationProperties) AnalyzerConfigurationProperties {
		if v != nil {
			return *v
		}
		var ret AnalyzerConfigurationProperties
		return ret
	}).(AnalyzerConfigurationPropertiesOutput)
}

func (o AnalyzerConfigurationPropertiesPtrOutput) UnusedAccessConfiguration() AnalyzerUnusedAccessConfigurationPtrOutput {
	return o.ApplyT(func(v *AnalyzerConfigurationProperties) *AnalyzerUnusedAccessConfiguration {
		if v == nil {
			return nil
		}
		return v.UnusedAccessConfiguration
	}).(AnalyzerUnusedAccessConfigurationPtrOutput)
}

type AnalyzerFilter struct {
	Contains []string `pulumi:"contains"`
	Eq       []string `pulumi:"eq"`
	Exists   *bool    `pulumi:"exists"`
	Neq      []string `pulumi:"neq"`
	Property string   `pulumi:"property"`
}

// AnalyzerFilterInput is an input type that accepts AnalyzerFilterArgs and AnalyzerFilterOutput values.
// You can construct a concrete instance of `AnalyzerFilterInput` via:
//
//	AnalyzerFilterArgs{...}
type AnalyzerFilterInput interface {
	pulumi.Input

	ToAnalyzerFilterOutput() AnalyzerFilterOutput
	ToAnalyzerFilterOutputWithContext(context.Context) AnalyzerFilterOutput
}

type AnalyzerFilterArgs struct {
	Contains pulumi.StringArrayInput `pulumi:"contains"`
	Eq       pulumi.StringArrayInput `pulumi:"eq"`
	Exists   pulumi.BoolPtrInput     `pulumi:"exists"`
	Neq      pulumi.StringArrayInput `pulumi:"neq"`
	Property pulumi.StringInput      `pulumi:"property"`
}

func (AnalyzerFilterArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*AnalyzerFilter)(nil)).Elem()
}

func (i AnalyzerFilterArgs) ToAnalyzerFilterOutput() AnalyzerFilterOutput {
	return i.ToAnalyzerFilterOutputWithContext(context.Background())
}

func (i AnalyzerFilterArgs) ToAnalyzerFilterOutputWithContext(ctx context.Context) AnalyzerFilterOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AnalyzerFilterOutput)
}

func (i AnalyzerFilterArgs) ToOutput(ctx context.Context) pulumix.Output[AnalyzerFilter] {
	return pulumix.Output[AnalyzerFilter]{
		OutputState: i.ToAnalyzerFilterOutputWithContext(ctx).OutputState,
	}
}

// AnalyzerFilterArrayInput is an input type that accepts AnalyzerFilterArray and AnalyzerFilterArrayOutput values.
// You can construct a concrete instance of `AnalyzerFilterArrayInput` via:
//
//	AnalyzerFilterArray{ AnalyzerFilterArgs{...} }
type AnalyzerFilterArrayInput interface {
	pulumi.Input

	ToAnalyzerFilterArrayOutput() AnalyzerFilterArrayOutput
	ToAnalyzerFilterArrayOutputWithContext(context.Context) AnalyzerFilterArrayOutput
}

type AnalyzerFilterArray []AnalyzerFilterInput

func (AnalyzerFilterArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]AnalyzerFilter)(nil)).Elem()
}

func (i AnalyzerFilterArray) ToAnalyzerFilterArrayOutput() AnalyzerFilterArrayOutput {
	return i.ToAnalyzerFilterArrayOutputWithContext(context.Background())
}

func (i AnalyzerFilterArray) ToAnalyzerFilterArrayOutputWithContext(ctx context.Context) AnalyzerFilterArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AnalyzerFilterArrayOutput)
}

func (i AnalyzerFilterArray) ToOutput(ctx context.Context) pulumix.Output[[]AnalyzerFilter] {
	return pulumix.Output[[]AnalyzerFilter]{
		OutputState: i.ToAnalyzerFilterArrayOutputWithContext(ctx).OutputState,
	}
}

type AnalyzerFilterOutput struct{ *pulumi.OutputState }

func (AnalyzerFilterOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*AnalyzerFilter)(nil)).Elem()
}

func (o AnalyzerFilterOutput) ToAnalyzerFilterOutput() AnalyzerFilterOutput {
	return o
}

func (o AnalyzerFilterOutput) ToAnalyzerFilterOutputWithContext(ctx context.Context) AnalyzerFilterOutput {
	return o
}

func (o AnalyzerFilterOutput) ToOutput(ctx context.Context) pulumix.Output[AnalyzerFilter] {
	return pulumix.Output[AnalyzerFilter]{
		OutputState: o.OutputState,
	}
}

func (o AnalyzerFilterOutput) Contains() pulumi.StringArrayOutput {
	return o.ApplyT(func(v AnalyzerFilter) []string { return v.Contains }).(pulumi.StringArrayOutput)
}

func (o AnalyzerFilterOutput) Eq() pulumi.StringArrayOutput {
	return o.ApplyT(func(v AnalyzerFilter) []string { return v.Eq }).(pulumi.StringArrayOutput)
}

func (o AnalyzerFilterOutput) Exists() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v AnalyzerFilter) *bool { return v.Exists }).(pulumi.BoolPtrOutput)
}

func (o AnalyzerFilterOutput) Neq() pulumi.StringArrayOutput {
	return o.ApplyT(func(v AnalyzerFilter) []string { return v.Neq }).(pulumi.StringArrayOutput)
}

func (o AnalyzerFilterOutput) Property() pulumi.StringOutput {
	return o.ApplyT(func(v AnalyzerFilter) string { return v.Property }).(pulumi.StringOutput)
}

type AnalyzerFilterArrayOutput struct{ *pulumi.OutputState }

func (AnalyzerFilterArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]AnalyzerFilter)(nil)).Elem()
}

func (o AnalyzerFilterArrayOutput) ToAnalyzerFilterArrayOutput() AnalyzerFilterArrayOutput {
	return o
}

func (o AnalyzerFilterArrayOutput) ToAnalyzerFilterArrayOutputWithContext(ctx context.Context) AnalyzerFilterArrayOutput {
	return o
}

func (o AnalyzerFilterArrayOutput) ToOutput(ctx context.Context) pulumix.Output[[]AnalyzerFilter] {
	return pulumix.Output[[]AnalyzerFilter]{
		OutputState: o.OutputState,
	}
}

func (o AnalyzerFilterArrayOutput) Index(i pulumi.IntInput) AnalyzerFilterOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) AnalyzerFilter {
		return vs[0].([]AnalyzerFilter)[vs[1].(int)]
	}).(AnalyzerFilterOutput)
}

// A key-value pair to associate with a resource.
type AnalyzerTag struct {
	// The key name of the tag. You can specify a value that is 1 to 127 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
	Key string `pulumi:"key"`
	// The value for the tag. You can specify a value that is 1 to 255 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
	Value string `pulumi:"value"`
}

// AnalyzerTagInput is an input type that accepts AnalyzerTagArgs and AnalyzerTagOutput values.
// You can construct a concrete instance of `AnalyzerTagInput` via:
//
//	AnalyzerTagArgs{...}
type AnalyzerTagInput interface {
	pulumi.Input

	ToAnalyzerTagOutput() AnalyzerTagOutput
	ToAnalyzerTagOutputWithContext(context.Context) AnalyzerTagOutput
}

// A key-value pair to associate with a resource.
type AnalyzerTagArgs struct {
	// The key name of the tag. You can specify a value that is 1 to 127 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
	Key pulumi.StringInput `pulumi:"key"`
	// The value for the tag. You can specify a value that is 1 to 255 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
	Value pulumi.StringInput `pulumi:"value"`
}

func (AnalyzerTagArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*AnalyzerTag)(nil)).Elem()
}

func (i AnalyzerTagArgs) ToAnalyzerTagOutput() AnalyzerTagOutput {
	return i.ToAnalyzerTagOutputWithContext(context.Background())
}

func (i AnalyzerTagArgs) ToAnalyzerTagOutputWithContext(ctx context.Context) AnalyzerTagOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AnalyzerTagOutput)
}

func (i AnalyzerTagArgs) ToOutput(ctx context.Context) pulumix.Output[AnalyzerTag] {
	return pulumix.Output[AnalyzerTag]{
		OutputState: i.ToAnalyzerTagOutputWithContext(ctx).OutputState,
	}
}

// AnalyzerTagArrayInput is an input type that accepts AnalyzerTagArray and AnalyzerTagArrayOutput values.
// You can construct a concrete instance of `AnalyzerTagArrayInput` via:
//
//	AnalyzerTagArray{ AnalyzerTagArgs{...} }
type AnalyzerTagArrayInput interface {
	pulumi.Input

	ToAnalyzerTagArrayOutput() AnalyzerTagArrayOutput
	ToAnalyzerTagArrayOutputWithContext(context.Context) AnalyzerTagArrayOutput
}

type AnalyzerTagArray []AnalyzerTagInput

func (AnalyzerTagArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]AnalyzerTag)(nil)).Elem()
}

func (i AnalyzerTagArray) ToAnalyzerTagArrayOutput() AnalyzerTagArrayOutput {
	return i.ToAnalyzerTagArrayOutputWithContext(context.Background())
}

func (i AnalyzerTagArray) ToAnalyzerTagArrayOutputWithContext(ctx context.Context) AnalyzerTagArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AnalyzerTagArrayOutput)
}

func (i AnalyzerTagArray) ToOutput(ctx context.Context) pulumix.Output[[]AnalyzerTag] {
	return pulumix.Output[[]AnalyzerTag]{
		OutputState: i.ToAnalyzerTagArrayOutputWithContext(ctx).OutputState,
	}
}

// A key-value pair to associate with a resource.
type AnalyzerTagOutput struct{ *pulumi.OutputState }

func (AnalyzerTagOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*AnalyzerTag)(nil)).Elem()
}

func (o AnalyzerTagOutput) ToAnalyzerTagOutput() AnalyzerTagOutput {
	return o
}

func (o AnalyzerTagOutput) ToAnalyzerTagOutputWithContext(ctx context.Context) AnalyzerTagOutput {
	return o
}

func (o AnalyzerTagOutput) ToOutput(ctx context.Context) pulumix.Output[AnalyzerTag] {
	return pulumix.Output[AnalyzerTag]{
		OutputState: o.OutputState,
	}
}

// The key name of the tag. You can specify a value that is 1 to 127 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
func (o AnalyzerTagOutput) Key() pulumi.StringOutput {
	return o.ApplyT(func(v AnalyzerTag) string { return v.Key }).(pulumi.StringOutput)
}

// The value for the tag. You can specify a value that is 1 to 255 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
func (o AnalyzerTagOutput) Value() pulumi.StringOutput {
	return o.ApplyT(func(v AnalyzerTag) string { return v.Value }).(pulumi.StringOutput)
}

type AnalyzerTagArrayOutput struct{ *pulumi.OutputState }

func (AnalyzerTagArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]AnalyzerTag)(nil)).Elem()
}

func (o AnalyzerTagArrayOutput) ToAnalyzerTagArrayOutput() AnalyzerTagArrayOutput {
	return o
}

func (o AnalyzerTagArrayOutput) ToAnalyzerTagArrayOutputWithContext(ctx context.Context) AnalyzerTagArrayOutput {
	return o
}

func (o AnalyzerTagArrayOutput) ToOutput(ctx context.Context) pulumix.Output[[]AnalyzerTag] {
	return pulumix.Output[[]AnalyzerTag]{
		OutputState: o.OutputState,
	}
}

func (o AnalyzerTagArrayOutput) Index(i pulumi.IntInput) AnalyzerTagOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) AnalyzerTag {
		return vs[0].([]AnalyzerTag)[vs[1].(int)]
	}).(AnalyzerTagOutput)
}

// The Configuration for Unused Access Analyzer
type AnalyzerUnusedAccessConfiguration struct {
	// The specified access age in days for which to generate findings for unused access. For example, if you specify 90 days, the analyzer will generate findings for IAM entities within the accounts of the selected organization for any access that hasn't been used in 90 or more days since the analyzer's last scan. You can choose a value between 1 and 180 days.
	UnusedAccessAge *int `pulumi:"unusedAccessAge"`
}

// AnalyzerUnusedAccessConfigurationInput is an input type that accepts AnalyzerUnusedAccessConfigurationArgs and AnalyzerUnusedAccessConfigurationOutput values.
// You can construct a concrete instance of `AnalyzerUnusedAccessConfigurationInput` via:
//
//	AnalyzerUnusedAccessConfigurationArgs{...}
type AnalyzerUnusedAccessConfigurationInput interface {
	pulumi.Input

	ToAnalyzerUnusedAccessConfigurationOutput() AnalyzerUnusedAccessConfigurationOutput
	ToAnalyzerUnusedAccessConfigurationOutputWithContext(context.Context) AnalyzerUnusedAccessConfigurationOutput
}

// The Configuration for Unused Access Analyzer
type AnalyzerUnusedAccessConfigurationArgs struct {
	// The specified access age in days for which to generate findings for unused access. For example, if you specify 90 days, the analyzer will generate findings for IAM entities within the accounts of the selected organization for any access that hasn't been used in 90 or more days since the analyzer's last scan. You can choose a value between 1 and 180 days.
	UnusedAccessAge pulumi.IntPtrInput `pulumi:"unusedAccessAge"`
}

func (AnalyzerUnusedAccessConfigurationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*AnalyzerUnusedAccessConfiguration)(nil)).Elem()
}

func (i AnalyzerUnusedAccessConfigurationArgs) ToAnalyzerUnusedAccessConfigurationOutput() AnalyzerUnusedAccessConfigurationOutput {
	return i.ToAnalyzerUnusedAccessConfigurationOutputWithContext(context.Background())
}

func (i AnalyzerUnusedAccessConfigurationArgs) ToAnalyzerUnusedAccessConfigurationOutputWithContext(ctx context.Context) AnalyzerUnusedAccessConfigurationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AnalyzerUnusedAccessConfigurationOutput)
}

func (i AnalyzerUnusedAccessConfigurationArgs) ToOutput(ctx context.Context) pulumix.Output[AnalyzerUnusedAccessConfiguration] {
	return pulumix.Output[AnalyzerUnusedAccessConfiguration]{
		OutputState: i.ToAnalyzerUnusedAccessConfigurationOutputWithContext(ctx).OutputState,
	}
}

func (i AnalyzerUnusedAccessConfigurationArgs) ToAnalyzerUnusedAccessConfigurationPtrOutput() AnalyzerUnusedAccessConfigurationPtrOutput {
	return i.ToAnalyzerUnusedAccessConfigurationPtrOutputWithContext(context.Background())
}

func (i AnalyzerUnusedAccessConfigurationArgs) ToAnalyzerUnusedAccessConfigurationPtrOutputWithContext(ctx context.Context) AnalyzerUnusedAccessConfigurationPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AnalyzerUnusedAccessConfigurationOutput).ToAnalyzerUnusedAccessConfigurationPtrOutputWithContext(ctx)
}

// AnalyzerUnusedAccessConfigurationPtrInput is an input type that accepts AnalyzerUnusedAccessConfigurationArgs, AnalyzerUnusedAccessConfigurationPtr and AnalyzerUnusedAccessConfigurationPtrOutput values.
// You can construct a concrete instance of `AnalyzerUnusedAccessConfigurationPtrInput` via:
//
//	        AnalyzerUnusedAccessConfigurationArgs{...}
//
//	or:
//
//	        nil
type AnalyzerUnusedAccessConfigurationPtrInput interface {
	pulumi.Input

	ToAnalyzerUnusedAccessConfigurationPtrOutput() AnalyzerUnusedAccessConfigurationPtrOutput
	ToAnalyzerUnusedAccessConfigurationPtrOutputWithContext(context.Context) AnalyzerUnusedAccessConfigurationPtrOutput
}

type analyzerUnusedAccessConfigurationPtrType AnalyzerUnusedAccessConfigurationArgs

func AnalyzerUnusedAccessConfigurationPtr(v *AnalyzerUnusedAccessConfigurationArgs) AnalyzerUnusedAccessConfigurationPtrInput {
	return (*analyzerUnusedAccessConfigurationPtrType)(v)
}

func (*analyzerUnusedAccessConfigurationPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**AnalyzerUnusedAccessConfiguration)(nil)).Elem()
}

func (i *analyzerUnusedAccessConfigurationPtrType) ToAnalyzerUnusedAccessConfigurationPtrOutput() AnalyzerUnusedAccessConfigurationPtrOutput {
	return i.ToAnalyzerUnusedAccessConfigurationPtrOutputWithContext(context.Background())
}

func (i *analyzerUnusedAccessConfigurationPtrType) ToAnalyzerUnusedAccessConfigurationPtrOutputWithContext(ctx context.Context) AnalyzerUnusedAccessConfigurationPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AnalyzerUnusedAccessConfigurationPtrOutput)
}

func (i *analyzerUnusedAccessConfigurationPtrType) ToOutput(ctx context.Context) pulumix.Output[*AnalyzerUnusedAccessConfiguration] {
	return pulumix.Output[*AnalyzerUnusedAccessConfiguration]{
		OutputState: i.ToAnalyzerUnusedAccessConfigurationPtrOutputWithContext(ctx).OutputState,
	}
}

// The Configuration for Unused Access Analyzer
type AnalyzerUnusedAccessConfigurationOutput struct{ *pulumi.OutputState }

func (AnalyzerUnusedAccessConfigurationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*AnalyzerUnusedAccessConfiguration)(nil)).Elem()
}

func (o AnalyzerUnusedAccessConfigurationOutput) ToAnalyzerUnusedAccessConfigurationOutput() AnalyzerUnusedAccessConfigurationOutput {
	return o
}

func (o AnalyzerUnusedAccessConfigurationOutput) ToAnalyzerUnusedAccessConfigurationOutputWithContext(ctx context.Context) AnalyzerUnusedAccessConfigurationOutput {
	return o
}

func (o AnalyzerUnusedAccessConfigurationOutput) ToAnalyzerUnusedAccessConfigurationPtrOutput() AnalyzerUnusedAccessConfigurationPtrOutput {
	return o.ToAnalyzerUnusedAccessConfigurationPtrOutputWithContext(context.Background())
}

func (o AnalyzerUnusedAccessConfigurationOutput) ToAnalyzerUnusedAccessConfigurationPtrOutputWithContext(ctx context.Context) AnalyzerUnusedAccessConfigurationPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v AnalyzerUnusedAccessConfiguration) *AnalyzerUnusedAccessConfiguration {
		return &v
	}).(AnalyzerUnusedAccessConfigurationPtrOutput)
}

func (o AnalyzerUnusedAccessConfigurationOutput) ToOutput(ctx context.Context) pulumix.Output[AnalyzerUnusedAccessConfiguration] {
	return pulumix.Output[AnalyzerUnusedAccessConfiguration]{
		OutputState: o.OutputState,
	}
}

// The specified access age in days for which to generate findings for unused access. For example, if you specify 90 days, the analyzer will generate findings for IAM entities within the accounts of the selected organization for any access that hasn't been used in 90 or more days since the analyzer's last scan. You can choose a value between 1 and 180 days.
func (o AnalyzerUnusedAccessConfigurationOutput) UnusedAccessAge() pulumi.IntPtrOutput {
	return o.ApplyT(func(v AnalyzerUnusedAccessConfiguration) *int { return v.UnusedAccessAge }).(pulumi.IntPtrOutput)
}

type AnalyzerUnusedAccessConfigurationPtrOutput struct{ *pulumi.OutputState }

func (AnalyzerUnusedAccessConfigurationPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**AnalyzerUnusedAccessConfiguration)(nil)).Elem()
}

func (o AnalyzerUnusedAccessConfigurationPtrOutput) ToAnalyzerUnusedAccessConfigurationPtrOutput() AnalyzerUnusedAccessConfigurationPtrOutput {
	return o
}

func (o AnalyzerUnusedAccessConfigurationPtrOutput) ToAnalyzerUnusedAccessConfigurationPtrOutputWithContext(ctx context.Context) AnalyzerUnusedAccessConfigurationPtrOutput {
	return o
}

func (o AnalyzerUnusedAccessConfigurationPtrOutput) ToOutput(ctx context.Context) pulumix.Output[*AnalyzerUnusedAccessConfiguration] {
	return pulumix.Output[*AnalyzerUnusedAccessConfiguration]{
		OutputState: o.OutputState,
	}
}

func (o AnalyzerUnusedAccessConfigurationPtrOutput) Elem() AnalyzerUnusedAccessConfigurationOutput {
	return o.ApplyT(func(v *AnalyzerUnusedAccessConfiguration) AnalyzerUnusedAccessConfiguration {
		if v != nil {
			return *v
		}
		var ret AnalyzerUnusedAccessConfiguration
		return ret
	}).(AnalyzerUnusedAccessConfigurationOutput)
}

// The specified access age in days for which to generate findings for unused access. For example, if you specify 90 days, the analyzer will generate findings for IAM entities within the accounts of the selected organization for any access that hasn't been used in 90 or more days since the analyzer's last scan. You can choose a value between 1 and 180 days.
func (o AnalyzerUnusedAccessConfigurationPtrOutput) UnusedAccessAge() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *AnalyzerUnusedAccessConfiguration) *int {
		if v == nil {
			return nil
		}
		return v.UnusedAccessAge
	}).(pulumi.IntPtrOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*AnalyzerArchiveRuleInput)(nil)).Elem(), AnalyzerArchiveRuleArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*AnalyzerArchiveRuleArrayInput)(nil)).Elem(), AnalyzerArchiveRuleArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*AnalyzerConfigurationPropertiesInput)(nil)).Elem(), AnalyzerConfigurationPropertiesArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*AnalyzerConfigurationPropertiesPtrInput)(nil)).Elem(), AnalyzerConfigurationPropertiesArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*AnalyzerFilterInput)(nil)).Elem(), AnalyzerFilterArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*AnalyzerFilterArrayInput)(nil)).Elem(), AnalyzerFilterArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*AnalyzerTagInput)(nil)).Elem(), AnalyzerTagArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*AnalyzerTagArrayInput)(nil)).Elem(), AnalyzerTagArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*AnalyzerUnusedAccessConfigurationInput)(nil)).Elem(), AnalyzerUnusedAccessConfigurationArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*AnalyzerUnusedAccessConfigurationPtrInput)(nil)).Elem(), AnalyzerUnusedAccessConfigurationArgs{})
	pulumi.RegisterOutputType(AnalyzerArchiveRuleOutput{})
	pulumi.RegisterOutputType(AnalyzerArchiveRuleArrayOutput{})
	pulumi.RegisterOutputType(AnalyzerConfigurationPropertiesOutput{})
	pulumi.RegisterOutputType(AnalyzerConfigurationPropertiesPtrOutput{})
	pulumi.RegisterOutputType(AnalyzerFilterOutput{})
	pulumi.RegisterOutputType(AnalyzerFilterArrayOutput{})
	pulumi.RegisterOutputType(AnalyzerTagOutput{})
	pulumi.RegisterOutputType(AnalyzerTagArrayOutput{})
	pulumi.RegisterOutputType(AnalyzerUnusedAccessConfigurationOutput{})
	pulumi.RegisterOutputType(AnalyzerUnusedAccessConfigurationPtrOutput{})
}

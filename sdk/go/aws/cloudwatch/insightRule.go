// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package cloudwatch

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::CloudWatch::InsightRule
//
// Deprecated: InsightRule is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
type InsightRule struct {
	pulumi.CustomResourceState

	Arn       pulumi.StringOutput      `pulumi:"arn"`
	RuleBody  pulumi.StringOutput      `pulumi:"ruleBody"`
	RuleName  pulumi.StringOutput      `pulumi:"ruleName"`
	RuleState pulumi.StringOutput      `pulumi:"ruleState"`
	Tags      InsightRuleTagsPtrOutput `pulumi:"tags"`
}

// NewInsightRule registers a new resource with the given unique name, arguments, and options.
func NewInsightRule(ctx *pulumi.Context,
	name string, args *InsightRuleArgs, opts ...pulumi.ResourceOption) (*InsightRule, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.RuleBody == nil {
		return nil, errors.New("invalid value for required argument 'RuleBody'")
	}
	if args.RuleName == nil {
		return nil, errors.New("invalid value for required argument 'RuleName'")
	}
	if args.RuleState == nil {
		return nil, errors.New("invalid value for required argument 'RuleState'")
	}
	var resource InsightRule
	err := ctx.RegisterResource("aws-native:cloudwatch:InsightRule", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetInsightRule gets an existing InsightRule resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetInsightRule(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *InsightRuleState, opts ...pulumi.ResourceOption) (*InsightRule, error) {
	var resource InsightRule
	err := ctx.ReadResource("aws-native:cloudwatch:InsightRule", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering InsightRule resources.
type insightRuleState struct {
}

type InsightRuleState struct {
}

func (InsightRuleState) ElementType() reflect.Type {
	return reflect.TypeOf((*insightRuleState)(nil)).Elem()
}

type insightRuleArgs struct {
	RuleBody  string           `pulumi:"ruleBody"`
	RuleName  string           `pulumi:"ruleName"`
	RuleState string           `pulumi:"ruleState"`
	Tags      *InsightRuleTags `pulumi:"tags"`
}

// The set of arguments for constructing a InsightRule resource.
type InsightRuleArgs struct {
	RuleBody  pulumi.StringInput
	RuleName  pulumi.StringInput
	RuleState pulumi.StringInput
	Tags      InsightRuleTagsPtrInput
}

func (InsightRuleArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*insightRuleArgs)(nil)).Elem()
}

type InsightRuleInput interface {
	pulumi.Input

	ToInsightRuleOutput() InsightRuleOutput
	ToInsightRuleOutputWithContext(ctx context.Context) InsightRuleOutput
}

func (*InsightRule) ElementType() reflect.Type {
	return reflect.TypeOf((**InsightRule)(nil)).Elem()
}

func (i *InsightRule) ToInsightRuleOutput() InsightRuleOutput {
	return i.ToInsightRuleOutputWithContext(context.Background())
}

func (i *InsightRule) ToInsightRuleOutputWithContext(ctx context.Context) InsightRuleOutput {
	return pulumi.ToOutputWithContext(ctx, i).(InsightRuleOutput)
}

type InsightRuleOutput struct{ *pulumi.OutputState }

func (InsightRuleOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**InsightRule)(nil)).Elem()
}

func (o InsightRuleOutput) ToInsightRuleOutput() InsightRuleOutput {
	return o
}

func (o InsightRuleOutput) ToInsightRuleOutputWithContext(ctx context.Context) InsightRuleOutput {
	return o
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*InsightRuleInput)(nil)).Elem(), &InsightRule{})
	pulumi.RegisterOutputType(InsightRuleOutput{})
}
